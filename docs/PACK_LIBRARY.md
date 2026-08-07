# Pack library — what to download

## Model (read this once)

```text
OLDER stock (≤4.7-ish)     →  HARD / unsoftened wording   ← we WANT this voice
NEWER stock (4.8+ p4k)     →  SOFT / CIG current wording  ← baseline of the live game

Pack = delta keys for CURRENT builds
     = hard wording (from history) applied onto latest key set
     ± community BP / XP / mission-details enhancements
```

**New missions that never existed pre-soften** are out of scope for auto-map (planned later: hand “OG voice” hardening).

---

## Downloads (under `packs/library/`)

| Pack | Keys (≈) | What it is | Use when |
|------|----------|------------|----------|
| **`01-classic-strict.ini`** | few | Only high-confidence **softens** (e.g. living hell → mess the place up) | You want surgical anti-soften only |
| **`01-classic-broad.ini`** | hundreds | **Oldest stock** narrative text for keys that changed over history | You want maximum “old SC voice” from stock history |
| **`02-community-mission-enhancements.ini`** | ~1.5k | BP / XP / MISSION DETAILS style layer (from community fixtures) | Layer-only; rarely import alone |
| **`composed-classic-strict-plus-community.ini`** | ~1.5k | Classic-strict **then** community enhancements | **Recommended default** with Smart Citizen-style extras |
| **`composed-classic-broad-plus-community.ini`** | ~2.1k | Classic-broad **then** community enhancements | Max classic + BP/XP |

Also:

| File | Role |
|------|------|
| `packs/classic-voice-user.ini` | Alias of **classic-strict** (small anti-soften pack) |

All of these are **deltas** (only changed keys) → Smart Citizen **Config → Import INI**, or merge with any overlay tool.

---

## Smart Citizen recipes

### A) Old hard wording only (current build)

1. Extract from Data.p4k  
2. Import **`01-classic-strict.ini`** or **`01-classic-broad.ini`**  
3. Apply  

### B) Old hard wording + BP/XP community style (current build)

1. Extract from Data.p4k  
2. Optional: enable Smart Citizen’s own enhancements **or**  
3. Import **`composed-classic-strict-plus-community.ini`** (or broad composed)  
4. Apply  

If you use **both** Smart Citizen auto-enhancements **and** our composed pack, import order / merge priority matters: user overrides should win. Prefer **one** community enhancement source to avoid double BP blocks.

### C) Smart Citizen enhancements + our strict softens only

1. Extract  
2. Enable SC mission BP/XP enhancements  
3. Import **`01-classic-strict.ini`** last  
4. Apply  

---

## Rebuild after a new SC patch

```bash
# 1) True stock from Data.p4k (not your customized install folder)
python3 ~/projects/sc-loc-mods/scripts/extract_stock_ini.py --channel LIVE
python3 ~/projects/sc-loc-mods/scripts/extract_stock_ini.py --channel PTU
# copy/link into corpus/ as 4.x.y-LIVE.ini / 4.x.y-PTU.ini

# 2) Maps (awareness + detection)
python3 scripts/diff_builds.py --target 4.10.0-PTU
python3 scripts/map_softening.py

# 3) Pack library
python3 scripts/build_library.py --target 4.10.0-PTU
```

---

## Maps (awareness / receipts)

| Report | Contents |
|--------|----------|
| `reports/build-diffs.md` | **All** text changes between consecutive builds |
| `reports/build-diffs.json` | Full machine-readable change log |
| `reports/key-history.json` | Per-key timeline vs latest stock |
| `reports/soften-map.md` | Soften / euphemism **candidates** (hard → soft detectors) |

Example (known):

| Key | Pre-soften (hard) | Post-soften (soft, 4.8+) |
|-----|-------------------|---------------------------|
| Headhunter multi bomb run | bomb the **living hell** out of the area | really **mess the place up** |
