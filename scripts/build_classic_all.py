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
    """Higher = harder / more OG-unsoftened voice.

    Keyword lists are *boosts*, not the only signal. Primary selection uses
    full text history + similarity (see pick_best_historical).
    """
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


def word_set(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z']+", plain(text).lower()))


def unique_word_edge(old: str, new: str) -> float:
    """
    Diff-based signal without a huge lexicon: words only in older vs only in newer.
    Slightly prefer older if it has more unique content words (often the removed edge).
    """
    o, n = word_set(old), word_set(new)
    only_old = o - n
    only_new = n - o
    # ignore very common words
    stop = {
        "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "is", "are",
        "be", "this", "that", "with", "at", "as", "it", "you", "we", "they", "from",
        "will", "can", "have", "has", "been", "was", "were", "by", "not", "but",
    }
    only_old = {w for w in only_old if w not in stop and len(w) > 2}
    only_new = {w for w in only_new if w not in stop and len(w) > 2}
    return float(len(only_old) - len(only_new))


def pick_best_historical(
    candidates: list[tuple[str, str, float]],
    tval: str,
    older_labels: list[str],
    *,
    require_harder: bool,
    min_hardness_gain: float,
) -> tuple[str, str, float, str] | None:
    """
    Smart pick among historical (label, value, hardness) vs target tval.

    Priority (not hardcoded-only):
      1. HIGH similarity to target (≥0.88): same sentence rewritten → prefer
         OLDEST different text (classic soften / euphemism case).
      2. MED similarity (0.45–0.88): prefer higher hardness, then older;
         word-diff boost for tokens only in older.
      3. LOW similarity (<0.45): major rewrite → only take older if clearly
         harder (avoid restoring obsolete lore as "tone").

    Returns (label, value, hardness, reason) or None.
    """
    t_hard = hardness_score(tval)
    t_plain = plain(tval)

    # Rank candidates with a sort key (higher tuple wins)
    ranked: list[tuple] = []
    for lab, val, h in candidates:
        if val == tval:
            continue
        sim = SequenceMatcher(None, plain(val), t_plain).ratio()
        age = older_labels.index(lab)  # smaller = older
        wdiff = unique_word_edge(val, tval)
        h_gain = h - t_hard

        if sim >= 0.88:
            # Near-paraphrase: age is king; hardness/word-diff break ties
            sort_key = (3, -age, h_gain, wdiff, h)
            reason = f"high_sim={sim:.3f}_prefer_oldest"
        elif sim >= 0.45:
            sort_key = (2, h_gain, wdiff, h, -age)
            reason = f"med_sim={sim:.3f}_prefer_harder"
        else:
            # Major rewrite — only compete if clearly harder
            if h_gain <= max(min_hardness_gain, 5.0):
                continue
            sort_key = (1, h_gain, h, -age)
            reason = f"low_sim={sim:.3f}_harder_only"

        ranked.append((sort_key, lab, val, h, reason, sim, h_gain))

    if not ranked:
        return None

    ranked.sort(key=lambda x: x[0], reverse=True)
    _sk, lab, val, h, reason, sim, h_gain = ranked[0]

    if require_harder:
        # high-sim softens: always allow oldest even if hardness score is flat
        if sim < 0.88 and h_gain <= min_hardness_gain:
            if not (
                h_gain >= -0.01 and len(edge_hits(val)) > len(edge_hits(tval))
            ):
                return None
    else:
        # at-least-as-hard OR high-sim older rewrite
        if sim < 0.88 and h_gain < min_hardness_gain:
            return None

    return lab, val, h, f"{reason};gain={h_gain:.1f}"


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

    # --- Per-key smart pick: all historical diffs, then older/harder ---
    for key, tval in target_ini.items():
        candidates: list[tuple[str, str, float]] = []  # label, value, hardness
        for lab in older_labels:
            if key not in by_label[lab]:
                continue
            val = by_label[lab][key]
            candidates.append((lab, val, hardness_score(val)))
        if not candidates:
            continue
        t_hard = hardness_score(tval)
        texts = {c[1] for c in candidates}
        texts.add(tval)
        if len(texts) == 1:
            continue  # never changed

        picked = pick_best_historical(
            candidates,
            tval,
            older_labels,
            require_harder=args.require_harder,
            min_hardness_gain=args.min_hardness_gain,
        )
        if picked is None:
            continue
        best_lab, best_val, best_h, reason = picked
        if best_val == tval:
            continue

        gain = best_h - t_hard
        pack[key] = best_val
        meta.append(
            {
                "key": key,
                "chosen_version": best_lab,
                "pick_reason": reason,
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
            f"Policy: full history compare; high-sim→oldest; med-sim→harder; "
            f"low-sim→harder-only; keyword boosts secondary\n"
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
