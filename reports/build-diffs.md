# Full build-to-build localization changes

Target stock: **4.10.0-PTU**

### How to read diffs

Each sample shows a **phrase-level wording diff** (GitHub paints `-` red / `+` green in `diff` fences). Full string previews are folded under details.

Shared helper: `scripts/phrase_diff.py` (same style as softens & spotlight).

## Pairwise change counts

| From | To | Keys changed |
|------|----|-------------:|
| 4.3.2-LIVE | 4.4.0-PTU | 581 |
| 4.4.0-PTU | 4.5.0-LIVE | 128 |
| 4.5.0-LIVE | 4.6.0-LIVE | 25 |
| 4.6.0-LIVE | 4.6.0-PTU | 123 |
| 4.6.0-PTU | 4.7.0-LIVE | 334 |
| 4.7.0-LIVE | 4.7.0-LIVE-HOTFIX | 0 |
| 4.7.0-LIVE-HOTFIX | 4.7.0-PTU | 0 |
| 4.7.0-PTU | 4.7.1-LIVE | 1 |
| 4.7.1-LIVE | 4.8.0-PTU | 359 |
| 4.8.0-PTU | 4.9.0-LIVE | 86 |
| 4.9.0-LIVE | 4.10.0-PTU | 86 |

**Total pairwise text changes:** 1723
**Keys where history differs from target:** 1538

## Narrative keys: oldest stock ≠ target (awareness sample)

_726 narrative keys with oldest≠target; showing first 40 by rewrite distance_

### `item_Desc_rrs_combat_heavy_backpack_01_04_01`  (4.9.0-LIVE → target, sim 0%)

| | 4.9.0-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Item Type: Heavy Backpack Carrying Capacity: 150K µSCU Core Compatibility: Heavy Comfortably carry vital gear with the Morozov-CH backpack. This softshell bag is made with an adva…` |

```diff
# 4.9.0-LIVE  →  target
+ Item Type: Heavy Backpack Carrying Capacity: 150K µSCU Core Compatibility: Heavy Comfortably carry vital gear with the Morozov-CH backpack. This softshell bag is made with an advanced duraweave that's lightweight yet re…
```

<details>
<summary>Full previews</summary>

- **Oldest:** 
- **Target:** Item Type: Heavy Backpack | Carrying Capacity: 150K µSCU | Core Compatibility: Heavy |  | Comfortably carry vital gear with the Morozov-CH backpack. This softshell bag is made with an advanced duraweave that's lightweight yet ready for battlefield action. It also features several easy to

</details>

### `item_Desc_rrs_specialist_heavy_core_06_01_01,P`  (4.9.0-LIVE → target, sim 1%)

| | 4.9.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PH - Description for rrs_specialist_heavy_core_06_01_01` | `Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Carrying Capacity: 12K µSCU Backpacks: Al…` |

```diff
# 4.9.0-LIVE  →  target
- PH - Description for rrs_specialist_heavy_core_06_01_01
+ Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Carrying Capacity: 12K µSCU Backpacks: All Featuring fortified armor plating, spe…
```

<details>
<summary>Full previews</summary>

- **Oldest:** PH - Description for rrs_specialist_heavy_core_06_01_01
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -70 / 100 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 12K µSCU | Backpacks: All |  | Featuring fortified armor plating, special anti-rip protective padding and ample storage, the Moro

</details>

### `item_Desc_rrs_specialist_heavy_legs_06_01_01,P`  (4.9.0-LIVE → target, sim 1%)

| | 4.9.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PH - Description for rrs_specialist_heavy_legs_06_01_01` | `Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Carrying Capacity: 8K µSCU Featuring fort…` |

```diff
# 4.9.0-LIVE  →  target
- PH - Description for rrs_specialist_heavy_legs_06_01_01
+ Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Carrying Capacity: 8K µSCU Featuring fortified armor plating, special anti-rip pr…
```

<details>
<summary>Full previews</summary>

- **Oldest:** PH - Description for rrs_specialist_heavy_legs_06_01_01
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -70 / 100 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8K µSCU |  | Featuring fortified armor plating, special anti-rip protective padding and ample storage, the Morozov-SH is ready 

</details>

### `item_Desc_rrs_specialist_heavy_arms_06_01_01,P`  (4.9.0-LIVE → target, sim 1%)

| | 4.9.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PH - Description for rrs_specialist_heavy_arms_06_01_01` | `Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Featuring fortified armor plating, specia…` |

```diff
# 4.9.0-LIVE  →  target
- PH - Description for rrs_specialist_heavy_arms_06_01_01
+ Item Type: Heavy Armor Damage Reduction: 40% Temp. Rating: -70 / 100 °C Radiation Protection: 26800 REM Radiation Scrub Rate: 145.8 REM/s Featuring fortified armor plating, special anti-rip protective padding and ample …
```

<details>
<summary>Full previews</summary>

- **Oldest:** PH - Description for rrs_specialist_heavy_arms_06_01_01
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -70 / 100 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | Featuring fortified armor plating, special anti-rip protective padding and ample storage, the Morozov-SH is ready to overcome all kinds of ad

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content`  (4.3.2-LIVE → target, sim 3%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `AMELIA BOYD SPOTTED IN STANTON Guild members advised` | `VOX POPULI Release Edition 4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and ba…` |
| 🔄 replaced | `on the lookout for Boyd. Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by…` | `establishing fortified settlements at an alarming rate. While it is not yet clear who these newcomers to Nyx are or what their intentions might be, what is rapidly becoming appare…` |
| 🔄 replaced | `another attack may` | `there will` |
| 🔄 replaced | `imminent. This activity comes amidst rumors of internal fighting and poor recruitment by the Frontier Fighters. While some guild officials see this as a time to be cautious, other…` | `only scraps left on the table when the governing committee does decide to act. DUBIOUS SHUBIN MINING RIGHTS As the massive conglomerate continues to pillage the system, many miner…` |

```diff
# 4.3.2-LIVE  →  target
- AMELIA BOYD SPOTTED IN STANTON Guild members advised
+ VOX POPULI Release Edition 4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance. Seemingly having learned…
- on the lookout for Boyd. Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by Frontier Fighters in both Stanton and P…
+ establishing fortified settlements at an alarming rate. While it is not yet clear who these newcomers to Nyx are or what their intentions might be, what is rapidly becoming apparent is that if the People’s Alliance do n…
- another attack may
+ there will
- imminent. This activity comes amidst rumors of internal fighting and poor recruitment by the Frontier Fighters. While some guild officials see this as a time to be cautious, others are arguing that now may be the ideal …
+ only scraps left on the table when the governing committee does decide to act. DUBIOUS SHUBIN MINING RIGHTS As the massive conglomerate continues to pillage the system, many miners question their standing in Nyx. It see…
```

<details>
<summary>Full previews</summary>

- **Oldest:** AMELIA BOYD SPOTTED IN STANTON | Guild members advised to be on the lookout for Boyd.  |  | Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by Frontier Fighters in both Stanton and P
- **Target:** VOX POPULI | Release Edition 4.7.0 |  | UEE INTERSYSTEM COMM NETWORK HACKED  | Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance.   |  | Seemingly having learned nothing from the botched introduction of regen tech, Im

</details>

### `Nyx1_Desc`  (4.3.2-LIVE → target, sim 3%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `[NOT CURRENTLY ACCESSIBLE]` |
| 🔄 replaced | `world` | `planet` |
| 🟢 added | — | `orbits closest to the sun in the Nyx system. Once considered impossible to terraform, Nyx I` |
| 🔄 replaced | `been mined clean.` | `undergone a drastic transformation thanks to new experimental technology developed by Genesis Terraforming.` |

```diff
# 4.3.2-LIVE  →  target
+ [NOT CURRENTLY ACCESSIBLE]
- world
+ planet
+ orbits closest to the sun in the Nyx system. Once considered impossible to terraform, Nyx I
- been mined clean.
+ undergone a drastic transformation thanks to new experimental technology developed by Genesis Terraforming.
```

<details>
<summary>Full previews</summary>

- **Oldest:** Nyx I is a coreless world that has been mined clean.  | 
- **Target:** [NOT CURRENTLY ACCESSIBLE] Nyx I is a coreless planet that orbits closest to the sun in the Nyx system. Once considered impossible to terraform, Nyx I has undergone a drastic transformation thanks to new experimental technology developed by Genesis Terraforming.

</details>

### `Journal_General_FrontendNewspaperHeadlines_From`  (4.3.2-LIVE → target, sim 18%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Crosshair: Mercenary Guild News` | `VOX POPULI: The Voice of the People’s Alliance` |

```diff
# 4.3.2-LIVE  →  target
- Crosshair: Mercenary Guild News
+ VOX POPULI: The Voice of the People’s Alliance
```

<details>
<summary>Full previews</summary>

- **Oldest:** Crosshair: Mercenary Guild News
- **Target:** VOX POPULI: The Voice of the People’s Alliance

</details>

### `item_Desc_srvl_heavy_armor_01_Shared`  (4.3.2-LIVE → target, sim 19%)
- Edge oldest: ['outlaws'] · target: —

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  target
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategical

</details>

### `item_Desc_srvl_heavy_armor_01_legs`  (4.3.2-LIVE → target, sim 21%)
- Edge oldest: ['outlaws'] · target: —

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `8.0` | `7.5` |
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  target
- 8.0
+ 7.5
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 7.5 µSCU |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable c

</details>

### `item_Desc_srvl_heavy_core_01`  (4.3.2-LIVE → target, sim 23%)
- Edge oldest: ['outlaws'] · target: —

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `8.0` | `12.0` |
| 🔴 removed | `Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in …` | — |
| 🔴 removed | `The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't sa…` | — |

```diff
# 4.3.2-LIVE  →  target
- 8.0
+ 12.0
- Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickass, distinct, and res…
- The Overlord is available in several distinct colors worn by members of the (in)famous faction. Maybe just don't wear one while in Pyro unless you're looking for trouble. Don't say we didn't warn you!
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU | Backpacks: All |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we k
- **Target:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 12.0 µSCU | Backpacks: All |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructe

</details>

### `Journal_General_Harvestables_Content`  (4.3.2-LIVE → target, sim 24%)
- Edge oldest: ['deadly'] · target: ['destroyed', 'outlaws', 'deadly']

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `This guide will help you identify what's useful, what's edible, and what's deadly. *STANTON SYSTEM*` |
| 🔴 removed | `This guide will help you identify what's useful, what's edible, and what's deadly. *A FORAGER'S GUIDE TO STANTON*` | — |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `` | `Where to Find: Grasslands of Hurston (Stanton I) GOLDEN MEDMON First cultivated on Jalan, the maru ebony tree is most notable for the fruit that it produces, the curiously-shaped …` |
| 🔄 replaced | `` | `` |
| 🔴 removed | `on and around microTech,` | — |
| 🔴 removed | `the` | — |
| 🔄 replaced | `MARU EBONY Most notable for the fruit it produces, the curiously-shaped GOLDEN MEDMON, the maru ebony tree was first cultivated on Jalan. When they are harvested, golden medmons a…` | `Where to Find: Forests of microTech (Stanton IV)` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `FRUIT` | `fruit` |
| 🔄 replaced | `It` | `While it is cultivated as a commercial crop, it` |
| 🔴 removed | `on worlds where it is commercially grown` | — |
| … | *+27 more hunks* | |

```diff
# 4.3.2-LIVE  →  target
+ This guide will help you identify what's useful, what's edible, and what's deadly. *STANTON SYSTEM*
- This guide will help you identify what's useful, what's edible, and what's deadly. *A FORAGER'S GUIDE TO STANTON*
+ Where to Find: Grasslands of Hurston (Stanton I) GOLDEN MEDMON First cultivated on Jalan, the maru ebony tree is most notable for the fruit that it produces, the curiously-shaped golden medmon. When they are harvested, …
- on and around microTech,
- the
- MARU EBONY Most notable for the fruit it produces, the curiously-shaped GOLDEN MEDMON, the maru ebony tree was first cultivated on Jalan. When they are harvested, golden medmons are extremely firm and astringent, with t…
+ Where to Find: Forests of microTech (Stanton IV)
- FRUIT
+ fruit
- It
+ While it is cultivated as a commercial crop, it
- on worlds where it is commercially grown
# … +27 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **Oldest:** It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. This guide will help you identify what's useful, what's edible, and what's deadly.   |  | *A FORAGER'S GUIDE TO STANTON* |  | DEGNOUS ROOT  | A type of macroalgae that has acclimat
- **Target:** This guide will help you identify what's useful, what's edible, and what's deadly. |  | *STANTON SYSTEM* | It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. |  | DEGNOUS ROOT | A type of macroalgae that has acclimated to much of the

</details>

### `item_Desc_clda_undersuit_02`  (4.3.2-LIVE → target, sim 28%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Built for adventure but comfortable enough for everyday, the Markanda undersuit has become beloved by explorers. A uniq
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | Built for adventure but comfortable enough for everyday, the Markanda undersuit has become beloved by explorers. A unique pa

</details>

### `Journal_General_FrontendNewspaperHeadlines_Title`  (4.3.2-LIVE → target, sim 28%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Crosshair - October 2955` | `Vox Populi - Release 4.7.0` |

```diff
# 4.3.2-LIVE  →  target
- Crosshair - October 2955
+ Vox Populi - Release 4.7.0
```

<details>
<summary>Full previews</summary>

- **Oldest:** Crosshair - October 2955
- **Target:** Vox Populi - Release 4.7.0

</details>

### `item_Desc_hdtc_undersuit_01_01_01`  (4.3.2-LIVE → target, sim 28%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | The Lamont looks so good you won't want to wear armor over it. Seamlessly blending lightweight plating with durable syn
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | The Lamont looks so good you won't want to wear armor over it. Seamlessly blending lightweight plating with durable syntheti

</details>

### `item_DescStinger_Paint_Silver_Grey_Teal`  (4.3.2-LIVE → target, sim 34%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Silvery gray highlights frame metallic blue wings in the` | `The` |
| 🔄 replaced | `for the Esperia` | `adds a sleek, ethereal teal and patina metal finish to emphasize and celebrate the otherworldly nature of the` |

```diff
# 4.3.2-LIVE  →  target
- Silvery gray highlights frame metallic blue wings in the
+ The
- for the Esperia
+ adds a sleek, ethereal teal and patina metal finish to emphasize and celebrate the otherworldly nature of the
```

<details>
<summary>Full previews</summary>

- **Oldest:** Silvery gray highlights frame metallic blue wings in the Insularis livery for the Esperia Stinger.
- **Target:** The Insularis livery adds a sleek, ethereal teal and patina metal finish to emphasize and celebrate the otherworldly nature of the Stinger.

</details>

### `item_Descarma_barrel_stab_s1_firerats01`  (4.3.2-LIVE → target, sim 37%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔴 removed | `Recoil Stability: +40% Recoil Kick: +40%` | — |
| 🔄 replaced | `-10%` | `-20%` |
| 🔄 replaced | `Reduce energy weapon recoil with` | `Aim Recoil: +40% Visual Recoil: +40% ArmaMod designed` |
| 🔄 replaced | `Stabilizer1. ArmaMod designed the` | `Stabilizer1` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure a` | `spread for a slower but` |

```diff
# 4.3.2-LIVE  →  target
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

- **Oldest:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Recoil Stability: +40% | Recoil Kick: +40% | Spread: -10% | Projectile Speed: -12.5% |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and ve
- **Target:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Spread: -20% | Projectile Speed: -12.5% | Aim Recoil: +40% | Visual Recoil: +40% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve spread for a slower but more precise shot. The Scorched edition 

</details>

### `item_Descarma_barrel_stab_s1`  (4.3.2-LIVE → target, sim 39%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Reduce energy weapon recoil with` | `Visual Recoil: -30% ArmaMod designed` |
| 🔄 replaced | `Stabilizer1. ArmaMod designed the` | `Stabilizer1` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `visual stability allowing for` |
| 🔴 removed | `` | — |

```diff
# 4.3.2-LIVE  →  target
- Reduce energy weapon recoil with
+ Visual Recoil: -30% ArmaMod designed
- Stabilizer1. ArmaMod designed the
+ Stabilizer1
- both horizontal and vertical recoil to ensure
+ visual stability allowing for
```

<details>
<summary>Full previews</summary>

- **Oldest:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **Target:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve visual stability allowing for a more precise shot.

</details>

### `item_Descarma_barrel_stab_s2`  (4.3.2-LIVE → target, sim 39%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Reduce energy weapon recoil with` | `Visual Recoil: -30% ArmaMod designed` |
| 🔄 replaced | `Stabilizer2. ArmaMod designed the` | `Stabilizer2` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `visual stability allowing for` |
| 🔴 removed | `` | — |

```diff
# 4.3.2-LIVE  →  target
- Reduce energy weapon recoil with
+ Visual Recoil: -30% ArmaMod designed
- Stabilizer2. ArmaMod designed the
+ Stabilizer2
- both horizontal and vertical recoil to ensure
+ visual stability allowing for
```

<details>
<summary>Full previews</summary>

- **Oldest:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **Target:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve visual stability allowing for a more precise shot.

</details>

### `Pyro1_desc`  (4.3.2-LIVE → target, sim 40%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Iron Copper Tin Stileron Potential Ground Vehicle Mineables: Beradon Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Iron Copper Tin Stileron Potential Ground Vehicle Mineables: Beradon Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Decari Pod Fotia Seedpod …
```

<details>
<summary>Full previews</summary>

- **Oldest:** Orbiting very close to Pyro's volatile star, Pyro I has high temperatures and atmospheric pressure.
- **Target:** Orbiting very close to Pyro's volatile star, Pyro I has high temperatures and atmospheric pressure. |  | Potential Ship Mineables: | Iron | Copper | Tin | Stileron |  | Potential Ground Vehicle Mineables: | Beradon |  | Potential Hand Mineables: | Aphorite | Dolivine | Hadanite | Janalite (Caves only) |  | Potent

</details>

### `Pyro6_desc`  (4.3.2-LIVE → target, sim 41%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Ice Copper Agricium Titanium Gold Riccite Stileron Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: Ranta Dung (Caves) Amiosh…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Ice Copper Agricium Titanium Gold Riccite Stileron Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Caves) Bluemoon Fungus (Caves)
```

<details>
<summary>Full previews</summary>

- **Oldest:** Terminus is a frigid, barely-habitable planet with a methane-laced atmosphere.
- **Target:** Terminus is a frigid, barely-habitable planet with a methane-laced atmosphere. |  | Potential Ship Mineables: | Ice | Copper | Agricium | Titanium | Gold | Riccite | Stileron |  | Potential Hand Mineables: | Aphorite | Dolivine | Janalite |  | Potential Harvestables: | Ranta Dung (Caves) | Amioshi Plague (Caves) | Bl

</details>

### `Pyro5d_Fairo_desc`  (4.3.2-LIVE → target, sim 41%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `` | `Potential Ship Mineables: Silicon Tungsten Gold Bexalite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amio…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Silicon Tungsten Gold Bexalite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Caves) Bluemoon Fungus (Cave…
```

<details>
<summary>Full previews</summary>

- **Oldest:** Frequent earthquakes rock Fairo, causing spectacular waves in its brackish seas.  
- **Target:** Frequent earthquakes rock Fairo, causing spectacular waves in its brackish seas. |  | Potential Ship Mineables: | Silicon | Tungsten | Gold | Bexalite |  | Potential Hand Mineables: | Aphorite | Dolivine | Hadanite | Janalite (Caves only) |  | Potential Harvestables: | Ranta Dung (Caves) | Amioshi Plague (Caves

</details>

### `item_Desc_dmc_frontier_gloves_01_02_11,P`  (4.5.0-LIVE → target, sim 42%)

| | 4.5.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PLACEHOLDER` | `PLACEHOLDER - dmc_frontier_gloves_01_02_11` |

```diff
# 4.5.0-LIVE  →  target
- PLACEHOLDER
+ PLACEHOLDER - dmc_frontier_gloves_01_02_11
```

<details>
<summary>Full previews</summary>

- **Oldest:** PLACEHOLDER
- **Target:** PLACEHOLDER - dmc_frontier_gloves_01_02_11

</details>

### `item_Desc_dmc_frontier_jacket_01_02_11,P`  (4.5.0-LIVE → target, sim 42%)

| | 4.5.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PLACEHOLDER` | `PLACEHOLDER - dmc_frontier_jacket_01_02_11` |

```diff
# 4.5.0-LIVE  →  target
- PLACEHOLDER
+ PLACEHOLDER - dmc_frontier_jacket_01_02_11
```

<details>
<summary>Full previews</summary>

- **Oldest:** PLACEHOLDER
- **Target:** PLACEHOLDER - dmc_frontier_jacket_01_02_11

</details>

### `Pyro3_desc`  (4.3.2-LIVE → target, sim 42%)
- Edge oldest: ['outlaws'] · target: ['outlaws']

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Quartz Borase Riccite Stileron Potential Ground Vehicle Mineables: Beradon Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: F…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Quartz Borase Riccite Stileron Potential Ground Vehicle Mineables: Beradon Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: Flareweed Stalk Amiant Pod Ranta Dung (Ca…
```

<details>
<summary>Full previews</summary>

- **Oldest:** This icy terrestrial world has a breathable atmosphere of nitrogen and oxygen and has been overrun by outlaws.
- **Target:** This icy terrestrial world has a breathable atmosphere of nitrogen and oxygen and has been overrun by outlaws. |  | Potential Ship Mineables: | Quartz | Borase | Riccite | Stileron |  | Potential Ground Vehicle Mineables: | Beradon |  | Potential Hand Mineables: | Aphorite | Dolivine | Janalite |  | Potential H

</details>

### `item_Desc_srvl_undersuit_01`  (4.3.2-LIVE → target, sim 42%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Featuring the same relatively reliable construction as the Why Not helmet, the Second Life takes some of those tattered
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | Featuring the same relatively reliable construction as the Why Not helmet, the Second Life takes some of those tattered old 

</details>

### `item_DescCRUS_Star_Runner_Front_Turret`  (4.3.2-LIVE → target, sim 42%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Turret` | `Weapon Mount` |
| 🔄 replaced | `nose turret` | `weapon mount` |
| 🔄 replaced | `mounted to the belly of` | `bespoke to` |
| 🔄 replaced | `Runner. Bespoke to the ship, the turret is` | `Runner and` |

```diff
# 4.3.2-LIVE  →  target
- Turret
+ Weapon Mount
- nose turret
+ weapon mount
- mounted to the belly of
+ bespoke to
- Runner. Bespoke to the ship, the turret is
+ Runner and
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Turret | Manufacturer: Crusader Industries | Size: 3 |  | This pilot-controlled, dual-linked nose turret is mounted to the belly of the Mercury Star Runner. Bespoke to the ship, the turret is outfitted with two size-3 laser repeaters ready to help keep your flight path clear.
- **Target:** Item Type: Weapon Mount | Manufacturer: Crusader Industries | Size: 3 |  | This pilot-controlled, dual-linked weapon mount is bespoke to the Mercury Star Runner and outfitted with two size-3 laser repeaters ready to help keep your flight path clear.

</details>

### `item_Desc_ctl_deckcrew_undersuit_01_lum01_01`  (4.3.2-LIVE → target, sim 42%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thi
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thing to

</details>

### `item_Desc_ctl_deckcrew_undersuit_01_lum01_06`  (4.3.2-LIVE → target, sim 42%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thi
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thing to

</details>

### `item_Desc_ctl_deckcrew_undersuit_01_lum01_07`  (4.3.2-LIVE → target, sim 42%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thi
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | Featuring durable poly-fiber fabric, a comfortable fit, and a special holiday design, this undersuit is the perfect thing to

</details>

### `item_Desc_dmc_frontier_pants_01_02_11,P`  (4.5.0-LIVE → target, sim 42%)

| | 4.5.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PLACEHOLDER` | `PLACEHOLDER - dmc_frontier_pants_01_02_11` |

```diff
# 4.5.0-LIVE  →  target
- PLACEHOLDER
+ PLACEHOLDER - dmc_frontier_pants_01_02_11
```

<details>
<summary>Full previews</summary>

- **Oldest:** PLACEHOLDER
- **Target:** PLACEHOLDER - dmc_frontier_pants_01_02_11

</details>

### `item_Desc_gsb_frontier_boots_01_02_11,P`  (4.5.0-LIVE → target, sim 42%)

| | 4.5.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PLACEHOLDER` | `PLACEHOLDER - gsb_frontier_boots_01_02_11` |

```diff
# 4.5.0-LIVE  →  target
- PLACEHOLDER
+ PLACEHOLDER - gsb_frontier_boots_01_02_11
```

<details>
<summary>Full previews</summary>

- **Oldest:** PLACEHOLDER
- **Target:** PLACEHOLDER - gsb_frontier_boots_01_02_11

</details>

### `Pyro5e_Fuego_desc`  (4.3.2-LIVE → target, sim 44%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Hephaestanite Aslarite Borase Bexalite Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Ca…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Hephaestanite Aslarite Borase Bexalite Potential Hand Mineables: Aphorite Dolivine Janalite Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Caves) Bluemoon Fungus (Caves)
```

<details>
<summary>Full previews</summary>

- **Oldest:** High amounts of iron-sulfide in Fuego’s soil turn it a livid shade of yellow-black.
- **Target:** High amounts of iron-sulfide in Fuego’s soil turn it a livid shade of yellow-black. |  | Potential Ship Mineables: | Hephaestanite | Aslarite | Borase | Bexalite |  | Potential Hand Mineables: | Aphorite | Dolivine | Janalite |  | Potential Harvestables: | Ranta Dung (Caves) | Amioshi Plague (Caves) | Bluemoon 

</details>

### `Pyro5c_Adir_desc`  (4.3.2-LIVE → target, sim 44%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Iron Tungsten Borase Riccite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amiosh…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Iron Tungsten Borase Riccite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Caves) Bluemoon Fungus (Caves)
```

<details>
<summary>Full previews</summary>

- **Oldest:** The crater-ridden surface of Adir is interspersed with rocky hills and jagged mountains.
- **Target:** The crater-ridden surface of Adir is interspersed with rocky hills and jagged mountains. |  | Potential Ship Mineables: | Iron | Tungsten | Borase | Riccite |  | Potential Hand Mineables: | Aphorite | Dolivine | Hadanite | Janalite (Caves only) |  | Potential Harvestables: | Ranta Dung (Caves) | Amioshi Plague 

</details>

### `Pyro2_desc`  (4.3.2-LIVE → target, sim 45%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Hephaestanite Iron Tin Stileron Potential Ground Vehicle Mineables: Glacosite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) …` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Hephaestanite Iron Tin Stileron Potential Ground Vehicle Mineables: Glacosite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Pingala Seeds Ra…
```

<details>
<summary>Full previews</summary>

- **Oldest:** The coreless Monox, nicknamed for the toxic carbon monoxide in its part-oxygen atmosphere, bears the scars of old mining operations.
- **Target:** The coreless Monox, nicknamed for the toxic carbon monoxide in its part-oxygen atmosphere, bears the scars of old mining operations. |  | Potential Ship Mineables: | Hephaestanite | Iron | Tin | Stileron |  | Potential Ground Vehicle Mineables: | Glacosite |  | Potential Hand Mineables: | Aphorite | Doliv

</details>

### `item_Desc_ksar_undersuit_01`  (4.3.2-LIVE → target, sim 46%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU` | `5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%` |

```diff
# 4.3.2-LIVE  →  target
- 10% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s Carrying Capacity: 8.0 µSCU
+ 5% Temp. Rating: -30 / 60 °C Radiation Protection: 15200 REM Radiation Scrub Rate: 81 REM/s G-Force Tolerance: +90%
```

<details>
<summary>Full previews</summary>

- **Oldest:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | This baseline undersuit from Kastak Arms offers complete protection seal from the elements and compatibility with multi
- **Target:** Item Type: Undersuit | Damage Reduction: 5% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | G-Force Tolerance: +90% |  | This baseline undersuit from Kastak Arms offers complete protection seal from the elements and compatibility with multiple a

</details>

### `item_Desc_cbd_hat_03_01_CFP_var2,P`  (4.5.0-LIVE → target, sim 47%)

| | 4.5.0-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `PLACEHOLDER` | `PLACEHOLDER - cbd_hat_03_01_CFP_var2` |

```diff
# 4.5.0-LIVE  →  target
- PLACEHOLDER
+ PLACEHOLDER - cbd_hat_03_01_CFP_var2
```

<details>
<summary>Full previews</summary>

- **Oldest:** PLACEHOLDER
- **Target:** PLACEHOLDER - cbd_hat_03_01_CFP_var2

</details>

### `Pyro5b_Vatra_desc`  (4.3.2-LIVE → target, sim 47%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Iron Silicon Gold Riccite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amioshi P…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Iron Silicon Gold Riccite Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Caves) Amioshi Plague (Caves) Bluemoon Fungus (Caves)
```

<details>
<summary>Full previews</summary>

- **Oldest:** The thick, high-pressure nitrogen-methane atmosphere of this moon hides a dark and eerie landscape.
- **Target:** The thick, high-pressure nitrogen-methane atmosphere of this moon hides a dark and eerie landscape. |  | Potential Ship Mineables: | Iron | Silicon | Gold | Riccite |  | Potential Hand Mineables: | Aphorite | Dolivine | Hadanite | Janalite (Caves only) |  | Potential Harvestables: | Ranta Dung (Caves) | Amioshi

</details>

### `item_descarma_barrel_stab_s2_contestedzonereward`  (4.3.2-LIVE → target, sim 49%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Heat: -80% Aim Recoil: +40% Visual Recoil: -15%` |
| 🔴 removed | `Recoil Stability: +15% Recoil Kick: +40% Spread: +25%` | — |
| 🔄 replaced | `Cost Per Shot:` | `Consumption:` |
| 🔄 replaced | `Reduce energy weapon recoil with` | `ArmaMod designed` |
| 🔄 replaced | `Stabilizer2. ArmaMod designed the` | `Stabilizer2` |
| 🔄 replaced | `both horizontal and vertical recoil to ensure` | `heat distribution and visual stability allowing for` |
| 🔄 replaced | `damage.` | `damage at the cost of expending more energy.` |

```diff
# 4.3.2-LIVE  →  target
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

- **Oldest:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Damage: +12.5% | Recoil Stability: +15% | Recoil Kick: +40% | Spread: +25% | Ammo Cost Per Shot: +100% |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both h
- **Target:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Heat: -80% | Aim Recoil: +40% | Visual Recoil: -15% | Damage: +12.5% | Ammo Consumption: +100% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve heat distribution and visual stability allowing for 

</details>

### `Pyro4_desc`  (4.3.2-LIVE → target, sim 50%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🟢 added | — | `Potential Ship Mineables: Copper Laranite Borase Stileron Potential Ground Vehicle Mineables: Feynmaline Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only)…` |

```diff
# 4.3.2-LIVE  →  target
+ Potential Ship Mineables: Copper Laranite Borase Stileron Potential Ground Vehicle Mineables: Feynmaline Potential Hand Mineables: Aphorite Dolivine Hadanite Janalite (Caves only) Potential Harvestables: Ranta Dung (Cav…
```

<details>
<summary>Full previews</summary>

- **Oldest:** Astronomers theorize that in the distant past, Pyro IV collided with a planet-sized mass, warping the landscape and knocking it into the orbit of Pyro V.
- **Target:** Astronomers theorize that in the distant past, Pyro IV collided with a planet-sized mass, warping the landscape and knocking it into the orbit of Pyro V. |  | Potential Ship Mineables: | Copper | Laranite | Borase | Stileron |  | Potential Ground Vehicle Mineables: | Feynmaline |  | Potential Hand Min

</details>

### `ui_pause_PopupQuitGame_Title`  (4.3.2-LIVE → target, sim 50%)

| | 4.3.2-LIVE | target |
|---|------------|-----------|
| 🔄 replaced | `Game` | `to desktop` |

```diff
# 4.3.2-LIVE  →  target
- Game
+ to desktop
```

<details>
<summary>Full previews</summary>

- **Oldest:** Quit Game
- **Target:** Quit to desktop

</details>

## High-similarity pairwise changes (clearest wording edits)

_Same key, consecutive builds, sim ≥ 88% — these are the edits that look identical in full-string tables but jump out in a diff._

### `Foxwell_ShipAmbush_VE_desc_001`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)
- Edge: ['outlaw', 'ambush'] → ['outlaw', 'ambush']

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `</EM4>~mission(AmbushTarget)</EM4>.` | `<EM4>~mission(AmbushTarget)</EM4>.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- </EM4>~mission(AmbushTarget)</EM4>.
+ <EM4>~mission(AmbushTarget)</EM4>.
```

**Inline:** Care to help us ghost a bad guy?  / / We’ve been hired to hunt down an outlaw flying a ~~</EM4>~mission(AmbushTarget)</EM4>.~~**<EM4>~mission(AmbushTarget)</EM4>.** Shouldn’t be too hard since they take the same flightpath each day. T … s interested, please reach out to one of our contract representatives.


### `Shubin_Industrial_HandMining_Nyx_M_PlanetarySystem_Desc_001`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)
- Edge: ['outlaws'] → ['outlaws']

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `<EM4> Sadaryx` | `<EM4>Sadaryx` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- <EM4> Sadaryx
+ <EM4>Sadaryx
```

**Inline:** CONTRACT: Mining Order / LOCATION: Nyx / / DETAILS: / One of our prospecting … gain access to a <EM4>QV Breaker Station</EM4>, collect the required ~~<EM4> Sadaryx~~**<EM4>Sadaryx** ore</EM4>, and deliver it to the freight elevator located at <EM4>~mi … countable for any damages accrued during the duration of the contract.


### `EckhartSecurity_EliminateAll_DC_Desc_001`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)
- Edge: ['outlaws', 'lethal'] → ['outlaws', 'lethal']

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `</EM4>~mission(Location)</EM4>.` | `<EM4>~mission(Location)</EM4>.` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- </EM4>~mission(Location)</EM4>.
+ <EM4>~mission(Location)</EM4>.
```

**Inline:** ECKHART SECURITY, LLC. / CONTRACTS & DISPATCH / / CONTRACT TYPE: Clear Loca … ding to onsite personnel, the outlaws are currently holed up near the ~~</EM4>~mission(Location)</EM4>.~~**<EM4>~mission(Location)</EM4>.** Approach with caution and be prepared to use lethal force if the outl … tended to be for the use of the individual or entity designated above.


### `fleetweek2950_holoviewer_g12_desc`  4.8.0-PTU → 4.9.0-LIVE (sim 100%)

| | 4.8.0-PTU | 4.9.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `gravlevs` | `grav-levs` |

```diff
# 4.8.0-PTU  →  4.9.0-LIVE
- gravlevs
+ grav-levs
```

**Inline:** While larger vehicles like the Tumbril Nova and Anvil Ballista may be … transported to provide greater mission flexibility, these rovers and ~~gravlevs~~**grav-levs** often allow tactical responsiveness to a wider variety of terrain and … ng sites located in active combat areas with severe weather patterns. /


### `Battaglia_RPT_RecoverItem_VH_01_desc`  4.9.0-LIVE → 4.10.0-PTU (sim 100%)
- Edge: ['killed', 'ambush'] → ['killed', 'ambush']

| | 4.9.0-LIVE | 4.10.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `be` | `bet` |

```diff
# 4.9.0-LIVE  →  4.10.0-PTU
- be
+ bet
```

**Inline:** *********** People's Alliance *********** / ******/ 'Stronger When Unite … y careful. They said it was a large group that attacked them, and I'd ~~be~~**bet** <EM4>they're still in the area</EM4>. / / PAYMENT: / Standard listed rate upon delivery / / AUTHORIZATION: / Battaglia, Recco


### `Vaughn_EliminateSpecific_FPS_storm_H_desc_003`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `surpremely` | `supremely` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- surpremely
+ supremely
```

**Inline:** A previous target I had thought to have been eliminated seems to have … erc over at <EM4>~mission(Location)</EM4> working for ASD. While I am ~~surpremely~~**supremely** disappointed with the contractor who claimed to have eliminated <EM4> … ority. / / I trust you'll do better than my former subcontractor, / / Vaughn


### `item_Desc_qrt_specialist_medium_core_01_03`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `detailings` | `detailing` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- detailings
+ detailing
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -61 / 91 ° … a knee length fitted cape. / / The Elysium edition combines bright gold ~~detailings~~**detailing** of winged skulls with a navy blue.


### `item_Desc_qrt_specialist_medium_legs_01_03`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `detailings` | `detailing` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- detailings
+ detailing
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -61 / 91 ° … a knee length fitted cape. / / The Elysium edition combines bright gold ~~detailings~~**detailing** of winged skulls with a navy blue.


### `item_Descvolt_sniper_energy_01_store01`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `embelished` | `embellished` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- embelished
+ embellished
```

**Inline:** Manufacturer: Verified Offworld Laser Technologies / Item Type: Sniper R … tly more noise and heat. / / The Golden Blossom version is mostly black, ~~embelished~~**embellished** with intricate golden flowers, giving your enemies one final glimpse of life before death.


### `Vaughn_EliminateSpecific_FPS_storm_H_desc_004`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `<EM4>~mission(TargetName\|Last)<EM4>` | `<EM4>~mission(TargetName\|Last)</EM4>` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- <EM4>~mission(TargetName|Last)<EM4>
+ <EM4>~mission(TargetName|Last)</EM4>
```

**Inline:** Have a difficult contract for a discerning operative. Target's name is … syndicate enforcer and bagman. / / I'll need you to get in and take out ~~<EM4>~mission(TargetName|Last)<EM4>~~**<EM4>~mission(TargetName|Last)</EM4>** which is easier said then done as they will undoubtedly be entrenched … ity forces, but I believe you'll figure it out. / / All the best, / / Vaughn


### `item_Desc_qrt_specialist_medium_arms_01_03`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `detailings` | `detailing` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- detailings
+ detailing
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -61 / 91 ° … a knee length fitted cape. / / The Elysium edition combines bright gold ~~detailings~~**detailing** of winged skulls with a navy blue.


### `item_Desc_qrt_specialist_medium_helmet_01_03`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `detailings` | `detailing` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- detailings
+ detailing
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -61 / 91 ° … a knee length fitted cape. / / The Elysium edition combines bright gold ~~detailings~~**detailing** of winged skulls with a navy blue.


### `item_Descvolt_optics_tsco_x8_s3_store01`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `embelished` | `embellished` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- embelished
+ embellished
```

**Inline:** Manufacturer: VOLT / Type: Telescopic / Attachment Point: Optic / Magnificat … ou always get your mark. / / The Golden Blossom version is mostly black, ~~embelished~~**embellished** with intricate golden flowers, giving your enemies one final glimpse of life before death.


### `RedWind_RecoverCargo_Super_Description`  4.6.0-PTU → 4.7.0-LIVE (sim 100%)
- Edge: ['killed', 'outlaws'] → ['killed', 'outlaws']

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `stationery` | `stationary` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- stationery
+ stationary
```

**Inline:** RED WIND LINEHAUL / 'YOUR GOODS IN GOOD HANDS' / ------------------------- … te their last job. The cargo they were supposed to deliver is sitting ~~stationery~~**stationary** in their former ship in the location listed below. / / RECOVERY LOCATION … vey on our Spectrum page for a chance to enter our monthly prize draw.


### `item_Desc_srvl_combat_medium_core_01_03_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `concotion` | `concoction` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- concotion
+ concoction
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -50 / 80 ° … rom scavenged metals and ragged clothes, the Carrion armor is a crude ~~concotion~~**concoction** of repurposed materials that demonstrates you'll do anything it takes … version is sprayed with white paint and anointed with bone fragments.


### `HeadHunters_RecoverCargo_Hard_Description`  4.7.1-LIVE → 4.8.0-PTU (sim 100%)
- Edge: ['hell', 'carcass'] → ['hell', 'carcass']

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `kopian` | `kopion` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- kopian
+ kopion
```

**Inline:** Looking for a hauler to pick up some cargo for me. Thing is, there’s a … ger there’s gonna be more ships swarming around there than flies on a ~~kopian~~**kopion** carcass. If you got some pals you can trust, bring them along and gho … tion|Address)</EM4>, I can get you a nice cut of the sale. / / Stows out.


### `item_Desc_qrt_specialist_medium_backpack_01_03`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `detailings` | `detailing` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- detailings
+ detailing
```

**Inline:** Item Type: Light Backpack / Carrying Capacity: 40K µSCU / Core Compatibili … to a wide variety armors.  / / The Elysium edition combines bright gold ~~detailings~~**detailing** of winged skulls with a navy blue.


### `item_Descnone_lmg_ballistic_01_tint02`  4.4.0-PTU → 4.5.0-LIVE (sim 100%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `50` | `.50` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- 50
+ .50
```

**Inline:** Manufacturer: Unknown / Item Type: LMG / Class: Ballistic / / Magazine Size: … pm / Effective Range: 100 m / / Nothing like ripping through a huge mag of ~~50~~**.50** cal bullets to scare away unwanted guests. Based on a modified FS9, t … ontational approach.  / / The Mustard version features a yellow paintjob.


### `IAE_2955_HoverQuad_Terminus_Desc`  4.8.0-PTU → 4.9.0-LIVE (sim 100%)

| | 4.8.0-PTU | 4.9.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `gravlev` | `grav-lev` |

```diff
# 4.8.0-PTU  →  4.9.0-LIVE
- gravlev
+ grav-lev
```

**Inline:** Manufacturer: Consolidated Outland / Focus: Transport / / Designed as a companion ground vehicle for the Nomad, the HoverQuad's sleek angular frame utilizes four ~~gravlev~~**grav-lev** pads for maximum maneuverability, making it the perfect transport acr … sublime HoverQuad Terminus livery, which is black with red flourishes.


### `item_Desc_srvl_combat_medium_arms_01_03_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `concotion` | `concoction` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- concotion
+ concoction
```

**Inline:** Item Type: Medium Armor / Damage Reduction: 30% / Temp. Rating: -50 / 80 ° … rom scavenged metals and ragged clothes, the Carrion armor is a crude ~~concotion~~**concoction** of repurposed materials that demonstrates you'll do anything it takes … version is sprayed with white paint and anointed with bone fragments.


### `item_Descnone_lmg_ballistic_01_tint03`  4.4.0-PTU → 4.5.0-LIVE (sim 100%)

| | 4.4.0-PTU | 4.5.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `50` | `.50` |

```diff
# 4.4.0-PTU  →  4.5.0-LIVE
- 50
+ .50
```

**Inline:** Manufacturer: Unknown / Item Type: LMG / Class: Ballistic / / Magazine Size: … pm / Effective Range: 100 m / / Nothing like ripping through a huge mag of ~~50~~**.50** cal bullets to scare away unwanted guests. Based on a modified FS9, t … frontational approach.  / / The Bleach version features a white paintjob.


### `item_Desc_kap_combat_light_core_02_02_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Carrying Capacity: 8k µSC … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … Snow Camo edition is perfect for stalking prey in frozen environments.


### `item_Desc_kap_combat_light_core_03_01_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Carrying Capacity: 8k µSC … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … n flowers, giving your enemies one final glimpse of life before death.


### `item_Desc_kap_combat_light_legs_02_02_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Carrying Capacity: 2.5k µ … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … Snow Camo edition is perfect for stalking prey in frozen environments.


### `item_Desc_kap_combat_light_legs_03_01_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Carrying Capacity: 2.5k µ … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … n flowers, giving your enemies one final glimpse of life before death.


### `item_Desc_kap_combat_light_arms_02_02_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Temp. Rating: -35 / 65 °C … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … Snow Camo edition is perfect for stalking prey in frozen environments.


### `item_Desc_kap_combat_light_arms_03_01_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Temp. Rating: -35 / 65 °C … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … n flowers, giving your enemies one final glimpse of life before death.


### `item_Desc_kap_combat_light_core_02_01_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Carrying Capacity: 8k µSC … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … printed with a dark urban camo pattern alongside ASD's signature logo.


### `item_Desc_kap_combat_light_helmet_02_02_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Temp. Rating: -35 / 65 °C … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … Snow Camo edition is perfect for stalking prey in frozen environments.


### `item_Desc_kap_combat_light_helmet_03_01_01`  4.3.2-LIVE → 4.4.0-PTU (sim 100%)

| | 4.3.2-LIVE | 4.4.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `info` | `into` |

```diff
# 4.3.2-LIVE  →  4.4.0-PTU
- info
+ into
```

**Inline:** Item Type: Light Armor / Damage Reduction: 20% / Temp. Rating: -35 / 65 °C … rers that protect the UEE's special forces. Hair-thin filaments woven ~~info~~**into** the fabric mask the wearer's emissions, making them undetectable via … n flowers, giving your enemies one final glimpse of life before death.

