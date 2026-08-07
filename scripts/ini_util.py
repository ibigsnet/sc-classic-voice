"""Shared INI helpers for sc-classic-voice."""

from __future__ import annotations

from pathlib import Path


def load_ini(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n\r")
            if not line or line.lstrip()[:1] in ";#" or "=" not in line:
                continue
            key, value = line.split("=", 1)
            entries[key.strip()] = value
    return entries


def write_ini(path: Path, entries: dict[str, str], header: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="\n") as f:
        if header:
            for hline in header.strip().splitlines():
                f.write(f"; {hline}\n" if not hline.startswith(";") else f"{hline}\n")
            f.write("\n")
        for key, value in entries.items():
            f.write(f"{key}={value}\n")


def plain(value: str) -> str:
    return value.replace("\\n", "\n").replace("\\t", "\t")


def version_sort_key(label: str) -> tuple:
    """Sort labels like 4.7.0-LIVE before 4.9.0-LIVE before 4.10.0-PTU."""
    import re

    m = re.match(r"(\d+)\.(\d+)\.(\d+)", label)
    if not m:
        return (0, 0, 0, label)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), label)
