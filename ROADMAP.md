# Roadmap — sc-classic-voice

Status as of **post-audit rebuild** (2026-08-07): full corpus map, hardness-gated packs, VCS-style wording diffs, review queue, one-shot rebuild.  
Logic check: **[docs/AUDIT.md](docs/AUDIT.md)**.

---

## North star

| Goal | Success looks like |
|------|--------------------|
| **Classic voice** | After each SC patch, players re-apply older, less-softened wording in minutes |
| **Evidence-based** | Every restored string traces to a stock extract version |
| **Composable** | Works with Smart Citizen (Import INI) — not a competing full editor |
| **Honest scope** | Wording only — not balance, netcode, or invented fanfic |

---

## What already ships

- [x] Public repo + manifesto README  
- [x] Corpus 4.3.2 → 4.10 (incl. **4.8.0-PTU**); local stocks not re-hosted  
- [x] Soften map + full build-to-build diffs (~1.7k pairwise changes)  
- [x] Hardness pick across **all keys / all versions** (`build_classic_all.py`)  
- [x] Pack library: strict / at-least-as-hard / broad / community / composed  
- [x] Editable `wordlists/` + euphemism pairs (reverse of studio sanitize lists)  
- [x] Phrase-level red/green diffs everywhere (`phrase_diff.py`)  
- [x] `rebuild_all.py` + `review-queue.md`  
- [x] Smart Citizen integration doc  
- [x] Flagship Headhunter softens restored (living hell, bomb→blow, bombing run→attack)  

**Known limits**

- Low-sim “harder” rewrites (newspapers, some industrial titles) still auto-pack — need human allow/deny  
- No 3.x / early 4.0–4.2 / pure 4.8 LIVE finals yet  
- No tagged GitHub Release zip for non-git players yet  
- No auto-install to game client (Smart Citizen / manual apply)

---

## Phase 1 — Corpus & truth

| Step | Work | Status |
|------|------|--------|
| 1.1 | 4.8.x stock in corpus | ✅ 4.8.0-PTU |
| 1.2 | EPTU / HOTFIX when they diverge | partial (4.7 HOTFIX) |
| 1.3 | `corpus/manifest.json` | ✅ |
| 1.4 | How to extract stock | ✅ CORPUS_SOURCES.md |
| 1.5 | Bank 3.x / 4.0–4.2 / 4.8 LIVE | open |

---

## Phase 2 — Detection quality

| Step | Work | Status |
|------|------|--------|
| 2.1 | Event classes (tone / lore / placeholder / noise) | open |
| 2.2 | Expand euphemism + hard/soft lists from reviews | ongoing |
| 2.3 | Focus mission Desc/Title; deprioritize newspapers | open |
| 2.4 | Human review queue | ✅ `reports/review-queue.md` |
| 2.5 | Allowlist / denylist keys | open |
| 2.6 | Phrase red/green diffs | ✅ all major reports |
| 2.7 | Placeholder/token-only skip | ✅ content_fingerprint |
| 2.8 | require_harder needs real hardness gain | ✅ |

---

## Phase 3 — Pack product

| Step | Work | Status |
|------|------|--------|
| 3.1 | Allowlist-curated release pack | next |
| 3.2 | GitHub Release `v0.2.0` with zip | next |
| 3.3 | Document target stock keys | partial |
| 3.4 | Profile packs (strict / broad / alash) | ✅ |
| 3.5 | Personal overlays separate | ✅ decision |

---

## Phase 4 — Install paths

| Step | Work | Status |
|------|------|--------|
| 4.1 | `docs/INSTALL.md` player path | next |
| 4.2 | Linux apply script | open |
| 4.3 | Compose order with Smart Citizen | ✅ SMART_CITIZEN.md |
| 4.4 | Issue template “new soften after patch” | open |
| 4.5 | In-game spot-check checklist | open |

---

## Phase 5 — Patch loop

| Step | Work | Status |
|------|------|--------|
| 5.1 | `docs/PATCH_RUNBOOK.md` | next |
| 5.2 | Pack diff vs previous release | open |
| 5.3 | Obsolete keys when CIG removes them | open |
| 5.4 | Optional notify | open |
| 5.5 | Wire to local sc-loc-mods pipeline | open |

---

## Near-term order (this project)

```text
1. ✅ Audit + fix pick logic (placeholder noise, bomb/blow scoring)
2. ✅ Rebuild packs + review queue + INDEX
3. → Human-review review-queue.md; seed allowlist.txt
4. → docs/INSTALL.md + GitHub Release v0.2.0
5. → PATCH_RUNBOOK.md; bank next LIVE/PTU stock when available
6. → Optional denylist: Journal_General_FrontendNewspaper*
```

---

## Explicit non-goals (for now)

- Replacing Smart Citizen  
- Inventing mission text that never shipped in stock  
- Hosting full multi-MB stock `global.ini` on GitHub  
- “Fixing” CIG’s politics on Spectrum — only **your client’s strings**

---

## Decision log

| Date | Decision |
|------|----------|
| 2026-08-07 | Project born; evidence from stock history, not fan rewrites |
| 2026-08-07 | Personal renames (Ironchad) stay out of public classic packs |
| 2026-08-07 | Phrase-level VCS diffs on every report |
| 2026-08-07 | High-sim alone ≠ require_harder; need hardness/edge gain |
| 2026-08-07 | Placeholder/token-only drift is not classic voice |
| 2026-08-07 | Soft substitutes (e.g. blow the life) must not be listed as hard words |
