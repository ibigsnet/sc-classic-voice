#!/usr/bin/env python3
"""Generate hard-vs-soft spotlight reports with clear wording diffs.

Uses unified/word-level diffs so readers see exactly what CIG changed —
like a VCS review (removed vs added), not three nearly-identical tables.
"""

from __future__ import annotations

import argparse
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ini_util import load_ini, plain  # noqa: E402

# Flagship Headhunter bomb-run softens (and friends can be added).
DEFAULT_KEYS = [
    "headhunters_bombingrun_multi_E_CFP_desc_001",
    "headhunters_Nyx_bombingrun_M_desc_001",
    "headhunters_bombingrun_S_desc_001",
]

def tokenize(text: str) -> list[str]:
    """Split into whitespace-preserving tokens for word-level diffs."""
    return re.findall(r"\S+|\s+", text)



def squash_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def common_prefix_suffix_opcodes(a: str, b: str) -> list[tuple[str, str, str]] | None:
    """Single-site phrase diff via shared ends (best for near-identical softens).

    Returns None if the middle hunk is empty or almost the whole string
    (rewrite / multi-site — fall back to word-level).
    """
    if a == b:
        return [("equal", a, b)]
    # Character-level shared prefix/suffix, then snap to word boundaries.
    i = 0
    n = min(len(a), len(b))
    while i < n and a[i] == b[i]:
        i += 1
    # Prefer cutting at whitespace so we don't split mid-word.
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

    # Multi-site / total rewrite: middles too large → word-level is clearer.
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
    """Return list of (tag, a_chunk, b_chunk) for equal/delete/insert/replace."""
    ta, tb = tokenize(a), tokenize(b)
    sm = SequenceMatcher(None, ta, tb, autojunk=False)
    out: list[tuple[str, str, str]] = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        out.append((tag, "".join(ta[i1:i2]), "".join(tb[j1:j2])))
    return out


# Short equal spans that often sit inside one soft rewrite ("the", "a", …).
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



def only_changes(opcodes: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    return [op for op in opcodes if op[0] != "equal"]


def format_unified_diff_block(a: str, b: str, label_a: str, label_b: str) -> str:
    """GitHub-colored ```diff fence: red '-' removals, green '+' additions."""
    changes = only_changes(phrase_opcodes(a, b))
    if not changes:
        return "_No wording difference._\n"
    lines = [
        "```diff",
        f"# {label_a}  →  {label_b}",
    ]
    for tag, ca, cb in changes:
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        if tag == "delete":
            lines.append(f"- {ca_s}")
        elif tag == "insert":
            lines.append(f"+ {cb_s}")
        elif tag == "replace":
            if ca_s:
                lines.append(f"- {ca_s}")
            if cb_s:
                lines.append(f"+ {cb_s}")
    lines.append("```")
    return "\n".join(lines) + "\n"


def format_inline_markup(a: str, b: str) -> str:
    """Inline view: ~~removed~~ **added** with context (equal spans kept)."""
    chunks: list[str] = []
    for tag, ca, cb in phrase_opcodes(a, b):
        if tag == "equal":
            if len(ca) > 160:
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


def format_change_table(a: str, b: str) -> str:
    """Table of phrase-level removed → added pairs."""
    rows: list[str] = []
    for tag, ca, cb in only_changes(phrase_opcodes(a, b)):
        ca_s, cb_s = squash_ws(ca), squash_ws(cb)
        # Escape pipes so markdown tables don't break.
        ca_s = ca_s.replace("|", "\\|")
        cb_s = cb_s.replace("|", "\\|")
        if tag == "delete":
            rows.append(f"| 🔴 removed | `{ca_s}` | — |")
        elif tag == "insert":
            rows.append(f"| 🟢 added | — | `{cb_s}` |")
        elif tag == "replace":
            rows.append(f"| 🔄 replaced | `{ca_s}` | `{cb_s}` |")
    if not rows:
        return "_No wording difference._\n"
    head = "| | Hard (old) | Soft (new) |\n|---|------------|-----------|\n"
    return head + "\n".join(rows) + "\n"



def resolve_corpus(root: Path, label: str) -> Path:
    """Prefer bank p4k-fresh, then bank, then corpus root."""
    candidates = [
        root / "corpus" / "bank" / f"{label}-p4k-fresh.ini",
        root / "corpus" / "bank" / f"{label}.ini",
        root / "corpus" / f"{label}.ini",
    ]
    for c in candidates:
        if c.is_file():
            return c
    raise FileNotFoundError(f"No corpus for {label}: tried {candidates}")


def build_report(
    hard_label: str,
    soft_label: str,
    current_label: str,
    keys: list[str],
    root: Path,
) -> str:
    hard = load_ini(resolve_corpus(root, hard_label))
    soft = load_ini(resolve_corpus(root, soft_label))
    cur = load_ini(resolve_corpus(root, current_label))

    lines: list[str] = [
        f"# Spotlight: hard (≤{hard_label.split('-')[0]}) vs soft ({soft_label.split('-')[0]}+)",
        "",
        f"Corpus: `{hard_label}` → `{soft_label}` → `{current_label}` "
        f"(stock strings; prefer p4k-fresh when banked).",
        "",
        "Classic-voice packs put the **hard** wording back onto current builds.",
        "",
        "## How to read this page",
        "",
        "Wide tables hide the real edit. Each key below is shown three ways:",
        "",
        "1. **Change table** — only the tokens that moved (hard → soft).",
        "2. **Unified diff** — GitHub paints `-` red (removed) and `+` green (added).",
        "3. **Inline markup** — `~~removed~~` / `**added**` with surrounding context.",
        "4. **Full stock text** — complete strings if you need to copy/search.",
        "",
        "Legend: 🔴 removed from hard stock · 🟢 added in soft stock · 🔄 replaced.",
        "",
        "---",
        "",
    ]

    for key in keys:
        h = hard.get(key)
        s = soft.get(key)
        c = cur.get(key)
        lines.append(f"## `{key}`")
        lines.append("")
        if h is None and s is None and c is None:
            lines.append("_Key missing from all three stocks._")
            lines.append("")
            continue

        h_plain = plain(h) if h is not None else ""
        s_plain = plain(s) if s is not None else ""
        c_plain = plain(c) if c is not None else ""

        same_soft_cur = s_plain == c_plain
        hard_differs = h_plain != c_plain

        # --- TL;DR change table (hard → soft era) ---
        lines.append(f"### What changed ({hard_label} → {soft_label})")
        lines.append("")
        if h is None:
            lines.append(f"_Missing in {hard_label}._")
            lines.append("")
        elif s is None:
            lines.append(f"_Missing in {soft_label}._")
            lines.append("")
        elif h_plain == s_plain:
            lines.append("_Identical between hard and soft era (no soften on this hop)._")
            lines.append("")
        else:
            lines.append(format_change_table(h_plain, s_plain))
            lines.append(format_unified_diff_block(h_plain, s_plain, hard_label, soft_label))
            lines.append("**Inline (context):**")
            lines.append("")
            lines.append(format_inline_markup(h_plain, s_plain))
            lines.append("")

        # --- soft → current if different ---
        if s is not None and c is not None and s_plain != c_plain:
            lines.append(f"### Later change ({soft_label} → {current_label})")
            lines.append("")
            lines.append(format_change_table(s_plain, c_plain))
            lines.append(format_unified_diff_block(s_plain, c_plain, soft_label, current_label))
            lines.append("")
        else:
            lines.append(
                f"- Same `{soft_label}` vs `{current_label}`? **{same_soft_cur}**"
            )
            lines.append(f"- `{hard_label}` differs from `{current_label}`? **{hard_differs}**")
            lines.append("")

        # --- Full texts (collapsed-friendly) ---
        lines.append("<details>")
        lines.append(f"<summary>Full stock text (all versions)</summary>")
        lines.append("")
        lines.append(f"**{hard_label} (hard)**")
        lines.append("")
        lines.append("```")
        lines.append(h_plain if h is not None else "(missing)")
        lines.append("```")
        lines.append("")
        lines.append(f"**{soft_label} (soft era)**")
        lines.append("")
        lines.append("```")
        lines.append(s_plain if s is not None else "(missing)")
        lines.append("```")
        lines.append("")
        lines.append(f"**{current_label} (current)**")
        lines.append("")
        lines.append("```")
        lines.append(c_plain if c is not None else "(missing)")
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(
        "*Regenerated by `scripts/spotlight_diff.py`. "
        "Packs restore hard-column wording; see `packs/library/`.*"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hard", default="4.7.1-LIVE", help="Hard / older stock label")
    ap.add_argument("--soft", default="4.8.0-PTU", help="Soft-era stock label")
    ap.add_argument("--current", default="4.10.0-PTU", help="Current stock label")
    ap.add_argument(
        "--keys",
        nargs="*",
        default=DEFAULT_KEYS,
        help="Localization keys to spotlight",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=ROOT / "reports" / "spotlight-hard-vs-soft-4.7-4.8.md",
    )
    args = ap.parse_args()

    report = build_report(args.hard, args.soft, args.current, list(args.keys), ROOT)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Wrote {args.output} ({len(args.keys)} keys)")


if __name__ == "__main__":
    main()
