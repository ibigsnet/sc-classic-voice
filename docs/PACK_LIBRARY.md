# Pack library — hard wording for current builds

## Goal

Detection details (word lists, hardness formula): **[DETECTION.md](DETECTION.md)**.


CIG softens strings over time. We:

1. **Compare every key** across **every banked stock** (as far back as we have)  
2. **Detect when wording changed** between builds  
3. **Pick older / harder** text  
4. Ship that as a **delta pack for the latest build** (keys that still exist)

**Not yet:** inventing OG voice for brand-new missions that never had old stock (planned later).

---

## How comparison works

```text
For each key on TARGET (e.g. 4.10 p4k stock):
  history = [text from 4.3.2, 4.4, …, 4.9] if key exists
  if all history == target → skip
  score each historical string for HARDNESS
    (living hell, bomb, kill, shit, … boost;
     mess the place up, neutralize, kindly, … reduce)
  winner = max hardness; ties → OLDEST version
  if winner is harder (or ≥ target) than current stock → pack it
```

Full receipts:

| Report | What |
|--------|------|
| [`reports/build-diffs.md`](../reports/build-diffs.md) | **All** text changes between consecutive builds (~1.7k steps) |
| [`reports/all-keys-change-ledger.md`](../reports/all-keys-change-ledger.md) | Soften steps + hardness-based restores |
| [`reports/all-keys-step-changes.json`](../reports/all-keys-step-changes.json) | Machine full step list |
| [`reports/spotlight-hard-vs-soft-4.7-4.8.md`](../reports/spotlight-hard-vs-soft-4.7-4.8.md) | Famous living-hell example with red/green wording diffs |

Rebuild:

```bash
python3 scripts/diff_builds.py --target 4.10.0-PTU
python3 scripts/build_classic_all.py --target 4.10.0-PTU --require-harder --name 01-classic-all
python3 scripts/build_classic_all.py --target 4.10.0-PTU --no-require-harder --name 01-classic-all-at-least-as-hard
python3 scripts/build_library.py --target 4.10.0-PTU   # broad + community + some composed
# then merge_layers for classic-all ± community (see scripts)
```

---

## Download which pack?

| Pack | ~Keys | Use |
|------|------:|-----|
| **`01-classic-all.ini`** | 14 | Only strings **strictly harder** than current soft stock |
| **`01-classic-all-at-least-as-hard.ini`** | **1512** | **Recommended classic:** older wording when ≥ as hard as now |
| **`01-classic-broad.ini`** | 608 | Oldest narrative stock whenever text changed (no hardness gate) |
| **`01-classic-strict.ini`** | 4 | Tiny phrase-level softens only |
| **`02-community-mission-enhancements.ini`** | 1570 | BP / XP / MISSION DETAILS style (community fixtures) |
| **`composed-classic-all-at-least-as-hard-plus-community.ini`** | **2960** | **Recommended full:** classic + BP/XP |
| `composed-classic-all-plus-community.ini` | 1576 | Strict-harder classic + community |
| `composed-classic-broad-plus-community.ini` | 2134 | Broad oldest + community |

See `packs/library/INDEX.json` for exact counts.

---

## Smart Citizen

https://github.com/Osiris-DevWorks/smart-citizen

1. Extract from Data.p4k (current soft stock)  
2. **Import INI** → choose pack above  
3. Apply  

Recipes:

| Want | Import |
|------|--------|
| Hard wording only | `01-classic-all-at-least-as-hard.ini` |
| Hard wording + BP/XP community style | `composed-classic-all-at-least-as-hard-plus-community.ini` |
| Surgical softens only | `01-classic-all.ini` or `01-classic-strict.ini` |

---

## Stack

```text
current p4k stock (soft baseline)
  + classic-all*          ← older/harder from history
  + community BP/XP       ← optional second layer
  = playable current build with OG voice
```
