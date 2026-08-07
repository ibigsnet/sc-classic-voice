#!/usr/bin/env python3
"""Phrase-level wording diffs for localization reports.

Goal: readers see *exactly* what changed — like a VCS review — not two
nearly-identical full-string previews.

GitHub renders fenced ```diff blocks with red `-` and green `+`.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from typing import Iterable


def tokenize(text: str) -> list[str]:
    """Whitespace-preserving tokens for word-level alignment."""
    return re.findall(r"\S+|\s+", text)


def squash_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def common_prefix_suffix_opcodes(
    a: str, b: str
) -> list[tuple[str, str, str]] | None:
    """Single-site phrase diff via shared ends (best for near-identical softens).

    Returns None for multi-site / total rewrites (fall back to word-level).
    """
    if a == b:
        return [("equal", a, b)]
    i = 0
    n = min(len(a), len(b))
    while i < n and a[i] == b[i]:
        i += 1
    while i > 0 and a[i - 1] not in " \t\n" and b[i - 1] not in " \t\n":
        i -= 1

    j = 0
    while j < (len(a) - i) and j < (len(b) - i) and a[-(j + 1)] == b[-(j + 1)]:
        j += 1
    while j > 0 and a[-j] not in " \t\n" and b[-j] not in " \t\n":
        j -= 1

    mid_a = a[i : len(a) - j if j else len(a)]
    mid_b = b[i : len(b) - j if j else len(b)]
    if not mid_a and not mid_b:
        return [("equal", a, b)]

    max_len = max(len(a), len(b), 1)
    if max(len(mid_a), len(mid_b)) > 0.55 * max_len and max_len > 80:
        return None

    out: list[tuple[str, str, str]] = []
    if i:
        out.append(("equal", a[:i], b[:i]))
    if mid_a or mid_b:
        if mid_a and mid_b:
            out.append(("replace", mid_a, mid_b))
        elif mid_a:
            out.append(("delete", mid_a, ""))
        else:
            out.append(("insert", "", mid_b))
    if j:
        out.append(("equal", a[-j:], b[-j:]))
    return out


def word_opcodes(a: str, b: str) -> list[tuple[str, str, str]]:
    ta, tb = tokenize(a), tokenize(b)
    sm = SequenceMatcher(None, ta, tb, autojunk=False)
    return [
        (tag, "".join(ta[i1:i2]), "".join(tb[j1:j2]))
        for tag, i1, i2, j1, j2 in sm.get_opcodes()
    ]


_BRIDGE_EQ = re.compile(
    r"^(?:\s+|(?:the|a|an|of|to|and|or|out|in|on|for|with)\s*)+$",
    re.I,
)


def coalesce_phrase_hunks(
    opcodes: list[tuple[str, str, str]],
) -> list[tuple[str, str, str]]:
    """Merge adjacent non-equal ops (and tiny bridging equals) into phrases."""
    hunks: list[tuple[str, str, str]] = []
    buf_a: list[str] = []
    buf_b: list[str] = []

    def flush() -> None:
        nonlocal buf_a, buf_b
        if not buf_a and not buf_b:
            return
        ca, cb = "".join(buf_a), "".join(buf_b)
        if ca and cb:
            hunks.append(("replace", ca, cb))
        elif ca:
            hunks.append(("delete", ca, ""))
        else:
            hunks.append(("insert", "", cb))
        buf_a, buf_b = [], []

    for tag, ca, cb in opcodes:
        if tag == "equal":
            if (buf_a or buf_b) and (
                ca.strip() == "" or (_BRIDGE_EQ.match(ca) and len(ca) <= 24)
            ):
                buf_a.append(ca)
                buf_b.append(cb)
                continue
            flush()
            hunks.append(("equal", ca, cb))
        else:
            buf_a.append(ca)
            buf_b.append(cb)
    flush()
    return hunks


def phrase_opcodes(a: str, b: str) -> list[tuple[str, str, str]]:
    """Prefer single-site prefix/suffix phrase hunks; else coalesced word ops."""
    cps = common_prefix_suffix_opcodes(a, b)
    if cps is not None:
        return cps
    return coalesce_phrase_hunks(word_opcodes(a, b))


def only_changes(
    opcodes: Iterable[tuple[str, str, str]],
) -> list[tuple[str, str, str]]:
    return [op for op in opcodes if op[0] != "equal"]


def hunk_dicts(
    a: str,
    b: str,
    *,
    max_hunks: int = 12,
    max_chars: int = 220,
) -> list[dict[str, str]]:
    """Machine-readable change hunks for JSON/CSV."""
    changes = only_changes(phrase_opcodes(a, b))
    out: list[dict[str, str]] = []
    for tag, ca, cb in changes[:max_hunks]:
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        if len(ca_s) > max_chars:
            ca_s = ca_s[: max_chars - 1] + "…"
        if len(cb_s) > max_chars:
            cb_s = cb_s[: max_chars - 1] + "…"
        out.append({"op": tag, "old": ca_s, "new": cb_s})
    if len(changes) > max_hunks:
        out.append(
            {
                "op": "truncated",
                "old": f"… +{len(changes) - max_hunks} more hunks",
                "new": "",
            }
        )
    return out


def format_unified_diff_block(
    a: str,
    b: str,
    label_a: str = "old",
    label_b: str = "new",
    *,
    max_hunks: int = 12,
    max_chars: int = 220,
) -> str:
    """GitHub-colored ```diff fence: red '-' removals, green '+' additions."""
    changes = only_changes(phrase_opcodes(a, b))
    if not changes:
        return "_No wording difference._\n"
    lines = [
        "```diff",
        f"# {label_a}  →  {label_b}",
    ]
    shown = 0
    for tag, ca, cb in changes:
        if shown >= max_hunks:
            lines.append(f"# … +{len(changes) - shown} more hunks (truncated)")
            break
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        if len(ca_s) > max_chars:
            ca_s = ca_s[: max_chars - 1] + "…"
        if len(cb_s) > max_chars:
            cb_s = cb_s[: max_chars - 1] + "…"
        if tag == "delete":
            if ca_s:
                lines.append(f"- {ca_s}")
                shown += 1
        elif tag == "insert":
            if cb_s:
                lines.append(f"+ {cb_s}")
                shown += 1
        elif tag == "replace":
            if ca_s:
                lines.append(f"- {ca_s}")
            if cb_s:
                lines.append(f"+ {cb_s}")
            shown += 1
    lines.append("```")
    return "\n".join(lines) + "\n"


def format_inline_markup(
    a: str,
    b: str,
    *,
    context_equal_max: int = 160,
) -> str:
    """Inline view: ~~removed~~ **added** with surrounding context."""
    chunks: list[str] = []
    for tag, ca, cb in phrase_opcodes(a, b):
        if tag == "equal":
            if len(ca) > context_equal_max:
                mid = " … "
                chunks.append(ca[:70].rstrip() + mid + ca[-70:].lstrip())
            else:
                chunks.append(ca)
        elif tag == "delete":
            s = squash_ws(ca)
            if s:
                chunks.append(f"~~{s}~~")
        elif tag == "insert":
            s = squash_ws(cb)
            if s:
                chunks.append(f"**{s}**")
        elif tag == "replace":
            sa, sb = squash_ws(ca), squash_ws(cb)
            if sa:
                chunks.append(f"~~{sa}~~")
            if sb:
                chunks.append(f"**{sb}**")
    body = "".join(chunks)
    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r"\n{2,}", " / / ", body)
    body = re.sub(r"\n", " / ", body)
    return body.strip()


def format_change_table(
    a: str,
    b: str,
    *,
    col_old: str = "Old / hard",
    col_new: str = "New / soft",
    max_hunks: int = 12,
    max_chars: int = 180,
) -> str:
    """Markdown table of phrase-level removed → added pairs."""
    rows: list[str] = []
    changes = only_changes(phrase_opcodes(a, b))
    for tag, ca, cb in changes[:max_hunks]:
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        if len(ca_s) > max_chars:
            ca_s = ca_s[: max_chars - 1] + "…"
        if len(cb_s) > max_chars:
            cb_s = cb_s[: max_chars - 1] + "…"
        ca_s = ca_s.replace("|", "\\|").replace("`", "'")
        cb_s = cb_s.replace("|", "\\|").replace("`", "'")
        if tag == "delete":
            rows.append(f"| 🔴 removed | `{ca_s}` | — |")
        elif tag == "insert":
            rows.append(f"| 🟢 added | — | `{cb_s}` |")
        elif tag == "replace":
            rows.append(f"| 🔄 replaced | `{ca_s}` | `{cb_s}` |")
    if len(changes) > max_hunks:
        rows.append(
            f"| … | *+{len(changes) - max_hunks} more hunks* | |"
        )
    if not rows:
        return "_No wording difference._\n"
    head = f"| | {col_old} | {col_new} |\n|---|------------|-----------|\n"
    return head + "\n".join(rows) + "\n"


def format_markdown_diff(
    a: str,
    b: str,
    label_a: str = "old",
    label_b: str = "new",
    *,
    include_table: bool = True,
    include_unified: bool = True,
    include_inline: bool = False,
    max_hunks: int = 12,
) -> str:
    """Standard report block used by all generators."""
    if (a or "").strip() == (b or "").strip():
        return "_No wording difference._\n"
    parts: list[str] = []
    if include_table:
        parts.append(
            format_change_table(
                a,
                b,
                col_old=label_a,
                col_new=label_b,
                max_hunks=max_hunks,
            )
        )
    if include_unified:
        parts.append(
            format_unified_diff_block(
                a, b, label_a, label_b, max_hunks=max_hunks
            )
        )
    if include_inline:
        parts.append("**Inline:** " + format_inline_markup(a, b))
        parts.append("")
    return "\n".join(parts)


def one_line_summary(a: str, b: str, max_chars: int = 120) -> str:
    """Compact single-line for CSV / logs: -foo +bar | -baz +qux"""
    bits: list[str] = []
    for tag, ca, cb in only_changes(phrase_opcodes(a, b))[:6]:
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        if len(ca_s) > max_chars:
            ca_s = ca_s[: max_chars - 1] + "…"
        if len(cb_s) > max_chars:
            cb_s = cb_s[: max_chars - 1] + "…"
        if tag == "delete" and ca_s:
            bits.append(f"-{ca_s}")
        elif tag == "insert" and cb_s:
            bits.append(f"+{cb_s}")
        elif tag == "replace":
            if ca_s:
                bits.append(f"-{ca_s}")
            if cb_s:
                bits.append(f"+{cb_s}")
    return " | ".join(bits) if bits else "(no phrase hunks)"
