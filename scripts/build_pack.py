#!/usr/bin/env python3
"""Build an anti-soften localization pack from the soften map + corpus."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, plain, write_ini
from map_softening import discover_versions, edge_hits


def main() -> None:
    ap = argparse.ArgumentParser(description="Build classic-voice anti-soften pack")
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--corpus", type=Path, default=root / "corpus")
    ap.add_argument("--map", type=Path, default=root / "reports" / "soften-map.json")
    ap.add_argument("--out", type=Path, default=root / "packs" / "classic-voice-user.ini")
    ap.add_argument("--target", default=None)
    ap.add_argument("--min-score", type=float, default=10.0)
    args = ap.parse_args()

    if not args.map.exists():
        print(f"ERROR: run map_softening.py first ({args.map} missing)")
        sys.exit(1)

    data = json.loads(args.map.read_text(encoding="utf-8"))
    events = data["events"]
    versions = discover_versions(args.corpus)
    by_label = {label: load_ini(path) for label, path in versions}
    labels_sorted = [v[0] for v in versions]

    target = args.target or labels_sorted[-1]
    if target not in by_label:
        print(f"ERROR: target {target} not in corpus")
        sys.exit(1)
    target_ini = by_label[target]

    by_key: dict[str, list[dict]] = {}
    for ev in events:
        if ev["score"] < args.min_score:
            continue
        # High confidence: lost edge tokens, or real euphemism pair "a→b"
        if not ev.get("edge_lost") and not any(
            "\u2192" in h or "->" in h for h in (ev.get("euphemism_hits") or [])
        ):
            continue
        # Skip "lost:foo" only noise without edge_lost
        if not ev.get("edge_lost") and not any(
            "\u2192" in h for h in (ev.get("euphemism_hits") or [])
        ):
            continue
        by_key.setdefault(ev["key"], []).append(ev)

    pack: dict[str, str] = {}
    meta: list[dict] = []

    for key, evs in by_key.items():
        if key not in target_ini:
            continue
        conf = [
            e
            for e in evs
            if e.get("edge_lost")
            or any("\u2192" in h for h in (e.get("euphemism_hits") or []))
        ]
        if not conf:
            continue
        top = sorted(conf, key=lambda e: e["score"], reverse=True)[0]
        prefer_ver = top["from_version"]
        if prefer_ver not in by_label or key not in by_label[prefer_ver]:
            continue
        cand = by_label[prefer_ver][key]
        if plain(cand) == plain(target_ini[key]):
            continue
        # Must still carry at least one lost edge token when edge_lost is set
        lost = top.get("edge_lost") or []
        if lost and not any(tok in edge_hits(cand) for tok in lost):
            # still allow if text differs and was explicit from_version of soften
            if top["score"] < 20:
                continue
        pack[key] = cand
        meta.append(
            {
                "key": key,
                "source_version": prefer_ver,
                "score": top["score"],
                "edge_lost": top["edge_lost"],
                "euphemism_hits": top["euphemism_hits"],
            }
        )

    header = f"""
sc-classic-voice anti-soften pack
Generated for target stock: {target}
Keys: {len(pack)}
Import into Smart Citizen: Config → Import INI (user overrides, applied last)
Do NOT redistribute full CIG stock global.ini — this is a fan overlay delta only.
""".strip()

    ordered = {k: pack[k] for k in sorted(pack)}
    write_ini(args.out, ordered, header=header)
    meta_path = args.out.with_suffix(".meta.json")
    meta_path.write_text(
        json.dumps(
            {"target": target, "min_score": args.min_score, "key_count": len(ordered), "entries": meta},
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Pack keys: {len(ordered)}")
    print(f"Wrote {args.out}")
    print(f"Wrote {meta_path}")
    for m in sorted(meta, key=lambda x: -x["score"])[:20]:
        print(f"  [{m['score']}] {m['key']}  ← {m['source_version']}  lost={m['edge_lost']}")


if __name__ == "__main__":
    main()
