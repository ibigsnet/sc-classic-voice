# Packs

## Player downloads (`library/`)

See **[docs/PACK_LIBRARY.md](../docs/PACK_LIBRARY.md)** for the full model.

| Pack | Purpose |
|------|---------|
| `library/01-classic-strict.ini` | Anti-soften only (hard wording where we detected softens) |
| `library/01-classic-broad.ini` | Older stock narrative wording for many changed keys |
| `library/composed-classic-strict-plus-community.ini` | Hard wording + BP/XP-style community enhancements |
| `library/composed-classic-broad-plus-community.ini` | Broad classic + community enhancements |
| `classic-voice-user.ini` | Same as classic-strict (simple default) |

**Import into [Smart Citizen](https://github.com/Osiris-DevWorks/smart-citizen):** Config → Import INI → Apply.

## Rebuild

```bash
python3 scripts/diff_builds.py --target 4.10.0-PTU
python3 scripts/map_softening.py
python3 scripts/build_library.py --target 4.10.0-PTU
```
