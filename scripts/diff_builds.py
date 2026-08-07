#!/usr/bin/env python3
"""
Full build-to-build localization change mapper.

Compares every consecutive corpus version and catalogs ALL key text changes
(not only soften heuristics). Also builds a per-key history summary vs a
target (latest) stock.

Outputs under reports/:
  build-diffs.json       — all pairwise changes
  build-diffs.md         — human summary
  key-history.json       — for each key that ever changed, version timeline
  key-history-sample.md  — top narrative changes for awareness

Usage:
  python3 scripts/diff_builds.py
  python3 scripts/diff_builds.py --target 4.10.0-PTU
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, plain, version_sort_key
from map_softening import discover_versions, edge_hits
from phrase_diff import format_markdown_diff, hunk_dicts, one_line_summary

NARRATIVE_RE = re.compile(
    r"(Desc|desc|Title|title|Journal|Brief|_GP_|mission|Mission|contract|Contract)",
    re.I,
)


@dataclass
class Change:
    key: str
    from_version: str
    to_version: str
    similarity: float
    old_len: int
    new_len: int
    narrative: bool
    edge_old: list[str]
    edge_new: list[str]
    old_preview: str
    new_preview: str
    diff_hunks: list[dict[str, str]]
    diff_summary: str


def preview(v: str, n: int = 280) -> str:
    return plain(v)[:n].replace("\n", " | ")


def main() -> None:
    ap = argparse.ArgumentParser()
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--corpus", type=Path, default=root / "corpus")
    ap.add_argument("--out", type=Path, default=root / "reports")
    ap.add_argument("--target", default=None)
    ap.add_argument("--min-len", type=int, default=1, help="Skip tiny values")
    args = ap.parse_args()

    versions = discover_versions(args.corpus)
    if len(versions) < 2:
        print("Need ≥2 corpus versions")
        sys.exit(1)

    loaded: list[tuple[str, dict[str, str]]] = []
    for label, path in versions:
        data = load_ini(path)
        print(f"  {label:18} keys={len(data)}")
        loaded.append((label, data))

    target_label = args.target or loaded[-1][0]
    target_ini = dict(loaded[[x[0] for x in loaded].index(target_label)][1])

    all_changes: list[Change] = []
    pair_stats = []

    for i in range(len(loaded) - 1):
        a_l, a = loaded[i]
        b_l, b = loaded[i + 1]
        n = 0
        for key, ov in a.items():
            if key not in b:
                continue
            nv = b[key]
            if ov == nv:
                continue
            if len(ov) < args.min_len and len(nv) < args.min_len:
                continue
            op, np_ = plain(ov), plain(nv)
            if op.strip() == np_.strip():
                continue
            sim = SequenceMatcher(None, op, np_).ratio()
            ch = Change(
                key=key,
                from_version=a_l,
                to_version=b_l,
                similarity=round(sim, 4),
                old_len=len(op),
                new_len=len(np_),
                narrative=bool(NARRATIVE_RE.search(key)) or len(op) > 80,
                edge_old=edge_hits(ov),
                edge_new=edge_hits(nv),
                old_preview=preview(ov),
                new_preview=preview(nv),
                diff_hunks=hunk_dicts(op, np_),
                diff_summary=one_line_summary(op, np_),
            )
            all_changes.append(ch)
            n += 1
        pair_stats.append({"from": a_l, "to": b_l, "changes": n})
        print(f"  {a_l} → {b_l}: {n} text changes")

    # Per-key history vs target
    key_history: dict[str, dict] = {}
    labels = [x[0] for x in loaded]
    by_label = {x[0]: x[1] for x in loaded}

    # keys that appear in target and differ from at least one older stock
    for key, tval in target_ini.items():
        timeline = []
        for lab in labels:
            if key in by_label[lab]:
                timeline.append({"version": lab, "value": by_label[lab][key]})
        if len(timeline) < 2:
            continue
        values = [t["value"] for t in timeline]
        if len(set(values)) == 1:
            continue
        # oldest != target?
        oldest = timeline[0]["value"]
        op, tp = plain(oldest), plain(tval)
        key_history[key] = {
            "key": key,
            "versions_present": [t["version"] for t in timeline],
            "unique_texts": len(set(values)),
            "oldest_version": timeline[0]["version"],
            "newest_version": timeline[-1]["version"],
            "oldest_differs_from_target": oldest != tval,
            "narrative": bool(NARRATIVE_RE.search(key)) or len(plain(tval)) > 80,
            "edge_oldest": edge_hits(oldest),
            "edge_target": edge_hits(tval),
            "similarity_oldest_target": round(
                SequenceMatcher(None, op, tp).ratio(), 4
            ),
            "oldest_preview": preview(oldest),
            "target_preview": preview(tval),
            "diff_hunks": hunk_dicts(op, tp),
            "diff_summary": one_line_summary(op, tp),
            # Full plain for markdown sample only (stripped when writing json).
            "_oldest_full": op,
            "_target_full": tp,
        }

    args.out.mkdir(parents=True, exist_ok=True)

    diff_doc = {
        "versions": labels,
        "target": target_label,
        "pair_stats": pair_stats,
        "total_pairwise_changes": len(all_changes),
        "keys_with_history_vs_target": len(key_history),
        "changes": [asdict(c) for c in all_changes],
    }
    (args.out / "build-diffs.json").write_text(
        json.dumps(diff_doc, indent=2), encoding="utf-8"
    )

    # Lighter key history (previews + hunks; no full bodies) for git
    keys_for_json = []
    for h in sorted(key_history.values(), key=lambda x: x["key"]):
        slim = {k: v for k, v in h.items() if not k.startswith("_")}
        keys_for_json.append(slim)
    (args.out / "key-history.json").write_text(
        json.dumps(
            {
                "target": target_label,
                "count": len(key_history),
                "diff_legend": "diff_hunks: phrase-level -old +new (phrase_diff.py)",
                "keys": keys_for_json,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    # Markdown summary
    md = [
        "# Full build-to-build localization changes",
        "",
        f"Target stock: **{target_label}**",
        "",
        "### How to read diffs",
        "",
        "Each sample shows a **phrase-level wording diff** "
        "(GitHub paints `-` red / `+` green in `diff` fences). "
        "Full string previews are folded under details.",
        "",
        "Shared helper: `scripts/phrase_diff.py` (same style as softens & spotlight).",
        "",
        "## Pairwise change counts",
        "",
        "| From | To | Keys changed |",
        "|------|----|-------------:|",
    ]
    for ps in pair_stats:
        md.append(f"| {ps['from']} | {ps['to']} | {ps['changes']} |")
    md += [
        "",
        f"**Total pairwise text changes:** {len(all_changes)}",
        f"**Keys where history differs from target:** {len(key_history)}",
        "",
        "## Narrative keys: oldest stock ≠ target (awareness sample)",
        "",
    ]
    narr = [
        h
        for h in key_history.values()
        if h["narrative"] and h["oldest_differs_from_target"]
    ]
    narr.sort(key=lambda h: h["similarity_oldest_target"])
    md.append(
        f"_{len(narr)} narrative keys with oldest≠target; "
        "showing first 40 by rewrite distance_"
    )
    md.append("")
    for h in narr[:40]:
        md.append(
            f"### `{h['key']}`  ({h['oldest_version']} → target, "
            f"sim {h['similarity_oldest_target']:.0%})"
        )
        if h["edge_oldest"] or h["edge_target"]:
            md.append(
                f"- Edge oldest: {h['edge_oldest'] or '—'} · "
                f"target: {h['edge_target'] or '—'}"
            )
        md.append("")
        md.append(
            format_markdown_diff(
                h["_oldest_full"],
                h["_target_full"],
                h["oldest_version"],
                "target",
                include_inline=h["similarity_oldest_target"] >= 0.85,
            )
        )
        md.append("<details>")
        md.append("<summary>Full previews</summary>")
        md.append("")
        md.append(f"- **Oldest:** {h['oldest_preview']}")
        md.append(f"- **Target:** {h['target_preview']}")
        md.append("")
        md.append("</details>")
        md.append("")

    # High-similarity pairwise softens sample (clearest red/green demos)
    md += [
        "## High-similarity pairwise changes (clearest wording edits)",
        "",
        "_Same key, consecutive builds, sim ≥ 88% — these are the edits that "
        "look identical in full-string tables but jump out in a diff._",
        "",
    ]
    high_sim = sorted(
        [c for c in all_changes if c.similarity >= 0.88 and c.narrative],
        key=lambda c: (-c.similarity, c.key),
    )[:30]
    for c in high_sim:
        # Need full text: re-load from loaded dicts
        a_data = by_label[c.from_version]
        b_data = by_label[c.to_version]
        if c.key not in a_data or c.key not in b_data:
            continue
        op, np_ = plain(a_data[c.key]), plain(b_data[c.key])
        md.append(
            f"### `{c.key}`  {c.from_version} → {c.to_version} "
            f"(sim {c.similarity:.0%})"
        )
        if c.edge_old or c.edge_new:
            md.append(
                f"- Edge: {c.edge_old or '—'} → {c.edge_new or '—'}"
            )
        md.append("")
        md.append(
            format_markdown_diff(
                op,
                np_,
                c.from_version,
                c.to_version,
                include_inline=True,
            )
        )
        md.append("")

    (args.out / "build-diffs.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote reports/build-diffs.json ({len(all_changes)} changes)")
    print(f"Wrote reports/key-history.json ({len(key_history)} keys)")
    print(f"Wrote reports/build-diffs.md")


if __name__ == "__main__":
    main()
