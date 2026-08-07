# Hard / soft wordlists

CIG does **not** publish an internal “words we soften” list. Studios that chase broader ratings / brand safety typically use **internal moderation lexicons** + editorial guidelines (and sometimes automated tools) similar to open **profanity / strong-language / violence** lists used in content filters — but **in reverse**.

This folder is **our** reverse lexicon: terms that tend to mark **harder / unsoftened** mission and narrative voice vs **softer / corporate** phrasing.

## Files

| File | Purpose |
|------|---------|
| `hard-words.txt` | Words/phrases that **boost** “hardness” when present |
| `soft-words.txt` | Words/phrases that **lower** hardness (euphemism / corporate) |
| `euphemism-pairs.tsv` | Known hard → soft substitutions (tab-separated) |
| `SOURCES.md` | Where open lists come from; what we do **not** claim |

## Format

- One entry per line  
- Lines starting with `#` are comments  
- Phrases may contain spaces (`living hell`)  
- Matching is case-insensitive whole-word / phrase (see `scripts/wordlists.py`)

## How used

Loaded by `scripts/wordlists.py` into:

- soften mapping (`map_softening.py`)  
- hardness scoring / pack pick (`build_classic_all.py`)  

Primary pack logic is still **full history compare + similarity**; these lists **boost ranking**, they are not the only detector.

## Expanding the list

1. Find a real soften in `reports/` (old text vs new)  
2. Add the removed hard phrase to `hard-words.txt`  
3. Add the new soft phrase to `soft-words.txt`  
4. Optionally add a row to `euphemism-pairs.tsv`  
5. Rebuild: `python3 scripts/build_classic_all.py --target 4.10.0-PTU …`
