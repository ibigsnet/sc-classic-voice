# All-keys wording map (older/harder wins)

**Target (current soft stock):** `4.10.0-PTU`

- Corpus versions: 4.3.2-LIVE, 4.4.0-PTU, 4.5.0-LIVE, 4.6.0-LIVE, 4.6.0-PTU, 4.7.0-LIVE, 4.7.0-LIVE-HOTFIX, 4.7.0-PTU, 4.7.1-LIVE, 4.8.0-PTU, 4.9.0-LIVE, 4.10.0-PTU
- Pairwise text changes (any wording change): **1727**
- Steps scored as **softened** (hardness dropped): **14**
- Steps scored as **hardened**: **19**
- Pack keys (harder than target, applied to current): **1263**

## Policy

1. For every key on the target build, look at all older stocks that have it.
2. If wording never changed → skip.
3. Score each historical string for hardness (edge words, living hell, etc.; soft phrases reduce score).
4. Pick **highest hardness**; ties → **oldest** version.
5. If that beats current target → ship it in `01-classic-all.ini`.

## Top pack restores (by hardness gain)

### `headhunters_bombingrun_multi_E_CFP_desc_001`  (+85.0 hard)  ← `4.3.2-LIVE`
- Edge: ['living_hell', 'bomb_the_living', 'hell', 'shit'] → target had ['shit']
- **Chosen:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure 
- **Target (soft stock):** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure 

### `Journal_General_FrontendNewspaperHeadlines_Content`  (+36.0 hard)  ← `4.5.0-LIVE`
- Edge: ['kill', 'execute'] → target had []
- **Chosen:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead research
- **Target (soft stock):** VOX POPULI | Release Edition 4.7.0 |  | UEE INTERSYSTEM COMM NETWORK HACKED  | Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance.   |  | 

### `headhunters_Nyx_bombingrun_M_desc_001`  (+28.0 hard)  ← `4.7.0-LIVE`
- Edge: ['bomb_the_life'] → target had []
- **Chosen:** Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>. |  | Now, I'm a fair man. I sent these nullbrains a message saying they 
- **Target (soft stock):** Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>. |  | Now, I'm a fair man. I sent these nullbrains a message saying they 

### `headhunters_bombingrun_S_desc_001`  (+20.0 hard)  ← `4.7.0-LIVE`
- Edge: ['bombing_run'] → target had []
- **Chosen:** We've heard news that a new gang are planning a bombing run on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the 
- **Target (soft stock):** We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taki

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials fr

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate you

### `Shubin_Industrial_ShipMining_Pyro_E_Local_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials fr

### `Shubin_Industrial_ShipMining_Pyro_M_Solar_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate you

### `Shubin_Industrial_ShipMining_Pyro_VE_Local_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials fr

### `Shubin_Industrial_ShipMining_Stanton_E_Local_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials fr

### `Shubin_Industrial_ShipMining_Stanton_M_Solar_Desc_001`  (+10.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)<
- **Target (soft stock):** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate you

### `Stanton3a_Desc,P`  (+1.0 hard)  ← `4.6.0-LIVE`
- Edge: [] → target had []
- **Chosen:** This icy moon features active cryogeysers and cryovolcanoes. |  | Potential Ship Mineables: | Beryl | Hephasestanite | Agricium | Laranite | Borase | Gold | Taranite | Bexalite | Quantanium | Quartz | Corundum | Tungsten |  | Potent
- **Target (soft stock):** This icy moon features active cryogeysers and cryovolcanoes. |  | Potential Ship Mineables: | Iron | Copper | Laranite | Quantainium |  | Potential Hand Mineables: | Aphorite | Dolivine | Janalite

### `item_Desc_ops_pants_02_01_01`  (+1.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Carrying Capacity: 0.5K µSCU |  | Cut to a narrow fit, OpalSky's Mivaldi pants feature bold asymmetrical design with smart yet casual dual material styling, making it the perfect addition to any wardrobe.
- **Target (soft stock):** Carrying Capacity: 0.5K µSCU |  | Cut to a narrow fit, OpalSky's Mivaldi pants feature bold asymmetrical design with smart yet casual dual material styling, making it the perfect addition to any wardrobe.

### `vehicle_DescAEGS_Retaliator`  (+1.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Manufacturer: Aegis Dynamics | Focus: Heavy Gunship |  | This civilian refit of the Retaliator updates the military ship's chassis with unladen space able to be fitted with various modules to suit your need
- **Target (soft stock):** Manufacturer: Aegis Dynamics | Focus: Modular |  | This civilian refit of the Retaliator updates the military ship's chassis with unladen space able to be fitted with various modules to suit your needs.

### `BHG_Certification_EscapedConvict_Desc,P`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** -------------------------------------------------------- | ----------------- BOUNTY CONTRACT ----------------- | -------------------------------------------------------- |  | BOUNTY HUNTERS GUILD | PROCESSING &
- **Target (soft stock):** -------------------------------------------------------- | ----------------- BOUNTY CONTRACT ----------------- | -------------------------------------------------------- |  | BOUNTY HUNTERS GUILD | PROCESSING &

### `BHG_Certification_Medium_Desc,P`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** -------------------------------------------------------- | ----------------- BOUNTY CONTRACT ----------------- | -------------------------------------------------------- |  | BOUNTY HUNTERS GUILD | PROCESSING &
- **Target (soft stock):** -------------------------------------------------------- | ----------------- BOUNTY CONTRACT ----------------- | -------------------------------------------------------- |  | BOUNTY HUNTERS GUILD | PROCESSING &

### `Badge_CleanAir_Personal_T4_Desc`  (+0.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** You have been awarded: Perseus Alliance Aid Camo Livery
- **Target (soft stock):** You've been awarded: Perseus Alliance Aid Camo, ParaMed AA Support Device, and Item Fabricator (Upon Release) | 

### `Battaglia_RPT_RecoverItem_VH_01_desc`  (+0.0 hard)  ← `4.9.0-LIVE`
- Edge: ['kill'] → target had ['kill']
- **Chosen:** *********** People's Alliance *********** | ******/ 'Stronger When United' /****** |  | RE: Blackbox Retrieval Very Dangerous |  | WORK BRIEF:  | There's been another attack out at ~mission(Location). Whoever did
- **Target (soft stock):** *********** People's Alliance *********** | ******/ 'Stronger When United' /****** |  | RE: Blackbox Retrieval Very Dangerous |  | WORK BRIEF:  | There's been another attack out at ~mission(Location). Whoever did

### `BitZeros_blackbox_E_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** So we were expecting a pretty important package earlier today but turns out the pilot got ghosted and they ripped the tracking chip from it and got away. Pretty clever right? Not really, because they 
- **Target (soft stock):** So we were expecting a pretty important package earlier today but turns out the pilot got ghosted and they ripped the tracking chip from it and got away. Pretty clever right? Not really, because they 

### `BitZeros_blackbox_H_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** Don’t know if you’ve heard, but there’s a bunch of ships over at <EM4>~mission(Location|Address)</EM4> surrounding a burnt-out ship. You curious why? I know we are. | Think you can get in that wreck, gr
- **Target (soft stock):** Don’t know if you’ve heard, but there’s a bunch of ships over at <EM4>~mission(Location|Address)</EM4> surrounding a burnt-out ship. You curious why? I know we are. | Think you can get in that wreck, gr

### `BitZeros_blackbox_Intro_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** Who we are and what we do is not important. All you gotta know is that we need things to get done and we pay people to do it. |  | If everything goes well, we don’t ever have to meet. Doesn’t that sound g
- **Target (soft stock):** Who we are and what we do is not important. All you gotta know is that we need things to get done and we pay people to do it. |  | If everything goes well, we don’t ever have to meet. Doesn’t that sound g

### `BitZeros_blackbox_M_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** We were a little too smart with this one and it’s kinda backfired. Sometimes you gotta dream big, you know? Anyway. we were looking to move some encrypted data to one of our data havens and decided to
- **Target (soft stock):** We were a little too smart with this one and it’s kinda backfired. Sometimes you gotta dream big, you know? Anyway. we were looking to move some encrypted data to one of our data havens and decided to

### `BitZeros_blackbox_S_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** Got a big job for a big player. We’re in the process of making someone disappear, like completely vanish, and a part of that is recovering the blackbox from the “accident” that they had recently over 
- **Target (soft stock):** Got a big job for a big player. We’re in the process of making someone disappear, like completely vanish, and a part of that is recovering the blackbox from the “accident” that they had recently over 

### `BitZeros_blackbox_VE_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** Someone of interest to us recently kicked the bucket (not our fault) over at <EM4>~mission(Location|Address)</EM4> and we’re pretty curious what happened. We need you to grab the blackbox from the shi
- **Target (soft stock):** Someone of interest to us recently kicked the bucket (not our fault) over at <EM4>~mission(Location|Address)</EM4> and we’re pretty curious what happened. We need you to grab the blackbox from the shi

### `BitZeros_blackbox_VH_Desc_001`  (+0.0 hard)  ← `4.4.0-PTU`
- Edge: [] → target had []
- **Chosen:** I’m not gonna give you the whole backstory of what this person has done to us, but all you need to know is that some scumbag is trying to get a payout for a ship crash and the insurance company wants 
- **Target (soft stock):** I’m not gonna give you the whole backstory of what this person has done to us, but all you need to know is that some scumbag is trying to get a payout for a ship crash and the insurance company wants 

### `CFPvsHH_Reward_Week1_HH`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** You've Earned: Headhunter Veritas Outift | Access It at Your Primary Residence's Inventory
- **Target (soft stock):** You've Earned: Headhunter Veritas Outfit | Access It at Your Primary Residence's Inventory

### `CleanAir_Defense-Milestone1_desc`  (+0.0 hard)  ← `4.6.0-LIVE`
- Edge: [] → target had []
- **Chosen:** Since you've been doing so much work helping out the Defense Division I wanted to come to you with this contract direct. It's a bit of a delicate one. Two VIPs fell ill and the worry was that if word 
- **Target (soft stock):** Since you've been doing so much work helping out the Defense Division I wanted to come to you with this contract direct. It's a bit of a delicate one. Two VIPs fell ill and the worry was that if word 

### `CleanAir_RecoverCargo_Easy_desc`  (+0.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-11 |  | FOR IMMEDIATE PROCESSING |  | With all these Alliance Aid ships hauling valuable cargo around, outlaws i
- **Target (soft stock):** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-11 |  | FOR IMMEDIATE PROCESSING |  | With all these Alliance Aid ships hauling valuable cargo around, outlaws i

### `CleanAir_RecoverCargo_Hard_desc`  (+0.0 hard)  ← `4.6.0-PTU`
- Edge: [] → target had []
- **Chosen:** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-13 |  | FOR IMMEDIATE PROCESSING |  | Alliance Aid just comm'd in a panic. A vital shipment that they were count
- **Target (soft stock):** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-13 |  | FOR IMMEDIATE PROCESSING |  | Alliance Aid just comm'd in a panic. A vital shipment that they were count

### `CleanAir_RecoverCargo_Medium_desc`  (+0.0 hard)  ← `4.6.0-PTU`
- Edge: ['kill'] → target had ['kill']
- **Chosen:** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-12 |  | FOR IMMEDIATE PROCESSING |  | Nothing like an emergency to bring out the worst in people. This Molina mo
- **Target (soft stock):** ECKHART SECURITY, LLC. | CONTRACTS & DISPATCH |  | CONTRACT TYPE: Cargo Retrieval  | APPROVAL CODE = JJ-12 |  | FOR IMMEDIATE PROCESSING |  | Nothing like an emergency to bring out the worst in people. This Molina mo

### `Covalex_HaulCargo_AToB_Intro_desc`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Earning such accolades as 'Imperial Finances' Top 10 Shipping Companies' and 'Delivery Digest's 2945's Most Trusted Transport,' Covalex is busier than ever. And that means more cargo going to more pla
- **Target (soft stock):** Earning such accolades as 'Imperial Finances' Top 10 Shipping Companies' and 'Delivery Digest's 2945's Most Trusted Transport,' Covalex is busier than ever. And that means more cargo going to more pla

### `Covalex_HaulCargo_AToB_Rehire_desc`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hey, |  | Have a bit of good news for you. Covalex recently finished an evaluation of our contractor pool, and decided to reconsider your status as a cargo hauler. To requalify, all you need is to success
- **Target (soft stock):** Hey, |  | Have a bit of good news for you. Covalex recently finished an evaluation of our contractor pool, and decided to reconsider your status as a cargo hauler. To requalify, all you need is to success

### `Covalex_HaulCargo_AToB_Scrap`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hello, |  | There’s some junk waiting at a freight elevator in <EM4>~mission(Location|Address)</EM4> that needs to go to a freight elevator at <EM4>~mission(Destination|Address)</EM4> for processing. I've
- **Target (soft stock):** Hello, |  | There’s some junk waiting at a freight elevator in <EM4>~mission(Location|Address)</EM4> that needs to go to a freight elevator at <EM4>~mission(Destination|Address)</EM4> for processing. I've

### `Covalex_HaulCargo_AToB_Stanton_Interstellar`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hey, |  | Any interest in doing the Stanton leg of an interstellar run?  |  | There’s a haul of <EM4>~mission(Item)</EM4> waiting in containers <EM4>~mission(MissionMaxSCUSize)</EM4> or smaller to be picked u
- **Target (soft stock):** Hey, |  | Any interest in doing the Stanton leg of an interstellar run?  |  | There’s a haul of <EM4>~mission(Item)</EM4> waiting in containers <EM4>~mission(MissionMaxSCUSize)</EM4> or smaller to be picked u

### `Covalex_HaulCargo_AToB_desc_01`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hello, |  | Need a contractor for a simple cargo haul going from a freight elevator at <EM4>~mission(Location|Address)</EM4> to a freight elevator at <EM4>~mission(Destination|Address)</EM4>. At most the 
- **Target (soft stock):** Hello, |  | Need a contractor for a simple cargo haul going from a freight elevator at <EM4>~mission(Location|Address)</EM4> to a freight elevator at <EM4>~mission(Destination|Address)</EM4>. At most the 

### `Covalex_HaulCargo_AToB_desc_02`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hi, |  | A freight elevator at <EM4>~mission(Location|Address)</EM4> has some cargo that needs to be delivered to a freight elevator at <EM4>~mission(Destination|Address)</EM4>. Another hauler backed out 
- **Target (soft stock):** Hi, |  | A freight elevator at <EM4>~mission(Location|Address)</EM4> has some cargo that needs to be delivered to a freight elevator at <EM4>~mission(Destination|Address)</EM4>. Another hauler backed out 

### `Covalex_HaulCargo_AToB_desc_03`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hi, |  | A new haul just popped up. Details are below, if you’re interested. |  | 1. Pick up cargo from a freight elevator at <EM4>~mission(Location|Address)</EM4>. Max size will be <EM4>~mission(MissionMaxSC
- **Target (soft stock):** Hi, |  | A new haul just popped up. Details are below, if you’re interested. |  | 1. Pick up cargo from a freight elevator at <EM4>~mission(Location|Address)</EM4>. Max size will be <EM4>~mission(MissionMaxSC

### `Covalex_HaulCargo_AToB_title`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** ~mission(ReputationRank) Rank - Direct ~mission(CargoRouteToken) ~mission(CargoGradeToken) Cargo Haul
- **Target (soft stock):** ~mission(ReputationRank) Rank - Direct ~mission(CargoGradeToken) Cargo Haul

### `Covalex_HaulCargo_AtoB_desc_ProcessedFood_Stanton2`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hi,  |  | Looks like Orison needs another resupply of processed food and pressurized ice. They have this stuff on a standard delivery schedule but they just requested a shipment as soon as possible.   |  | Ar
- **Target (soft stock):** Hi,  |  | Looks like Orison needs another resupply of processed food and pressurized ice. They have this stuff on a standard delivery schedule but they just requested a shipment as soon as possible.   |  | Ar

### `Covalex_HaulCargo_AtoB_desc_RawOre_Stanton1`  (+0.0 hard)  ← `4.3.2-LIVE`
- Edge: [] → target had []
- **Chosen:** Hey, |  | A Hurston logistics manager just requested priority pick up from their facility. Sounds like they struck a new vein of ore and need to make room for what they're extracting. |  | The raw ore needs t
- **Target (soft stock):** Hey, |  | A Hurston logistics manager just requested priority pick up from their facility. Sounds like they struck a new vein of ore and need to make room for what they're extracting. |  | The raw ore needs t

## Top soften steps (history receipts)

### `headhunters_bombingrun_multi_E_CFP_desc_001`  4.7.1-LIVE → 4.8.0-PTU  (hard 92.0 → 7.0)
- **From:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure they could use a rem
- **To:** Every day it seems like Citizens for Prosperity is out here trying to snatch up more people for their shitty little cause and make life more difficult for hardworkin' folks like ourselves.  |  | I figure they could use a rem

### `headhunters_Nyx_bombingrun_M_desc_001`  4.7.1-LIVE → 4.8.0-PTU  (hard 29.0 → 1.0)
- **From:** Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>. |  | Now, I'm a fair man. I sent these nullbrains a message saying they either vacate the fa
- **To:** Seems we got a bit of competition out here in Nyx. Scouts have spotted a gang holding up at  <EM4>~mission(Location|Address)</EM4>. |  | Now, I'm a fair man. I sent these nullbrains a message saying they either vacate the fa

### `headhunters_bombingrun_S_desc_001`  4.7.1-LIVE → 4.8.0-PTU  (hard 11.0 → -9.0)
- **From:** We've heard news that a new gang are planning a bombing run on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking. |  | But little 
- **To:** We've heard news that a new gang are planning an attack on a place over at <EM4>~mission(Location|Address)</EM4>. They figure if they can take out the fuel supplies there then it's theirs for the taking. |  | But little do t

### `Journal_General_FrontendNewspaperHeadlines_Content`  4.5.0-LIVE → 4.6.0-LIVE  (hard 37.0 → 19.0)
- **From:** Terra Gazette | December 2955 |  | FTL COMMS BREAKTHROUGH | Scientists reveal cutting-edge discovery allowing for real-time inter-system comms. |  | “The universe has just grown a bit smaller,” said lead researcher Dr. Allo Betel as
- **To:** New United | Release Edition 4.6.0 |  | FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT | Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. |  | Following weeks of reports of a new unknown illness afflicting the resident

### `Journal_General_FrontendNewspaperHeadlines_Content`  4.6.0-PTU → 4.7.0-LIVE  (hard 19.0 → 1.0)
- **From:** New United | Release Edition 4.6.0 |  | FAULTY FILTER TO BLAME FOR MYSTERIOUS AILMENT | Deadly ‘Molina Mold’ contaminates Levski station in Nyx System. |  | Following weeks of reports of a new unknown illness afflicting the resident
- **To:** VOX POPULI | Release Edition 4.7.0 |  | UEE INTERSYSTEM COMM NETWORK HACKED  | Another rushed initiative by the crumbling empire once again proves an unacceptable lack of forethought and basic governance.   |  | Seemingly having lea

### `Shubin_Industrial_ShipMining_Nyx_E_Local_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials from independent miner

### `Shubin_Industrial_ShipMining_Nyx_M_Solar_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate your help in this matte

### `Shubin_Industrial_ShipMining_Pyro_E_Local_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials from independent miner

### `Shubin_Industrial_ShipMining_Pyro_M_Solar_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate your help in this matte

### `Shubin_Industrial_ShipMining_Pyro_VE_Local_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials from independent miner

### `Shubin_Industrial_ShipMining_Stanton_E_Local_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Due to changes in our sourcing pipeline, Shubin Interstellar is currently looking to purchase a variety of refined materials from independent miner

### `Shubin_Industrial_ShipMining_Stanton_M_Solar_Desc_001`  4.6.0-PTU → 4.7.0-LIVE  (hard 1.0 → -9.0)
- **From:** POSTING: Industrial | LOCATION: ~mission(System) | REQ EXPERIENCE: Ship Mining |  | TERMS*:  |  | Shubin Interstellar is in need of a variety of ore, mineable from numerous locations across <EM4>~mission(System)</EM4>. |  | ~mission(Hin
- **To:** POSTING: Purchase Order | LOCATION: <EM4>~mission(System) </EM4> |  | TERMS*:  | Shubin Interstellar is currently looking to fulfil another purchase order for a variety of refined materials. We appreciate your help in this matte

### `vehicle_DescAEGS_Retaliator`  4.7.1-LIVE → 4.8.0-PTU  (hard 1.0 → 0.0)
- **From:** Manufacturer: Aegis Dynamics | Focus: Heavy Gunship |  | This civilian refit of the Retaliator updates the military ship's chassis with unladen space able to be fitted with various modules to suit your needs.
- **To:** Manufacturer: Aegis Dynamics | Focus: Modular |  | This civilian refit of the Retaliator updates the military ship's chassis with unladen space able to be fitted with various modules to suit your needs.

### `item_Desc_ops_pants_02_01_01`  4.9.0-LIVE → 4.10.0-PTU  (hard 1.0 → 0.0)
- **From:** Carrying Capacity: 0.5K µSCU |  | Cut to a narrow fit, OpalSky's Mivaldi pants feature bold asymmetrical design with smart yet casual dual material styling, making it the perfect addition to any wardrobe. |  | Women's sizes curr
- **To:** Carrying Capacity: 0.5K µSCU |  | Cut to a narrow fit, OpalSky's Mivaldi pants feature bold asymmetrical design with smart yet casual dual material styling, making it the perfect addition to any wardrobe.
