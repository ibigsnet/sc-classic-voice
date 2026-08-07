# Spotlight: hard (≤4.7.1) vs soft (4.8.0+)

Corpus: `4.7.1-LIVE` → `4.8.0-PTU` → `4.10.0-PTU` (stock strings; prefer p4k-fresh when banked).

Classic-voice packs put the **hard** wording back onto current builds.

## How to read this page

Wide tables hide the real edit. Each key below is shown three ways:

1. **Change table** — only the tokens that moved (hard → soft).
2. **Unified diff** — GitHub paints `-` red (removed) and `+` green (added).
3. **Inline markup** — `~~removed~~` / `**added**` with surrounding context.
4. **Full stock text** — complete strings if you need to copy/search.

Legend: 🔴 removed from hard stock · 🟢 added in soft stock · 🔄 replaced.

Same style is used project-wide in `soften-map.md`, `build-diffs.md`, and `all-keys-change-ledger.md` via `scripts/phrase_diff.py`.

---

## `headhunters_bombingrun_multi_E_CFP_desc_001`

### What changed (4.7.1-LIVE → 4.8.0-PTU)

| | Hard (old) | Soft (new) |
|---|------------|-----------|
| 🔄 replaced | `bomb the living hell out of the area.` | `really mess the place up.` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- bomb the living hell out of the area.
+ really mess the place up.
```

**Inline (context):**

Every day it seems like Citizens for Prosperity is out here trying to … who really is in charge here. Head to ~mission(Location|Address) and ~~bomb the living hell out of the area.~~**really mess the place up.**  / / Nothing like a bit of property damage to get a point across. / / -Stows out

- Same `4.8.0-PTU` vs `4.10.0-PTU`? **True**
- `4.7.1-LIVE` differs from `4.10.0-PTU`? **True**

<details>
<summary>Full stock text (all versions)</summary>

**4.7.1-LIVE (hard)**

```
Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves. 

I figure they could use a reminder about who really is in charge here. Head to ~mission(Location|Address) and bomb the living hell out of the area. 

Nothing like a bit of property damage to get a point across.

-Stows out
```

**4.8.0-PTU (soft era)**

```
Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves. 

I figure they could use a reminder about who really is in charge here. Head to ~mission(Location|Address) and really mess the place up. 

Nothing like a bit of property damage to get a point across.

-Stows out
```

**4.10.0-PTU (current)**

```
Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves. 

I figure they could use a reminder about who really is in charge here. Head to ~mission(Location|Address) and really mess the place up. 

Nothing like a bit of property damage to get a point across.

-Stows out
```

</details>

---

## `headhunters_Nyx_bombingrun_M_desc_001`

### What changed (4.7.1-LIVE → 4.8.0-PTU)

| | Hard (old) | Soft (new) |
|---|------------|-----------|
| 🔄 replaced | `bomb` | `blow` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- bomb
+ blow
```

**Inline (context):**

Seems we got a bit of competition out here in Nyx. Scouts have spotted … , and they made their choice. So now I need you to fly over there and ~~bomb~~**blow** the life out of the fuel tanks. Let's see how long they stick around without them. / / -Stows out

- Same `4.8.0-PTU` vs `4.10.0-PTU`? **True**
- `4.7.1-LIVE` differs from `4.10.0-PTU`? **True**

<details>
<summary>Full stock text (all versions)</summary>

**4.7.1-LIVE (hard)**

```
Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>.

Now, I'm a fair man. I sent these nullbrains a message saying they either vacate the facility or we make them wish they had, and they made their choice. So now I need you to fly over there and bomb the life out of the fuel tanks. Let's see how long they stick around without them.

-Stows out
```

**4.8.0-PTU (soft era)**

```
Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>.

Now, I'm a fair man. I sent these nullbrains a message saying they either vacate the facility or we make them wish they had, and they made their choice. So now I need you to fly over there and blow the life out of the fuel tanks. Let's see how long they stick around without them.

-Stows out
```

**4.10.0-PTU (current)**

```
Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>.

Now, I'm a fair man. I sent these nullbrains a message saying they either vacate the facility or we make them wish they had, and they made their choice. So now I need you to fly over there and blow the life out of the fuel tanks. Let's see how long they stick around without them.

-Stows out
```

</details>

---

## `headhunters_bombingrun_S_desc_001`

### What changed (4.7.1-LIVE → 4.8.0-PTU)

| | Hard (old) | Soft (new) |
|---|------------|-----------|
| 🔄 replaced | `a bombing run` | `an attack` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- a bombing run
+ an attack
```

**Inline (context):**

We've heard news that a new gang are planning ~~a bombing run~~**an attack** on a place over at <EM4>~mission(Location|Address)</EM4>. They figure … ose fuel tanks out of action. We'll take care of the rest. / / -Stows out

- Same `4.8.0-PTU` vs `4.10.0-PTU`? **True**
- `4.7.1-LIVE` differs from `4.10.0-PTU`? **True**

<details>
<summary>Full stock text (all versions)</summary>

**4.7.1-LIVE (hard)**

```
We've heard news that a new gang are planning a bombing run on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking.

But little do they know that we're gonna send you in first to blow the fuel tanks so we can claim the place before they do. If it all goes to plan, we can clear the location out and stick it to that gang at the same time. Two birds, one stone.

Only problem is this place is armed to the teeth. Bring a crew and get those fuel tanks out of action. We'll take care of the rest.

-Stows out
```

**4.8.0-PTU (soft era)**

```
We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking.

But little do they know that we're gonna send you in first to blow the fuel tanks so we can claim the place before they do. If it all goes to plan, we can clear the location out and stick it to that gang at the same time. Two birds, one stone.

Only problem is this place is armed to the teeth. Bring a crew and get those fuel tanks out of action. We'll take care of the rest.

-Stows out
```

**4.10.0-PTU (current)**

```
We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking.

But little do they know that we're gonna send you in first to blow the fuel tanks so we can claim the place before they do. If it all goes to plan, we can clear the location out and stick it to that gang at the same time. Two birds, one stone.

Only problem is this place is armed to the teeth. Bring a crew and get those fuel tanks out of action. We'll take care of the rest.

-Stows out
```

</details>

---

*Regenerated by `scripts/spotlight_diff.py` (shared `phrase_diff`). Packs restore hard-column wording; see `packs/library/`.*
