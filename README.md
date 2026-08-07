# sc-classic-voice

**Restore less-softened Star Citizen localization wording** across patch history.

CIG occasionally rewrites mission and narrative strings toward softer / more corporate language (“bomb the living hell out of the area” → “really mess the place up”). This project:

1. **Maps** those changes across versioned stock `global.ini` extracts  
2. **Builds** a delta pack that re-applies the older wording on keys that still exist  
3. **Integrates** cleanly with [Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen) via **Import INI** → user overrides  

This is a **fan localization overlay** (same class of mod as community language packs). Not affiliated with CIG / RSI.

## Why not a full Smart Citizen fork?

Smart Citizen already does extract, merge, BP/XP enhancements, and Apply.  
**sc-classic-voice** only owns the *historical wording preference* layer — a small `user.ini`-style delta that Smart Citizen can import so your classic voice coexists with their auto enhancements.

## Quick start

### 1. Corpus (local stock extracts)

See [corpus/README.md](corpus/README.md). You need multiple versioned stock files, e.g. 4.3 → 4.10.

### 2. Map softens

```bash
python3 scripts/map_softening.py
```

Writes:

- `reports/soften-map.md` — human-readable  
- `reports/soften-map.json` / `.csv` — full event list  

### 3. Build the pack

```bash
python3 scripts/build_pack.py --target 4.10.0-PTU
```

Writes:

- `packs/classic-voice-user.ini` — **only changed keys** (Smart Citizen import)  
- `packs/classic-voice-user.meta.json` — which version each key came from  

### 4. Use with Smart Citizen

See **[docs/SMART_CITIZEN.md](docs/SMART_CITIZEN.md)**.

Short version: Extract → (optional enhancements) → **Import INI** `classic-voice-user.ini` → Apply.

## Example softens already detected (4.7 → 4.9+)

| Key | Older | Newer |
|-----|--------|--------|
| `headhunters_bombingrun_multi_E_CFP_desc_001` | bomb the **living hell** out of the area | really **mess the place up** |
| `headhunters_Nyx_bombingrun_M_desc_001` | **bomb** the life out of the fuel tanks | **blow** the life out of the fuel tanks |
| `headhunters_bombingrun_S_desc_001` | planning a **bombing run** | planning an **attack** |

Intersec **Strategic Bombing** (`Intersec_TSG_BombRun_*`) first appeared in **4.8** with the corporate memo text; there is no older stock body for that key in our corpus.

## Project layout

```text
sc-classic-voice/
├── README.md
├── docs/SMART_CITIZEN.md
├── corpus/           # local stock .ini (gitignored)
├── scripts/
│   ├── map_softening.py
│   ├── build_pack.py
│   └── ini_util.py
├── packs/            # generated delta INI (committed when small)
└── reports/          # soften map outputs
```

## Expanding the corpus

Whenever a new LIVE/PTU drops:

1. Extract stock `global.ini`  
2. Save as `corpus/{version}-{CHANNEL}.ini`  
3. Re-run map + build  
4. Review `soften-map.md` for new euphemisms; extend patterns in `map_softening.py` if needed  

## Legal

- Fan use of `global.ini` overlays is discussed by CIG in the [Community Localization Update](https://robertsspaceindustries.com/spectrum/community/SC/forum/1/thread/star-citizen-community-localization-update).  
- **Do not** commit or re-host full stock `global.ini` dumps from `Data.p4k` in this repo.  
- Star Citizen and related marks are property of Cloud Imperium.  
- Smart Citizen is Apache-2.0 by Osiris DevWorks — we integrate with it; we do not rebrand it.

## License

MIT for **scripts and docs** in this repository. Game string content remains CIG’s; the pack is a selection of historical official wording for personal/fan overlay use.
