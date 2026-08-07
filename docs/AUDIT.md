# Project audit — logic check (2026-08-07)

Deep dive after the first full pipeline (corpus → maps → packs → red/green diffs).

## North star (still correct)

| Intent | Status |
|--------|--------|
| Restore **older, harder** stock wording on **current** keys | ✅ Core design |
| Evidence from banked stocks, not invented fanfic | ✅ |
| Compose with Smart Citizen (Import INI) | ✅ docs + pack format |
| Show softens with receipts | ✅ phrase_diff everywhere |

## Architecture (logical flow)

```text
corpus/*.ini (symlinks → archives/bank)
        │
        ├─ map_softening.py  → soften-map (heuristic tone softens)
        ├─ diff_builds.py    → full pairwise change map
        └─ build_classic_all.py → hardness pick → classic packs
                │
                ├─ 01-classic-all              (require harder)
                └─ 01-classic-all-at-least-as-hard
        build_library.py → strict / broad / community
        merge_layers.py  → composed classic + BP/XP
        phrase_diff.py   → red/green presentation (all reports)
```

This is coherent: **detect → pick → pack → display**.

## What was wrong (fixed or flagged)

### 1. High-sim “prefer oldest” packed noise (FIXED)

`01-classic-all` claimed “strictly harder” but after wordlist wiring it shipped **~709 keys**, of which **~638 had hardness gain ≤ 0**.

Examples of junk restores:

- `Stanton` → `~mission(System)` (placeholder modernization)
- `Address` → `Destination|Target|Address` (token shape change)
- `be` → `bet` (typo fix)

**Root cause:** for `sim ≥ 0.88`, `require_harder` always accepted the oldest text even with zero hardness gain.

**Fix:**

- `content_fingerprint()` — strip mission tokens / tags; if equal, skip (not a soften).
- `require_harder` now requires **hardness gain > 0** (or more edge hits).
- `at-least-as-hard` requires **hardness gain ≥ 0** (never pack softer history).

### 2. Stale docs vs live packs (FIXED in same pass)

| Claim (old INDEX / PACK_LIBRARY) | Reality before fix |
|----------------------------------|--------------------|
| classic-all = **14** keys | was **709** (mostly noise) |
| at-least-as-hard = **1512** | was **1263** on disk |
| README “build_pack.py only” | real product is pack **library** + rebuild_all |

### 3. Packs out of sync with each other

Only `01-classic-all` was regenerated with new wordlists/diffs; composed packs lagged.  
**Fix:** `scripts/rebuild_all.py` rebuilds maps → both classic packs → library → composed → spotlight → review queue → INDEX.

### 4. Low-sim “harder” lore / newspapers (FLAGGED)

Some restores (e.g. full `Journal_General_FrontendNewspaperHeadlines_Content` swap) are **different articles**, not tone softens. Hardness can still rise if older text has kill/execute words.

**Mitigation later:** denylist journal headlines, or require high/med sim for pack unless human-allowlisted. Not auto-fixed yet — appears in review queue.

### 5. Soft wordlist can reverse-score industrial rewrites

`purchase order` / `sourcing pipeline` in `soft-words.txt` correctly lower **new** industrial copy, so older “POSTING: Industrial” wins. That’s intentional reverse-corporate, but it’s **not** the same class as living hell. Review queue should separate:

| Class | Example |
|-------|---------|
| Tone soften | living hell → mess the place up |
| Corporate rewrite | Industrial → Purchase Order |
| Lore / news rewrite | Terra Gazette ↔ Vox Populi |
| Placeholder noise | ~~should no longer pack~~ |

## What is solid

- Flagship Headhunter bomb-run softens detected and restored (CFP / Nyx / S).
- Phrase-level red/green diffs on all major reports.
- Editable `wordlists/` as reverse of studio sanitize lists (honest SOURCES.md).
- Corpus discovery across 4.3.2 → 4.10 with 4.8.0-PTU filled.
- Community BP/XP as a **separate** layer (correct separation of concerns).

## Recommended player path (post-fix)

1. **Primary classic:** `01-classic-all-at-least-as-hard.ini`  
2. **Full stack:** `composed-classic-all-at-least-as-hard-plus-community.ini`  
3. **Surgical anti-soften only:** `01-classic-all.ini` (strict harder)  
4. Import via Smart Citizen after extract.

## Rebuild command

```bash
python3 scripts/rebuild_all.py --target 4.10.0-PTU
```

## Next product steps (priority)

1. Human-review `reports/review-queue.md` → allowlist curated pack for v0.2 release  
2. `docs/INSTALL.md` player path + tag GitHub Release  
3. Optional denylist: newspapers / pure item-stat rewrites  
4. Patch runbook after next LIVE/PTU stock bank  
5. Personal Ironchad / BP overlays stay out of public classic packs  

## Post-fix pack counts (after rebuild)

| Pack | Keys | Notes |
|------|-----:|-------|
| `01-classic-all` | ~76 | All positive hardness gain; includes all 3 flagship Headhunter softens |
| `01-classic-all-at-least-as-hard` | ~1165 | Gain ≥ 0; recommended classic |
| `composed-…-at-least-as-hard-plus-community` | ~2655 | Classic + BP/XP |
| `01-classic-strict` | ~7 | Soften-map edge/euphemism only |

Flagship scoring after wordlist fix:

```text
bomb the life …  → high positive
blow the life …  → soft penalty (no longer listed as hard)
bombing run      → hard; "an attack" via euphemism pair
living hell      → hard; mess the place up → soft
```

## Decision log

| Date | Decision |
|------|----------|
| 2026-08-07 | Prefer evidence from stock history over fan rewrites |
| 2026-08-07 | Phrase-level VCS diffs everywhere (not full-string walls) |
| 2026-08-07 | High-sim alone is **not** enough for require_harder; need hardness/edge gain |
| 2026-08-07 | Placeholder/token-only drift is not classic voice |
| 2026-08-07 | Soft substitutes must not appear on the hard list (broke bomb→blow) |
