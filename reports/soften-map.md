# Soften map — Star Citizen localization

Wording changes across stock `global.ini` extracts that look like **tone softening** (lost edge, euphemism swaps). Auto-detected; review before shipping a pack.

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

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.3.2-LIVE → 4.4.0-PTU (score 34.45, sim 2%)

- **Old:** AMELIA BOYD SPOTTED IN STANTON | Guild members advised to be on the lookout for Boyd.  |  | Multiple confirmed sightings of Amelia Boyd in Stanton have some Mercenary Guild officials concerned. Boyd’s movements coincide with increased activity by Frontier Fighters in both Stanton and Pyro, leading to speculation that another attack may be imminent.
- **New:** VOX POPULI | The Voice of the People’s Alliance | November 2955 |  | ALBERTSON FAMILY KILLED IN VANDUUL RAID  | Governing committee offers condolences but no solutions as the death toll continues to rise. |  | The Albertson Family Mining Post had just started its shift, when the Vanduul raiders struck without warning, killing the entire crew within

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.3.2-LIVE → 4.4.0-PTU (score 31.93, sim 18%)

- **Old:** Crosshair: Mercenary Guild News
- **New:** VOX POPULI: The Voice of the People’s Alliance

### `item_Desc_srvl_heavy_armor_01_Shared` — 4.3.2-LIVE → 4.4.0-PTU (score 31.62, sim 19%)

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting outlaws in Pyro has some kickas
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed to disperse the force of impacts and a high, rei

### `item_Desc_srvl_heavy_armor_01_legs` — 4.3.2-LIVE → 4.4.0-PTU (score 30.67, sim 21%)

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for itself targeting o
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 7.5 µSCU |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed to disperse the fo

### `item_Desc_srvl_heavy_core_01` — 4.3.2-LIVE → 4.4.0-PTU (score 30.1, sim 23%)

- **Old:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 8.0 µSCU | Backpacks: All |  | Some consider the Overlords heroes and other criminals. Doomsday doesn't care either way. All we know is that the vigilante group that made a name for i
- **New:** Item Type: Heavy Armor | Damage Reduction: 40% | Temp. Rating: -77 / 107 °C | Radiation Protection: 26800 REM | Radiation Scrub Rate: 145.8 REM/s | Carrying Capacity: 12.0 µSCU | Backpacks: All |  | The Overlord armor lets your foes know that you mean business. This heavy armor set is constructed with durable composite plating strategically placed 

### `item_Desc_srvl_undersuit_02_01_02` — 4.3.2-LIVE → 4.4.0-PTU (score 20.79, sim 46%)

- **Old:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s | Carrying Capacity: 8.0 µSCU |  | Roughly sewn together from a variety of ransacked materials, the Wastelander undersuit will just about do the job. This version features a bold rust color.
- **New:** Item Type: Undersuit | Damage Reduction: 10% | Temp. Rating: -30 / 60 °C | Radiation Protection: 15200 REM | Radiation Scrub Rate: 81 REM/s |  | Roughly sewn together from a variety of ransacked materials, the Wastelander undersuit will just about do the job. This version features a bold rust color.

### `defend_UGF_obj_long_02` — 4.3.2-LIVE → 4.4.0-PTU (score 16.86, sim 56%)

- **Old:** Defend the site against ~mission(DefendWaveNumber) waves of hostiles.
- **New:** Defend the site against oncoming attackers

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.3.2-LIVE → 4.4.0-PTU (score 16.8, sim 56%)

- **Old:** Crosshair - October 2955
- **New:** Vox Populi - November 2955

### `civilian_localdelivery_holiday_desc_004` — 4.3.2-LIVE → 4.4.0-PTU (score 15.13, sim 60%)

- **Old:** I know things get busy around the holidays, but I was reaching out to see if you had any extra time to do a delivery run. |  | Got a few presents at <EM4>~mission(Pickup1|Address)</EM4> for close friends that I won't be able to deliver myself.  | You would need to take one to ~mission(GiftRecipient1) at <EM4>~mission(DropOff1)</EM4>, another to ~mi
- **New:** I know things get busy around the holidays, but I was reaching out to see if you had any extra time to do a delivery run. |  | Got a few presents at <EM4>~mission(Location|Address)</EM4> for close friends that I won't be able to deliver myself. ~mission(DescriptionSetup) |  | Much appreciated, | ~mission(GiftSender)

### `civilian_localdelivery_holiday_desc_002` — 4.3.2-LIVE → 4.4.0-PTU (score 12.96, sim 66%)

- **Old:** I'm in desperate need of a little Luminalia magic and I hope you're the one to help. |  | There are three gifts stuck at <EM4>~mission(Pickup1|Address)</EM4> that need to be delivered.  |  | I tried scheduling a pick up but just got notified that they won't be able to make it until after the holidays. Would you be able to take care of the deliverie
- **New:** I'm in desperate need of a little Luminalia magic and I hope you're the one to help. |  | There are some gifts stuck at <EM4>~mission(Location|Address)</EM4> that need to be delivered.  |  | I tried scheduling a pick up but just got notified that they won't be able to make it until after the holidays. Would you be able to take care of the deliverie

### `civilian_localdelivery_holiday_desc_003` — 4.3.2-LIVE → 4.4.0-PTU (score 10.67, sim 71%)

- **Old:** Hope the holiday season is treating you well. |  | Mine's been a bit stressful so far. It turns out that I put the wrong delivery address on a handful of gifts and I'm desperately seeking a way to get them delivered on time.  |  | It would mean so much to me if you could get me out of this jam.  |  | The presents are at <EM4>~mission(Pickup1|Addres
- **New:** Hope the holiday season is treating you well. |  | Mine's been a bit stressful so far. It turns out that I put the wrong delivery address on a handful of gifts and I'm desperately seeking a way to get them delivered on time.  |  | It would mean so much to me if you could get me out of this jam.  |  | The presents are at <EM4>~mission(Location|Addre

### `TheCollector_GenericCollect_Long,P` — 4.3.2-LIVE → 4.4.0-PTU (score 10.48, sim 72%)

- **Old:** Bring ~mission(amount)/~mission(total) of ~mission(item). Bring to ~mission(destination|ListAll).
- **New:** Bring ~mission(amount)/~mission(total) of ~mission(item). Bring to <EM4>any Wikelo Emporium</EM4>.

### `item_DescMTC_Paint_Grey_Black_Yellow_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 9.98, sim 73%)

- **Old:** Equip the Filament livery to make the MTC grey with black and yellow highlights.
- **New:** Equip the Filament livery to make the MTC grey with black and yellow highlights. It's also compatible with other Greycat M-series vehicles.

### `item_DescMTC_Paint_Grey_Lightgrey_Orange_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.75, sim 76%)

- **Old:** The Boreal livery brings a mix of metallic light grey, grey, and orange highlights to the MTC.
- **New:** The Boreal livery brings a mix of metallic light grey, grey, and orange highlights to the MTC. It's also compatible with other Greycat M-series vehicles.

### `item_DescMTC_Paint_Grey_Black_Red_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.74, sim 76%)

- **Old:** Bold red highlights add a bit of color and break up the black base paint of the MTC Baracus livery.
- **New:** Bold red highlights add a bit of color and break up the black base paint of the MTC Baracus livery, which can also be applied to other Greycat M-Series vehicles.

### `item_DescMTC_Paint_Black_Grey_Blue_Solid` — 4.3.2-LIVE → 4.4.0-PTU (score 8.06, sim 78%)

- **Old:** Crisp, metallic blue with grey and black highlights provide the Moonstone livery a spirited look for the MTC.
- **New:** Crisp, metallic blue with grey and black highlights provide the Moonstone livery a spirited look for the MTC, which can also be applied to other Greycat M-Series vehicles.

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.4.0-PTU → 4.5.0-LIVE (score 35.13, sim 10%)

- **Old:** VOX POPULI: The Voice of the People’s Alliance
- **New:** Terra Gazette

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.4.0-PTU → 4.5.0-LIVE (score 33.97, sim 3%)

- **Old:** VOX POPULI | The Voice of the People’s Alliance | November 2955 |  | ALBERTSON FAMILY KILLED IN VANDUUL RAID  | Governing committee offers condolences but no solutions as the death toll continues to rise. |  | The Albertson Family Mining Post had just started its shift, when the Vanduul raiders struck without warning, killing the entire crew within
- **New:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated the first public test of faster-than-light communications to a stunned crowd. Speaking in real time

### `item_Descarma_barrel_stab_s1_firerats01` — 4.4.0-PTU → 4.5.0-LIVE (score 24.55, sim 37%)

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Recoil Stability: +40% | Recoil Kick: +40% | Spread: -10% | Projectile Speed: -12.5% |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. The S
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Spread: -20% | Projectile Speed: -12.5% | Aim Recoil: +40% | Visual Recoil: +40% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve spread for a slower but more precise shot. The Scorched edition features a unique flame patina.

### `item_Descarma_barrel_stab_s1` — 4.4.0-PTU → 4.5.0-LIVE (score 23.76, sim 39%)

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Reduce energy weapon recoil with the Emod Stabilizer1. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 1 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer1 attachment to improve visual stability allowing for a more precise shot.

### `item_Descarma_barrel_stab_s2` — 4.4.0-PTU → 4.5.0-LIVE (score 23.76, sim 39%)

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more precise shot. 
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Visual Recoil: -30% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve visual stability allowing for a more precise shot.

### `item_descarma_barrel_stab_s2_contestedzonereward` — 4.4.0-PTU → 4.5.0-LIVE (score 19.56, sim 49%)

- **Old:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Damage: +12.5% | Recoil Stability: +15% | Recoil Kick: +40% | Spread: +25% | Ammo Cost Per Shot: +100% |  | Reduce energy weapon recoil with the Emod Stabilizer2. ArmaMod designed the attachment to improve both horizontal and vertical recoil to ensure a more p
- **New:** Manufacturer: ArmaMod | Type: Energy Stabilizer | Attachment Point: Barrel | Size: 2 |  | Heat: -80% | Aim Recoil: +40% | Visual Recoil: -15% | Damage: +12.5% | Ammo Consumption: +100% |  | ArmaMod designed the Emod Stabilizer2 attachment to improve heat distribution and visual stability allowing for a more precise shot. This "Tweaker" version has 

### `ui_pause_PopupQuitGame_Title` — 4.4.0-PTU → 4.5.0-LIVE (score 19.2, sim 50%)

- **Old:** Quit Game
- **New:** Quit to desktop

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.4.0-PTU → 4.5.0-LIVE (score 18.84, sim 51%)

- **Old:** Vox Populi - November 2955
- **New:** Terra Gazette - December 2955

### `Journal_General_FrontendNewspaperHeadlines_Content` — 4.5.0-LIVE → 4.6.0-LIVE (score 50.36, sim 2%)
- Edge lost: execute

- **Old:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as they demonstrated the first public test of faster-than-light communications to a stunned crowd. Speaking in real time
- **New:** New United | Release Edition 4.6.0 |  | FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT | Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. |  | Following weeks of reports of a new unknown illness afflicting the residents of Levski, the source has been confirmed as a new species of mold whose airborne spores cause potentially fatal fung

### `Journal_General_FrontendNewspaperHeadlines_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 25.29, sim 35%)

- **Old:** Terra Gazette
- **New:** New United

### `Journal_General_FrontendNewspaperHeadlines_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 24.28, sim 37%)

- **Old:** Terra Gazette - December 2955
- **New:** New United - Release Ed. 4.6.0

### `Journal_General_Mining_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 17.95, sim 53%)

- **Old:** The Fundamentals of Mining
- **New:** Mining Fundamentals #1: Basic Overview

### `Journal_General_Harvestables_Content` — 4.5.0-LIVE → 4.6.0-LIVE (score 16.18, sim 58%)

- **Old:** It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. This guide will help you identify what's useful, what's edible, and what's deadly.   |  | *A FORAGER'S GUIDE TO STANTON* |  | DEGNOUS ROOT  | A type of macroalgae that has acclimated to much of the Stanton system, the degnous root is origin
- **New:** This guide will help you identify what's useful, what's edible, and what's deadly.   |  | *STANTON SYSTEM* | It may seem completely corporate, but the Stanton system is rich with resources for the enterprising forager. |  | DEGNOUS ROOT  | A type of macroalgae that has acclimated to much of the Stanton system, the degnous root is originally from Te

### `Journal_General_Harvestables_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 9.01, sim 75%)

- **Old:** Stanton Wildlife Federation
- **New:** Empire Wildlife Federation

### `Journal_General_Wildlife_From` — 4.5.0-LIVE → 4.6.0-LIVE (score 9.01, sim 75%)

- **Old:** Stanton Wildlife Federation
- **New:** Empire Wildlife Federation

### `Journal_General_Harvestables_Title` — 4.5.0-LIVE → 4.6.0-LIVE (score 8.98, sim 76%)

- **Old:** A Forager's Guide to Stanton
- **New:** A Forager's Guide

### `Shubin_Industrial_ShipMining_S_Org_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 42.15, sim 30%)
- Euphemism: lost:'kill '

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. This purchase order is more complex than typical, requiring multiple mining methods, but since you've proven your skill thus far, we think you and your team ar
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. |  | We are in need of a vast amount of ore, ranging from common to rare. A variety of different 

### `Shubin_Industrial_ShipMining_VH_Org_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 42.15, sim 30%)
- Euphemism: lost:'kill '

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. This purchase order is more complex than typical, requiring multiple mining methods, but since you've proven your skill thus far, we think you and your team ar
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar values the continuous and consistent deliveries of ore that you have provided and now wishes for you to push your performance further. |  | We are in need of a vast amount of ore, ranging from common to rare. A variety of different 

### `Shubin_Industrial_HandMining_Intro_Local_Desc_001` — 4.6.0-LIVE → 4.6.0-PTU (score 35.53, sim 9%)

- **Old:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of materials from independent miners operating in the area. While selling at a trade hub may net you a more competitive price than fulfilling our order, many miners 
- **New:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Hand Mining |  | TERMS*: |  | Shubin Interstellar are looking to expand our existing list of contractors across <EM4>~mission(System)</EM4> to include entry-level mining contractors. |  | If you are self-motivated, hardworking, and resilient, we would be interested in working with y

### `Shubin_Industrial_ShipMining_VH_Org_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.89, sim 31%)

- **Old:** Special Purchase Order: Mined Materials
- **New:** Ship Mining Request: Special Assignment

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

### `Shubin_Industrial_ShipMining_Pyro_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

### `Shubin_Industrial_ShipMining_Stanton_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.26, sim 32%)

- **Old:** Small Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Small Scale

### `Shubin_Industrial_HandMining_Nyx_E_Interstellar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

### `Shubin_Industrial_HandMining_Pyro_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

### `Shubin_Industrial_HandMining_Stanton_E_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

### `Shubin_Industrial_HandMining_Stanton_E_PlanetarySystem_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 26.23, sim 32%)

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Small Scale

### `Shubin_Industrial_HandMining_Intro_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.54, sim 34%)

- **Old:** Small Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Shubin Interstellar

### `Shubin_Industrial_ShipMining_Nyx_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

### `Shubin_Industrial_ShipMining_Pyro_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

### `Shubin_Industrial_ShipMining_Stanton_VE_Local_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.49, sim 34%)

- **Old:** XS Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Very Small Scale

### `Shubin_Industrial_ShipMining_Nyx_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

### `Shubin_Industrial_ShipMining_Pyro_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

### `Shubin_Industrial_ShipMining_Stanton_S_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.29, sim 35%)

- **Old:** Mjr. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Extreme Scale

### `Shubin_Industrial_HandMining_Pyro_M_DiscoverPlanetary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.15, sim 35%)

- **Old:** Med. Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Medium Scale

### `Shubin_Industrial_HandMining_Stanton_M_DiscoverPlanetary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.15, sim 35%)

- **Old:** Med. Purchase Order: Hand Mined Materials
- **New:** Hand Mining Request: Medium Scale

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

### `Shubin_Industrial_ShipMining_Pyro_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

### `Shubin_Industrial_ShipMining_Stanton_M_Solar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 25.08, sim 35%)

- **Old:** Med. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Medium Scale

### `Shubin_Industrial_ShipMining_Nyx_H_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

### `Shubin_Industrial_ShipMining_Pyro_H_PrimarySecondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

### `Shubin_Industrial_ShipMining_Pyro_H_Secondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

### `Shubin_Industrial_ShipMining_Stanton_H_PrimarySecondary_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale

### `Shubin_Industrial_ShipMining_Stanton_H_Secondary_Interstellar_Title_001` — 4.6.0-LIVE → 4.6.0-PTU (score 24.87, sim 36%)

- **Old:** Lrg. Purchase Order: Ship Mined Ore
- **New:** Ship Mining Request: Large Scale
