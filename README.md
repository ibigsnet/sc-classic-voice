# sc-classic-voice

**Put the teeth back in Star Citizen’s text.**

Star Citizen used to sound like a hard sci-fi outlaw sandbox: rough contract briefings, blunt violence, Headhunters who talk like criminals. Over recent patches, Cloud Imperium has been sanding that down—mission copy gets softer, more corporate, more “please don’t offend anyone.” Edge becomes euphemism. “Bomb the living hell out of the area” becomes “really mess the place up.” That’s not polish. That’s the studio leaning **woke-adjacent / soy-safe** with the fiction, and it drags the whole game’s personality with it.

**This project exists to push back.**

We track wording changes across stock localization history and build **fan localization packs** that restore the less-softened (older, sharper) strings wherever those keys still exist. You can drop the pack into your install—or import it into [Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen)—and undo the studio’s recent tone policing in your client without waiting for CIG to grow a spine.

### We’ve seen this movie before

When a franchise loses its spine—new leadership, new “broad audience” mandate, identity sanded off for safety—the game dies long before the servers do. Halo is the cautionary tale: a property that once owned the culture, then got run into the ground by the wrong direction after the old soul left the building.

Worth the watch: **[Why Halo died](https://youtu.be/kkHVTAkaMdk)** (AndyPants Gaming).

Star Citizen is not Halo. Different studio, different tech debt, different mess. But the **pattern** is what we care about: when the fiction starts apologizing for itself, when edge becomes PR-safe mush, you’re watching the same slide. **We don’t want that outcome here.** Classic voice packs won’t fix netcode or ship balance—but they *do* keep the verse from sounding like it was rewritten for people who get the vapors at a Headhunters contract. Death by a thousand softens is still death.

### What we believe
- A mercenary game should **sound** like a mercenary game.  
- Softening every contract for maximum mass-market comfort is the **wrong direction**.  
- Players should be free to run **classic voice** on their own machines.  
- Localization overlays are the lawful, CIG-discussed channel for community string work—we use that lane to reject the watered-down rewrites.  
- Franchises die when they forget who they were for. We’re not waiting politely for SC to finish that journey.

### What this repo does
1. **Maps** softens across versioned stock `global.ini` extracts (4.3 → 4.10 and expanding)  
2. **Builds** a delta pack that re-applies older wording on keys that still exist  
3. **Integrates** with Smart Citizen via **Import INI** → user overrides (enhancements + classic voice together)  

This is a **fan localization overlay** (same class as community language packs). Not affiliated with CIG / RSI. Opinions in this README are the project’s; the tooling is MIT.

## Why not a full Smart Citizen fork?

Smart Citizen already does extract, merge, BP/XP enhancements, and Apply.  
**sc-classic-voice** is the *anti-soften / classic voice* layer—a small `user.ini`-style delta you import so their auto enhancements and our restored wording stack cleanly. Use both.

## Roadmap

See **[ROADMAP.md](ROADMAP.md)** for phases to full product (corpus, review, releases, patch loop).

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
