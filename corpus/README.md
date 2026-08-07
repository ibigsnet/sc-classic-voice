# Corpus (local only)

Place or symlink versioned **stock** `global.ini` extracts here:

```text
corpus/
  4.3.2-LIVE.ini
  4.4.0-PTU.ini
  4.5.0-LIVE.ini
  4.6.0-LIVE.ini
  4.6.0-PTU.ini
  4.7.0-LIVE.ini
  4.9.0-LIVE.ini
  4.10.0-PTU.ini
```

Naming: `{gameVersion}-{CHANNEL}.ini` (semver-ish + channel).

These files are **not** committed (see root `.gitignore`). Extract from each channel’s `Data.p4k` with any stock extractor (Smart Citizen, sc-loc-mods, ScCompLangPack tools, etc.).

Optional sources already used on the author’s machine:

- `ScCompLangPackRemix/archives/{version}/…/stock-global.ini`
- `sc-loc-mods/channels/{LIVE|PTU}/stock-global.ini`
