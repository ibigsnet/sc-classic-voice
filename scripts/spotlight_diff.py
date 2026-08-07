#!/usr/bin/env python3
"""Generate hard-vs-soft spotlight reports with clear wording diffs.

Uses shared phrase_diff (VCS-style red/green) so readers see exactly what
CIG changed — not three nearly-identical full-string tables.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ini_util import load_ini, plain  # noqa: E402
from phrase_diff import (  # noqa: E402
    format_change_table,
    format_inline_markup,
    format_unified_diff_block,
)

# Flagship Headhunter bomb-run softens (and friends can be added).
DEFAULT_KEYS = [
    "headhunters_bombingrun_multi_E_CFP_desc_001",
    "headhunters_Nyx_bombingrun_M_desc_001",
    "headhunters_bombingrun_S_desc_001",
]


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
        "Same style is used project-wide in `soften-map.md`, `build-diffs.md`, "
        "and `all-keys-change-ledger.md` via `scripts/phrase_diff.py`.",
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
            lines.append(
                format_change_table(
                    h_plain, s_plain, col_old="Hard (old)", col_new="Soft (new)"
                )
            )
            lines.append(
                format_unified_diff_block(h_plain, s_plain, hard_label, soft_label)
            )
            lines.append("**Inline (context):**")
            lines.append("")
            lines.append(format_inline_markup(h_plain, s_plain))
            lines.append("")

        if s is not None and c is not None and s_plain != c_plain:
            lines.append(f"### Later change ({soft_label} → {current_label})")
            lines.append("")
            lines.append(
                format_change_table(
                    s_plain, c_plain, col_old=soft_label, col_new=current_label
                )
            )
            lines.append(
                format_unified_diff_block(s_plain, c_plain, soft_label, current_label)
            )
            lines.append("")
        else:
            lines.append(
                f"- Same `{soft_label}` vs `{current_label}`? **{same_soft_cur}**"
            )
            lines.append(
                f"- `{hard_label}` differs from `{current_label}`? **{hard_differs}**"
            )
            lines.append("")

        lines.append("<details>")
        lines.append("<summary>Full stock text (all versions)</summary>")
        lines.append("")
        for lab, txt, missing in (
            (hard_label + " (hard)", h_plain, h is None),
            (soft_label + " (soft era)", s_plain, s is None),
            (current_label + " (current)", c_plain, c is None),
        ):
            lines.append(f"**{lab}**")
            lines.append("")
            lines.append("```")
            lines.append("(missing)" if missing else txt)
            lines.append("```")
            lines.append("")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(
        "*Regenerated by `scripts/spotlight_diff.py` (shared `phrase_diff`). "
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
