# Hard vs soft comparisons

**CIG changed the wording. Here are the receipts.**

Every report below uses **phrase-level VCS-style diffs** — GitHub paints `-` red (removed hard wording) and `+` green (softer replacement). Not three nearly-identical full strings.

---

## Start here

| Link | What you’ll see |
|------|-----------------|
| **[Flagship spotlight (4.7 → 4.8+)](../reports/spotlight-hard-vs-soft-4.7-4.8.md)** | Headhunter bomb runs: *living hell* → *mess the place up*, *bomb* → *blow*, *bombing run* → *attack* |
| **[Human examples + coverage](EXAMPLES.md)** | Side-by-sides, what we compared, what we did not yet bank |
| **[Review queue](../reports/review-queue.md)** | High-confidence softens checklist (hardness gain + edge lost) |

---

## Full maps (all banked history)

| Link | Scope |
|------|--------|
| **[Soften map](../reports/soften-map.md)** | Tone-soften candidates across consecutive builds (with red/green diffs) |
| **[Build-to-build diffs](../reports/build-diffs.md)** | Every wording change between stocks + high-similarity edit samples |
| **[Change ledger (strict pack)](../reports/all-keys-change-ledger.md)** | Keys restored because older text scores **harder** than current soft stock |
| [Ledger — at-least-as-hard](../reports/all-keys-change-ledger-01-classic-all-at-least-as-hard.md) | Same pipeline, larger pack (hardness ≥ current) |

Machine-readable: `reports/soften-map.json`, `reports/build-diffs.json`, `reports/hard-to-soft-examples.json`.

---

## How detection works

| Link | Topic |
|------|--------|
| [DETECTION.md](DETECTION.md) | Hardness scoring, wordlists, pick rules |
| [wordlists/](../wordlists/) | Editable hard / soft / euphemism lists |
| [AUDIT.md](AUDIT.md) | Logic check of the pipeline |

---

## Download the fix

Packs put the **hard column** back on current builds:

→ **[PACK_LIBRARY.md](PACK_LIBRARY.md)** · [packs/library/](../packs/library/)

---

*Regenerate after banking stock: `python3 scripts/rebuild_all.py --target 4.10.0-PTU`*
