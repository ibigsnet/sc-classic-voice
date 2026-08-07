# Banking old localization — where stock `global.ini` comes from

**Goal:** go as far back as possible so players get **old-style Star Citizen wording**, and so we can **prove in public** how CIG has softened the fiction over time.

We only need **stock English `global.ini`** (from `Data.p4k` → `Data/Localization/english/global.ini`). We do **not** need full game installs published on GitHub.

---

## What this project banks

| Layer | Stored where | In git? |
|-------|----------------|---------|
| Versioned stock extracts | `corpus/{version}-{CHANNEL}.ini` (symlink or copy) | **No** (CIG data; large) |
| Manifest (hashes, key counts, labels) | `corpus/manifest.json` | **Yes** |
| Soften map (diffs / evidence) | `reports/soften-map.*` | **Yes** (quotes, not full files) |
| Classic-voice pack (delta only) | `packs/classic-voice-user.ini` | **Yes** (selected historical strings) |

---

## Banked so far (author machine)

| Label | Approx keys | Source |
|-------|------------:|--------|
| 4.3.2-LIVE | ~83k | ScCompLangPackRemix `archives/4.3.2` |
| 4.4.0-PTU | ~85k | archives |
| 4.5.0-LIVE | ~85k | archives |
| 4.6.0-LIVE / PTU | ~86k | archives |
| 4.7.0-LIVE | ~88k | archives |
| 4.9.0-LIVE | ~90k | sc-loc-mods extract |
| 4.10.0-PTU | ~90k | sc-loc-mods extract |

**Gaps to fill:** 4.0–4.2, **4.8.x**, mid-4.x HOTFIX, and anything **pre-4.3** (3.x era) if we can get a `Data.p4k`.

Oldest we currently hold: **4.3.2**. That is not “day one,” but it’s enough to show multi-year drift once 4.8+ softens are mapped against 4.7 and earlier.

---

## How to acquire older stocks (legal / practical)

### 1. Your own old installs / backups (best)

If you ever kept:

- `…/StarCitizen/LIVE/Data.p4k` from an older patch  
- A copy of `data/Localization/english/global.ini` after a clean extract  
- RSI launcher “verify” leftovers renamed as `Data.p4k.old`

→ Extract `global.ini` only (see below) and drop into `corpus/`.

### 2. RSI Launcher historical builds (when CIG still hosts them)

Historically, backers could pull older public build indexes/files CIG left online (community guides reference `FileIndex/sc-alpha-…` style URLs). Availability **comes and goes**. If you still have launcher access to an old branch folder on disk, prefer that over random mirrors.

### 3. Community language-pack archives

Projects that ship **stock** beside remixes:

- [BeltaKoda/ScCompLangPackRemix](https://github.com/BeltaKoda/ScCompLangPackRemix) — `archives/{version}/` + `stock-global.ini`  
- [ExoAE/ScCompLangPack](https://github.com/ExoAE/ScCompLangPack) — releases often include full `global.ini` (may be *modified*; prefer files labeled stock/vanilla)  
- Git **history** of those repos sometimes keeps older stocks after main moves on  

**Caution:** remix packs rename components. For classic-voice we need **unmodified stock** when possible. If only a remix exists, use it only as a last resort and flag `quality: remix` in the manifest.

### 4. Fresh extract from any `Data.p4k` you can open

```bash
# Using sc-loc-mods / same pure-Python idea:
python3 /path/to/extract_stock_ini.py --channel LIVE
# or point at a specific p4k if your tool supports it
```

Tools:

- Smart Citizen — Extract from Data.p4k  
- [dolkensp/unp4k](https://github.com/dolkensp/unp4k) / [odw-fast-unp4k](https://github.com/Osiris-DevWorks/odw-fast-unp4k) — `unp4k Data.p4k global.ini` / Localization filter  
- sc-loc-mods `scripts/extract_stock_ini.py`  

Then:

```bash
cp stock-global.ini corpus/4.8.3-LIVE.ini
python3 scripts/map_softening.py
python3 scripts/build_pack.py --target 4.10.0-PTU
```

### 5. What we will **not** do

- Host multi-GB `Data.p4k` files on this GitHub repo  
- Scrape pirate mirrors of full game builds  
- Claim CIG “authorized” our politics — only the **localization overlay mechanism** is community-discussed  

---

## Naming convention

```text
corpus/{MAJOR.MINOR.PATCH}-{CHANNEL}.ini

Examples:
  3.22.1-LIVE.ini
  4.0.2-LIVE.ini
  4.8.3-LIVE.ini
  4.10.0-PTU.ini
```

Optional metadata in `corpus/manifest.json`:

```json
{
  "label": "4.7.0-LIVE",
  "channel": "LIVE",
  "game_version": "4.7.0",
  "source": "ScCompLangPackRemix/archives/4.7.0/LIVE/stock-global.ini",
  "quality": "stock",
  "key_count": 87591,
  "sha256": "…"
}
```

---

## Awareness mission (why deep history matters)

Classic-voice is not only a comfort pack. **Side-by-side history is the evidence:**

1. Extract stock at version A and B  
2. Soften map shows the exact key and the old vs new sentence  
3. Players see the slide without conspiracy-board vibes — the files are the receipts  

The further back the corpus goes, the harder it is to hand-wave “it was always like this.”

---

## Wishlist (help wanted)

If you have any of these as stock extracts (or a p4k you’re willing to extract from offline), open an issue with the version label:

- [ ] 3.17 / 3.18 / 3.19 / 3.20–3.24 LIVE stock `global.ini`  
- [ ] 4.0 / 4.1 / 4.2 LIVE stock  
- [ ] **4.8.0–4.8.3** LIVE stock (fills the hole before 4.9 softens)  
- [ ] Any PTU snapshot that differs heavily from LIVE the same week  

Do **not** upload full p4ks to GitHub issues; share hashes + how you extracted, or host privately and PR only the `global.ini` if license/size allows—or just contribute the **diff events** / allowlisted keys.
