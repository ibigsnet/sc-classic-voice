#!/usr/bin/env python3
"""
Load hard/soft wordlists from wordlists/ for scoring and soften detection.

Lists are editable text files — expand them without rewriting Python heuristics.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

WORDLIST_DIR = Path(__file__).resolve().parent.parent / "wordlists"


def _read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


@lru_cache(maxsize=1)
def hard_words() -> list[str]:
    return _read_lines(WORDLIST_DIR / "hard-words.txt")


@lru_cache(maxsize=1)
def soft_words() -> list[str]:
    return _read_lines(WORDLIST_DIR / "soft-words.txt")


@lru_cache(maxsize=1)
def euphemism_pairs() -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    path = WORDLIST_DIR / "euphemism-pairs.tsv"
    if not path.exists():
        return pairs
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            continue
        a, b = line.split("\t", 1)
        pairs.append((a.strip(), b.strip()))
    return pairs


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    """Match phrase as whole words when single token; substring-safe for multiword."""
    parts = phrase.split()
    if len(parts) == 1:
        return re.compile(rf"\b{re.escape(phrase)}\b", re.I)
    # multiword: flexible whitespace
    body = r"\s+".join(re.escape(p) for p in parts)
    return re.compile(body, re.I)


@lru_cache(maxsize=1)
def hard_patterns() -> list[tuple[str, re.Pattern[str]]]:
    return [(w, _phrase_pattern(w)) for w in hard_words()]


@lru_cache(maxsize=1)
def soft_patterns() -> list[tuple[str, re.Pattern[str]]]:
    return [(w, _phrase_pattern(w)) for w in soft_words()]


def hard_hits(text: str) -> list[str]:
    t = text.replace("\\n", "\n")
    return [name for name, pat in hard_patterns() if pat.search(t)]


def soft_hits(text: str) -> list[str]:
    t = text.replace("\\n", "\n")
    return [name for name, pat in soft_patterns() if pat.search(t)]


def hardness_from_lists(text: str) -> float:
    """Score from editable wordlists only (boosts + penalties).

    Also applies euphemism-pairs.tsv: hard form present → boost;
    soft form present without hard form → penalty (so bomb→blow ranks).
    """
    t = text.replace("\\n", "\n")
    score = 0.0
    # longer phrases first conceptually — count each hit once
    for name, pat in hard_patterns():
        if pat.search(t):
            # weight multiword harder phrases more
            score += 8.0 + 4.0 * max(0, len(name.split()) - 1)
    for name, pat in soft_patterns():
        if pat.search(t):
            score -= 10.0
    # Known hard→soft substitutions (editable TSV)
    for hard_p, soft_p in euphemism_pairs():
        h_pat = _phrase_pattern(hard_p)
        s_pat = _phrase_pattern(soft_p)
        has_h = bool(h_pat.search(t))
        has_s = bool(s_pat.search(t))
        if has_h:
            score += 6.0 + 2.0 * max(0, len(hard_p.split()) - 1)
        elif has_s:
            score -= 12.0
    if len(text) > 200:
        score += 1.0
    return score


def list_stats() -> dict:
    return {
        "hard_words": len(hard_words()),
        "soft_words": len(soft_words()),
        "euphemism_pairs": len(euphemism_pairs()),
        "dir": str(WORDLIST_DIR),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(list_stats(), indent=2))
    sample = "bomb the living hell out of the area"
    soft = "really mess the place up"
    print("hard sample hits:", hard_hits(sample), "score", hardness_from_lists(sample))
    print("soft sample hits:", soft_hits(soft), "score", hardness_from_lists(soft))
