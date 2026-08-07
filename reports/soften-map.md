# Soften map — Star Citizen localization

Wording changes across stock `global.ini` extracts that look like **tone softening** (lost edge, euphemism swaps). Auto-detected; review before shipping a pack.

### How to read diffs

Each event shows a **phrase-level wording diff** (not two near-identical full strings):

- 🔴 / `-` = removed (older / harder)
- 🟢 / `+` = added (newer / softer)
- GitHub paints fenced `diff` blocks red/green automatically.

Shared helper: `scripts/phrase_diff.py`.

## Corpus

- **4.3.2-LIVE** — `global.ini`
- **4.4.0-PTU** — `stock-global.ini`
- **4.5.0-LIVE** — `stock-global.ini`
- **4.6.0-LIVE** — `stock-global.ini`
- **4.6.0-PTU** — `stock-global.ini`
- **4.7.0-LIVE** — `stock-global.ini`
- **4.7.0-LIVE-HOTFIX** — `4.7.0-LIVE-HOTFIX.ini`
- **4.7.0-PTU** — `4.7.0-PTU.ini`
- **4.7.1-LIVE** — `4.7.1-LIVE.ini`
- **4.8.0-PTU** — `4.8.0-PTU.ini`
- **4.9.0-LIVE** — `4.9.0-LIVE-p4k-fresh.ini`
- **4.10.0-PTU** — `4.10.0-PTU-p4k-fresh.ini`

## Pair counts

| From | To | Soften candidates |
|------|----|------------------:|
| 4.3.2-LIVE | 4.4.0-PTU | 16 |
| 4.4.0-PTU | 4.5.0-LIVE | 8 |
| 4.5.0-LIVE | 4.6.0-LIVE | 8 |
| 4.6.0-LIVE | 4.6.0-PTU | 110 |
| 4.6.0-PTU | 4.7.0-LIVE | 120 |
| 4.7.0-LIVE | 4.7.0-LIVE-HOTFIX | 0 |
| 4.7.0-LIVE-HOTFIX | 4.7.0-PTU | 0 |
| 4.7.0-PTU | 4.7.1-LIVE | 1 |
| 4.7.1-LIVE | 4.8.0-PTU | 5 |
| 4.8.0-PTU | 4.9.0-LIVE | 14 |
| 4.9.0-LIVE | 4.10.0-PTU | 12 |

**Total events:** 294

## Top events (by score)

### `item_Desc_srvl_heavy_armor_01_Shared` — 4.3.2-LIVE → 4.4.0-PTU (score 43.62, sim 19%)
- Edge lost: outlaws

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickas
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed to disperse the force of impacts and a high, rei

</details>

### `item_Desc_srvl_heavy_armor_01_legs` — 4.3.2-LIVE → 4.4.0-PTU (score 42.67, sim 21%)
- Edge lost: outlaws

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `8.0` | `7.5` |
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- 8.0
+ 7.5
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting o
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 7.5 µSCU |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed to disperse the fo

</details>

### `item_Desc_srvl_heavy_core_01` — 4.3.2-LIVE → 4.4.0-PTU (score 42.1, sim 23%)
- Edge lost: outlaws

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `8.0` | `12.0` |
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- 8.0
+ 12.0
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU | Backpacks: All |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for i
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 12.0 µSCU | Backpacks: All |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed 

</details>

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.3.2-LIVE → 4.4.0-PTU (score 31.93, sim 18%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Crosshair: Mercenary Guild News` | `VOX POPULI: The Voice of the People’s Alliance` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- Crosshair: Mercenary Guild News
+ VOX POPULI: The Voice of the People’s Alliance
```

<details>
<summary>Full previews</summary>

- **Old:** Crosshair: Mercenary Guild News
- **New:** VOX POPULI: The Voice of the People’s Alliance

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.3.2-LIVE → 4.4.0-PTU (score 26.45, sim 2%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `AMELIA BOYD SPOTTED IN STANTON Guild` | `VOX POPULI The Voice of the People’s Alliance November 2955 ALBERTSON FAMILY KILLED IN VANDUUL RAID Governing committee offers condolences but no solutions as the death toll conti…` |
| 🔄 replaced | `advised to be on the lookout for Boyd. Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increas…` | `of the governing committee argued in last month’s session that the time has come to ask the UEE Navy for assistance in securing the system. While Executive Allard has commented th…` |
| 🔄 replaced | `imminent. This activity comes amidst rumors of internal fighting and poor recruitment by the Frontier Fighters. While some guild officials see this as a time to be cautious, other…` | `satisfied to gather and gawk at the latest offerings from the various military-industrial complex stooges like Aegis Dynamics and Anvil Aerospace, this year’s grotesque pageantry …` |
| 🔄 replaced | `ideal time to focus forces on the group to bring Boyd to justice. IMPERATOR ADDISON SHARES CITIZEN'S DAY MESSAGE Halfway through her term, the Imperator makes the case for her vis…` | `dawn of a new home for our people? FOOD PANTRY CHARITY DRIVE A SUCCESS Donations to assist those affected by recent Vanduul raids nearly doubles the goal amount. AIR FILTER REPAIR…` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- AMELIA BOYD SPOTTED IN STANTON Guild
+ VOX POPULI The Voice of the People’s Alliance November 2955 ALBERTSON FAMILY KILLED IN VANDUUL RAID Governing committee offers condolences but no solutions as the death toll continues to rise. The Albertson Family Minin…
- advised to be on the lookout for Boyd. Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by Frontier Fighters in both…
+ of the governing committee argued in last month’s session that the time has come to ask the UEE Navy for assistance in securing the system. While Executive Allard has commented that no options are off the table when it …
- imminent. This activity comes amidst rumors of internal fighting and poor recruitment by the Frontier Fighters. While some guild officials see this as a time to be cautious, others are arguing that now may
+ satisfied to gather and gawk at the latest offerings from the various military-industrial complex stooges like Aegis Dynamics and Anvil Aerospace, this year’s grotesque pageantry of parading war machines to a population…
- ideal time to focus forces on the group to bring Boyd to justice. IMPERATOR ADDISON SHARES CITIZEN'S DAY MESSAGE Halfway through her term, the Imperator makes the case for her vision for the future. In anticipation of C…
+ dawn of a new home for our people? FOOD PANTRY CHARITY DRIVE A SUCCESS Donations to assist those affected by recent Vanduul raids nearly doubles the goal amount. AIR FILTER REPAIR WORK COMPLETED With the new filters ins…
```

<details>
<summary>Full previews</summary>

- **Old:** AMELIA BOYD SPOTTED IN STANTON | Guild members advised to be on the lookout for Boyd.  |  | Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by Frontier Fighters in both Stanton and Pyro, leading to speculation that another attack may be imminent.
- **New:** VOX POPULI | The Voice of the People’s Alliance | November 2955 |  | ALBERTSON FAMILY KILLED IN VANDUUL RAID  | Governing committee offers condolences but no solutions as the death toll continues to rise. |  | The Albertson Family Mining Post had just started its shift, when the Vanduul raiders struck without warning, killing the entire crew within

</details>

### `item_Desc_srvl_undersuit_02_01_02` — 4.3.2-LIVE → 4.4.0-PTU (score 20.79, sim 46%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔴 removed | `Carrying Capacity: 8.0 µSCU` | — |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- Carrying Capacity: 8.0 µSCU
```

<details>
<summary>Full previews</summary>

- **Old:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Roughly sewn together from a variety of ransacked materials, the Wastelander undersuit will just about do the job. This version features a bold rust color.
- **New:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s |  | Roughly sewn together from a variety of ransacked materials, the Wastelander undersuit will just about do the job. This version features a bold rust color.

</details>

### `defend_UGF_obj_long_02` — 4.3.2-LIVE → 4.4.0-PTU (score 16.86, sim 56%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `~mission(DefendWaveNumber) waves of hostiles.` | `oncoming attackers` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- ~mission(DefendWaveNumber) waves of hostiles.
+ oncoming attackers
```

<details>
<summary>Full previews</summary>

- **Old:** Defend the site against ~mission(DefendWaveNumber) waves of hostiles.
- **New:** Defend the site against oncoming attackers

</details>

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.3.2-LIVE → 4.4.0-PTU (score 16.8, sim 56%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Crosshair - October` | `Vox Populi - November` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- Crosshair - October
+ Vox Populi - November
```

<details>
<summary>Full previews</summary>

- **Old:** Crosshair - October 2955
- **New:** Vox Populi - November 2955

</details>

### `civilian_localdelivery_holiday_desc_004` — 4.3.2-LIVE → 4.4.0-PTU (score 15.13, sim 60%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `<EM4>~mission(Pickup1\|Address)</EM4>` | `<EM4>~mission(Location\|Address)</EM4>` |
| 🔄 replaced | `You would need to take one to ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>, another to ~mission(GiftRecipient2) at <EM4>~mission(DropOff2)</EM4>, and the last to ~mis…` | `~mission(DescriptionSetup)` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- <EM4>~mission(Pickup1|Address)</EM4>
+ <EM4>~mission(Location|Address)</EM4>
- You would need to take one to ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>, another to ~mission(GiftRecipient2) at <EM4>~mission(DropOff2)</EM4>, and the last to ~mission(GiftRecipient3) at <EM4>~mission(Dr…
+ ~mission(DescriptionSetup)
```

<details>
<summary>Full previews</summary>

- **Old:** I know things get busy around the holidays, but I was reaching out to see if you had any extra time to do a delivery run. |  | Got a few presents at <EM4>~mission(Pickup1|Address)</EM4> for close friends that I won't be able to deliver myself.  | You would need to take one to ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>, another to ~mi
- **New:** I know things get busy around the holidays, but I was reaching out to see if you had any extra time to do a delivery run. |  | Got a few presents at <EM4>~mission(Location|Address)</EM4> for close friends that I won't be able to deliver myself. ~mission(DescriptionSetup) |  | Much appreciated, | ~mission(GiftSender)

</details>

### `civilian_localdelivery_holiday_desc_002` — 4.3.2-LIVE → 4.4.0-PTU (score 12.96, sim 66%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `three` | `some` |
| 🔄 replaced | `<EM4>~mission(Pickup1\|Address)</EM4>` | `<EM4>~mission(Location\|Address)</EM4>` |
| 🔄 replaced | `hard. One is for ~mission(GiftRecipient1) over at <EM4>~mission(DropOff1)</EM4>, another's for ~mission(GiftRecipient2) at <EM4>~mission(DropOff2)</EM4>, and the last one is for ~…` | `hard.~mission(DescriptionSetup).` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- three
+ some
- <EM4>~mission(Pickup1|Address)</EM4>
+ <EM4>~mission(Location|Address)</EM4>
- hard. One is for ~mission(GiftRecipient1) over at <EM4>~mission(DropOff1)</EM4>, another's for ~mission(GiftRecipient2) at <EM4>~mission(DropOff2)</EM4>, and the last one is for ~mission(GiftRecipient3) who's at <EM4>~m…
+ hard.~mission(DescriptionSetup).
```

<details>
<summary>Full previews</summary>

- **Old:** I'm in desperate need of a little Luminalia magic and I hope you're the one to help. |  | There are three gifts stuck at <EM4>~mission(Pickup1|Address)</EM4> that need to be delivered.  |  | I tried scheduling a pick up but just got notified that they won't be able to make it until after the holidays. Would you be able to take care of the deliverie
- **New:** I'm in desperate need of a little Luminalia magic and I hope you're the one to help. |  | There are some gifts stuck at <EM4>~mission(Location|Address)</EM4> that need to be delivered.  |  | I tried scheduling a pick up but just got notified that they won't be able to make it until after the holidays. Would you be able to take care of the deliverie

</details>

### `civilian_localdelivery_holiday_desc_003` — 4.3.2-LIVE → 4.4.0-PTU (score 10.67, sim 71%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `<EM4>~mission(Pickup1\|Address)</EM4> and will need to be delivered to: - ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>. - ~mission(GiftRecipient2) at <EM4>~mission(Dro…` | `<EM4>~mission(Location\|Address)</EM4> and will need to be delivered to ~mission(DescriptionSetup)` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- <EM4>~mission(Pickup1|Address)</EM4> and will need to be delivered to: - ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>. - ~mission(GiftRecipient2) at <EM4>~mission(DropOff2)</EM4>. - ~mission(GiftRecipient3)…
+ <EM4>~mission(Location|Address)</EM4> and will need to be delivered to ~mission(DescriptionSetup)
```

<details>
<summary>Full previews</summary>

- **Old:** Hope the holiday season is treating you well. |  | Mine's been a bit stressful so far. It turns out that I put the wrong delivery address on a handful of gifts and I'm desperately seeking a way to get them delivered on time.  |  | It would mean so much to me if you could get me out of this jam.  |  | The presents are at <EM4>~mission(Pickup1|Addres
- **New:** Hope the holiday season is treating you well. |  | Mine's been a bit stressful so far. It turns out that I put the wrong delivery address on a handful of gifts and I'm desperately seeking a way to get them delivered on time.  |  | It would mean so much to me if you could get me out of this jam.  |  | The presents are at <EM4>~mission(Location|Addre

</details>

### `TheCollector_GenericCollect_Long,P` — 4.3.2-LIVE → 4.4.0-PTU (score 10.48, sim 72%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `~mission(destination\|ListAll).` | `<EM4>any Wikelo Emporium</EM4>.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- ~mission(destination|ListAll).
+ <EM4>any Wikelo Emporium</EM4>.
```

<details>
<summary>Full previews</summary>

- **Old:** Bring ~mission(amount)/~mission(total) of ~mission(item). Bring to ~mission(destination|ListAll).
- **New:** Bring ~mission(amount)/~mission(total) of ~mission(item). Bring to <EM4>any Wikelo Emporium</EM4>.

</details>

### `item_DescMTC_Paint_Grey_Black_Yellow_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 9.98, sim 73%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `highlights.` | `highlights. It's also compatible with other Greycat M-series vehicles.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- highlights.
+ highlights. It's also compatible with other Greycat M-series vehicles.
```

<details>
<summary>Full previews</summary>

- **Old:** Equip the Filament livery to make the MTC grey with black and yellow highlights.
- **New:** Equip the Filament livery to make the MTC grey with black and yellow highlights. It's also compatible with other Greycat M-series vehicles.

</details>

### `item_DescMTC_Paint_Grey_Lightgrey_Orange_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.75, sim 76%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `MTC.` | `MTC. It's also compatible with other Greycat M-series vehicles.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- MTC.
+ MTC. It's also compatible with other Greycat M-series vehicles.
```

<details>
<summary>Full previews</summary>

- **Old:** The Boreal livery brings a mix of metallic light grey, grey, and orange highlights to the MTC.
- **New:** The Boreal livery brings a mix of metallic light grey, grey, and orange highlights to the MTC. It's also compatible with other Greycat M-series vehicles.

</details>

### `item_DescMTC_Paint_Grey_Black_Red_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.74, sim 76%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `livery.` | `livery, which can also be applied to other Greycat M-Series vehicles.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- livery.
+ livery, which can also be applied to other Greycat M-Series vehicles.
```

<details>
<summary>Full previews</summary>

- **Old:** Bold red highlights add a bit of color and break up the black base paint of the MTC Baracus livery.
- **New:** Bold red highlights add a bit of color and break up the black base paint of the MTC Baracus livery, which can also be applied to other Greycat M-Series vehicles.

</details>

### `item_DescMTC_Paint_Black_Grey_Blue_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.06, sim 78%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `MTC.` | `MTC, which can also be applied to other Greycat M-Series vehicles.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- MTC.
+ MTC, which can also be applied to other Greycat M-Series vehicles.
```

<details>
<summary>Full previews</summary>

- **Old:** Crisp, metallic blue with grey and black highlights provide the Moonstone livery a spirited look for the MTC.
- **New:** Crisp, metallic blue with grey and black highlights provide the Moonstone livery a spirited look for the MTC, which can also be applied to other Greycat M-Series vehicles.

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.4.0-PTU → 4.5.0-LIVE (score 53.97, sim 3%)
- Edge lost: killing, raid

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `VOX POPULI The Voice of the People’s Alliance November 2955 ALBERTSON FAMILY KILLED IN VANDUUL RAID Governing committee offers condolences but no solutions as the death toll conti…` | `Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe has just grown a bit smaller,”…` |
| 🔄 replaced | `session` | `coordinated assault on the Pyro system utilizing multiple stolen RSI Polaris, leader of the terrorist organization Frontier Fighters, Amelia Boyd, has been brutally executed follo…` |
| 🔄 replaced | `time has come to ask` | `group will no longer to be a threat. WEAPONS OF MASS CELEBRATION? Retailers report that Luminalia-themed weapons are this year’s most popular gift. In what is considered by some t…` |
| 🔄 replaced | `Navy for assistance in securing the system. While Executive Allard has commented that no options are off the table when it comes to ensuring Levski’s future, senior committee memb…` | `reverse course and finally claim the system?` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- VOX POPULI The Voice of the People’s Alliance November 2955 ALBERTSON FAMILY KILLED IN VANDUUL RAID Governing committee offers condolences but no solutions as the death toll continues to rise. The Albertson Family Minin…
+ Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as …
- session
+ coordinated assault on the Pyro system utilizing multiple stolen RSI Polaris, leader of the terrorist organization Frontier Fighters, Amelia Boyd, has been brutally executed following her capture by the notorious outlaw…
- time has come to ask
+ group will no longer to be a threat. WEAPONS OF MASS CELEBRATION? Retailers report that Luminalia-themed weapons are this year’s most popular gift. In what is considered by some to be a concerning sign of the times, sal…
- Navy for assistance in securing the system. While Executive Allard has commented that no options are off the table when it comes to ensuring Levski’s future, senior committee member Thorean Basque has made it clear that…
+ reverse course and finally claim the system?
```

<details>
<summary>Full previews</summary>

- **Old:** VOX POPULI | The Voice of the People’s Alliance | November 2955 |  | ALBERTSON FAMILY KILLED IN VANDUUL RAID  | Governing committee offers condolences but no solutions as the death toll continues to rise. |  | The Albertson Family Mining Post had just started its shift, when the Vanduul raiders struck without warning, killing the entire crew within
- **New:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated the first public test of faster-than-light communications to a stunned crowd. Speaking in real time

</details>

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.4.0-PTU → 4.5.0-LIVE (score 35.13, sim 10%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `VOX POPULI: The Voice of the People’s Alliance` | `Terra Gazette` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- VOX POPULI: The Voice of the People’s Alliance
+ Terra Gazette
```

<details>
<summary>Full previews</summary>

- **Old:** VOX POPULI: The Voice of the People’s Alliance
- **New:** Terra Gazette

</details>

### `item_Descarma_barrel_stab_s1_firerats01` — 4.4.0-PTU → 4.5.0-LIVE (score 24.55, sim 37%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔴 removed | `Recoil Stability: +40% Recoil Kick: +40%` | — |
| 🔄 replaced | `-10%` | `-20%` |
| 🔄 replaced | `Reduce energy weapon recoil with` | `Aim Recoil: +40% Visual Recoil: +40% ArmaMod designed` |
| 🔄 replaced | `Stabilizer1. ArmaMod designed the` | `Stabilizer1` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure a` | `spread for a slower but` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- Recoil Stability: +40% Recoil Kick: +40%
- -10%
+ -20%
- Reduce energy weapon recoil with
+ Aim Recoil: +40% Visual Recoil: +40% ArmaMod designed
- Stabilizer1. ArmaMod designed the
+ Stabilizer1
- both horizontal and vertical recoil to ensure a
+ spread for a slower but
```

<details>
<summary>Full previews</summary>

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Recoil Stability: +40% | Recoil Kick: +40% | Spread: -10% | Projectile Speed: -12.5% |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. The S
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Spread: -20% | Projectile Speed: -12.5% | Aim Recoil: +40% | Visual Recoil: +40% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve spread for a slower but more precise shot. The Scorched edition features a unique flame patina.

</details>

### `item_Descarma_barrel_stab_s1` — 4.4.0-PTU → 4.5.0-LIVE (score 23.76, sim 39%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Reduce energy weapon recoil with` | `Visual Recoil: -30% ArmaMod designed` |
| 🔄 replaced | `Stabilizer1. ArmaMod designed the` | `Stabilizer1` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `visual stability allowing for` |
| 🔴 removed | `` | — |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- Reduce energy weapon recoil with
+ Visual Recoil: -30% ArmaMod designed
- Stabilizer1. ArmaMod designed the
+ Stabilizer1
- both horizontal and vertical recoil to ensure
+ visual stability allowing for
```

<details>
<summary>Full previews</summary>

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve visual stability allowing for a more precise shot.

</details>

### `item_Descarma_barrel_stab_s2` — 4.4.0-PTU → 4.5.0-LIVE (score 23.76, sim 39%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Reduce energy weapon recoil with` | `Visual Recoil: -30% ArmaMod designed` |
| 🔄 replaced | `Stabilizer2. ArmaMod designed the` | `Stabilizer2` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `visual stability allowing for` |
| 🔴 removed | `` | — |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- Reduce energy weapon recoil with
+ Visual Recoil: -30% ArmaMod designed
- Stabilizer2. ArmaMod designed the
+ Stabilizer2
- both horizontal and vertical recoil to ensure
+ visual stability allowing for
```

<details>
<summary>Full previews</summary>

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve visual stability allowing for a more precise shot.

</details>

### `item_descarma_barrel_stab_s2_contestedzonereward` — 4.4.0-PTU → 4.5.0-LIVE (score 19.56, sim 49%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🟢 added | — | `Heat: -80% Aim Recoil: +40% Visual Recoil: -15%` |
| 🔴 removed | `Recoil Stability: +15% Recoil Kick: +40% Spread: +25%` | — |
| 🔄 replaced | `Cost Per Shot:` | `Consumption:` |
| 🔄 replaced | `Reduce energy weapon recoil with` | `ArmaMod designed` |
| 🔄 replaced | `Stabilizer2. ArmaMod designed the` | `Stabilizer2` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `heat distribution and visual stability allowing for` |
| 🔄 replaced | `damage.` | `damage at the cost of expending more energy.` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
+ Heat: -80% Aim Recoil: +40% Visual Recoil: -15%
- Recoil Stability: +15% Recoil Kick: +40% Spread: +25%
- Cost Per Shot:
+ Consumption:
- Reduce energy weapon recoil with
+ ArmaMod designed
- Stabilizer2. ArmaMod designed the
+ Stabilizer2
- both horizontal and vertical recoil to ensure
+ heat distribution and visual stability allowing for
- damage.
+ damage at the cost of expending more energy.
```

<details>
<summary>Full previews</summary>

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Damage: +12.5% | Recoil Stability: +15% | Recoil Kick: +40% | Spread: +25% | Ammo Cost Per Shot: +100% |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more p
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Heat: -80% | Aim Recoil: +40% | Visual Recoil: -15% | Damage: +12.5% | Ammo Consumption: +100% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve heat distribution and visual stability allowing for a more precise shot. This "Tweaker" version has 

</details>

### `ui_pause_PopupQuitGame_Title` — 4.4.0-PTU → 4.5.0-LIVE (score 19.2, sim 50%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Game` | `to desktop` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- Game
+ to desktop
```

<details>
<summary>Full previews</summary>

- **Old:** Quit Game
- **New:** Quit to desktop

</details>

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.4.0-PTU → 4.5.0-LIVE (score 18.84, sim 51%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Vox Populi - November` | `Terra Gazette - December` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- Vox Populi - November
+ Terra Gazette - December
```

<details>
<summary>Full previews</summary>

- **Old:** Vox Populi - November 2955
- **New:** Terra Gazette - December 2955

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.5.0-LIVE → 4.6.0-LIVE (score 73.36, sim 2%)
- Edge lost: executed, outlaw
- Euphemism: lost:'execute'

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe` | `New United Release Edition 4.6.0 FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. Following weeks of reports of a new …` |
| 🔄 replaced | `just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated` | `been confirmed as a new species of mold whose airborne spores cause potentially fatal fungal infections in Humans. The source of the mold growth was traced back to recently instal…` |
| 🔄 replaced | `public test of faster-than-light communications to a stunned crowd. Speaking in real time` | `person to be killed by the ailment, it has since filled clinics and hospitals in the Nyx system with people experiencing symptoms. While the People’s Alliance is working with the …` |
| 🔄 replaced | `press conference in New York, Sol system to a colleague located in Prime, Terra system, Dr. Betel made history with a transmission of “Can you hear me?” While the current system o…` | `project to outfit their entire comm network with the new faster-than-light upgrades. An Aciedo spokesperson said that they have begun to seamlessly roll out access to the service,…` |
| 🔄 replaced | `threat. WEAPONS OF MASS CELEBRATION? Retailers report` | `key participant in the ongoing pay-to-play scandal` |
| 🔄 replaced | `Luminalia-themed weapons are this year’s most popular gift. In what is considered by some to be a concerning sign of the times, sales of Luminalia-themed weapons have sky-rocketed…` | `has rocked the Goss system.` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe
+ New United Release Edition 4.6.0 FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. Following weeks of reports of a new unknown illness afflicting the residents…
- just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated
+ been confirmed as a new species of mold whose airborne spores cause potentially fatal fungal infections in Humans. The source of the mold growth was traced back to recently installed ventilation filters from manufacture…
- public test of faster-than-light communications to a stunned crowd. Speaking in real time
+ person to be killed by the ailment, it has since filled clinics and hospitals in the Nyx system with people experiencing symptoms. While the People’s Alliance is working with the UEE-based “Alliance Aid” relief group to…
- press conference in New York, Sol system to a colleague located in Prime, Terra system, Dr. Betel made history with a transmission of “Can you hear me?” While the current system of jump tunnel comm-drones had been impro…
+ project to outfit their entire comm network with the new faster-than-light upgrades. An Aciedo spokesperson said that they have begun to seamlessly roll out access to the service, with hundreds of thousands of users uti…
- threat. WEAPONS OF MASS CELEBRATION? Retailers report
+ key participant in the ongoing pay-to-play scandal
- Luminalia-themed weapons are this year’s most popular gift. In what is considered by some to be a concerning sign of the times, sales of Luminalia-themed weapons have sky-rocketed this year to become the holiday’s most …
+ has rocked the Goss system.
```

<details>
<summary>Full previews</summary>

- **Old:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated the first public test of faster-than-light communications to a stunned crowd. Speaking in real time
- **New:** New United | Release Edition 4.6.0 |  | FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT | Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. |  | Following weeks of reports of a new unknown illness afflicting the residents of Levski, the source has been confirmed as a new species of mold whose airborne spores cause potentially fatal fung

</details>

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 25.29, sim 35%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Terra Gazette` | `New United` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Terra Gazette
+ New United
```

<details>
<summary>Full previews</summary>

- **Old:** Terra Gazette
- **New:** New United

</details>

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 24.28, sim 37%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Terra Gazette - December 2955` | `New United - Release Ed. 4.6.0` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Terra Gazette - December 2955
+ New United - Release Ed. 4.6.0
```

<details>
<summary>Full previews</summary>

- **Old:** Terra Gazette - December 2955
- **New:** New United - Release Ed. 4.6.0

</details>

### `Journal_General_Mining_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 17.95, sim 53%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `The Fundamentals of Mining` | `Mining Fundamentals #1: Basic Overview` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- The Fundamentals of Mining
+ Mining Fundamentals #1: Basic Overview
```

<details>
<summary>Full previews</summary>

- **Old:** The Fundamentals of Mining
- **New:** Mining Fundamentals #1: Basic Overview

</details>

### `Journal_General_Harvestables_Content` — 4.5.0-LIVE → 4.6.0-LIVE (score 12.18, sim 58%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🟢 added | — | `This guide will help you identify what's useful, what's edible, and what's deadly. *STANTON SYSTEM*` |
| 🔴 removed | `This guide will help you identify what's useful, what's edible, and what's deadly. *A FORAGER'S GUIDE TO STANTON*` | — |
| 🔄 replaced | `` | `Where to Find: Grasslands of Hurston (Stanton I), Deserts of Arial (Stanton 1a), Deserts of Magda (Stanton 1c), Deserts of Daymar (Stanton 2b), Tundras of microTech (Stanton IV), …` |
| 🔄 replaced | `` | `Where to Find: Forests of microTech (Stanton IV), Tundras of Calliope (Stanton 4a)` |
| 🔄 replaced | `` | `Where to Find: Grasslands of Hurston (Stanton I)` |
| 🔄 replaced | `` | `Where to Find: Grasslands of Hurston (Stanton I), Tundras of microTech (Stanton IV)` |
| 🔄 replaced | `` | `Where to Find: Grasslands of Hurston (Stanton I), Deserts of Arial (Stanton 1a), Deserts of Daymar (Stanton 2b)` |
| 🔄 replaced | `` | `Where to Find: Deserts of Magda (Stanton 1c), Ice deserts of Clio (Stanton 4b)` |
| 🔄 replaced | `` | `Where to Find: Forests of microTech (Stanton IV), Tundras of microTech (Stanton IV)` |
| 🔄 replaced | `*STANTON HABITATS AND BIOMES* Interested in tracking these fascinating specimens down? Check out this list of biomes and you're sure to find what you're looking for in no time.` | `Where to Find:` |
| 🔄 replaced | `I) • Whether sandy or rocky, the desert is home to many plants and animals, including the stone bug. Remember: if it gets too hot, you can get water from a revenant tree (as long …` | `I),` |
| 🔄 replaced | `1c) • Desolate and dry, Magda is nonetheless home to the stone bug, along with the degnous root and revenant tree.` | `1c),` |
| … | *+6 more hunks* | |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
+ This guide will help you identify what's useful, what's edible, and what's deadly. *STANTON SYSTEM*
- This guide will help you identify what's useful, what's edible, and what's deadly. *A FORAGER'S GUIDE TO STANTON*
+ Where to Find: Grasslands of Hurston (Stanton I), Deserts of Arial (Stanton 1a), Deserts of Magda (Stanton 1c), Deserts of Daymar (Stanton 2b), Tundras of microTech (Stanton IV), Tundras of Calliope (Stanton 4a), Ice de…
+ Where to Find: Forests of microTech (Stanton IV), Tundras of Calliope (Stanton 4a)
+ Where to Find: Grasslands of Hurston (Stanton I)
+ Where to Find: Grasslands of Hurston (Stanton I), Tundras of microTech (Stanton IV)
+ Where to Find: Grasslands of Hurston (Stanton I), Deserts of Arial (Stanton 1a), Deserts of Daymar (Stanton 2b)
+ Where to Find: Deserts of Magda (Stanton 1c), Ice deserts of Clio (Stanton 4b)
+ Where to Find: Forests of microTech (Stanton IV), Tundras of microTech (Stanton IV)
- *STANTON HABITATS AND BIOMES* Interested in tracking these fascinating specimens down? Check out this list of biomes and you're sure to find what you're looking for in no time.
+ Where to Find:
- I) • Whether sandy or rocky, the desert is home to many plants and animals, including the stone bug. Remember: if it gets too hot, you can get water from a revenant tree (as long as you don't mind the awful taste). Gras…
+ I),
- 1c) • Desolate and dry, Magda is nonetheless home to the stone bug, along with the degnous root and revenant tree.
+ 1c),
# … +6 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **Old:** It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. This guide will help you identify what's useful, what's edible, and what's deadly.   |  | *A FORAGER'S GUIDE TO STANTON* |  | DEGNOUS ROOT  | A type of macroalgae that has acclimated to much of the Stanton system, the degnous root is origin
- **New:** This guide will help you identify what's useful, what's edible, and what's deadly.   |  | *STANTON SYSTEM* | It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. |  | DEGNOUS ROOT  | A type of macroalgae that has acclimated to much of the Stanton system, the degnous root is originally from Te

</details>

### `Journal_General_Harvestables_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 9.01, sim 75%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Stanton` | `Empire` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Stanton
+ Empire
```

<details>
<summary>Full previews</summary>

- **Old:** Stanton Wildlife Federation
- **New:** Empire Wildlife Federation

</details>

### `Journal_General_Wildlife_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 9.01, sim 75%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Stanton` | `Empire` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Stanton
+ Empire
```

<details>
<summary>Full previews</summary>

- **Old:** Stanton Wildlife Federation
- **New:** Empire Wildlife Federation

</details>

### `Journal_General_Harvestables_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 8.98, sim 76%)

| | 4.5.0-LIVE | 4.6.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Guide to Stanton` | `Guide` |

```diff
# 4.5.0-LIVE  →  4.6.0-LIVE
- Guide to Stanton
+ Guide
```

<details>
<summary>Full previews</summary>

- **Old:** A Forager's Guide to Stanton
- **New:** A Forager's Guide

</details>

### `Shubin_Industrial_ShipMining_S_Org_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 42.15, sim 30%)
- Euphemism: lost:'kill'

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Purchase Order` | `Industrial` |
| 🔄 replaced | `<EM4>~mission(System) </EM4>` | `~mission(System) REQ EXPERIENCE: Ship Mining` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `is currently looking to fulfil another purchase order for a` | `values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. We are in need of a vast amount of ore, rang…` |
| 🔄 replaced | `refined materials. This purchase` | `different methods will need to be employed to gather these resources and most importantly, you will need a large organization of fellow contractors in` |
| 🔄 replaced | `is more complex than typical, requiring multiple mining methods,` | `to achieve this. mineable from numerous locations across <EM4>~mission(System)</EM4>. Reward will be proportionate to the effort and scale of this contract. As one of our most exp…` |
| 🔄 replaced | `since you've proven` | `should you need a reminder, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in` |
| 🔄 replaced | `skill thus far, we think` | `mobiGlas Journal. All Shubin Interstellar contractors are expected to provide their own equipment. For this contract` |
| 🔄 replaced | `team are up for the challenge. Reminder, <EM4>materials` | `fellow contractors will need a <EM4>Multi-Tool with a Mining Attachment, a Ground Vehicle capable of mining, and a Ship capable of mining</EM4>. As always, <EM4>the ore` |
| 🔄 replaced | `delivery</EM4>, and since this is a purchase order and not a mining contract, you are expected to provide your own equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re…` | `it is submitted</EM4>. This can be done at any refinery, the location of which can be found in your starmap. Once you have successfully gathered and refined the` |
| 🔄 replaced | `*By` | `DISCLAIMER: As a part of our Employee Incentive Program, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain f…` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Purchase Order
+ Industrial
- <EM4>~mission(System) </EM4>
+ ~mission(System) REQ EXPERIENCE: Ship Mining
- is currently looking to fulfil another purchase order for a
+ values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. We are in need of a vast amount of ore, ranging from common to rare. A
- refined materials. This purchase
+ different methods will need to be employed to gather these resources and most importantly, you will need a large organization of fellow contractors in
- is more complex than typical, requiring multiple mining methods,
+ to achieve this. mineable from numerous locations across <EM4>~mission(System)</EM4>. Reward will be proportionate to the effort and scale of this contract. As one of our most experienced contractors, we would expect yo…
- since you've proven
+ should you need a reminder, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in
- skill thus far, we think
+ mobiGlas Journal. All Shubin Interstellar contractors are expected to provide their own equipment. For this contract
- team are up for the challenge. Reminder, <EM4>materials
+ fellow contractors will need a <EM4>Multi-Tool with a Mining Attachment, a Ground Vehicle capable of mining, and a Ship capable of mining</EM4>. As always, <EM4>the ore
- delivery</EM4>, and since this is a purchase order and not a mining contract, you are expected to provide your own equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re ready to sell us the required
+ it is submitted</EM4>. This can be done at any refinery, the location of which can be found in your starmap. Once you have successfully gathered and refined the
- *By
+ DISCLAIMER: As a part of our Employee Incentive Program, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain from this contract</EM4>. This surplus ca…
```

<details>
<summary>Full previews</summary>

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. This purchase order is more complex than typical, requiring multiple mining methods, but since you've proven your skill thus far, we think you and your team ar
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. |  | We are in need of a vast amount of ore, ranging from common to rare. A variety of different 

</details>

### `Shubin_Industrial_ShipMining_VH_Org_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 42.15, sim 30%)
- Euphemism: lost:'kill'

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Purchase Order` | `Industrial` |
| 🔄 replaced | `<EM4>~mission(System) </EM4>` | `~mission(System) REQ EXPERIENCE: Ship Mining` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `is currently looking to fulfil another purchase order for a` | `values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. We are in need of a vast amount of ore, rang…` |
| 🔄 replaced | `refined materials. This purchase` | `different methods will need to be employed to gather these resources and most importantly, you will need a large organization of fellow contractors in` |
| 🔄 replaced | `is more complex than typical, requiring multiple mining methods,` | `to achieve this. mineable from numerous locations across <EM4>~mission(System)</EM4>. Reward will be proportionate to the effort and scale of this contract. As one of our most exp…` |
| 🔄 replaced | `since you've proven` | `should you need a reminder, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in` |
| 🔄 replaced | `skill thus far, we think` | `mobiGlas Journal. All Shubin Interstellar contractors are expected to provide their own equipment. For this contract` |
| 🔄 replaced | `team are up for the challenge. Reminder, <EM4>materials` | `fellow contractors will need a <EM4>Multi-Tool with a Mining Attachment, a Ground Vehicle capable of mining, and a Ship capable of mining</EM4>. As always, <EM4>the ore` |
| 🔄 replaced | `delivery</EM4>, and since this is a purchase order and not a mining contract, you are expected to provide your own equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re…` | `it is submitted</EM4>. This can be done at any refinery, the location of which can be found in your starmap. Once you have successfully gathered and refined the` |
| 🔄 replaced | `*By` | `DISCLAIMER: As a part of our Employee Incentive Program, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain f…` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Purchase Order
+ Industrial
- <EM4>~mission(System) </EM4>
+ ~mission(System) REQ EXPERIENCE: Ship Mining
- is currently looking to fulfil another purchase order for a
+ values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. We are in need of a vast amount of ore, ranging from common to rare. A
- refined materials. This purchase
+ different methods will need to be employed to gather these resources and most importantly, you will need a large organization of fellow contractors in
- is more complex than typical, requiring multiple mining methods,
+ to achieve this. mineable from numerous locations across <EM4>~mission(System)</EM4>. Reward will be proportionate to the effort and scale of this contract. As one of our most experienced contractors, we would expect yo…
- since you've proven
+ should you need a reminder, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in
- skill thus far, we think
+ mobiGlas Journal. All Shubin Interstellar contractors are expected to provide their own equipment. For this contract
- team are up for the challenge. Reminder, <EM4>materials
+ fellow contractors will need a <EM4>Multi-Tool with a Mining Attachment, a Ground Vehicle capable of mining, and a Ship capable of mining</EM4>. As always, <EM4>the ore
- delivery</EM4>, and since this is a purchase order and not a mining contract, you are expected to provide your own equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re ready to sell us the required
+ it is submitted</EM4>. This can be done at any refinery, the location of which can be found in your starmap. Once you have successfully gathered and refined the
- *By
+ DISCLAIMER: As a part of our Employee Incentive Program, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain from this contract</EM4>. This surplus ca…
```

<details>
<summary>Full previews</summary>

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. This purchase order is more complex than typical, requiring multiple mining methods, but since you've proven your skill thus far, we think you and your team ar
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. |  | We are in need of a vast amount of ore, ranging from common to rare. A variety of different 

</details>

### `Shubin_Industrial_HandMining_Intro_Local_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 35.53, sim 9%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Purchase Order` | `Industrial` |
| 🔄 replaced | `<EM4>~mission(System) </EM4>` | `~mission(System) REQ EXPERIENCE: Hand Mining` |
| 🔄 replaced | `Due to changes in our sourcing pipeline,` | `` |
| 🔄 replaced | `is currently` | `are` |
| 🔄 replaced | `purchase a variety of materials from independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling` | `expand` |
| 🔄 replaced | `order, many miners find that strengthening their ties to Shubin to be a wise long-term investment for their career. ~mission(Hint_Location) For a comprehensive` | `existing` |
| 🔄 replaced | `where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. While you're there, feel free to read the first part <EM4>Mining F…` | `contractors across <EM4>~mission(System)</EM4> to include entry-level` |
| 🔄 replaced | `contract,` | `contractors. If` |
| 🟢 added | — | `self-motivated, hardworking, and resilient, we would be interested in working with you. Head to our mining facility located at <EM4>~mission(Destination\|Address)</EM4> and search …` |
| 🔄 replaced | `equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re ready to sell us the required materials, deposit them in the freight elevator located at <EM4>~mission(Destination…` | `<EM4>~mission(Hint_Tool)</EM4> and any personal safety equipment. Payment and further opportunities will be provided upon successful completion of the contract. DISCLAIMER: As a p…` |
| 🔄 replaced | `contract."` | `contract.` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Purchase Order
+ Industrial
- <EM4>~mission(System) </EM4>
+ ~mission(System) REQ EXPERIENCE: Hand Mining
- Due to changes in our sourcing pipeline,
- is currently
+ are
- purchase a variety of materials from independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling
+ expand
- order, many miners find that strengthening their ties to Shubin to be a wise long-term investment for their career. ~mission(Hint_Location) For a comprehensive
+ existing
- where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. While you're there, feel free to read the first part <EM4>Mining Fundamentals #1: Basic Overview</EM4> if …
+ contractors across <EM4>~mission(System)</EM4> to include entry-level
- contract,
+ contractors. If
+ self-motivated, hardworking, and resilient, we would be interested in working with you. Head to our mining facility located at <EM4>~mission(Destination|Address)</EM4> and search the caves located nearby. Harvest the re…
- equipment, such as a <EM4>~mission(Hint_Tool)</EM4>. Once you’re ready to sell us the required materials, deposit them in the freight elevator located at <EM4>~mission(Destination|Address)</EM4>. *By
+ <EM4>~mission(Hint_Tool)</EM4> and any personal safety equipment. Payment and further opportunities will be provided upon successful completion of the contract. DISCLAIMER: As a part of our Employee Incentive Program, S…
- contract."
+ contract.
```

<details>
<summary>Full previews</summary>

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of materials from independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners 
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Hand Mining |  | TERMS*: |  | Shubin Interstellar are looking to expand our existing list of contractors across <EM4>~mission(System)</EM4> to include entry-level mining contractors. |  | If you are self-motivated, hardworking, and resilient, we would be interested in working with y

</details>

### `Shubin_Industrial_ShipMining_VH_Org_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.89, sim 31%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Special Purchase Order: Mined Materials` | `Ship Mining Request: Special Assignment` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Special Purchase Order: Mined Materials
+ Ship Mining Request: Special Assignment
```

<details>
<summary>Full previews</summary>

- **Old:** Special Purchase Order: Mined Materials
- **New:** Ship Mining Request: Special Assignment

</details>

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Ship Mined Ore` | `Ship Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Ship Mined Ore
+ Ship Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Ship Mined Ore` | `Ship Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Ship Mined Ore
+ Ship Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Ship Mined Ore` | `Ship Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Ship Mined Ore
+ Ship Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

</details>

### `Shubin_Industrial_HandMining_Nyx_E_Interstellar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Hand Mined Materials` | `Hand Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Hand Mined Materials
+ Hand Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

</details>

### `Shubin_Industrial_HandMining_Pyro_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Hand Mined Materials` | `Hand Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Hand Mined Materials
+ Hand Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

</details>

### `Shubin_Industrial_HandMining_Stanton_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Hand Mined Materials` | `Hand Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Hand Mined Materials
+ Hand Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

</details>

### `Shubin_Industrial_HandMining_Stanton_E_PlanetarySystem_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Hand Mined Materials` | `Hand Mining Request: Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Hand Mined Materials
+ Hand Mining Request: Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

</details>

### `Shubin_Industrial_HandMining_Intro_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.54, sim 34%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Small Purchase Order: Hand Mined Materials` | `Hand Mining Request: Shubin Interstellar` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Small Purchase Order: Hand Mined Materials
+ Hand Mining Request: Shubin Interstellar
```

<details>
<summary>Full previews</summary>

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Shubin Interstellar

</details>

### `Shubin_Industrial_ShipMining_Nyx_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `XS Purchase Order: Ship Mined Ore` | `Ship Mining Request: Very Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- XS Purchase Order: Ship Mined Ore
+ Ship Mining Request: Very Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `XS Purchase Order: Ship Mined Ore` | `Ship Mining Request: Very Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- XS Purchase Order: Ship Mined Ore
+ Ship Mining Request: Very Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `XS Purchase Order: Ship Mined Ore` | `Ship Mining Request: Very Small Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- XS Purchase Order: Ship Mined Ore
+ Ship Mining Request: Very Small Scale
```

<details>
<summary>Full previews</summary>

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

</details>

### `Shubin_Industrial_ShipMining_Nyx_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Mjr. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Extreme Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Mjr. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Extreme Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Mjr. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Extreme Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Mjr. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Extreme Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Mjr. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Extreme Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Mjr. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Extreme Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

</details>

### `Shubin_Industrial_HandMining_Pyro_M_DiscoverPlanetary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.15, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Med. Purchase Order: Hand Mined Materials` | `Hand Mining Request: Medium Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Med. Purchase Order: Hand Mined Materials
+ Hand Mining Request: Medium Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Med. Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Medium Scale

</details>

### `Shubin_Industrial_HandMining_Stanton_M_DiscoverPlanetary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.15, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Med. Purchase Order: Hand Mined Materials` | `Hand Mining Request: Medium Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Med. Purchase Order: Hand Mined Materials
+ Hand Mining Request: Medium Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Med. Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Medium Scale

</details>

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Med. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Medium Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Med. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Medium Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Med. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Medium Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Med. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Medium Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Med. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Medium Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Med. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Medium Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

</details>

### `Shubin_Industrial_ShipMining_Nyx_H_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Lrg. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Large Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Lrg. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Large Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_H_PrimarySecondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Lrg. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Large Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Lrg. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Large Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

</details>

### `Shubin_Industrial_ShipMining_Pyro_H_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Lrg. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Large Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Lrg. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Large Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_H_PrimarySecondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Lrg. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Large Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Lrg. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Large Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

</details>

### `Shubin_Industrial_ShipMining_Stanton_H_Secondary_Interstellar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

| | 4.6.0-LIVE | 4.6.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `Lrg. Purchase Order: Ship Mined Ore` | `Ship Mining Request: Large Scale` |

```diff
# 4.6.0-LIVE  →  4.6.0-PTU
- Lrg. Purchase Order: Ship Mined Ore
+ Ship Mining Request: Large Scale
```

<details>
<summary>Full previews</summary>

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

</details>
