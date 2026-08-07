#!/usr/bin/env python3
"""
Build the pack library:

  packs/library/
    01-classic-strict.ini     — soften/euphemism restores only
    01-classic-broad.ini      — oldest stock text for narrative keys that changed
    02-community-mission-enhancements.ini  — BP/XP style layer from fixtures
    composed-classic-strict-plus-community.ini
    composed-classic-broad-plus-community.ini

Classic packs are deltas vs --target stock (Import INI safe).
Community layer is derived from Smart Citizen / Kraken fixtures when present.

Usage:
  python3 scripts/build_library.py --target 4.10.0-PTU
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, plain, write_ini
from map_softening import discover_versions, edge_hits, event_score, euphemism_hits
from difflib import SequenceMatcher

NARRATIVE_RE = re.compile(
    r"(Desc|desc|Title|title|Journal|_GP_|Brief)",
    re.I,
)


def build_classic_strict(
    by_label: dict[str, dict[str, str]], labels: list[str], target: str, min_score: float
) -> dict[str, str]:
    target_ini = by_label[target]
    pack: dict[str, str] = {}
    for i, lab in enumerate(labels):
        if lab == target:
            break
        older = by_label[lab]
        for key, oval in older.items():
            if key not in target_ini:
                continue
            tval = target_ini[key]
            if oval == tval:
                continue
            lost = [e for e in edge_hits(oval) if e not in edge_hits(tval)]
            eu = euphemism_hits(oval, tval)
            sim = SequenceMatcher(None, plain(oval), plain(tval)).ratio()
            score = event_score(lost, [e for e in edge_hits(tval) if e not in edge_hits(oval)], eu, sim)
            if score < min_score and not lost:
                continue
            if not lost and not any("\u2192" in h or "→" in h for h in eu):
                continue
            # Prefer oldest successful restore
            if key not in pack:
                pack[key] = oval
    return pack


def build_classic_broad(
    by_label: dict[str, dict[str, str]], labels: list[str], target: str
) -> dict[str, str]:
    """For narrative keys on target: use oldest corpus value that differs."""
    target_ini = by_label[target]
    pack: dict[str, str] = {}
    for key, tval in target_ini.items():
        if not (NARRATIVE_RE.search(key) or len(plain(tval)) > 100):
            continue
        oldest_val = None
        oldest_lab = None
        for lab in labels:
            if lab == target:
                break
            if key in by_label[lab]:
                oldest_val = by_label[lab][key]
                oldest_lab = lab
                break
        if oldest_val is None or oldest_val == tval:
            continue
        # skip pure whitespace / trivial
        if plain(oldest_val).strip() == plain(tval).strip():
            continue
        pack[key] = oldest_val
    return pack


def build_community_layer(fixture_paths: list[Path], target_ini: dict[str, str]) -> dict[str, str]:
    """
    Load community enhancement fixtures. Keep only keys that exist in target
    stock and whose values look like enhancements (or differ with markers).
    """
    markers = (
        "MISSION DETAILS",
        "POTENTIAL BLUEPRINTS",
        "Potential Blueprints",
        "[BP]",
        "[BP?]",
        "Reputation XP",
        "ITEM REWARDS",
        "Multiple Blueprint",
    )
    layer: dict[str, str] = {}
    for fp in fixture_paths:
        if not fp.exists():
            print(f"  skip missing fixture {fp}")
            continue
        data = load_ini(fp)
        n = 0
        for key, val in data.items():
            if key not in target_ini:
                continue
            if any(m in val for m in markers) or any(m in plain(val) for m in markers):
                # Prefer longer / more enhanced if multiple fixtures
                if key not in layer or len(val) > len(layer[key]):
                    layer[key] = val
                    n += 1
        print(f"  {fp.name}: {n} enhancement keys usable on target")
    return layer


def main() -> None:
    ap = argparse.ArgumentParser()
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--corpus", type=Path, default=root / "corpus")
    ap.add_argument("--out-dir", type=Path, default=root / "packs" / "library")
    ap.add_argument("--target", default="4.10.0-PTU")
    ap.add_argument("--min-score", type=float, default=10.0)
    ap.add_argument(
        "--community-fixture",
        action="append",
        default=[],
        help="Path to community/Smart Citizen enhancement INI (repeatable)",
    )
    args = ap.parse_args()

    versions = discover_versions(args.corpus)
    labels = [v[0] for v in versions]
    by_label = {lab: load_ini(path) for lab, path in versions}
    if args.target not in by_label:
        print(f"ERROR: target {args.target} not in corpus: {labels}")
        sys.exit(1)

    target_path = dict(versions)[args.target]
    target_ini = by_label[args.target]
    args.out_dir.mkdir(parents=True, exist_ok=True)

    print("Building classic-strict…")
    strict = build_classic_strict(by_label, labels, args.target, args.min_score)
    write_ini(
        args.out_dir / "01-classic-strict.ini",
        dict(sorted(strict.items())),
        header=f"classic-strict: soften/euphemism restores only\ntarget={args.target}\nkeys={len(strict)}\nSmart Citizen: Import INI",
    )
    print(f"  → {len(strict)} keys")

    print("Building classic-broad…")
    broad = build_classic_broad(by_label, labels, args.target)
    write_ini(
        args.out_dir / "01-classic-broad.ini",
        dict(sorted(broad.items())),
        header=f"classic-broad: oldest stock text for narrative keys that changed\ntarget={args.target}\nkeys={len(broad)}\nSmart Citizen: Import INI",
    )
    print(f"  → {len(broad)} keys")

    fixtures = [Path(p) for p in args.community_fixture]
    if not fixtures:
        # defaults from smart-citizen research clone if present
        home = Path.home()
        fixtures = [
            home
            / "projects/reference/smart-citizen/tests/fixtures/mission_rewards_enhancements.ini",
            home / "projects/reference/smart-citizen/tests/fixtures/kraken_contracts_latest.ini",
            home / "projects/reference/smart-citizen/tests/fixtures/kraken_global_latest.ini",
        ]
    print("Building community mission enhancements layer…")
    community = build_community_layer(fixtures, target_ini)
    write_ini(
        args.out_dir / "02-community-mission-enhancements.ini",
        dict(sorted(community.items())),
        header=f"community BP/XP/mission-details style layer (from fixtures)\ntarget={args.target}\nkeys={len(community)}\nMerge with append_enhancements onto classic or stock",
    )
    print(f"  → {len(community)} keys")

    merge = root / "scripts" / "merge_layers.py"
    py = sys.executable

    def compose(classic_name: str, out_name: str) -> None:
        classic = args.out_dir / classic_name
        out = args.out_dir / out_name
        cmd = [
            py,
            str(merge),
            "--base",
            str(target_path),
            "--layer",
            f"{classic}:replace",
            "--layer",
            f"{args.out_dir / '02-community-mission-enhancements.ini'}:append_enhancements",
            "--out",
            str(out),
            "--delta-only",
        ]
        print("Compose", out_name, "…")
        subprocess.check_call(cmd)
        # count
        d = load_ini(out)
        print(f"  → composed delta {len(d)} keys")

    compose("01-classic-strict.ini", "composed-classic-strict-plus-community.ini")
    compose("01-classic-broad.ini", "composed-classic-broad-plus-community.ini")

    # index
    index = {
        "target": args.target,
        "packs": {
            "01-classic-strict.ini": {"keys": len(strict), "role": "old wording (softens only)"},
            "01-classic-broad.ini": {
                "keys": len(broad),
                "role": "oldest stock narrative wording for all changed narrative keys",
            },
            "02-community-mission-enhancements.ini": {
                "keys": len(community),
                "role": "BP/XP/mission-details style from community fixtures",
            },
            "composed-classic-strict-plus-community.ini": {
                "role": "classic-strict then community enhancements appended"
            },
            "composed-classic-broad-plus-community.ini": {
                "role": "classic-broad then community enhancements appended"
            },
        },
    }
    (args.out_dir / "INDEX.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print("Wrote", args.out_dir / "INDEX.json")
    print("Done.")


if __name__ == "__main__":
    main()
