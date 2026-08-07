# Examples map — hard vs soft wording across builds

This page answers: **Did we compare everything we have?** and **What does a real soften look like?**

---

## Coverage status (honest)

### ✅ Fully compared (our banked corpus)

Every **consecutive** pair of stocks we hold was fully key-diffed. Every key on the **target** build (`4.10.0-PTU`) was checked against **all older** banked versions.

| # | From | To | Text changes |
|---|------|----|-------------:|
| 1 | 4.3.2-LIVE | 4.4.0-PTU | 582 |
| 2 | 4.4.0-PTU | 4.5.0-LIVE | 128 |
| 3 | 4.5.0-LIVE | 4.6.0-LIVE | 25 |
| 4 | 4.6.0-LIVE | 4.6.0-PTU | 123 |
| 5 | 4.6.0-PTU | 4.7.0-LIVE | 334 |
| 6 | 4.7.0-LIVE | 4.7.0-LIVE-HOTFIX | 0 |
| 7 | 4.7.0-LIVE-HOTFIX | 4.7.0-PTU | 0 |
| 8 | 4.7.0-PTU | 4.7.1-LIVE | 1 |
| 9 | 4.7.1-LIVE | **4.8.0-PTU** | **359** |
| 10 | 4.8.0-PTU | 4.9.0-LIVE | 89 |
| 11 | 4.9.0-LIVE | 4.10.0-PTU | 86 |
| | **Total consecutive wording changes** | | **1,727** |

Additional stats on target `4.10.0-PTU`:

| Metric | Count |
|--------|------:|
| Keys with ≥2 distinct texts in history | 1,538 |
| Keys where some older text scores **harder** than current soft stock | **14** |
| Pack: older wording ≥ as hard as current (`01-classic-all-at-least-as-hard.ini`) | **~1,512** |
| Pack: classic + BP/XP community (`composed-classic-all-at-least-as-hard-plus-community.ini`) | **~2,960** |

### ❌ Not 100% of all Star Citizen history

We do **not** yet have stock extracts for e.g. **3.x**, **4.0–4.2**, or final **4.8 LIVE** (we have **4.8.0-PTU**). Those gaps are why the bank keeps growing — see [CORPUS_SOURCES.md](CORPUS_SOURCES.md).

**Within the 12 versions we bank: yes — every pair is compared; every target key is evaluated.**

---

## Flagship example: “living hell” → “mess the place up”

**Key:** `headhunters_bombingrun_multi_E_CFP_desc_001`  
**Mission voice:** Headhunters / Stows (bomb run vs CFP)

### Timeline (all banked stocks)

| Version | Phrase in stock |
|---------|-----------------|
| 4.3.2-LIVE | **bomb the living hell out of the area** |
| 4.4.0-PTU | living hell |
| 4.5.0-LIVE | living hell |
| 4.6.0-LIVE / PTU | living hell |
| 4.7.0-LIVE / HOTFIX / PTU | living hell |
| 4.7.1-LIVE | living hell |
| **4.8.0-PTU** | **really mess the place up** ← soft begins |
| 4.9.0-LIVE (fresh p4k) | mess the place up |
| 4.10.0-PTU (fresh p4k) | mess the place up |

### Side by side (VCS-style)

Wide three-row tables hide the edit. Prefer a **unified diff** (GitHub paints `-` red, `+` green):

```diff
# 4.7.1-LIVE  →  4.8.0-PTU / 4.10.0-PTU
- bomb the living hell out of the area.
+ really mess the place up.
```

| **HARD (4.7.1 stock)** | **SOFT (4.10.0 p4k stock)** |
|------------------------|-----------------------------|
| …Head to ~mission(Location\|Address) and **bomb the living hell out of the area**. | …Head to ~mission(Location\|Address) and **really mess the place up**. |

Same mission, same key — CIG changed one sentence.  
**Our pack restores the hard line on current builds.**

Full multi-key spotlight with change tables + inline `~~removed~~` / `**added**` markup:  
[`reports/spotlight-hard-vs-soft-4.7-4.8.md`](../reports/spotlight-hard-vs-soft-4.7-4.8.md)  
(regenerate: `python3 scripts/spotlight_diff.py`)

---

## More clear hard → soft examples

### 1. “bomb the life” → “blow the life”

**Key:** `headhunters_Nyx_bombingrun_M_desc_001`

| HARD (4.7.0) | SOFT (4.10) |
|--------------|-------------|
| …fly over there and **bomb the life out of the fuel tanks**. | …fly over there and **blow the life out of the fuel tanks**. |

Tiny word swap; hardness score still treats **bomb** as harder.

### 2. “bombing run” → “attack”

**Key:** `headhunters_bombingrun_S_desc_001`

| HARD (4.7.0) | SOFT (4.10) |
|--------------|-------------|
| a new gang are planning a **bombing run** on a place… | a new gang are planning an **attack** on a place… |

### 3. Industrial mission tone → corporate “purchase order”

**Keys:** several `Shubin_Industrial_ShipMining_*_Desc_001`

| HARD-er older (4.6.0-PTU style) | SOFT-er newer (4.10) |
|---------------------------------|----------------------|
| **POSTING: Industrial** / REQ EXPERIENCE: Ship Mining / “in need of a variety of ore…” | **POSTING: Purchase Order** / “sourcing pipeline” / “fulfil another purchase order…” |

Not always “swear words removed” — sometimes **corporate rewrite**. Hardness scoring still flags many of these; broad pack can restore older industrial framing.

---

## What is *not* a “soften” (but still a change)

Most of the **1,727** pairwise changes are:

- New items / ships / missions  
- Balance or system renames  
- Placeholder cleanup  
- Lore updates that don’t reduce edge  

We still **map all of them** in [`reports/build-diffs.md`](../reports/build-diffs.md).  
The **anti-soft pack** only **overrides** keys where older text wins on **hardness** (or ≥ hardness + older).

| Layer | Role |
|-------|------|
| Full map | Awareness — every wording change we can prove |
| Classic pack | Playable — hard wording on **current** keys |
| + Community | BP / XP / mission-details style on top |

---

## How to re-read the maps on GitHub

**Every report uses VCS-style wording diffs** (shared `scripts/phrase_diff.py`):

- Change table: only the tokens that moved  
- Unified `diff` fence: GitHub paints `-` **red** / `+` **green**  
- High-sim softens also get inline `~~removed~~` / `**added**`  
- Full string previews folded under `<details>`  

1. **This page** — human examples  
2. [`reports/build-diffs.md`](../reports/build-diffs.md) — consecutive change counts + high-sim red/green samples  
3. [`reports/all-keys-change-ledger.md`](../reports/all-keys-change-ledger.md) — hardness ledger with diffs per restore  
4. [`reports/soften-map.md`](../reports/soften-map.md) — soften candidates with phrase diffs  
5. [`reports/spotlight-hard-vs-soft-4.7-4.8.md`](../reports/spotlight-hard-vs-soft-4.7-4.8.md) — living hell deep dive  
6. [`reports/hard-to-soft-examples.json`](../reports/hard-to-soft-examples.json) — machine list of hardness wins vs target  

Regenerate everything:

```bash
python3 scripts/map_softening.py
python3 scripts/diff_builds.py
python3 scripts/build_classic_all.py --target 4.10.0-PTU
python3 scripts/spotlight_diff.py
```

---

## Download packs (apply hard text to new builds)

See [PACK_LIBRARY.md](PACK_LIBRARY.md).

| Pack | What you get |
|------|----------------|
| `01-classic-all-at-least-as-hard.ini` | Older/harder wording for current game |
| `composed-classic-all-at-least-as-hard-plus-community.ini` | Same + BP/XP community layer |

Import via [Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen) → Config → Import INI → Apply.
