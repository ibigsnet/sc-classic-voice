# Roadmap — bringing sc-classic-voice to life

Status as of **v0.1.0** (first public cut): tooling + multi-version soften map + small high-confidence pack + Smart Citizen import path.  
This document is the plan to grow that into a maintained, patch-following product players can trust.

---

## North star

| Goal | Success looks like |
|------|--------------------|
| **Classic voice** | After each SC patch, players can re-apply older, less-softened mission/narrative wording in minutes |
| **Evidence-based** | Every restored string traces to a stock extract version (not invented fanfic) |
| **Composable** | Works *with* Smart Citizen (and headless Linux tools)—not a competing full editor |
| **Honest scope** | We fix *wording*, not balance, netcode, or politics of the live servers |

---

## What already ships (v0.1)

- [x] Public repo + manifesto README  
- [x] Corpus layout (local versioned stocks; not re-hosted full CIG dumps)  
- [x] `map_softening.py` — pair-wise soften detection (4.3 → 4.10)  
- [x] `build_pack.py` — high-confidence delta `classic-voice-user.ini`  
- [x] Reports: `soften-map.md` / `.json` / `.csv`  
- [x] Smart Citizen integration doc (`docs/SMART_CITIZEN.md`)  
- [x] Example restores (Headhunter bombing-run softens 4.7 → later)

**Known limits of v0.1**

- Pack is **small** (~4 keys at high confidence)—most of the 290 “events” need human review  
- **No 4.8** pure stock in corpus (gap between 4.7 and 4.9)  
- No auto-install to game / no CI that extracts from P4K  
- Detection heuristics will false-positive (news blurbs, unrelated rewrites)

---

## Phase 1 — Corpus & truth (foundation)

*Make the history complete and trustworthy.*

| Step | Work | Done when |
|------|------|-----------|
| 1.1 | Add **4.8.x LIVE/PTU** stock extracts to corpus | `4.8.*-*.ini` linked; re-map shows new pairs |
| 1.2 | Optional: EPTU / HOTFIX / TECH-PREVIEW snapshots when they diverge | Manifest lists channel + CL / build id |
| 1.3 | `corpus/manifest.json` — version, channel, build stamp, key count, sha256 | One file describes every extract |
| 1.4 | Document **how to extract** stock (Smart Citizen, sc-loc-mods, unp4k path) | CONTRIBUTING.md “Adding a version” section |
| 1.5 | Store **key fingerprints only** for CI if we never want full INIs in git | Optional later; keep full INIs local |

**Exit:** Any new patch can be dropped in as one named file and the map re-runs cleanly.

---

## Phase 2 — Detection quality (smarter map)

*Fewer false positives, clearer “this is a soften.”*

| Step | Work | Done when |
|------|------|-----------|
| 2.1 | Split event classes: `tone_soften`, `lore_rewrite`, `typo_fix`, `placeholder`, `noise` | CSV/JSON has `class` field |
| 2.2 | Expand euphemism dictionary from real map reviews | New pairs land in `map_softening.py` after each pass |
| 2.3 | Focus filters: mission Desc/Title first; deprioritize item fluff / newspapers unless edge lost | Default pack build uses focus filter |
| 2.4 | **Human review queue** — `reports/review-queue.md` top N by score | Maintainers check boxes |
| 2.5 | Allowlist / denylist keys (`patches/allowlist.txt`, `denylist.txt`) | Pack only ships allowlisted or auto+reviewed |
| 2.6 | Side-by-side HTML report (old vs new, highlighted) | Optional `reports/soften-diff.html` |

**Exit:** You can open the map and trust “high confidence” without reading 290 rows of noise.

---

## Phase 3 — Pack product (what players download)

*A real release artifact, not just a script output.*

| Step | Work | Done when |
|------|------|-----------|
| 3.1 | **Allowlist-curated pack** — only reviewed keys | `packs/classic-voice-user.ini` is intentional, not pure auto |
| 3.2 | Version the pack (`packs/VERSION`, release tags `v0.2.0`) | GitHub Release with zip |
| 3.3 | Channels: note “built for stock keys present in 4.10; safe no-op if key missing” | Documented in pack header |
| 3.4 | Optional **profile packs**: `strict` (edge-only), `broad` (more rewrites) | Two INIs or build flags |
| 3.5 | Keep personal overlays separate (Ironchad, ScComp renames, BP notes) | `packs/personal/` gitignored or other repo |

**Exit:** A player who never runs Python can download a release zip and import one file.

---

## Phase 4 — Smart Citizen & install paths

*Make “use it” brainless.*

| Step | Work | Done when |
|------|------|-----------|
| 4.1 | One-page **player install** (Smart Citizen Import INI) with screenshots | `docs/INSTALL.md` |
| 4.2 | Linux / Wine path: merge overlay with sc-loc-mods or a tiny `apply_pack.py` | Script installs to `data/Localization/english/` |
| 4.3 | Compose order documented: stock → SC enhancements → classic-voice → personal | Diagram in SMART_CITIZEN.md |
| 4.4 | Optional: issue template “new soften after patch X” | `.github/ISSUE_TEMPLATE/` |
| 4.5 | Test: apply pack on clean stock; key count; spot-check Headhunter lines in-game | Checklist in release notes |

**Exit:** README “Quick start” is player-first; developer path secondary.

---

## Phase 5 — Patch loop (stay alive every update)

*This is the real product: survive rolling SC updates.*

| Step | Work | Done when |
|------|------|-----------|
| 5.1 | After each LIVE/PTU: extract stock → map → review new events → rebuild pack | Written runbook `docs/PATCH_RUNBOOK.md` |
| 5.2 | Diff pack vs previous release (`pack-diff.md`) | Release notes list gained/lost keys |
| 5.3 | Keys removed by CIG: drop or mark obsolete in meta | meta.json has `status: obsolete` |
| 5.4 | Optional notify (Discord webhook / GitHub Action on schedule) | “new stock detected” if you host extracts |
| 5.5 | Wire to **sc-loc-mods** full pipeline for your machine | One command: extract + classic-voice + mission notes + install |

**Exit:** Patch day is a 30–60 minute ritual, not a research project.

---

## Phase 6 — Growth (optional, later)

| Step | Work | Notes |
|------|------|-------|
| 6.1 | Community PRs of reviewed softens | Need contribution rules (evidence = stock pair) |
| 6.2 | Website / Pages with soften gallery | Nice-to-have |
| 6.3 | Deeper DataForge-era strings (if ever exposed differently) | Out of scope until needed |
| 6.4 | Non-English classic voice | Only if someone maintains translations |

---

## Suggested near-term order (next 2–4 sessions)

```text
1. Extract & add 4.8 stock to corpus → re-run map
2. Human-review top soften-map.md rows → allowlist
3. Rebuild pack; cut GitHub Release v0.2.0 (downloadable INI)
4. Write docs/INSTALL.md + docs/PATCH_RUNBOOK.md
5. apply_pack.py for Linux (your box + sc-loc-mods merge)
6. After next SC patch: run the runbook once end-to-end
```

---

## Explicit non-goals (for now)

- Replacing Smart Citizen or ScCompLangPack  
- Inventing new mission text that never shipped in stock  
- Hosting full multi-megabyte stock `global.ini` on GitHub  
- “Fixing” CIG’s politics on Spectrum—only **your client’s strings**

---

## Decision log (fill as we go)

| Date | Decision |
|------|----------|
| 2026-08-07 | Project born; v0.1 auto pack + map; Smart Citizen import path |
| | Prefer **evidence from stock history**, not fan rewrites |
| | Personal renames (Ironchad) stay out of public classic-voice pack unless curated later |
| 2026-08-07 | Expanded corpus: 4.7.x tags + **4.8.0-PTU** stock from ScCompLangPackRemix git history; corpus bank + manifest; CORPUS_SOURCES doc |

