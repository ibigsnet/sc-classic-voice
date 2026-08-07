# Pack library — hard wording for current builds

Detection details (word lists, hardness formula): **[DETECTION.md](DETECTION.md)**.  
Logic audit: **[AUDIT.md](AUDIT.md)**.

## Goal

CIG softens strings over time. We:

1. **Compare every key** across **every banked stock** (as far back as we have)  
2. **Skip placeholder/tag-only drift** (e.g. `Stanton` → `~mission(System)`)  
3. **Score hardness** (hard words boost; soft/euphemism forms penalize)  
4. **Pick older / harder** text  
5. Ship that as a **delta pack for the latest build** (keys that still exist)

**Not yet:** inventing OG voice for brand-new missions that never had old stock (planned later).

---

## How comparison works

```text
For each key on TARGET (e.g. 4.10 p4k stock):
  history = [text from 4.3.2, 4.4, …, 4.9] if key exists
  if all history == target → skip
  if only mission-tokens/tags differ → skip (not a soften)
  score each historical string for HARDNESS
  winner = max hardness; ties → OLDEST version
  01-classic-all:          only if hardness strictly higher than target
  01-classic-all-at-least-as-hard: if hardness ≥ target
```

Full receipts:

| Report | What |
|--------|------|
| [`reports/build-diffs.md`](../reports/build-diffs.md) | **All** text changes + red/green phrase diffs |
| [`reports/all-keys-change-ledger.md`](../reports/all-keys-change-ledger.md) | Strict pack restores (hardness gain > 0) |
| [`reports/soften-map.md`](../reports/soften-map.md) | Heuristic soften detector |
| [`reports/spotlight-hard-vs-soft-4.7-4.8.md`](../reports/spotlight-hard-vs-soft-4.7-4.8.md) | Flagship living-hell / bomb-run |
| [`reports/review-queue.md`](../reports/review-queue.md) | Human review checklist |

Rebuild everything:

```bash
python3 scripts/rebuild_all.py --target 4.10.0-PTU
```

---

## Download which pack?

Live counts from `packs/library/INDEX.json` (regenerated on rebuild):

| Pack | Role |
|------|------|
| **`01-classic-all-at-least-as-hard.ini`** | **Recommended classic** — older wording when hardness ≥ current |
| **`composed-classic-all-at-least-as-hard-plus-community.ini`** | **Recommended full** — classic + BP/XP community |
| **`01-classic-all.ini`** | Surgical — only **strictly harder** than stock (anti-soften core) |
| `01-classic-broad.ini` | Oldest narrative stock whenever text changed (no hardness gate) |
| `01-classic-strict.ini` | Tiny high-confidence soften phrases only |
| `02-community-mission-enhancements.ini` | BP / XP / MISSION DETAILS style (community fixtures) |
| `composed-classic-all-plus-community.ini` | Strict-harder classic + community |
| `composed-classic-broad-plus-community.ini` | Broad oldest + community |

See `packs/library/INDEX.json` for exact key counts after each rebuild.

---

## Smart Citizen

https://github.com/Osiris-DevWorks/smart-citizen

1. Extract from Data.p4k (current soft stock)  
2. **Import INI** → choose pack above  
3. Apply  

| Want | Import |
|------|--------|
| Hard wording only | `01-classic-all-at-least-as-hard.ini` |
| Hard wording + BP/XP | `composed-classic-all-at-least-as-hard-plus-community.ini` |
| Surgical softens only | `01-classic-all.ini` or `01-classic-strict.ini` |

---

## Stack

```text
current p4k stock (soft baseline)
  + classic-all*          ← older/harder from history
  + community BP/XP       ← optional second layer
  = playable current build with OG voice
```
