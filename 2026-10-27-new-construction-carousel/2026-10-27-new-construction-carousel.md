# DRAFT — AWAITING DENISE APPROVAL
## Daily New Construction Deal Carousel — Tuesday, Oct 27, 2026 (Charlotte metro)
Nothing has been posted, scheduled, sent or added to Buffer. Theme `fullbleed_teal`: full builder photo on every slide, light teal-tinted fade, text anchored at the bottom, teal #0F4C5C + gold #F2B705, tag "NEW BUILD DEALS / NC + SC". Offers verified on the builders' own websites Oct 27, 2026, about 4:12–4:40 AM ET. Builder photos only, each credited "Photo: <Builder>"; no stock, no "Illustrative image", no "SWIPE" text.

Two native slide sets (per Denise's Oct 24 rule; no 9:16 set, no YouTube Short for New Construction):
- 4:5 1080x1350 (Instagram + LinkedIn): slide-01.png … slide-10.png, slides.zip, 2026-10-27-new-construction-carousel-DRAFT.pdf
- 1:1 1080x1080 (Facebook page + personal profile): slides-1x1/, slides-1x1.zip (laid out natively for the square frame)
Captions: captions.md (Buffer copy, also below). Build scripts: build/prep_photos.py, build/build_slides.py.

Count: **5 verified builder offers** in 5 communities (KB Home x4, Mattamy Homes x1), all new to new-construction-carousel-tracker.csv (checked against every row), all in the Charlotte metro (Lincoln, Cabarrus, Union and Mecklenburg counties NC; York, SC). KB Home is a builder not used in any past Charlotte carousel. **Tip slides used: 3** (slides 7–9: ARM vs buydown, sign-by vs close-by, the builder's lender), because only 5 local offers could be verified today.

Checked and cut today: Toll Brothers (statewide 5.49%/5.76% APR rate on select QMIs, not tied to a community page; the unused Charlotte communities Overbrook Estates and Toll Brothers at South Park show no promo); Shea Homes (Home for the Season Event, all Charlotte communities already featured, and Tega Cay is outside the SC towns allowed); Pulte Parkside Crossing / Elmbrook / Michaux Gardens (only an occupation-based Hometown Heroes offer, left off for Fair Housing caution); Century Grants Landing (Hometown Heroes only); Dream Finders Cottages at Wingate (community badge shows 2.99% but the Charlotte terms posted are a different 5.49% rate on "select communities", contracts written and closed by Oct 30; could not tie either to the community, so cut); Meritage Crossrail Station / Nolen Farm (no offer on the pages); KB Cottages at Clovis Point (Kings Mountain, outside the core metro) and Wilson Creek (Indian Land; no rate banner on its page); Taylor Morrison 14-Day Sale (community terms not confirmable in time).

## Verified offers (builders' own pages, verified 2026-10-27 ~4:20–4:40 AM ET)
KB Home offer terms (https://www.kbhome.com/special-low-rate): rate as low as 4.99% (5.781% APR) on a 5/1 FHA ARM through KBHS Home Loans; buyer must sign a purchase agreement by 10/31/26, rate-lock with KBHS within 30 days, owner-occupied, close with KBHS as lender; advertised APRs factor in a $5,000 closing cost credit and additional seller contributions from KB Home; rates valid as of 9/24/26; builder example: payments 1–60 at 4.990% (5.781% APR), payments 61–360 at 6.430% (7.225% APR); caps 1% first / 1% yearly / 5% lifetime; "certain communities may be excluded" (each community below shows the offer on its own page).
1. **KB Home — Bella Vista, Denver, NC.** https://www.kbhome.com/new-homes-charlotte-area/bella-vista-classic (also Bella Vista Heritage)
2. **KB Home — Midland Crossing, Midland, NC.** https://www.kbhome.com/new-homes-charlotte-area/midland-crossing
3. **KB Home — Wellington Pointe (The Estates at Wellington Pointe + Wellington Pointe Classic), Monroe, NC.** https://www.kbhome.com/new-homes-charlotte-area/the-estates-at-wellington-pointe ; https://www.kbhome.com/new-homes-charlotte-area/wellington-pointe-classic
4. **KB Home — Bellina, York, SC.** https://www.kbhome.com/new-homes-charlotte-area-sc/bellina
5. **Mattamy Homes — The Townes at Wade Ardrey, Charlotte, NC.** Community page: "3.99% (6.784% APR) Year 1 Buydown Payment (based on a 5.99% FHA Fixed-Rate Mortgage)" on select quick move-in homes with affiliate lender Mattamy Home Funding; promo terms: contracts 10/2/2026–10/31/2026, close on or before 11/30/2026, owner-occupied, must use Mattamy Home Funding and seller's closing agent. https://mattamyhomes.com/north-carolina/charlotte/charlotte/townes-at-wade-ardrey (terms: https://mattamyhomes.com/north-carolina/charlotte/promos/21-buydown)

## Slides
1. Cover: "5 builder rate deals near Charlotte." (Photo: KB Home, Bella Vista 2338 model exterior, bright daylight)
2. Bella Vista: 4.99% 5/1 FHA ARM (Photo: KB Home, Bella Vista 1910 exterior)
3. Midland Crossing: 4.99% ARM, APR counts a $5,000 credit (Photo: KB Home, Midland Crossing 2338 exterior)
4. Wellington Pointe: 4.99% for years 1–5, builder's adjustment example (Photo: KB Home, Wellington Pointe 2539 exterior)
5. Bellina: 4.99% 5/1 FHA ARM (Photo: KB Home, Bellina 1808 exterior)
6. The Townes at Wade Ardrey: 3.99% first-year rate (Photo: Mattamy Homes, Caswell End model exterior)
7. TIP · Compare: ARM or buydown? Look past year 1. (Photo: Mattamy Homes, Caswell End model great room/kitchen)
8. TIP · Deadlines: Sign-by is not close-by. (Photo: KB Home, Bella Vista 1910 covered porch)
9. TIP · Lender: The builder's lender is part of the deal. (Photo: KB Home, Wellington Pointe exterior)
10. CTA: "DM or comment DEALS and we'll get started." + contact block (Photo: Mattamy Homes, Caswell End model kitchen)
Every offer slide carries: "Builder's offer, verified on the builder's site Oct 27, 2026. Terms and eligibility set by the builder; subject to change." Tip slides carry: "Tip from each builder's posted terms, read Oct 27, 2026. Terms and eligibility set by the builder; subject to change."

Photo review (full size, both sets): first cover (KB Bella Vista ranch, tight roof crop) replaced with the brighter 2338 exterior. House numbers retouched out of slides 1, 2, 3 and 9 (checked at full size in 4:5 and 1:1). KB's builder photos are published at 1200x800 (largest available from kbhome.com), so slides 1–5, 8 and 9 are upscaled ~1.7x with Lanczos + stronger unsharp mask; Mattamy photos are 2000 px.
Photo check: all 10 builder photos checked with photo_registry.py check against TEMPLATES/photo-registry.csv: no source-ID/URL match (no KB Home or Wade Ardrey photo in the registry); only loose perceptual-hash hits at distance 14–18 against unrelated photos (e.g. slide 5 vs Oct 26 Cheyney kitchen), reviewed as different photos. Registered in TEMPLATES/photo-registry.csv (photo, slide render, original).

---
## Instagram
A 3.99% rate and a 4.99% rate can cost you very different amounts. 🏡
It comes down to what happens after year one.

📍 Denver · Midland · Monroe · York SC · Charlotte
✨ 5 builder rate offers, each checked on the builder's site Oct 27, 2026

One 5/1 ARM.
One 2/1 buydown.
And 3 slides on how to compare them. 🔑

Builder offers; terms set by each builder and subject to change.

💬 Comment DEALS or send me a DM and we'll get started.

When you compare rates, do you look at year one or year five?

Denise Wilson
Broker/REALTOR®
Lifestyle International Realty

#CharlotteNewConstruction #NewHomesCharlotte #MonroeNC #YorkSC #NewBuild

## Facebook (page)
🏡 5 builder rate offers near Charlotte, checked Oct 27, 2026.
A 5/1 ARM vs. a 2/1 buydown. 🔑
💬 Comment DEALS.

Which would you pick, and why?

Denise Wilson
Broker/REALTOR®
Lifestyle International Realty

#CharlotteNewConstruction #CharlotteRealEstate #NewHomes

## LinkedIn
Two builder rate offers can look alike on day one and split apart by year three. 🔑

📍 This morning I checked 5 builder offers on the builders' own sites in Denver, Midland, Monroe, York SC and Charlotte.

✨ What stood out:
A 4.99% 5/1 FHA ARM at four KB Home communities, tied to a purchase agreement by Oct 31.
A 3.99% first-year 2/1 buydown at a Mattamy Homes townhome community, with a Nov 30 close-by date.
Both tied to the builder's affiliated lender.

Builder offers; terms set by each builder and subject to change.

💬 Comment DEALS or send me a message if you or someone on your team is weighing a new build here.

When you weigh a builder rate offer, which matters more to you: the first-year payment or the payment in year six?

Denise Wilson
Broker/REALTOR®
Lifestyle International Realty

#CharlotteRealEstate #NewConstruction #Relocation #HomeBuying

## TikTok
Two low rates on the flyer. Very different payments by year three. 🏡

📍 5 new-build rate offers near Charlotte
✨ Checked on each builder's site Oct 27, 2026

ARM or buydown? The slides break it down. 🔑
Builder offers; terms set by each builder and subject to change.

💬 Comment DEALS and we'll get started.

Would you take the ARM or the buydown?

Denise Wilson
Broker/REALTOR®
Lifestyle International Realty

#CharlotteNC #NewConstruction #CharlotteRealEstate #YorkSC

## Facebook (personal profile)
Friends, if a new home near Charlotte is on your list, here's something worth a closer look 🏡

Two builders are advertising low rates right now, but they work in very different ways.

📍 This morning I checked 5 builder offers on the builders' own websites, in Denver, Midland, Monroe, York SC and Charlotte.
✨ One is a 5/1 ARM that holds its rate for five years. The other is a buydown that starts lower and steps up. Both have October deadlines set by the builder.

The slides walk through each one, plus how to compare them. 🔑
Builder offers; terms set by each builder and subject to change.

💬 Comment DEALS or send me a message and we'll get started.

If you were choosing today, would you lean toward the ARM or the buydown?

Denise Wilson
Broker/REALTOR®
Lifestyle International Realty

#CharlotteNewConstruction #CharlotteRealEstate #NewHomes #MonroeNC

## Compliance check
- `python3 TEMPLATES/compliance_check.py 2026-10-27-new-construction-carousel`: no banned/flag words in any slide HTML (4:5 and 1:1) or caption; slide 10 contact block complete (4:5 and 1:1). The only FAIL lines are the caption firm-name/phone/EHO/last-line-question checks, which Denise's Oct 22 caption format overrides (signature "Denise Wilson / Broker/REALTOR® / Lifestyle International Realty", no phone in captions, phone + firm + EHO on slide 10, hashtags last after a question).
- Checklist, every slide:
  - Slide 10 reads "DM or comment DEALS and we'll get started" with the left-aligned block: Denise Wilson | REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / blank / Equal Housing Opportunity (checked at full size, both sets).
  - Each incentive is labeled as the builder's offer with its verified date and "Terms and eligibility set by the builder; subject to change"; builder and affiliated lender named; nothing implies Denise is the builder or lender; no guarantees.
  - Rate trigger terms carry APR on every slide and caption that states a rate (4.99% / 5.781% APR; 3.99% / 6.784% APR, 5.99% fixed); ARM adjustment and buydown step-up disclosed per the builders' examples.
  - Every number names its source (the builder) and date (Oct 27, 2026); deadlines are the builders' stated dates, not urgency; no home prices or addresses.
  - Homes, places and offers only. No people, schools, "safe", "family-friendly", "exclusive" or "perfect for"; occupation-based Hometown Heroes offers left off.
  - Real dates only. Not legal, tax or lending advice.
- Captions in Denise's format: FB page caption 261 characters (within 100–300); no phone number in any caption; IG has no email; 3–5 hashtags after one blank line.
