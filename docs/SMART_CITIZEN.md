# Using sc-classic-voice with Smart Citizen

| | |
|--|--|
| **Smart Citizen repo** | https://github.com/Osiris-DevWorks/smart-citizen |
| **Downloads** | https://github.com/Osiris-DevWorks/smart-citizen/releases |
| **Linux (Wine)** | https://github.com/Osiris-DevWorks/smart-citizen/blob/main/docs/LINUX.md |
| **This project** | https://github.com/ibigsnet/sc-classic-voice |

[Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen) (Osiris DevWorks) is a full localization editor: extract stock strings from `Data.p4k`, auto-enhancements (mission BP tags, XP, ship/item stats, etc.), merge sources, and Apply to the game with backups.

**sc-classic-voice** produces a **small delta INI** of preferred older wording — not a fork of Smart Citizen. Import it so classic voice stacks **on top** of their enhancements.

## Recommended workflow

1. Install **[Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen/releases)** and select your channel (LIVE / PTU / …).
2. **Extract from Data.p4k** so stock strings match your current build.
3. Enable any auto-enhancements you want (mission BP tags, XP, stats, …).
4. **Config → Import INI** and choose:
   ```text
   packs/classic-voice-user.ini
   ```
   Smart Citizen folds this into **user overrides** (`user.ini`), which apply **last** in the merge stack — so they win over stock and over generated enhancements for the same keys.
5. **Apply Enhancements** to write `global.ini` into the game tree (Smart Citizen backups first).

## Merge priority (conceptual)

```text
stock (Data.p4k)
  + language overlay (optional)
  + Smart Citizen enhancements (BP / XP / stats / …)
  + user.ini  ← classic-voice-user.ini lands here
  = installed global.ini
```

## After a Star Citizen patch

1. Smart Citizen: re-extract Data.p4k → Apply.
2. Optionally re-run this repo’s pipeline if you added new corpus versions:
   ```bash
   python3 scripts/map_softening.py
   python3 scripts/build_pack.py --target 4.10.0-PTU
   ```
3. Re-import `packs/classic-voice-user.ini` (or replace `user.ini` keys) and Apply again.

## Linux without the GUI

Merge the pack onto stock yourself (sc-loc-mods style):

```bash
# after extracting stock-global.ini for the channel
python3 - <<'PY'
# load stock, overlay packs/classic-voice-user.ini, write global.ini
PY
```

Or use `sc-loc-mods` / any tool that applies a key=value overlay.

## What this pack does *not* do

- Ship/component **stat** blocks (use Smart Citizen enhancements).
- Mission **blueprint pool** dumps from DataForge (Smart Citizen / StarStrings).
- Fun renames (Ironchad, etc.) — keep those in a separate personal overlay if desired.
