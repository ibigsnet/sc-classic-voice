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
1. **Banks** stock English localization from as many old patches as we can get (Data.p4k extracts / community archives — see [docs/CORPUS_SOURCES.md](docs/CORPUS_SOURCES.md))  
2. **Maps** softens across that history so the changes are **visible with receipts** (not vibes alone)  
3. **Builds** a delta pack that re-applies older, sharper wording on keys that still exist  
4. **Integrates** with Smart Citizen via **Import INI** → user overrides (enhancements + classic voice together)  

**Two jobs, one project:** give players the **old-style Star Citizen voice** they backed — and **bring the softens to light** so the community can see what was rewritten.

This is a **fan localization overlay** (same class as community language packs). Not affiliated with CIG / RSI. Opinions in this README are the project’s; the tooling is MIT.

## Why not a full Smart Citizen fork?

Smart Citizen already does extract, merge, BP/XP enhancements, and Apply.  
**sc-classic-voice** is the *anti-soften / classic voice* layer—a small `user.ini`-style delta you import so their auto enhancements and our restored wording stack cleanly. Use both.

## Examples (hard vs soft)

**Clear side-by-side map of real softens** (living hell → mess the place up, etc.) and full coverage status:

→ **[docs/EXAMPLES.md](docs/EXAMPLES.md)**

## Download packs

| Want | File |
|------|------|
| **Older/harder wording** (recommended) | [`packs/library/01-classic-all-at-least-as-hard.ini`](packs/library/01-classic-all-at-least-as-hard.ini) |
| **Older/harder + BP/XP community** | [`packs/library/composed-classic-all-at-least-as-hard-plus-community.ini`](packs/library/composed-classic-all-at-least-as-hard-plus-community.ini) |
| Strict “harder than stock only” | [`packs/library/01-classic-all.ini`](packs/library/01-classic-all.ini) |
| Maps / receipts | [`reports/build-diffs.md`](reports/build-diffs.md), [`reports/all-keys-change-ledger.md`](reports/all-keys-change-ledger.md) |

Full guide: **[docs/PACK_LIBRARY.md](docs/PACK_LIBRARY.md)**. Works with **[Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen)** (Import INI).

## Related projects

| Project | Role | Link |
|---------|------|------|
| **Smart Citizen** | Full localization editor: extract from `Data.p4k`, BP/XP/stat enhancements, Apply + backups. **Import our pack as user overrides.** | [github.com/Osiris-DevWorks/smart-citizen](https://github.com/Osiris-DevWorks/smart-citizen) |
| Smart Citizen releases | Windows installer / portable builds | [Releases](https://github.com/Osiris-DevWorks/smart-citizen/releases) |
| Smart Citizen on Linux | Wine / same prefix as SC | [docs/LINUX.md](https://github.com/Osiris-DevWorks/smart-citizen/blob/main/docs/LINUX.md) |
| This pack + Smart Citizen | Step-by-step import order | **[docs/SMART_CITIZEN.md](docs/SMART_CITIZEN.md)** |

**sc-classic-voice does not replace Smart Citizen.** Use Smart Citizen for extract, enhancements, and Apply; use this repo for the **classic / unsoftened wording** layer.

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

Install **[Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen)** first ([releases](https://github.com/Osiris-DevWorks/smart-citizen/releases)).

Full steps: **[docs/SMART_CITIZEN.md](docs/SMART_CITIZEN.md)**.

Short version:

1. Smart Citizen → **Extract from Data.p4k**  
2. (Optional) enable BP / XP / other enhancements  
3. **Config → Import INI** → `packs/classic-voice-user.ini`  
4. **Apply Enhancements**

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

## Going as far back as we can

We want **every** stock `global.ini` we can bank — 3.x if someone still has a p4k, every 4.x LIVE/PTU/HOTFIX. Full datapacks are **not** published here (size + rights); we extract **only** localization and keep stocks local. Public repo ships the **map, pack, and tooling**.

| Currently banked (author) | Notes |
|---------------------------|--------|
| 4.3.2 → 4.7.x | ScCompLangPackRemix archives + git tags |
| **4.8.0-PTU** | Recovered from community pack git tag |
| 4.9 LIVE / 4.10 PTU | Fresh extract from install |
| **Wishlist** | 3.17–3.24, 4.0–4.2, 4.8 LIVE finals |

How to add more / where archives come from: **[docs/CORPUS_SOURCES.md](docs/CORPUS_SOURCES.md)**.

```bash
# after dropping a new stock file into corpus/
python3 scripts/build_manifest.py
python3 scripts/map_softening.py
python3 scripts/build_pack.py --target 4.10.0-PTU
```

## Legal

- Fan use of `global.ini` overlays is discussed by CIG in the [Community Localization Update](https://robertsspaceindustries.com/spectrum/community/SC/forum/1/thread/star-citizen-community-localization-update).  
- **Do not** commit or re-host full stock `global.ini` dumps from `Data.p4k` in this repo.  
- Star Citizen and related marks are property of Cloud Imperium.  
- [Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen) is Apache-2.0 by [Osiris DevWorks](https://github.com/Osiris-DevWorks) — we integrate with it; we do not rebrand it.

## License

MIT for **scripts and docs** in this repository. Game string content remains CIG’s; the pack is a selection of historical official wording for personal/fan overlay use.
