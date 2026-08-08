# Preview packs (do NOT auto-apply to game)

These are **Import INI candidates** for review only. Nothing here is written into your Star Citizen install unless you explicitly Apply in Smart Citizen (or copy files yourself).

## `preview-personal-classic-scbp-delta.ini`

Merge order:

1. **Your personal overrides** (`sc-loc-mods/recovery/user-overrides-from-20260607.ini`) — Ironchad, renames, your BP/rep tags  
2. **Classic hard wording** (`01-classic-all-at-least-as-hard`) — living hell / bomb / etc.  
3. **Re-append personal enhancement blocks** so BP tags survive classic body replace  
4. **Smart Citizen community BP layer** (`02-community-mission-enhancements`) — fixture-style POTENTIAL BLUEPRINTS / mission details  

Built against stock **4.10.0-PTU**. **Delta-only** (keys that differ from stock).

### Safe use with Smart Citizen

1. Launch Smart Citizen (**skip Apply to Game** while exploring).  
2. Optional: Extract from Data.p4k (writes to Smart Citizen’s Documents cache, not game files until Apply).  
3. Config → **Import INI** → this file, e.g.  
   `Z:\home\rifle\projects\sc-classic-voice\packs\preview\preview-personal-classic-scbp-delta.ini`  
4. Browse / filter / preview in the UI.  
5. Click **Apply to Game** only when you want the install to change.

### Rebuild

```bash
cd ~/projects/sc-classic-voice
python3 scripts/merge_layers.py \
  --base corpus/4.10.0-PTU.ini \
  --layer /home/rifle/projects/sc-loc-mods/recovery/user-overrides-from-20260607.ini:replace \
  --layer packs/library/01-classic-all-at-least-as-hard.ini:replace \
  --layer /home/rifle/projects/sc-loc-mods/recovery/user-overrides-from-20260607.ini:append_enhancements \
  --layer packs/library/02-community-mission-enhancements.ini:append_enhancements \
  --out packs/preview/preview-personal-classic-scbp-delta.ini \
  --delta-only
```

### Notes on “newer” BP data

The community layer is from **Smart Citizen test fixtures** (mission_rewards + kraken), not a live DataForge extract from your current p4k.  
To get **true current-build BP pools** from Smart Citizen: open the app → Extract Data.p4k + generate enhancements → export/copy the generated enhancement INIs from `Documents\Smart Citizen\…` into this merge (still without Apply). That step can replace layer 4 with fresher files later.
