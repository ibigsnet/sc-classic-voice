# Using sc-classic-voice with Smart Citizen

| | |
|--|--|
| **Smart Citizen repo** | https://github.com/Osiris-DevWorks/smart-citizen |
| **Downloads** | https://github.com/Osiris-DevWorks/smart-citizen/releases |
| **Linux (upstream)** | https://github.com/Osiris-DevWorks/smart-citizen/blob/main/docs/LINUX.md |
| **This project** | https://github.com/ibigsnet/sc-classic-voice |

[Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen) (Osiris DevWorks) is a full localization editor: extract stock strings from `Data.p4k`, auto-enhancements (mission BP tags, XP, ship/item stats, etc.), merge sources, and Apply to the game with backups.

**sc-classic-voice** produces a **delta INI** of preferred older wording — not a fork of Smart Citizen. Import it so classic voice stacks **on top of** (or together with) their enhancements.

---

## Recommended packs to import

From this repo’s `packs/library/`:

| Want | Import this |
|------|-------------|
| **Hard wording + BP/XP** (recommended full) | `composed-classic-all-at-least-as-hard-plus-community.ini` |
| Hard wording only | `01-classic-all-at-least-as-hard.ini` |
| Surgical anti-soften only | `01-classic-all.ini` |

See [PACK_LIBRARY.md](PACK_LIBRARY.md).

---

## Windows (or Wine GUI)

1. Install Smart Citizen ([releases](https://github.com/Osiris-DevWorks/smart-citizen/releases) — portable preferred on Wine).
2. **Extract from Data.p4k** so stock matches your channel.
3. (Optional) enable auto-enhancements (BP / XP / stats).
4. **Config → Import INI** → pick a pack from the table above.
5. **Apply Enhancements** (Smart Citizen backups first).

### Merge priority (conceptual)

```text
stock (Data.p4k)
  + language overlay (optional)
  + Smart Citizen enhancements (BP / XP / stats / …)
  + user overrides  ← Import INI / classic-voice packs land here
  = installed global.ini
```

If you import the **composed** pack, BP/XP-style strings are already merged with classic wording in one file.

---

## Linux (LUG / Wine) — this machine

Official guide: [docs/LINUX.md](https://github.com/Osiris-DevWorks/smart-citizen/blob/main/docs/LINUX.md).

### Installed layout (rifle)

| Item | Path |
|------|------|
| Wine prefix | `/home/rifle/Games/star-citizen` |
| Wine runner (matches `sc-launch.sh`) | `runners/lug-wine-tkg-git-11.14-1/bin/wine` |
| Smart Citizen portable v2.3.0 | `drive_c/users/rifle/SmartCitizen/SmartCitizen-Portable-v2.3.0/` |
| Launch script | `/home/rifle/Games/star-citizen/launch_smartcitizen.sh` |

```bash
# Start Smart Citizen (game/launcher should be closed first)
/home/rifle/Games/star-citizen/launch_smartcitizen.sh
```

Or desktop entry: **Smart Citizen (SC Wine)** (if installed under `~/.local/share/applications/`).

### Import classic-voice from Linux paths

Wine can see the Linux filesystem as `Z:\`. In Smart Citizen **Import INI**, browse to e.g.:

```text
Z:\home\rifle\projects\sc-classic-voice\packs\library\composed-classic-all-at-least-as-hard-plus-community.ini
```

Or copy the pack into the prefix first:

```bash
cp /home/rifle/projects/sc-classic-voice/packs/library/composed-classic-all-at-least-as-hard-plus-community.ini \
  "/home/rifle/Games/star-citizen/drive_c/users/rifle/Documents/"
```

### Rules of thumb

1. **Do not** run Star Citizen / RSI Launcher and Smart Citizen in the same prefix at the same time.  
2. Use the **same Wine runner** as the game (`sc-launch.sh` → currently `lug-wine-tkg-git-11.14-1`).  
3. Prefer the **portable** zip, not the Setup.exe installer.  
4. After an SC patch: re-extract in Smart Citizen → re-import pack if needed → Apply.

### Update Smart Citizen later

```bash
# Download new portable zip from GitHub releases, extract to a new folder under:
#   .../drive_c/users/rifle/SmartCitizen/SmartCitizen-Portable-vX.Y.Z/
# Then edit APP_DIR / EXE_NAME in launch_smartcitizen.sh
```

---

## After a Star Citizen patch

1. Close the game. Open Smart Citizen → re-extract Data.p4k → Apply.  
2. Optionally rebuild classic packs if you banked a new stock:
   ```bash
   cd ~/projects/sc-classic-voice
   python3 scripts/rebuild_all.py --target 4.10.0-PTU   # or new label
   ```
3. Re-import the composed (or classic) INI and Apply again.

---

## What this pack does *not* do

- Ship/component **stat** blocks (use Smart Citizen enhancements, or composed pack only has fixture-style BP/XP text).  
- Live DataForge BP dumps beyond what’s in our community fixture layer.  
- Fun renames (Ironchad, etc.) — keep those in a separate personal overlay.

---

## Linux without the Smart Citizen GUI

Overlay packs yourself (sc-loc-mods / merge script style) onto extracted stock `global.ini`. Smart Citizen remains the smoother path for extract + backup + Apply.
