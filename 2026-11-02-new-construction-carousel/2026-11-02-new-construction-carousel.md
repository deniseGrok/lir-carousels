# DRAFT — AWAITING DENISE APPROVAL
## Daily New Construction Deal Carousel — Monday, Nov 2, 2026 (Charlotte metro)
Nothing has been posted, scheduled, sent or added to Buffer. After approval: Buffer 9:30 AM ET — Instagram 4:5, Facebook Page 1:1, TikTok 9:16.
Design: New Construction — Bright Contemporary (Denise, Oct 31, 2026). Renderer: TEMPLATES/bright_contemporary.py (docs TEMPLATES/BRIGHT_CONTEMPORARY.md), matched to TEMPLATES/new-construction-bright-contemporary/.
Offers verified on the builder's own website Nov 2, 2026, about 4:09–4:20 AM ET. Builder photos only, credited on-slide "Photo: Eastwood Homes".
No PDF (Denise, Nov 1, 2026). No YouTube Short.

Three native slide sets (each laid out for its frame, not cropped or padded):
- 4:5 1080x1350 (Instagram): slide-01.png … slide-10.png, slides.zip
- 1:1 1080x1080 (Facebook Page + personal profile): slides-1x1/, slides-1x1.zip
- 9:16 1080x1920 (TikTok; text clear of ~150 px top / 350 px bottom / 140 px right): slides-9x16/, slides-9x16.zip
Captions: below and in captions.md. Build: build/build_slides.py. Photo sources: build/CREDITS.txt.

Count: 4 verified builder offers in 4 new communities (1 builder: Eastwood Homes), all new to the tracker, all NC (Mecklenburg, Union, Iredell counties). Fewer than 8 verified local offers were available today, so the set is filled with one comparison slide (6) and three tip slides (7, 8, 9) rather than unverified or out-of-area deals.

## Verified offer (builder website, 2026-11-02)
Eastwood Homes — https://www.eastwoodhomes.com/special-offers (Charlotte NC): "Move-in Package with Refrigerator, Blinds, and Washer and Dryer Package on Select Homes!" — "For a limited time, receive a move-in package on your new home, which includes a stainless-steel side-by-side refrigerator, a washer and dryer, and window blinds!" No end date posted. Each community page below shows the "Move-in Package!" banner and lists the same promotion.
1. Enclave at Riverdale, Huntersville, NC — page: "quaint, wooded community", "minutes from Birkdale Village", "ranch, two-, and three-story homes". https://www.eastwoodhomes.com/charlotte/huntersville/enclave-at-riverdale
2. Ashton Park, Monroe, NC — page: "72 thoughtfully designed homes and wooded homesites", "walking trails", "dog park", "less than one mile from the 74 Bypass". https://www.eastwoodhomes.com/charlotte/monroe/ashton-park
3. Norman Creek, Troutman, NC — page: "easy access to Lake Norman and I-77"; amenities Pool, Cabana ("May still be under construction"). https://www.eastwoodhomes.com/charlotte/troutman/norman-creek
4. Norman Creek Townhomes, Troutman, NC — page: same description; amenities Pool, Cabana. https://www.eastwoodhomes.com/charlotte/troutman/norman-creek-townhomes

Checked and cut / held: Eastwood's other Charlotte move-in-package communities (Caldwell Forest, The Fairways / The Greens at Springlake, Harrisburg Village Townhomes, Robinson Oaks, Waterford Commons, Carrington — already featured or Rock Hill, outside the SC list), Founders Landing (55+; left off to keep copy free of people-based language), The Meadows / The Enclave at Laurelbrook (Laurelbrook already featured), free-blinds communities (Chasewood, Rone Creek, Blythe Mill — already featured). Closing-cost amounts seen only in embedded page data (not in the visible offer list for these communities) were not used. M/I Homes "Home Sweet Savings": every listed Charlotte community already featured (Laurelbrook skipped). Lennar Charlotte page: no specific offer posted server-side. Other builders (D.R. Horton, Pulte/Centex/Del Webb, Meritage, Taylor Morrison, Toll, Mattamy, Dream Finders, Century, KB, Stanley Martin, True Homes, Smith Douglas, Ryan, Brookline, Profile, Tri Pointe, Hopper) could not be verified before the 5 AM deadline (client-rendered or 404 offer pages), so nothing from them is included.

## Slides
1. Cover "4 communities. Move-in package." (Photo: Eastwood Homes — Ashton Park community hero exterior)
2. Enclave at Riverdale: move-in package on select homes (Photo: Eastwood Homes — Enclave at Riverdale page hero)
3. Ashton Park: fridge, washer, dryer and blinds (Photo: Eastwood Homes — Ashton Park aerial)
4. Norman Creek: appliances + blinds on select homes (Photo: Eastwood Homes — Norman Creek page hero)
5. Norman Creek Townhomes: townhomes with a move-in package (Photo: Eastwood Homes — Norman Creek Townhomes page hero)
6. COMPARE • Items vs. dollars (Photo: Eastwood Homes — Norman Creek pool and cabana)
7. TIP • Ask which homes qualify (Photo: Eastwood Homes — kitchen, Ashton Park page gallery)
8. TIP • Get the details in writing (Photo: Eastwood Homes — living room, Enclave at Riverdale page gallery)
9. TIP • Check the dates (Photo: Eastwood Homes — exterior, Norman Creek page gallery)
10. CTA "DM or comment DEALS and we'll get started." + contact card (Denise Wilson | Broker/REALTOR® / firm / site / phone / blank / Equal Housing Opportunity) (Photo: Eastwood Homes — kitchen, Enclave at Riverdale page gallery)
Every offer slide: "Builder's offer, verified on the builder's site Nov 2, 2026. Terms and eligibility set by the builder; subject to change." Slides 6–9: "Comparison/Tip based on Eastwood Homes' posted offer, read Nov 2, 2026. Terms and eligibility set by the builder; subject to change."

## Photo review
All 10 checked at full size in all three sizes: bright daylight exteriors with blue skies, one aerial, one pool amenity, bright interiors. All builder photos are 2000–2908 px wide and are downscaled in every size (no upscaling needed; ESRGAN not used). House numbers retouched out on slides 01 and 09 (column digits blended from the clean column either side; homes otherwise unaltered). Note: gallery photos on slides 7–10 come from each community's page gallery; Eastwood galleries can include plan photos shot at other locations.
Photo check: all 10 sources checked with photo_registry.py check — no source-id or SHA match; only loose hash hits (12–18) to unrelated photos. Registered in TEMPLATES/photo-registry.csv.

## Compliance check
compliance_check.py: slide HTML (all three sizes) PASS — no banned words, contact block complete on slide 10 in 4:5, 1:1 and 9:16. Caption FAIL lines are the approved Oct 31 overrides only: "Equal Housing Opportunity" (EHO is on slide 10), "ends with a question" (format ends with signature + hashtags), and "Swipe" on the IG and FB Page captions (TikTok uses "Save this"; no "swipe" on any slide).
Checklist: R1/R2/R4/R5 on slide 10 (title Broker/REALTOR®); firm name + phone in every caption signature. T1 every fact read on the builder's site Nov 2, 2026; T2 no guarantees; T3 no urgency (only the builder's own "for a limited time" wording, quoted as the builder's); T4 every slide carries the builder + date line; T5 house numbers retouched on 01 and 09, others below the gradient or not legible; T7 every incentive labeled as the builder's, with date and "terms and eligibility set by the builder; subject to change"; T9 no rates, payments, prices or down payments stated. F1–F5: homes, amenities and terms only; no people, schools, safety or "perfect for" language; no addresses or home prices.

---

## Instagram
🏡 Four Charlotte-area new build communities are posting a move-in package today.

On Nov 2, 2026, I checked each offer on Eastwood Homes' own website.

📍 Enclave at Riverdale in Huntersville: the builder's move-in package on select homes
🌳 Ashton Park in Monroe: the builder's refrigerator, washer and dryer, and blinds offer
🏊 Norman Creek in Troutman: the builder's move-in package on select homes
🏘️ Norman Creek Townhomes in Troutman: the builder's offer on select townhomes
📄 Which homes qualify, and what exactly comes with the package?

These details shape what you spend after the keys are in your hand.

An appliance package sounds great. The written terms decide what it's worth.

👉 Swipe through and save this post before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #NewHomesCharlotte #HuntersvilleNC #TroutmanNC #CharlotteRealEstate

## Facebook (page)
🏡 Four new build communities near Charlotte are posting a move-in package today.

On Nov 2, 2026, I checked each offer on Eastwood Homes' own website.

📍 Enclave at Riverdale (Huntersville): the builder's move-in package on select homes
🌳 Ashton Park (Monroe): the builder's refrigerator, washer and dryer, and blinds offer
🏊 Norman Creek and Norman Creek Townhomes (Troutman): the builder's offer on select homes
📄 Which homes qualify, and what exactly comes with the package?

These details shape what you spend after closing.

An appliance package sounds great. The written terms decide what it's worth.

👉 Swipe through and save this post before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #CharlotteRealEstate #NewHomes

## TikTok
🏡 Four Charlotte-area new builds are posting a move-in package today.

📍 Huntersville, Monroe and two Troutman communities, one builder
🧺 The builder's offer: refrigerator, washer and dryer, and blinds on select homes
📄 Each offer checked on Eastwood Homes' site Nov 2, 2026

An appliance package sounds great. The written terms decide what it's worth.

💾 Save this before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNC #NewConstruction #CharlotteRealEstate #NewHomes

## Facebook (personal profile)
🏡 Friends, four new build communities near Charlotte are posting a move-in package today.

On Nov 2, 2026, I checked each offer on Eastwood Homes' own website, and these are the questions I walk my buyers through before they sign.

📍 Enclave at Riverdale in Huntersville: the builder's move-in package on select homes
🌳 Ashton Park in Monroe: the builder's refrigerator, washer and dryer, and blinds offer
🏊 Norman Creek in Troutman: the builder's move-in package on select homes
🏘️ Norman Creek Townhomes in Troutman: the builder's offer on select townhomes
📄 Which homes qualify, and what exactly comes with the package?

These details shape what you spend after closing.

An appliance package sounds great. The written terms decide what it's worth.

👉 Share this with anyone who's touring new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #CharlotteRealEstate
