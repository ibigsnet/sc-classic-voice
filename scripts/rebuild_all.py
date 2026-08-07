#!/usr/bin/env python3
"""One-shot rebuild: maps + classic packs + library + composed + spotlight + INDEX.

Usage:
  python3 scripts/rebuild_all.py --target 4.10.0-PTU
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    print("\n>>>", " ".join(cmd))
    subprocess.check_call(cmd, cwd=ROOT)


def count_ini(path: Path) -> int:
    if not path.exists():
        return 0
    n = 0
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            if not line.strip() or line.lstrip()[:1] in ";#" or "=" not in line:
                continue
            n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", default="4.10.0-PTU")
    ap.add_argument("--skip-maps", action="store_true", help="Skip soften/diff maps")
    args = ap.parse_args()
    py = sys.executable
    lib = ROOT / "packs" / "library"

    if not args.skip_maps:
        run([py, "scripts/map_softening.py"])
        run([py, "scripts/diff_builds.py", "--target", args.target])

    # Strict harder + at-least-as-hard classic packs
    run(
        [
            py,
            "scripts/build_classic_all.py",
            "--target",
            args.target,
            "--require-harder",
            "--name",
            "01-classic-all",
        ]
    )
    run(
        [
            py,
            "scripts/build_classic_all.py",
            "--target",
            args.target,
            "--no-require-harder",
            "--name",
            "01-classic-all-at-least-as-hard",
        ]
    )

    # strict/broad/community (+ partial compose)
    run([py, "scripts/build_library.py", "--target", args.target])

    # Compose classic-all variants with community (build_library only does strict/broad)
    merge = ROOT / "scripts" / "merge_layers.py"
    # Resolve target stock path via discover
    sys.path.insert(0, str(ROOT / "scripts"))
    from map_softening import discover_versions  # noqa: E402

    versions = dict(discover_versions(ROOT / "corpus"))
    if args.target not in versions:
        print(f"ERROR: target {args.target} not found")
        sys.exit(1)
    target_path = str(versions[args.target])
    community = str(lib / "02-community-mission-enhancements.ini")

    for classic, out_name in (
        ("01-classic-all.ini", "composed-classic-all-plus-community.ini"),
        (
            "01-classic-all-at-least-as-hard.ini",
            "composed-classic-all-at-least-as-hard-plus-community.ini",
        ),
    ):
        run(
            [
                py,
                str(merge),
                "--base",
                target_path,
                "--layer",
                f"{lib / classic}:replace",
                "--layer",
                f"{community}:append_enhancements",
                "--out",
                str(lib / out_name),
                "--delta-only",
            ]
        )

    run([py, "scripts/spotlight_diff.py"])
    run([py, "scripts/build_review_queue.py"])

    # Full INDEX with live counts
    packs = {
        "01-classic-all.ini": {
            "keys": count_ini(lib / "01-classic-all.ini"),
            "role": "Strictly HARDER than current soft stock (anti-soften core)",
        },
        "01-classic-all-at-least-as-hard.ini": {
            "keys": count_ini(lib / "01-classic-all-at-least-as-hard.ini"),
            "role": "Older wording when hardness ≥ current (recommended classic)",
        },
        "01-classic-broad.ini": {
            "keys": count_ini(lib / "01-classic-broad.ini"),
            "role": "Oldest stock narrative text whenever narrative keys changed",
        },
        "01-classic-strict.ini": {
            "keys": count_ini(lib / "01-classic-strict.ini"),
            "role": "High-confidence soften phrases only",
        },
        "02-community-mission-enhancements.ini": {
            "keys": count_ini(lib / "02-community-mission-enhancements.ini"),
            "role": "BP/XP/mission-details community layer",
        },
        "composed-classic-all-at-least-as-hard-plus-community.ini": {
            "keys": count_ini(
                lib / "composed-classic-all-at-least-as-hard-plus-community.ini"
            ),
            "role": "Recommended full: at-least-as-hard + community BP/XP",
        },
        "composed-classic-all-plus-community.ini": {
            "keys": count_ini(lib / "composed-classic-all-plus-community.ini"),
            "role": "strict-harder classic + community",
        },
        "composed-classic-broad-plus-community.ini": {
            "keys": count_ini(lib / "composed-classic-broad-plus-community.ini"),
            "role": "broad oldest + community",
        },
        "composed-classic-strict-plus-community.ini": {
            "keys": count_ini(lib / "composed-classic-strict-plus-community.ini"),
            "role": "strict softens + community",
        },
    }
    index = {
        "target": args.target,
        "policy": (
            "Walk ALL keys on the target build across ALL corpus versions. "
            "Skip placeholder/tag-only drift. Score hardness; pick higher "
            "hardness (ties → oldest). require_harder packs need gain>0."
        ),
        "maps": {
            "reports/build-diffs.md": "Every text change + phrase-level red/green diffs",
            "reports/all-keys-change-ledger.md": "Hardness-scored softens + pack restores",
            "reports/soften-map.md": "Heuristic soften detector with diffs",
            "reports/spotlight-hard-vs-soft-4.7-4.8.md": "Flagship Headhunter softens",
            "reports/review-queue.md": "Human review queue for high-confidence softens",
        },
        "packs": packs,
        "rebuild": "python3 scripts/rebuild_all.py --target " + args.target,
    }
    (lib / "INDEX.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print("\n=== INDEX (live counts) ===")
    for name, info in packs.items():
        print(f"  {info['keys']:5d}  {name}")
    print("\nDone.")


if __name__ == "__main__":
    main()
