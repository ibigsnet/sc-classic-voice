# Packs

| File | Purpose |
|------|---------|
| `classic-voice-user.ini` | Delta overlay for Smart Citizen **Import INI** / manual merge |
| `classic-voice-user.meta.json` | Provenance: which corpus version each key came from |

Regenerate after updating `corpus/` and re-running:

```bash
python3 scripts/map_softening.py
python3 scripts/build_pack.py --target 4.10.0-PTU
```
