#!/usr/bin/env python3
"""
Merge localization layers onto a base stock global.ini.

Layer order (later wins for same key, unless merge mode says append):

  base stock
    + layer1.ini
    + layer2.ini
    ...

Modes per layer file header or CLI:
  replace (default) — full key value from layer
  append_enhancements — if layer value has SC-style enhancement blocks
                        not in base, append those blocks to current value

Usage:
  python3 scripts/merge_layers.py \\
    --base corpus/4.10.0-PTU.ini \\
    --layer packs/library/01-classic-broad.ini \\
    --layer packs/library/02-community-mission-enhancements.ini:append_enhancements \\
    --out packs/library/composed-classic-plus-community.ini \\
    --delta-only
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ini_util import load_ini, plain, write_ini

# Blocks Smart Citizen / StarStrings-style packs often append
ENHANCEMENT_MARKERS = (
    "MISSION DETAILS",
    "POTENTIAL BLUEPRINTS",
    "Potential Blueprints",
    "ITEM REWARDS",
    "BLUEPRINT DATA",
    "Reputation XP:",
    "Rewards Note",
    "Multiple Blueprint Pools",
    "<EM4>[BP]",
    "[BP]",
    "[BP?]",
    "--- STATS ---",
    "<EM3>STATS</EM3>",
)


def split_layer_arg(s: str) -> tuple[Path, str]:
    if ":" in s and not (len(s) > 2 and s[1] == ":"):  # avoid C:\ 
        # path:mode — mode is last colon segment if known
        path_s, mode = s.rsplit(":", 1)
        if mode in ("replace", "append_enhancements"):
            return Path(path_s), mode
    return Path(s), "replace"


def extract_appended_blocks(base_val: str, layer_val: str) -> str | None:
    """
    If layer_val is base + extras (or shares a long common prefix), return the
    suffix extras. Also handles title tags like 'Name <EM4>[BP]</EM4>'.
    """
    bp, lp = plain(base_val), plain(layer_val)
    if lp == bp:
        return None
    # Exact prefix append
    if lp.startswith(bp):
        extra = lp[len(bp) :]
        return extra.replace("\n", "\\n") if extra else None

    # Common prefix of substantial length
    i = 0
    max_i = min(len(bp), len(lp))
    while i < max_i and bp[i] == lp[i]:
        i += 1
    # require at least 40 chars shared or 60% of shorter
    if i >= 40 or i >= 0.6 * min(len(bp), len(lp)):
        extra = lp[i:]
        if any(m in extra for m in ENHANCEMENT_MARKERS) or extra.strip().startswith("<"):
            return extra.replace("\n", "\\n")

    # Title-style: layer adds [BP] / XP tags after title text
    if len(bp) < 200 and bp in lp and lp.index(bp) == 0:
        return lp[len(bp) :].replace("\n", "\\n")

    # Layer is full enhanced string: pull from first enhancement marker
    for m in ENHANCEMENT_MARKERS:
        if m in lp and m not in bp:
            idx = lp.index(m)
            # include a bit of leading newlines
            start = idx
            while start > 0 and lp[start - 1] in "\n\r":
                start -= 1
            extra = lp[start:]
            return ("\\n\\n" + extra.replace("\n", "\\n")).replace("\\n\\n\\n\\n", "\\n\\n")

    return None


def already_has_enhancements(val: str) -> bool:
    return any(m in val for m in ENHANCEMENT_MARKERS)


def merge_append(current: str, layer_val: str) -> str:
    extra = extract_appended_blocks(current, layer_val)
    if extra is None:
        # If layer is clearly enhancement-heavy and current has no markers, use layer wholesale
        if already_has_enhancements(layer_val) and not already_has_enhancements(current):
            # Prefer: keep current body, append extracted from layer vs empty base
            extra2 = extract_appended_blocks("", layer_val)
            # fall back: try strip layer down by finding MISSION DETAILS
            lp = plain(layer_val)
            for m in ("MISSION DETAILS", "POTENTIAL BLUEPRINTS", "Potential Blueprints"):
                if m in lp:
                    idx = lp.index(m)
                    start = idx
                    while start > 0 and lp[start - 1] in "\n":
                        start -= 1
                    return current + "\\n\\n" + lp[start:].replace("\n", "\\n")
            return layer_val  # last resort replace
        return current
    # avoid double-append
    if plain(extra).strip() and plain(extra).strip() in plain(current):
        return current
    if not current.endswith("\\n") and not extra.startswith("\\n"):
        return current + "\\n" + extra if extra else current
    return current + extra


def main() -> None:
    ap = argparse.ArgumentParser(description="Merge loc layers")
    ap.add_argument("--base", type=Path, required=True, help="Stock global.ini")
    ap.add_argument(
        "--layer",
        action="append",
        default=[],
        help="path or path:replace|append_enhancements (repeatable)",
    )
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument(
        "--delta-only",
        action="store_true",
        help="Write only keys that differ from base (Smart Citizen Import INI)",
    )
    args = ap.parse_args()

    base = load_ini(args.base)
    current = dict(base)
    stats = []

    for layer_arg in args.layer:
        path, mode = split_layer_arg(layer_arg)
        if not path.exists():
            print(f"ERROR: missing layer {path}")
            sys.exit(1)
        layer = load_ini(path)
        changed = 0
        for key, lval in layer.items():
            if key not in current:
                # only apply keys that exist in base for game safety unless not delta
                if key not in base and args.delta_only:
                    continue
                current[key] = lval
                changed += 1
                continue
            before = current[key]
            if mode == "append_enhancements":
                current[key] = merge_append(current[key], lval)
            else:
                current[key] = lval
            if current[key] != before:
                changed += 1
        stats.append({"layer": str(path), "mode": mode, "keys_in_layer": len(layer), "changed": changed})
        print(f"Layer {path.name} mode={mode}: touched {changed}")

    if args.delta_only:
        delta = {k: v for k, v in current.items() if k not in base or base[k] != v}
        header = "composed delta (differs from base stock)\n" + "\n".join(
            f"{s['layer']} [{s['mode']}] → {s['changed']} keys" for s in stats
        )
        write_ini(args.out, dict(sorted(delta.items())), header=header)
        print(f"Wrote delta {args.out} ({len(delta)} keys)")
    else:
        write_ini(args.out, current)
        print(f"Wrote full ini {args.out} ({len(current)} keys)")


if __name__ == "__main__":
    main()
