#!/usr/bin/env python3
"""Build corpus/manifest.json from versioned .ini files in corpus/."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, version_sort_key


def sha256_file(path: Path, max_bytes: int | None = None) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        if max_bytes is None:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        else:
            h.update(f.read(max_bytes))
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--corpus", type=Path, default=root / "corpus")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    out = args.out or (args.corpus / "manifest.json")

    entries = []
    for p in sorted(args.corpus.glob("*.ini")):
        if p.name.endswith("-global.ini"):
            continue
        label = p.stem
        data = load_ini(p)
        m = re.match(r"(\d+\.\d+\.\d+)-([A-Z0-9-]+)", label)
        entries.append(
            {
                "label": label,
                "game_version": m.group(1) if m else label,
                "channel": m.group(2) if m else "UNKNOWN",
                "path": p.name,
                "resolved": str(p.resolve()),
                "bytes": p.stat().st_size,
                "key_count": len(data),
                "sha256": sha256_file(p),
                "quality": "stock",  # author may edit after review
            }
        )
    entries.sort(key=lambda e: version_sort_key(e["label"]))
    doc = {
        "description": "Local stock global.ini corpus for sc-classic-voice. Full files are not committed to git.",
        "count": len(entries),
        "versions": entries,
    }
    out.write_text(json.dumps(doc, indent=2), encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} versions)")
    for e in entries:
        print(f"  {e['label']:16} keys={e['key_count']:6}  {e['bytes']/1e6:.1f} MB")


if __name__ == "__main__":
    main()
