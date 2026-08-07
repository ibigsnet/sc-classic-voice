# How we detect harder vs softer wording

This page documents **how sc-classic-voice scores and chooses** “hard / unsoftened” vs “soft / current CIG” text.  
Detection is **rule-based** (keyword and phrase heuristics), not an LLM or machine-learning model.

---

## Big picture

Two layers:

1. **Map changes** — whenever the same localization **key** has different text between stock versions  
2. **Score hardness** — keyword/phrase rules so packs prefer older **harder** wording  

We do **not** do full NLP “sentiment analysis.” We look for known **edge words** and **soft/corporate** phrases, plus known hard→soft swaps.

```text
stock A (older) ──diff──► stock B (newer)
        │
        ├─ edge tags lost?  → soften candidate
        ├─ euphemism pair?  → soften candidate
        └─ hardness_score(old) > hardness_score(new)?
                 │
                 ▼
         pack uses older/harder text on CURRENT builds
```

---

## Step 1: Diff every key across builds

For each **consecutive** pair of stocks in the corpus (e.g. 4.3.2 → 4.4 → … → 4.10):

1. Load both `global.ini` files  
2. For every key present in both: if `value_old != value_new` → record a **change**  
3. That produces the full change map (on the order of **~1.7k** consecutive text changes in the current bank)

Also, for the **target** (current soft stock, e.g. 4.10.0-PTU): for each key, collect every older version’s text and compare.

**Code:** `scripts/diff_builds.py`  
**Reports:** `reports/build-diffs.md`, `reports/build-diffs.json`, `reports/key-history.json`

---

## Step 2: Detect “edge” / hard words

List: `EDGE_PATTERNS` in `scripts/map_softening.py`.

If a regex matches, the string is tagged with that edge name:

| Tag | Matches (roughly) |
|-----|-------------------|
| `living_hell` | “living hell” |
| `bomb_the_life` / `bomb_the_living` | “bomb the life/living…” |
| `bombing_run` | “bombing run” |
| `kill` | kill / killing / killed / kills |
| `murder` / `slaughter` | murder, slaughter |
| `hell` / `shit` / `crap` / `fuck` / `bastard` / `whore` | harsh / swear tone |
| `corpse` / `blood` / `execute` / `massacre` / `annihilate` / `obliterate` | violence vocab |
| `wipe_out` / `blow_up` / `gut` / `terminate` / `dead_body` | more violence phrasing |

**Soften signal:** old text **had** an edge tag that new text **lost**  
→ e.g. old has `living_hell`, new does not.

---

## Step 3: Known hard → soft swaps (euphemism pairs)

List: `EUPHEMISM_PAIRS` in `scripts/map_softening.py`.

| Harder (old) | Softer (new) |
|--------------|--------------|
| bomb the living hell out of | really mess the place up |
| bomb the life out of | blow the life out of |
| bombing run | attack |
| kill the | eliminate the |
| kill … | take out … |
| murder | eliminate |
| slaughter | defeat |
| corpses | bodies |
| bloody | brutal |

If old contains the hard phrase and new contains the soft one (or the hard phrase is gone), that step scores as a soften.

---

## Step 4: Numeric hardness score (for picking which old text to keep)

Function: `hardness_score()` in `scripts/build_classic_all.py`.

```text
score = 0
+ 8     for each EDGE_PATTERNS hit
+ 6–25  for HARD_BOOST_PHRASES (living hell +25, bomb the life +20, kill +10, …)
− 10    for each SOFT_PATTERNS hit
+ 1     if text length > 200 characters
```

**Higher score = harder / more OG unsoftened voice.**

### Hard boosts (extra weight)

| Phrase / pattern | Approx boost |
|------------------|-------------:|
| living hell | +25 |
| bomb the life / bomb the living | +20 |
| bombing run | +12 |
| murder / slaughter | +15 |
| fuck… | +12 |
| kill… | +10 |
| bastard / corpse / execute / gut… | +10 |
| hell / shit / crap / blood / wipe out / blow up | +6–8 |

### Soft penalties (lower score)

`SOFT_PATTERNS` in `scripts/build_classic_all.py`:

| Soft phrase | Effect |
|-------------|--------|
| mess the place up | −10 |
| take care of / deal with | −10 |
| neutralize / eliminate / subdue / apprehend | −10 |
| unfortunate / please note / kindly | −10 |

---

## Step 5: Soften event score (for soften-map reports)

When version A → B changes a key, `event_score()` in `map_softening.py`:

```text
soften_score =
  +12 × (number of edge tags lost)
  −4  × (number of edge tags gained)   # got harsher → not a soften
  +15 × (euphemism pair hits)
  + bonus if rewrite is large (low string similarity)
```

High score → likely intentional soften → listed in `reports/soften-map.md`.

---

## Step 6: Choose wording for the pack

For each key on **current** (target) stock:

1. Look at all **older** stocks that have that key  
2. Score each historical string with `hardness_score`  
3. **Winner = highest hardness; ties → oldest version**  
4. If winner is harder (or ≥ as hard, depending on pack) than current soft text → include in the delta pack  

### Example

| Version | Snippet | Hardness (approx) |
|---------|---------|-------------------:|
| 4.3–4.7 | bomb the **living hell** out of the area | high (~90) |
| 4.8–4.10 | really **mess the place up** | low (~7) |

→ Pack ships **living hell** for current builds.

### Pack variants

| Pack | Rule |
|------|------|
| `01-classic-all.ini` | Only if chosen is **strictly harder** than target |
| `01-classic-all-at-least-as-hard.ini` | Chosen hardness **≥** target (larger pack) |
| `01-classic-broad.ini` | Oldest narrative stock when text changed (no hardness gate) |
| `composed-*-plus-community.ini` | Classic layer + BP/XP-style community enhancements |

See [PACK_LIBRARY.md](PACK_LIBRARY.md).

---

## What this does **not** do (yet)

| Limitation | Effect |
|------------|--------|
| Fixed word lists | Misses softens that use none of our phrases |
| No semantic / AI model | Tone shifts without keyword hits need human review or list updates |
| Broad packs without review | Can restore old lore/system text that isn’t “tone” |
| Brand-new missions | No old key to restore — planned “OG harden” later |

**Improving detection** = extend `EDGE_PATTERNS`, `HARD_BOOST_PHRASES`, `SOFT_PATTERNS`, and `EUPHEMISM_PAIRS` when we find new softens in the maps.

---

## Code map

| Piece | File |
|-------|------|
| Edge patterns + euphemism pairs + soften event score | [`scripts/map_softening.py`](../scripts/map_softening.py) |
| Hardness score + soft penalties + pack pick | [`scripts/build_classic_all.py`](../scripts/build_classic_all.py) |
| Full key diffs across builds | [`scripts/diff_builds.py`](../scripts/diff_builds.py) |
| Layer merge (classic + community BP/XP) | [`scripts/merge_layers.py`](../scripts/merge_layers.py) |

---

## Related docs

- [EXAMPLES.md](EXAMPLES.md) — side-by-side real softens  
- [PACK_LIBRARY.md](PACK_LIBRARY.md) — which pack to download  
- [SMART_CITIZEN.md](SMART_CITIZEN.md) — import into Smart Citizen  
- Reports under [`reports/`](../reports/) — soften-map, build-diffs, change ledger  
