# DRAFT — AWAITING DENISE APPROVAL
## Daily New Construction Deal Carousel — Tuesday, Nov 3, 2026 (Charlotte metro)
Nothing has been posted, scheduled, sent or added to Buffer. After approval: Buffer 9:30 AM ET — Instagram 4:5, Facebook Page 1:1, TikTok 9:16.
Design: New Construction — Bright Contemporary (Denise, Oct 31, 2026). Renderer: TEMPLATES/bright_contemporary.py (docs TEMPLATES/BRIGHT_CONTEMPORARY.md), matched to TEMPLATES/new-construction-bright-contemporary/.
Offers verified on the builder's own website Nov 3, 2026, about 4:15–4:20 AM ET. Builder photos only, credited on-slide "Photo: Eastwood Homes".
No PDF (Denise, Nov 1, 2026). No YouTube Short.

Three native slide sets (each laid out for its frame, not cropped or padded):
- 4:5 1080x1350 (Instagram): slide-01.png … slide-10.png, slides.zip
- 1:1 1080x1080 (Facebook Page + personal profile): slides-1x1/, slides-1x1.zip
- 9:16 1080x1920 (TikTok; text clear of ~150 px top / 350 px bottom / 140 px right): slides-9x16/, slides-9x16.zip
Captions: below and in captions.md. Build: build/build_slides.py. Photo sources: build/CREDITS.txt.

Count: 3 verified builder offers in 3 new communities (1 builder: Eastwood Homes), all new to the tracker, all NC (Catawba and Gaston counties). Fewer than 8 verified local offers were available today, so the set is filled with one comparison slide (5) and four tip slides (6–9) rather than unverified or out-of-area deals.

## Verified offer (builder website, 2026-11-03)
Eastwood Homes — Big Red Bow Sales Event, https://www.eastwoodhomes.com/special-offers (Charlotte NC). Posted terms on each community page: "For a limited time, receive a Move-In Package available on select homes in the Eastwood Homes Charlotte Division on contracts written by December 31, 2026. This package includes whole-house blinds on operative windows only, a side-by-side stainless steel refrigerator, top-load washer, and dryer. Appliance models and blind locations are subject to change without notice and may vary. Restrictions may apply. ... Promotions can stop or change at any time without notice. Offer not valid on prior contracts."
1. The Enclave at Laurelbrook, Sherrills Ford, NC — page: "Move-in Package!" banner; "brand-new 800-home community in Sherrills Ford, less than two miles from Lake Norman"; "Incredible Amenities Now Open! Pool and cabana". Listed on the Big Red Bow offer (6 homesites participating). https://www.eastwoodhomes.com/charlotte/lake-norman/laurelbrook
2. The Meadows at Laurelbrook, Sherrills Ford, NC — page: "Move-in Package!" banner; "basement homesites less than two miles from Lake Norman"; "pool, cabana, pocket parks, a recreation field, pickleball courts". Listed on the Big Red Bow offer (6 homesites). https://www.eastwoodhomes.com/charlotte/lake-norman/the-meadows-at-laurelbrook
3. Founders Landing (55+ community, per the builder), Gastonia, NC — offer card: "save big with a move-in package with a refrigerator, washer, and dryer, and whole-house blinds"; page: "55+ homes with one-level living", "first-floor primary bedrooms", "lawn maintenance for all residents", "minutes from shopping, dining, and I-85". https://www.eastwoodhomes.com/charlotte/gastonia/founders-landing

Not used: the "below-market interest rates" part of the Laurelbrook offer card (no rate or APR posted, so no rate shown; slide 9 only tells buyers to ask for rate and APR in writing). A "Closing Costs Paid up to $5,000!" tag on one Meadows home card (home-specific, not used). Eastwood's other Charlotte Big Red Bow communities (Enclave at Riverdale, Harrisburg Village Townhomes, Norman Creek (+ Townhomes), Rone Creek, Fairways/Greens at Springlake, Waterford Commons (Rock Hill, outside SC list), Chasewood, Robinson Oaks, Rock Creek, Ashton Park, Blythe Mill Townhomes, Bryton Crossing Townhomes, Caldwell Forest, Carrington) are already in the tracker. Other builders checked server-side today: M/I Homes (Home Sweet Savings, all listed communities already featured), Shea Homes (all Charlotte QMI communities already featured), Tri Pointe (Southmont is new but no offer shown on its page server-side), KB, Toll, Century, D.R. Horton, Pulte, Mattamy, Taylor Morrison, Smith Douglas (no community-level offer for a new community readable server-side before the deadline). Nothing unverified included.

## Slides
1. Cover "3 communities. Move-in package." (Photo: Eastwood Homes — Meadows at Laurelbrook amenities aerial)
2. The Enclave at Laurelbrook: move-in package on select homes (Photo: Eastwood Homes — Enclave at Laurelbrook page hero)
3. The Meadows at Laurelbrook: fridge, washer, dryer and blinds (Photo: Eastwood Homes — pool and cabana)
4. Founders Landing: one-level homes + move-in package (Photo: Eastwood Homes — Founders Landing exterior)
5. COMPARE • Items vs. dollars (Photo: Eastwood Homes — Laurelbrook pickleball and pool aerial)
6. TIP • Ask which homes qualify (Photo: Eastwood Homes — Founders Landing kitchen)
7. TIP • Get the details in writing (Photo: Eastwood Homes — Enclave at Laurelbrook laundry room)
8. TIP • Check the dates (Photo: Eastwood Homes — Founders Landing living room)
9. TIP • Ask for the APR too (Photo: Eastwood Homes — Enclave at Laurelbrook rear exterior)
10. CTA "DM or comment DEALS and we'll get started." + contact card (Denise Wilson | Broker/REALTOR® / firm / site / phone / blank / Equal Housing Opportunity) (Photo: Eastwood Homes — Enclave at Laurelbrook kitchen)
Every offer slide: "Builder's offer, verified on the builder's site Nov 3, 2026. Terms and eligibility set by the builder; subject to change." Slides 5–9: "Comparison/Tip based on Eastwood Homes' posted offer (terms), read Nov 3, 2026. Terms and eligibility set by the builder; subject to change."

## Photo review
All 10 checked at full size in all three sizes: bright daylight exteriors and amenity aerials with blue skies, bright interiors. All builder photos are 2000–4235 px wide and downscaled in every size (no upscaling; ESRGAN not used). House numbers retouched out on slides 02 and 04. Gallery photos come from each community's page gallery; Eastwood galleries can include plan photos shot at other locations.
Photo check: all 10 sources checked with photo_registry.py check — no source-id or SHA match; only loose hash hits (12–19) to unrelated photos from other builders/carousels. Registered in TEMPLATES/photo-registry.csv.

## Compliance check
compliance_check.py: slide HTML (all three sizes) PASS — no banned words, contact block complete on slide 10 in 4:5, 1:1 and 9:16 ("Church" flag in a road name on slide 4 removed by rewording). Caption FAIL lines are the approved Oct 31 overrides only: "Equal Housing Opportunity" (EHO is on slide 10), "ends with a question" (format ends with signature + hashtags), and "Swipe" on the IG, FB Page and FB personal captions (TikTok uses "Save this"; no "swipe" on any slide).
Checklist: R1/R2/R4/R5 on slide 10 (title Broker/REALTOR®); firm name + phone in every caption signature. T1 every fact read on the builder's site Nov 3, 2026; T2 no guarantees; T3 no urgency (only the builder's own contract date, labeled as the builder's terms); T4 every slide carries the builder + date line; T5 house numbers retouched on 02 and 04, others not legible; T7 every incentive labeled as the builder's, with date and "terms and eligibility set by the builder; subject to change"; T9 no interest rates, payments, prices or down payments stated (APR rule: no rate shown, so no APR needed; slide 9 only advises asking for rate and APR). F1–F5: homes, amenities and terms only; no people, schools, safety or "perfect for" language; "55+ community" is the builder's own housing-for-older-persons designation, stated as the builder's; no addresses or home prices.

---

## Instagram
🏡 Three Charlotte-area new build communities are posting a move-in package today.

On Nov 3, 2026, I checked each offer on Eastwood Homes' own website.

🌊 The Enclave at Laurelbrook in Sherrills Ford: the builder's move-in package on select homes
🏊 The Meadows at Laurelbrook in Sherrills Ford: the builder's refrigerator, washer and dryer, and blinds offer
🏘️ Founders Landing in Gastonia: the builder's move-in package on select one-level homes
📅 The builder's terms cover contracts written by Dec 31, 2026
📄 Which homes qualify, and which models come with the package?

These details shape what you spend after the keys are in your hand.

An appliance package sounds great. The written terms decide what it's worth.

👉 Swipe through and save this post before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #NewHomesCharlotte #LakeNormanHomes #GastoniaNC #CharlotteRealEstate

## Facebook (page)
🏡 Three new build communities near Charlotte are posting a move-in package today.

On Nov 3, 2026, I checked each offer on Eastwood Homes' own website.

🌊 The Enclave at Laurelbrook and The Meadows at Laurelbrook (Sherrills Ford): the builder's move-in package on select homes
🏘️ Founders Landing (Gastonia): the builder's refrigerator, washer and dryer, and blinds offer on select homes
📅 The builder's terms cover contracts written by Dec 31, 2026
📄 Which homes qualify, and which models come with the package?

These details shape what you spend after closing.

An appliance package sounds great. The written terms decide what it's worth.

👉 Swipe through and save this post before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #CharlotteRealEstate #NewHomes

## TikTok
🏡 Three Charlotte-area new builds are posting a move-in package today.

📍 Two Sherrills Ford communities near Lake Norman, plus one in Gastonia
🧺 The builder's offer: refrigerator, washer and dryer, and blinds on select homes
📄 Each offer checked on Eastwood Homes' site Nov 3, 2026

An appliance package sounds great. The written terms decide what it's worth.

💾 Save this before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNC #NewConstruction #CharlotteRealEstate #NewHomes

## Facebook (personal profile)
🏡 Friends, three new build communities near Charlotte are posting a move-in package today.

On Nov 3, 2026, I checked each offer on Eastwood Homes' own website, and these are the questions I walk my buyers through before they sign.

🌊 The Enclave at Laurelbrook in Sherrills Ford: the builder's move-in package on select homes
🏊 The Meadows at Laurelbrook in Sherrills Ford: the builder's refrigerator, washer and dryer, and blinds offer
🏘️ Founders Landing in Gastonia: the builder's move-in package on select one-level homes
📅 The builder's terms cover contracts written by Dec 31, 2026
📄 Which homes qualify, and which models come with the package?

These details shape what you spend after closing.

An appliance package sounds great. The written terms decide what it's worth.

👉 Swipe through and save this post before you tour new homes.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#CharlotteNewConstruction #CharlotteRealEstate
