#!/usr/bin/env python3
"""
Map wording softens across versioned stock global.ini files.

Compares every consecutive pair in the corpus (oldest → newest) and flags
keys whose text lost edge / gained euphemism.

Outputs:
  reports/soften-map.json   machine-readable events
  reports/soften-map.md     human summary
  reports/soften-map.csv    spreadsheet-friendly

Usage:
  python3 scripts/map_softening.py
  python3 scripts/map_softening.py --corpus corpus --out reports
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, plain, version_sort_key
from wordlists import (
    euphemism_pairs as _load_euphemism_pairs,
    hard_patterns as _load_hard_patterns,
)

# Loaded from wordlists/hard-words.txt and wordlists/euphemism-pairs.tsv
# (editable without changing Python — reverse of studio sanitize lists).
def _edge_patterns():
    return _load_hard_patterns()


def _euphemism_pairs():
    return _load_euphemism_pairs()


# Back-compat names used by other modules
EDGE_PATTERNS = None  # resolved lazily via edge_hits
EUPHEMISM_PAIRS = None


@dataclass
class SoftenEvent:
    key: str
    from_version: str
    to_version: str
    similarity: float
    edge_lost: list[str]
    edge_gained: list[str]
    euphemism_hits: list[str]
    score: float
    old_preview: str
    new_preview: str
    old_len: int
    new_len: int


def edge_hits(text: str) -> list[str]:
    t = plain(text)
    return [name for name, pat in _edge_patterns() if pat.search(t)]


def euphemism_hits(old: str, new: str) -> list[str]:
    o, n = plain(old).lower(), plain(new).lower()
    hits = []
    for a, b in _euphemism_pairs():
        if a.lower() in o and b.lower() in n and a.lower() not in n:
            hits.append(f"{a!r}→{b!r}")
        # also if old had a and new lost it without exact pair
        elif a.lower() in o and a.lower() not in n:
            hits.append(f"lost:{a!r}")
    return hits


def event_score(edge_lost: list[str], edge_gained: list[str], eu: list[str], sim: float) -> float:
    # Higher = more likely intentional soften
    s = 0.0
    s += 12.0 * len(edge_lost)
    s -= 4.0 * len(edge_gained)  # new text got edgier = not a soften
    s += 15.0 * len(eu)
    s += max(0.0, (0.98 - sim) * 40.0)  # more rewrite → higher
    return s


def discover_versions(corpus: Path) -> list[tuple[str, Path]]:
    versions = []
    for p in sorted(corpus.glob("*.ini")):
        if p.name.endswith("-global.ini"):
            continue
        label = p.stem  # 4.7.0-LIVE
        versions.append((label, p.resolve()))
    versions.sort(key=lambda x: version_sort_key(x[0]))
    return versions


def compare_pair(
    from_label: str,
    from_ini: dict[str, str],
    to_label: str,
    to_ini: dict[str, str],
    min_score: float,
) -> list[SoftenEvent]:
    events: list[SoftenEvent] = []
    for key, old_val in from_ini.items():
        if key not in to_ini:
            continue
        new_val = to_ini[key]
        if old_val == new_val:
            continue
        old_p, new_p = plain(old_val), plain(new_val)
        if old_p.strip() == new_p.strip():
            continue
        sim = SequenceMatcher(None, old_p, new_p).ratio()
        lost = [e for e in edge_hits(old_val) if e not in edge_hits(new_val)]
        gained = [e for e in edge_hits(new_val) if e not in edge_hits(old_val)]
        eu = euphemism_hits(old_val, new_val)
        score = event_score(lost, gained, eu, sim)
        # Require some signal: lost edge, euphemism, or substantial mission rewrite with edge in old
        if score < min_score and not lost and not eu:
            continue
        if not lost and not eu and sim > 0.97:
            continue
        # Prefer narrative keys
        if not any(
            x in key for x in ("Desc", "desc", "Title", "title", "Journal", "Brief", "_GP_", "mission")
        ) and len(old_p) < 60 and not lost and not eu:
            continue
        events.append(
            SoftenEvent(
                key=key,
                from_version=from_label,
                to_version=to_label,
                similarity=round(sim, 4),
                edge_lost=lost,
                edge_gained=gained,
                euphemism_hits=eu,
                score=round(score, 2),
                old_preview=old_p[:400].replace("\n", " | "),
                new_preview=new_p[:400].replace("\n", " | "),
                old_len=len(old_p),
                new_len=len(new_p),
            )
        )
    events.sort(key=lambda e: e.score, reverse=True)
    return events


def main() -> None:
    ap = argparse.ArgumentParser(description="Map localization softens across versions")
    ap.add_argument("--corpus", type=Path, default=Path(__file__).resolve().parent.parent / "corpus")
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    ap.add_argument("--min-score", type=float, default=8.0)
    args = ap.parse_args()

    versions = discover_versions(args.corpus)
    if len(versions) < 2:
        print(f"ERROR: need ≥2 versioned .ini files in {args.corpus}")
        sys.exit(1)

    print("Versions (oldest → newest):")
    loaded: list[tuple[str, dict[str, str]]] = []
    for label, path in versions:
        data = load_ini(path)
        print(f"  {label:16} keys={len(data):6}  {path}")
        loaded.append((label, data))

    all_events: list[SoftenEvent] = []
    pair_stats = []
    for i in range(len(loaded) - 1):
        a_label, a_data = loaded[i]
        b_label, b_data = loaded[i + 1]
        ev = compare_pair(a_label, a_data, b_label, b_data, args.min_score)
        all_events.extend(ev)
        pair_stats.append({"from": a_label, "to": b_label, "events": len(ev)})
        print(f"  {a_label} → {b_label}: {len(ev)} soften candidates")

    args.out.mkdir(parents=True, exist_ok=True)
    json_path = args.out / "soften-map.json"
    json_path.write_text(
        json.dumps(
            {
                "versions": [v[0] for v in versions],
                "pair_stats": pair_stats,
                "event_count": len(all_events),
                "events": [asdict(e) for e in all_events],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    csv_path = args.out / "soften-map.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "score",
                "key",
                "from_version",
                "to_version",
                "similarity",
                "edge_lost",
                "edge_gained",
                "euphemism_hits",
                "old_preview",
                "new_preview",
            ],
        )
        w.writeheader()
        for e in all_events:
            w.writerow(
                {
                    "score": e.score,
                    "key": e.key,
                    "from_version": e.from_version,
                    "to_version": e.to_version,
                    "similarity": e.similarity,
                    "edge_lost": "|".join(e.edge_lost),
                    "edge_gained": "|".join(e.edge_gained),
                    "euphemism_hits": "|".join(e.euphemism_hits),
                    "old_preview": e.old_preview,
                    "new_preview": e.new_preview,
                }
            )

    md = args.out / "soften-map.md"
    lines = [
        "# Soften map — Star Citizen localization",
        "",
        "Wording changes across stock `global.ini` extracts that look like **tone softening** "
        "(lost edge, euphemism swaps). Auto-detected; review before shipping a pack.",
        "",
        "## Corpus",
        "",
    ]
    for label, path in versions:
        lines.append(f"- **{label}** — `{path.name}`")
    lines += ["", "## Pair counts", "", "| From | To | Soften candidates |", "|------|----|------------------:|"]
    for ps in pair_stats:
        lines.append(f"| {ps['from']} | {ps['to']} | {ps['events']} |")
    lines += ["", f"**Total events:** {len(all_events)}", "", "## Top events (by score)", ""]
    for e in all_events[:60]:
        lines.append(
            f"### `{e.key}` — {e.from_version} → {e.to_version} "
            f"(score {e.score}, sim {e.similarity:.0%})"
        )
        if e.edge_lost:
            lines.append(f"- Edge lost: {', '.join(e.edge_lost)}")
        if e.euphemism_hits:
            lines.append(f"- Euphemism: {', '.join(e.euphemism_hits)}")
        lines.append("")
        lines.append(f"- **Old:** {e.old_preview[:350]}")
        lines.append(f"- **New:** {e.new_preview[:350]}")
        lines.append("")
    md.write_text("\n".join(lines), encoding="utf-8")

    print(f"\nWrote {json_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {md}")
    print(f"Total soften events: {len(all_events)}")


if __name__ == "__main__":
    main()
