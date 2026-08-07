# All-keys wording map (older/harder wins)

**Target (current soft stock):** `4.10.0-PTU`

- Corpus versions: 4.3.2-LIVE, 4.4.0-PTU, 4.5.0-LIVE, 4.6.0-LIVE, 4.6.0-PTU, 4.7.0-LIVE, 4.7.0-LIVE-HOTFIX, 4.7.0-PTU, 4.7.1-LIVE, 4.8.0-PTU, 4.9.0-LIVE, 4.10.0-PTU
- Pairwise text changes (any wording change): **1727**
- Steps scored as **softened** (hardness dropped): **71**
- Steps scored as **hardened**: **76**
- Pack keys (harder than target, applied to current): **709**

### How to read diffs

Each restore shows a **phrase-level wording diff** (GitHub paints `-` red / `+` green). Same style as spotlight, soften-map, and build-diffs via `scripts/phrase_diff.py`.

## Policy

1. For every key on the target build, look at all older stocks that have it.
2. If wording never changed → skip.
3. Score each historical string for hardness (edge words, living hell, etc.; soft phrases reduce score).
4. Pick **highest hardness**; ties → **oldest** version.
5. If that beats current target → ship it in `01-classic-all.ini`.

## Top pack restores (by hardness gain)

### `headhunters_bombingrun_multi_E_CFP_desc_001`  (+68.0 hard)  ← `4.3.2-LIVE`
- Edge: ['living hell', 'bomb the living', 'bomb the', 'shitty', 'hell', 'property damage', 'hardworkin'] → target had ['shitty', 'property damage', 'hardworkin']
- Pick: `high_sim=0.926_prefer_oldest;gain=68.0`

| | chosen (4.3.2-LIVE) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `bomb the living hell out of the area.` | `really mess the place up.` |

```diff
# chosen (4.3.2-LIVE)  →  target (soft stock)
- bomb the living hell out of the area.
+ really mess the place up.
```

**Inline:** Every day it seems like Citizens for Prosperity is out here trying to … who really is in charge here. Head to ~mission(Location|Address) and ~~bomb the living hell out of the area.~~**really mess the place up.**  / / Nothing like a bit of property damage to get a point across. / / -Stows out

<details>
<summary>Full previews</summary>

- **Chosen:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure 
- **Target (soft stock):** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure 

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content`  (+24.0 hard)  ← `4.5.0-LIVE`
- Edge: ['killed', 'executed', 'outlaw'] → target had []
- Pick: `low_sim=0.036_harder_only;gain=24.0`

| | chosen (4.5.0-LIVE) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe` | `VOX POPULI Release Edition 4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and ba…` |
| 🔄 replaced | `just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated` | `begun to sell mining rights to the abandoned QV Breaker Stations near the Keeger Belt. But many local miners are wondering what gives Shubin the rights to sell these claims in` |
| 🔄 replaced | `public test of faster-than-light communications to a stunned crowd. Speaking in real time from the press conference in New York, Sol system to a colleague located in Prime, Terra …` | `place? TRIGGERFISH PRANKS ARE ANYTHING BUT FUN Learn how to protect yourself from so-called merrymakers as the hurtful holiday once again threatens to ruin everyone’s day with a g…` |

```diff
# chosen (4.5.0-LIVE)  →  target (soft stock)
- Terra Gazette December 2955 FTL COMMS BREAKTHROUGH Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. “The universe
+ VOX POPULI Release Edition 4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance. Seemingly having learned…
- just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated
+ begun to sell mining rights to the abandoned QV Breaker Stations near the Keeger Belt. But many local miners are wondering what gives Shubin the rights to sell these claims in
- public test of faster-than-light communications to a stunned crowd. Speaking in real time from the press conference in New York, Sol system to a colleague located in Prime, Terra system, Dr. Betel made history with a tr…
+ place? TRIGGERFISH PRANKS ARE ANYTHING BUT FUN Learn how to protect yourself from so-called merrymakers as the hurtful holiday once again threatens to ruin everyone’s day with a good time. LEVSKI JOB FAIR DECLARED SUCCE…
```

<details>
<summary>Full previews</summary>

- **Chosen:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead research
- **Target (soft stock):** VOX POPULI | Release Edition 4.7.0 |  | UEE INTERSYSTEM COMM NETWORK HACKED  | Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance.   |  | 

</details>

### `headhunters_bombingrun_S_desc_001`  (+12.0 hard)  ← `4.7.0-LIVE`
- Edge: ['bombing run', 'blow the'] → target had ['blow the']
- Pick: `high_sim=0.983_prefer_oldest;gain=12.0`

| | chosen (4.7.0-LIVE) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `a bombing run` | `an attack` |

```diff
# chosen (4.7.0-LIVE)  →  target (soft stock)
- a bombing run
+ an attack
```

**Inline:** We've heard news that a new gang are planning ~~a bombing run~~**an attack** on a place over at <EM4>~mission(Location|Address)</EM4>. They figure … ose fuel tanks out of action. We'll take care of the rest. / / -Stows out

<details>
<summary>Full previews</summary>

- **Chosen:** We've heard news that a new gang are planning a bombing run on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the 
- **Target (soft stock):** We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taki

</details>

### `Shubin_Industrial_GroundVehicle_Nyx_VH_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.410_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_E_DiscoverPlanetary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.395_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Small Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Small Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_H_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.425_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Large Scale` | `Lrg. Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Large Scale
+ Lrg. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_M_PlanetarySystem_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.444_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Medium Scale` | `Med. Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Medium Scale
+ Med. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Medium Scale
- **Target (soft stock):** Med. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_VH_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.410_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_E_DiscoverPlanetary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.395_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Small Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Small Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_H_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.400_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Large Scale` | `Med. Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Large Scale
+ Med. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Large Scale
- **Target (soft stock):** Med. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_M_PlanetarySystem_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.439_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Medium Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Medium Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Medium Scale
- **Target (soft stock):** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_VH_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.410_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ground Vehicle Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_HandMining_Intro_Local_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.317_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Shubin Interstellar` | `Small Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Shubin Interstellar
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Shubin Interstellar
- **Target (soft stock):** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_E_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.297_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Desc_002`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.132_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Hand Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `in need of` | `currently looking to fulfil another purchase order for` |
| 🔄 replaced | `ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.` | `materials. We appreciate your help in this matter.` |
| 🔄 replaced | `For a comprehensive list of where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. All Shubin Interstellar contractors` | `There have been reported kopion sightings within the area, so caution is advised. Reminder, since this is a purchase order and not a mining contract, you` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔴 removed | `Prospectors have reported kopion sightings within these caves, so caution is advised.` | — |
| 🔄 replaced | `you have successfully gathered the` | `you’re ready to sell us the required` |
| 🔄 replaced | `DISCLAIMER: As many of these sites have been designated as abandoned or otherwise untenable, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any …` | `*By` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Hand Mining
+ <EM4>~mission(System) </EM4>
- in need of
+ currently looking to fulfil another purchase order for
- ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.
+ materials. We appreciate your help in this matter.
- For a comprehensive list of where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. All Shubin Interstellar contractors
+ There have been reported kopion sightings within the area, so caution is advised. Reminder, since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- Prospectors have reported kopion sightings within these caves, so caution is advised.
- you have successfully gathered the
+ you’re ready to sell us the required
- DISCLAIMER: As many of these sites have been designated as abandoned or otherwise untenable, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain from …
+ *By
```

<details>
<summary>Full previews</summary>

- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Hand Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of materials. We appreciate your help i

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Title`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Title_002`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_E_Local_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.297_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_H_PlanetarySystem_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.301_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_M_DiscoverPlanetary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.405_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Medium Scale` | `Med. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Medium Scale
+ Med. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Medium Scale
- **Target (soft stock):** Med. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_Nyx_VH_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.423_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_S_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_S_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_VH_Interstellar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.423_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_E_Local_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.297_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_E_PlanetarySystem_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.297_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_PlanetarySystem_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.301_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_Planetary_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.301_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.301_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_M_DiscoverPlanetary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.405_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Medium Scale` | `Med. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Medium Scale
+ Med. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Medium Scale
- **Target (soft stock):** Med. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_S_Solar_Title`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_S_Solar_Title_002`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.293_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_VH_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.423_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **Chosen:** Hand Mining Request: Major Scale
- **Target (soft stock):** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.093_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Ship Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `Due to changes in our sourcing pipeline,` |
| 🔄 replaced | `in need of` | `currently looking to purchase` |
| 🔄 replaced | `ore, mineable` | `refined materials` |
| 🔄 replaced | `numerous locations across <EM4>~mission(System)</EM4>.` | `independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners find that strengthening their ti…` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `All Shubin Interstellar contractors` | `While you're there, feel free to read the first part <EM4>Mining Fundamentals #1: Basic Overview</EM4> if you want a refresher on how to get the materials. Since this is a purchas…` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔄 replaced | `As we wish` | `Please note that in an effort` |
| 🔄 replaced | `this process as quickly as possible, <EM4>the ore` | `future use of these materials, <EM4>they` |
| … | *+6 more hunks* | |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Ship Mining
+ <EM4>~mission(System) </EM4>
+ Due to changes in our sourcing pipeline,
- in need of
+ currently looking to purchase
- ore, mineable
+ refined materials
- numerous locations across <EM4>~mission(System)</EM4>.
+ independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners find that strengthening their ties to Shubin to be a wise long-term inve…
- All Shubin Interstellar contractors
+ While you're there, feel free to read the first part <EM4>Mining Fundamentals #1: Basic Overview</EM4> if you want a refresher on how to get the materials. Since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- As we wish
+ Please note that in an effort
- this process as quickly as possible, <EM4>the ore
+ future use of these materials, <EM4>they
# … +6 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials fr

</details>

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.294_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Small Scale` | `Small Purchase Order: Ship Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ship Mining Request: Small Scale
+ Small Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ship Mining Request: Small Scale
- **Target (soft stock):** Small Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_H_Secondary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.299_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Large Scale` | `Lrg. Purchase Order: Ship Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ship Mining Request: Large Scale
+ Lrg. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ship Mining Request: Large Scale
- **Target (soft stock):** Lrg. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.130_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Ship Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `in need of` | `currently looking to fulfil another purchase order for` |
| 🔄 replaced | `ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.` | `refined materials. We appreciate your help in this matter.` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `All Shubin Interstellar contractors` | `Since this is a purchase order and not a mining contract, you` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔄 replaced | `In` | `Please note that in` |
| 🔄 replaced | `minerals, <EM4>the ore` | `materials, <EM4>they` |
| 🔄 replaced | `it is submitted</EM4>.` | `delivery</EM4>.` |
| … | *+5 more hunks* | |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Ship Mining
+ <EM4>~mission(System) </EM4>
- in need of
+ currently looking to fulfil another purchase order for
- ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.
+ refined materials. We appreciate your help in this matter.
- All Shubin Interstellar contractors
+ Since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- In
+ Please note that in
- minerals, <EM4>the ore
+ materials, <EM4>they
- it is submitted</EM4>.
+ delivery</EM4>.
# … +5 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate you

</details>

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.353_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Medium Scale` | `Med. Purchase Order: Ship Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ship Mining Request: Medium Scale
+ Med. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ship Mining Request: Medium Scale
- **Target (soft stock):** Med. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_S_Secondary_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.319_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Extreme Scale` | `Mjr. Purchase Order: Ship Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ship Mining Request: Extreme Scale
+ Mjr. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ship Mining Request: Extreme Scale
- **Target (soft stock):** Mjr. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_VE_Local_Title_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- Pick: `low_sim=0.286_harder_only;gain=10.0`

| | chosen (4.6.0-PTU) | target (soft stock) |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Very Small Scale` | `XS Purchase Order: Ship Mined Ore` |

```diff
# chosen (4.6.0-PTU)  →  target (soft stock)
- Ship Mining Request: Very Small Scale
+ XS Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **Chosen:** Ship Mining Request: Very Small Scale
- **Target (soft stock):** XS Purchase Order: Ship Mined Ore

</details>

## Top soften steps (history receipts)

### `headhunters_bombingrun_multi_E_CFP_desc_001`  4.7.1-LIVE → 4.8.0-PTU  (hard 77.0 → 9.0)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `bomb the living hell out of the area.` | `really mess the place up.` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- bomb the living hell out of the area.
+ really mess the place up.
```

**Inline:** Every day it seems like Citizens for Prosperity is out here trying to … who really is in charge here. Head to ~mission(Location|Address) and ~~bomb the living hell out of the area.~~**really mess the place up.**  / / Nothing like a bit of property damage to get a point across. / / -Stows out

<details>
<summary>Full previews</summary>

- **From:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure they could use a rem
- **To:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure they could use a rem

</details>

### `Journal_General_FrontendNewspaperHeadlines_Content`  4.6.0-PTU → 4.7.0-LIVE  (hard 17.0 → 1.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `New United` | `VOX POPULI` |
| 🔄 replaced | `4.6.0 FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT Deadly ‘Molina Mold’ contaminates Levski station in` | `4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance. Seemingly h…` |
| 🔄 replaced | `System. Following weeks of` | `I shows no signs of slowing. Most concerning are` |
| 🔄 replaced | `unknown illness afflicting the residents of Levski, the source has been confirmed as a new species of mold whose airborne spores cause potentially fatal fungal infections in Human…` | `group who seem` |
| 🔄 replaced | `faulty. Named “Molina Mold” after the first person to be killed by the ailment, it has since filled clinics and hospitals in the` | `establishing fortified settlements at an alarming rate. While it is not yet clear who these newcomers to` |
| 🔄 replaced | `system with people experiencing symptoms. While` | `are or what their intentions might be, what is rapidly becoming apparent is that if` |
| 🟢 added | — | `do not start to take the task of settling on Nyx I seriously, there` |
| 🔄 replaced | `working with the UEE-based “Alliance Aid” relief group to replace the filters and distribute treatment, residents and visitors alike are being strongly advised to avoid areas in L…` | `a high chance that there will be only scraps left on the table when the governing committee does decide to act. DUBIOUS SHUBIN MINING RIGHTS As the massive conglomerate continues …` |
| 🔄 replaced | `the project to outfit their entire comm network with the new faster-than-light upgrades. An Aciedo spokesperson` | `mining to mercenary work have` |
| 🔄 replaced | `they have begun to seamlessly roll out access to the service, with hundreds of thousands of users utilizing the new inter-system comms already. NEW RSI MUSEUM EXHIBIT UNVEILED Ent…` | `it ha led to a sharp spike in employment rates in Nyx.` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- New United
+ VOX POPULI
- 4.6.0 FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT Deadly ‘Molina Mold’ contaminates Levski station in
+ 4.7.0 UEE INTERSYSTEM COMM NETWORK HACKED Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance. Seemingly having learned nothing from the botched i…
- System. Following weeks of
+ I shows no signs of slowing. Most concerning are
- unknown illness afflicting the residents of Levski, the source has been confirmed as a new species of mold whose airborne spores cause potentially fatal fungal infections in Humans. The source of the mold growth was tra…
+ group who seem
- faulty. Named “Molina Mold” after the first person to be killed by the ailment, it has since filled clinics and hospitals in the
+ establishing fortified settlements at an alarming rate. While it is not yet clear who these newcomers to
- system with people experiencing symptoms. While
+ are or what their intentions might be, what is rapidly becoming apparent is that if
+ do not start to take the task of settling on Nyx I seriously, there
- working with the UEE-based “Alliance Aid” relief group to replace the filters and distribute treatment, residents and visitors alike are being strongly advised to avoid areas in Levski experiencing mold growth. ACIEDO F…
+ a high chance that there will be only scraps left on the table when the governing committee does decide to act. DUBIOUS SHUBIN MINING RIGHTS As the massive conglomerate continues to pillage the system, many miners quest…
- the project to outfit their entire comm network with the new faster-than-light upgrades. An Aciedo spokesperson
+ mining to mercenary work have
- they have begun to seamlessly roll out access to the service, with hundreds of thousands of users utilizing the new inter-system comms already. NEW RSI MUSEUM EXHIBIT UNVEILED Enthusiasts of the ship manufacturer giving…
+ it ha led to a sharp spike in employment rates in Nyx.
```

<details>
<summary>Full previews</summary>

- **From:** New United | Release Edition 4.6.0 |  | FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT | Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. |  | Following weeks of reports of a new unknown illness afflicting the resident
- **To:** VOX POPULI | Release Edition 4.7.0 |  | UEE INTERSYSTEM COMM NETWORK HACKED  | Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance.   |  | Seemingly having lea

</details>

### `headhunters_bombingrun_S_desc_001`  4.7.1-LIVE → 4.8.0-PTU  (hard 5.0 → -7.0)

| | 4.7.1-LIVE | 4.8.0-PTU |
|---|------------|-----------|
| 🔄 replaced | `a bombing run` | `an attack` |

```diff
# 4.7.1-LIVE  →  4.8.0-PTU
- a bombing run
+ an attack
```

**Inline:** We've heard news that a new gang are planning ~~a bombing run~~**an attack** on a place over at <EM4>~mission(Location|Address)</EM4>. They figure … ose fuel tanks out of action. We'll take care of the rest. / / -Stows out

<details>
<summary>Full previews</summary>

- **From:** We've heard news that a new gang are planning a bombing run on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking. |  | But little 
- **To:** We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking. |  | But little do t

</details>

### `Shubin_Industrial_GroundVehicle_Nyx_VH_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Major Scale
- **To:** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_E_DiscoverPlanetary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Small Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Small Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Small Scale
- **To:** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_H_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Large Scale` | `Lrg. Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Large Scale
+ Lrg. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_M_PlanetarySystem_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Medium Scale` | `Med. Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Medium Scale
+ Med. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Medium Scale
- **To:** Med. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Pyro_VH_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Major Scale
- **To:** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_E_DiscoverPlanetary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Small Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Small Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Small Scale
- **To:** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_H_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Large Scale` | `Med. Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Large Scale
+ Med. Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Large Scale
- **To:** Med. Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_M_PlanetarySystem_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Medium Scale` | `Small Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Medium Scale
+ Small Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Medium Scale
- **To:** Small Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_GroundVehicle_Stanton_VH_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ground Vehicle Mining Request: Major Scale` | `XL Purchase Order: Vehicle Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ground Vehicle Mining Request: Major Scale
+ XL Purchase Order: Vehicle Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ground Vehicle Mining Request: Major Scale
- **To:** XL Purchase Order: Vehicle Mined Ore

</details>

### `Shubin_Industrial_HandMining_Intro_Local_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Shubin Interstellar` | `Small Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Shubin Interstellar
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Shubin Interstellar
- **To:** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_E_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Small Scale
- **To:** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Desc_002`  4.6.0-PTU → 4.7.0-LIVE  (hard -9.0 → -19.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Hand Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `in need of` | `currently looking to fulfil another purchase order for` |
| 🔄 replaced | `ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.` | `materials. We appreciate your help in this matter.` |
| 🔄 replaced | `For a comprehensive list of where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. All Shubin Interstellar contractors` | `There have been reported kopion sightings within the area, so caution is advised. Reminder, since this is a purchase order and not a mining contract, you` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔴 removed | `Prospectors have reported kopion sightings within these caves, so caution is advised.` | — |
| 🔄 replaced | `you have successfully gathered the` | `you’re ready to sell us the required` |
| 🔄 replaced | `DISCLAIMER: As many of these sites have been designated as abandoned or otherwise untenable, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any …` | `*By` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Hand Mining
+ <EM4>~mission(System) </EM4>
- in need of
+ currently looking to fulfil another purchase order for
- ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.
+ materials. We appreciate your help in this matter.
- For a comprehensive list of where to find these minerals, consult <EM4>Mining Fundamentals #2: Where to Mine</EM4> in your mobiGlas Journal. All Shubin Interstellar contractors
+ There have been reported kopion sightings within the area, so caution is advised. Reminder, since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- Prospectors have reported kopion sightings within these caves, so caution is advised.
- you have successfully gathered the
+ you’re ready to sell us the required
- DISCLAIMER: As many of these sites have been designated as abandoned or otherwise untenable, Shubin Interstellar is willing to award contractors by <EM4>allowing them to keep any surplus materials that they obtain from …
+ *By
```

<details>
<summary>Full previews</summary>

- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Hand Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of materials. We appreciate your help in this matter. |  | ~mis

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Title`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Nyx_S_Interstellar_Title_002`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_E_Local_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Small Scale
- **To:** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_H_PlanetarySystem_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_M_DiscoverPlanetary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Medium Scale` | `Med. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Medium Scale
+ Med. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Medium Scale
- **To:** Med. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_Nyx_VH_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Major Scale
- **To:** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_S_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_S_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Pyro_VH_Interstellar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Major Scale
- **To:** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_E_Local_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Small Scale
- **To:** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_E_PlanetarySystem_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Small Scale` | `Small Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Small Scale
+ Small Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Small Scale
- **To:** Small Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_PlanetarySystem_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_Planetary_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_H_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Large Scale` | `Lrg. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Large Scale
+ Lrg. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_M_DiscoverPlanetary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Medium Scale` | `Med. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Medium Scale
+ Med. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Medium Scale
- **To:** Med. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_S_Solar_Title`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_S_Solar_Title_002`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Extreme Scale` | `Mjr. Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Extreme Scale
+ Mjr. Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_HandMining_Stanton_VH_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Hand Mining Request: Major Scale` | `XL Purchase Order: Hand Mined Materials` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Hand Mining Request: Major Scale
+ XL Purchase Order: Hand Mined Materials
```

<details>
<summary>Full previews</summary>

- **From:** Hand Mining Request: Major Scale
- **To:** XL Purchase Order: Hand Mined Materials

</details>

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard -19.0 → -29.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Ship Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `Due to changes in our sourcing pipeline,` |
| 🔄 replaced | `in need of` | `currently looking to purchase` |
| 🔄 replaced | `ore, mineable` | `refined materials` |
| 🔄 replaced | `numerous locations across <EM4>~mission(System)</EM4>.` | `independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners find that strengthening their ti…` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `All Shubin Interstellar contractors` | `While you're there, feel free to read the first part <EM4>Mining Fundamentals #1: Basic Overview</EM4> if you want a refresher on how to get the materials. Since this is a purchas…` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔄 replaced | `As we wish` | `Please note that in an effort` |
| 🔄 replaced | `this process as quickly as possible, <EM4>the ore` | `future use of these materials, <EM4>they` |
| … | *+6 more hunks* | |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Ship Mining
+ <EM4>~mission(System) </EM4>
+ Due to changes in our sourcing pipeline,
- in need of
+ currently looking to purchase
- ore, mineable
+ refined materials
- numerous locations across <EM4>~mission(System)</EM4>.
+ independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners find that strengthening their ties to Shubin to be a wise long-term inve…
- All Shubin Interstellar contractors
+ While you're there, feel free to read the first part <EM4>Mining Fundamentals #1: Basic Overview</EM4> if you want a refresher on how to get the materials. Since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- As we wish
+ Please note that in an effort
- this process as quickly as possible, <EM4>the ore
+ future use of these materials, <EM4>they
# … +6 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials from independent miner

</details>

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Small Scale` | `Small Purchase Order: Ship Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ship Mining Request: Small Scale
+ Small Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ship Mining Request: Small Scale
- **To:** Small Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_H_Secondary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Large Scale` | `Lrg. Purchase Order: Ship Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ship Mining Request: Large Scale
+ Lrg. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ship Mining Request: Large Scale
- **To:** Lrg. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard -19.0 → -29.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Industrial` | `Purchase Order` |
| 🔄 replaced | `~mission(System) REQ EXPERIENCE: Ship Mining` | `<EM4>~mission(System) </EM4>` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `in need of` | `currently looking to fulfil another purchase order for` |
| 🔄 replaced | `ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.` | `refined materials. We appreciate your help in this matter.` |
| 🔄 replaced | `` | `` |
| 🔄 replaced | `All Shubin Interstellar contractors` | `Since this is a purchase order and not a mining contract, you` |
| 🔄 replaced | `their` | `your` |
| 🔄 replaced | `equipment. For this contract you will need` | `equipment, such as` |
| 🔄 replaced | `In` | `Please note that in` |
| 🔄 replaced | `minerals, <EM4>the ore` | `materials, <EM4>they` |
| 🔄 replaced | `it is submitted</EM4>.` | `delivery</EM4>.` |
| … | *+5 more hunks* | |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Industrial
+ Purchase Order
- ~mission(System) REQ EXPERIENCE: Ship Mining
+ <EM4>~mission(System) </EM4>
- in need of
+ currently looking to fulfil another purchase order for
- ore, mineable from numerous locations across <EM4>~mission(System)</EM4>.
+ refined materials. We appreciate your help in this matter.
- All Shubin Interstellar contractors
+ Since this is a purchase order and not a mining contract, you
- their
+ your
- equipment. For this contract you will need
+ equipment, such as
- In
+ Please note that in
- minerals, <EM4>the ore
+ materials, <EM4>they
- it is submitted</EM4>.
+ delivery</EM4>.
# … +5 more hunks (truncated)
```

<details>
<summary>Full previews</summary>

- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate your help in this matte

</details>

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Medium Scale` | `Med. Purchase Order: Ship Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ship Mining Request: Medium Scale
+ Med. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ship Mining Request: Medium Scale
- **To:** Med. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_S_Secondary_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Extreme Scale` | `Mjr. Purchase Order: Ship Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ship Mining Request: Extreme Scale
+ Mjr. Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ship Mining Request: Extreme Scale
- **To:** Mjr. Purchase Order: Ship Mined Ore

</details>

### `Shubin_Industrial_ShipMining_Nyx_VE_Local_Title_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 0.0 → -10.0)

| | 4.6.0-PTU | 4.7.0-LIVE |
|---|------------|-----------|
| 🔄 replaced | `Ship Mining Request: Very Small Scale` | `XS Purchase Order: Ship Mined Ore` |

```diff
# 4.6.0-PTU  →  4.7.0-LIVE
- Ship Mining Request: Very Small Scale
+ XS Purchase Order: Ship Mined Ore
```

<details>
<summary>Full previews</summary>

- **From:** Ship Mining Request: Very Small Scale
- **To:** XS Purchase Order: Ship Mined Ore

</details>
