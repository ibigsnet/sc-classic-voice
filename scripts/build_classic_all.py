#!/usr/bin/env python3
"""
Compare EVERY key across ALL corpus versions and pick older/harder wording
for the target (latest) build.

For each key present in target stock:
  1. Collect text from every older version that has that key
  2. If all identical → skip (no pack entry)
  3. Score each historical text for "hardness"
  4. Choose best: highest hardness, ties → oldest version
  5. If winner differs from target → include in pack

Also writes a full change ledger (when wording changed along the timeline).

Outputs:
  packs/library/01-classic-all.ini          — delta for target
  packs/library/01-classic-all.meta.json    — provenance per key
  reports/all-keys-change-ledger.json       — every step-change observed
  reports/all-keys-change-ledger.md         — human sample + stats

Usage:
  python3 scripts/build_classic_all.py --target 4.10.0-PTU
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
from ini_util import load_ini, plain, write_ini
from map_softening import EDGE_PATTERNS, discover_versions, edge_hits

# Soft / corporate phrasing that lowers hardness when present
SOFT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("mess_the_place", re.compile(r"\bmess the place up\b", re.I)),
    ("take_care_of", re.compile(r"\btake care of\b", re.I)),
    ("deal_with", re.compile(r"\bdeal with\b", re.I)),
    ("neutralize", re.compile(r"\bneutraliz\w*\b", re.I)),
    ("eliminate", re.compile(r"\beliminat\w*\b", re.I)),  # often softer than kill
    ("subdue", re.compile(r"\bsubdue\b", re.I)),
    ("apprehend", re.compile(r"\bapprehend\b", re.I)),
    ("unfortunate", re.compile(r"\bunfortunate\b", re.I)),
    ("please_note", re.compile(r"\bplease note\b", re.I)),
    ("we_kindly", re.compile(r"\bkindly\b", re.I)),
]

HARD_BOOST_PHRASES = [
    (r"\bliving hell\b", 25),
    (r"\bbomb the life\b", 20),
    (r"\bbomb the living\b", 20),
    (r"\bbombing run\b", 12),
    (r"\bkill(?:ing|ed|s)?\b", 10),
    (r"\bmurder\b", 15),
    (r"\bslaughter\b", 15),
    (r"\bhell\b", 6),
    (r"\bshit(?:ty)?\b", 8),
    (r"\bcrap\b", 6),
    (r"\bfuck(?:ing)?\b", 12),
    (r"\bbastards?\b", 10),
    (r"\bcorpses?\b", 10),
    (r"\bblood(?:y)?\b", 6),
    (r"\bexecut(?:e|ion|ed)\b", 10),
    (r"\bwipe(?:s|d)? out\b", 8),
    (r"\bblow(?:s|n)? up\b", 8),
    (r"\bgut(?:s|ted)?\b", 10),
]


def hardness_score(text: str) -> float:
    """Higher = harder / more OG-unsoftened voice."""
    t = plain(text)
    score = 0.0
    for name, pat in EDGE_PATTERNS:
        if pat.search(t):
            score += 8.0
    for pat_s, boost in HARD_BOOST_PHRASES:
        if re.search(pat_s, t, re.I):
            score += boost
    for name, pat in SOFT_PATTERNS:
        if pat.search(t):
            score -= 10.0
    # slight preference for denser, longer combat/mission copy (not fluff)
    if len(t) > 200:
        score += 1.0
    return score


@dataclass
class StepChange:
    key: str
    from_version: str
    to_version: str
    hardness_from: float
    hardness_to: float
    softened: bool  # to is softer than from
    hardened: bool
    similarity: float
    from_preview: str
    to_preview: str


def main() -> None:
    ap = argparse.ArgumentParser(description="All-keys classic wording pick")
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--corpus", type=Path, default=root / "corpus")
    ap.add_argument("--target", default="4.10.0-PTU")
    ap.add_argument("--out-dir", type=Path, default=root / "packs" / "library")
    ap.add_argument("--reports", type=Path, default=root / "reports")
    ap.add_argument(
        "--min-hardness-gain",
        type=float,
        default=0.0,
        help="Only pack if chosen text hardness - target hardness > this",
    )
    ap.add_argument(
        "--require-harder",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Only include keys where chosen is strictly harder than target (default on)",
    )
    ap.add_argument(
        "--name",
        default="01-classic-all",
        help="Output basename under out-dir (default 01-classic-all)",
    )
    args = ap.parse_args()

    versions = discover_versions(args.corpus)
    labels = [v[0] for v in versions]
    by_label = {lab: load_ini(path) for lab, path in versions}
    if args.target not in by_label:
        print(f"ERROR: target {args.target} not in {labels}")
        sys.exit(1)

    target_ini = by_label[args.target]
    older_labels = [lab for lab in labels if lab != args.target]
    # only versions before target in sort order
    ti = labels.index(args.target)
    older_labels = labels[:ti]

    pack: dict[str, str] = {}
    meta: list[dict] = []
    step_changes: list[StepChange] = []

    # --- Full timeline step changes (all pairs consecutive, all keys) ---
    for i in range(len(labels) - 1):
        a_l, b_l = labels[i], labels[i + 1]
        a, b = by_label[a_l], by_label[b_l]
        for key, av in a.items():
            if key not in b or b[key] == av:
                continue
            ha, hb = hardness_score(av), hardness_score(b[key])
            sim = SequenceMatcher(None, plain(av), plain(b[key])).ratio()
            step_changes.append(
                StepChange(
                    key=key,
                    from_version=a_l,
                    to_version=b_l,
                    hardness_from=round(ha, 2),
                    hardness_to=round(hb, 2),
                    softened=hb < ha - 0.5,
                    hardened=hb > ha + 0.5,
                    similarity=round(sim, 4),
                    from_preview=plain(av)[:220].replace("\n", " | "),
                    to_preview=plain(b[key])[:220].replace("\n", " | "),
                )
            )

    # --- Per-key pick oldest/harder for target ---
    for key, tval in target_ini.items():
        candidates: list[tuple[str, str, float]] = []  # label, value, hardness
        for lab in older_labels:
            if key not in by_label[lab]:
                continue
            val = by_label[lab][key]
            candidates.append((lab, val, hardness_score(val)))
        if not candidates:
            continue
        # include target as reference
        t_hard = hardness_score(tval)
        # unique texts only
        texts = {c[1] for c in candidates}
        texts.add(tval)
        if len(texts) == 1:
            continue

        # Best among historical (and optionally beat target)
        # Sort: hardness desc, then older first (stable by walking older_labels order)
        best_lab, best_val, best_h = None, None, -1e9
        for lab, val, h in candidates:
            if val == tval:
                continue
            better = h > best_h + 1e-6
            tie_older = abs(h - best_h) <= 1e-6 and best_lab is not None
            # on tie, prefer older (smaller index)
            if better or (
                abs(h - best_h) <= 1e-6
                and (
                    best_lab is None
                    or older_labels.index(lab) < older_labels.index(best_lab)
                )
            ):
                # only replace on tie if older
                if abs(h - best_h) <= 1e-6 and best_lab is not None:
                    if older_labels.index(lab) >= older_labels.index(best_lab):
                        continue
                best_lab, best_val, best_h = lab, val, h

        if best_val is None:
            continue

        if best_val == tval:
            continue

        gain = best_h - t_hard
        if args.require_harder:
            # Must be strictly harder than current soft stock
            if gain <= args.min_hardness_gain:
                if not (
                    gain >= -0.01
                    and len(edge_hits(best_val)) > len(edge_hits(tval))
                ):
                    continue
        else:
            # At least as hard as target; older wording kept on ties
            if gain < args.min_hardness_gain:
                continue

        pack[key] = best_val
        meta.append(
            {
                "key": key,
                "chosen_version": best_lab,
                "hardness_chosen": round(best_h, 2),
                "hardness_target": round(t_hard, 2),
                "gain": round(gain, 2),
                "similarity_to_target": round(
                    SequenceMatcher(None, plain(best_val), plain(tval)).ratio(), 4
                ),
                "edge_chosen": edge_hits(best_val),
                "edge_target": edge_hits(tval),
                "chosen_preview": plain(best_val)[:200].replace("\n", " | "),
                "target_preview": plain(tval)[:200].replace("\n", " | "),
            }
        )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.reports.mkdir(parents=True, exist_ok=True)

    out_ini = args.out_dir / f"{args.name}.ini"
    write_ini(
        out_ini,
        dict(sorted(pack.items())),
        header=(
            f"{args.name}: older/harder wording for every key that changed across corpus\n"
            f"target={args.target}\n"
            f"keys={len(pack)}\n"
            f"Policy: max hardness among historical stocks; ties → oldest\n"
            f"require_harder={args.require_harder}\n"
            f"Smart Citizen: Import INI (delta vs current stock)"
        ),
    )

    meta_path = args.out_dir / f"{args.name}.meta.json"
    meta_path.write_text(
        json.dumps(
            {
                "target": args.target,
                "policy": "max_hardness_then_oldest",
                "require_harder": args.require_harder,
                "key_count": len(pack),
                "entries": sorted(meta, key=lambda m: -m["gain"]),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    softens = [s for s in step_changes if s.softened]
    hardens = [s for s in step_changes if s.hardened]

    ledger = {
        "target": args.target,
        "versions": labels,
        "pairwise_text_changes": len(step_changes),
        "steps_softened": len(softens),
        "steps_hardened": len(hardens),
        "pack_keys": len(pack),
        "softened_steps": [asdict(s) for s in sorted(softens, key=lambda x: x.hardness_from - x.hardness_to, reverse=True)],
        "all_steps_sample": [asdict(s) for s in step_changes[:500]],
    }
    # full steps is large — write separate full file
    full_steps_path = args.reports / "all-keys-step-changes.json"
    full_steps_path.write_text(
        json.dumps([asdict(s) for s in step_changes], indent=2),
        encoding="utf-8",
    )
    (args.reports / "all-keys-change-ledger.json").write_text(
        json.dumps(ledger, indent=2), encoding="utf-8"
    )

    md = [
        "# All-keys wording map (older/harder wins)",
        "",
        f"**Target (current soft stock):** `{args.target}`",
        "",
        f"- Corpus versions: {', '.join(labels)}",
        f"- Pairwise text changes (any wording change): **{len(step_changes)}**",
        f"- Steps scored as **softened** (hardness dropped): **{len(softens)}**",
        f"- Steps scored as **hardened**: **{len(hardens)}**",
        f"- Pack keys (harder than target, applied to current): **{len(pack)}**",
        "",
        "## Policy",
        "",
        "1. For every key on the target build, look at all older stocks that have it.",
        "2. If wording never changed → skip.",
        "3. Score each historical string for hardness (edge words, living hell, etc.; soft phrases reduce score).",
        "4. Pick **highest hardness**; ties → **oldest** version.",
        "5. If that beats current target → ship it in `01-classic-all.ini`.",
        "",
        "## Top pack restores (by hardness gain)",
        "",
    ]
    for m in sorted(meta, key=lambda x: -x["gain"])[:40]:
        md.append(
            f"### `{m['key']}`  (+{m['gain']} hard)  ← `{m['chosen_version']}`"
        )
        md.append(f"- Edge: {m['edge_chosen']} → target had {m['edge_target']}")
        md.append(f"- **Chosen:** {m['chosen_preview']}")
        md.append(f"- **Target (soft stock):** {m['target_preview']}")
        md.append("")

    md += [
        "## Top soften steps (history receipts)",
        "",
    ]
    for s in sorted(softens, key=lambda x: x.hardness_from - x.hardness_to, reverse=True)[:40]:
        md.append(
            f"### `{s.key}`  {s.from_version} → {s.to_version}  "
            f"(hard {s.hardness_from} → {s.hardness_to})"
        )
        md.append(f"- **From:** {s.from_preview}")
        md.append(f"- **To:** {s.to_preview}")
        md.append("")

    (args.reports / "all-keys-change-ledger.md").write_text("\n".join(md), encoding="utf-8")

    print(f"Pairwise wording changes: {len(step_changes)}")
    print(f"Softened steps: {len(softens)}  Hardened steps: {len(hardens)}")
    print(f"Pack keys (classic-all): {len(pack)}")
    print(f"Wrote {out_ini}")
    print(f"Wrote {meta_path}")
    print(f"Wrote {args.reports / 'all-keys-change-ledger.md'}")
    for m in sorted(meta, key=lambda x: -x["gain"])[:12]:
        print(f"  +{m['gain']:5.1f}  {m['key'][:50]:50}  ← {m['chosen_version']}")


if __name__ == "__main__":
    main()
