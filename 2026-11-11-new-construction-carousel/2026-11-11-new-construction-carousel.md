# 2026-11-11 New Construction — Quick move-in savings, closing cost help, a reduced price & amenities (NO rates/APR)

Bright Contemporary design. Verified Wed Nov 11, 2026 (~4:30–4:55 AM ET) on builders' live sites. NO PDF. No YouTube Short.
Denise rule (Nov 5, 2026): New Construction focuses on deal price reductions and amenities — never interest rates or APR.
Status: DRAFT — awaiting Denise approval. Not in Buffer. Buffer plan after approval: 9:30 AM ET (IG 4:5, FB Page 1:1, TikTok 9:16).

## Offers (verified Nov 11, 2026)

1. David Weekley Homes — North Creek Village – Townhomes (Huntersville, NC 28078; "Huntersville, NC | Southeast"; page label FINAL OPPORTUNITIES)
   50th Anniversary "Half a Century of Home Sweet Home Savings": up to $40,000 toward a home discount or financing on a select David Weekley Quick Move-in Home in the Charlotte area, purchased Nov 1–Dec 6, 2026, financing with Grace Home Lending; home must close by Dec 22, 2026; offer must be presented before signing; not valid with any other offer or on previously written contracts; discount does not apply to options, lot premiums or other incentives. Disclosure: buyers are NOT required to use Grace Home Lending (the financing incentive requires it). The offer is listed in the Offers section of the North Creek Village – Townhomes page (Nov 11). The builder's 7%-of-price formula is NOT quoted (no % rule); slides state only "up to $40,000".
   Community: two-story townhomes with detached garages and fenced yards; six quick move-ins listed "Ready Now" from $439,382 (The Parklane, 10024 Mamillion Dr) to $524,616 (The Gardengate, 11411 Prosperity Church Rd); community trails ("walking distance to nearby shops using the community trails"); amenities list: Gazebo, Park, Playground, Sidewalks, Low Maintenance, HOA. Address 10013 Mamillion Drive (not on slides).
   Sources: https://www.davidweekleyhomes.com/new-homes/nc/charlotte/huntersville/north-creek-village-townhomes · https://www.davidweekleyhomes.com/promo/50th-anniversary-charlotte
   Not used: school lines (Fair Housing), HOA/tax figures, "Up to $5,000 Preferred Lender Credit" offer.

2. Stanley Martin — Coventry (Pineville, NC 28134; 12718 Downs Circle)
   Community-page banner (Nov 11): "Now Selling: ... or receive up to $15,000** towards closing costs for a limited time!" Only the closing-cost option is quoted; the rate/APR half of the banner is omitted (Denise rule). The ** footnote text and an end date are NOT posted on the page, so the slide says "for a limited time, per Stanley Martin" and tells buyers to get the full terms in writing.
   Community: new townhomes priced from $399,000; resort-style pool and cabana; scenic walking trails; homes with a versatile lower level (rec room or bedroom), double covered porches, attached garages.
   Source: https://www.stanleymartin.com/north-carolina/charlotte/pineville/pnv/coventry
   Not used: rate/APR text, school lines, Pineville Lake Park photos, "small town charm" area copy.

3. Taylor Morrison — Fincastle Glen (Shelby, NC; Cleveland County; listed in Taylor Morrison's Charlotte division)
   Ready home 302 Fincastle Glen Road (Homesite 26, Linville plan, 3 bed / 2.5 bath, 1,772 sq ft, ready date 11/1/2026): $268,990, was $281,500 (save $12,510) — on the home's own page and the community page. Also 308 Fincastle Glen Road (Manteo, ready 11/1/2026): $284,990, was $295,530. (232 Fincastle Glen Rd $288,990 was $299,060, not on slides.) Listed on Taylor Morrison's Charlotte "Homes eligible for limited-time offers" page (make-moves/charlotte). No end date posted for the reduced prices.
   Community: featured amenity "Butterfly garden"; "steps away from Food Lion, and only minutes away from Uptown Shelby, with easy access to I-85, I-74, Uptown Charlotte".
   Sources: https://www.taylormorrison.com/nc/charlotte/shelby/fincastle-glen · https://www.taylormorrison.com/nc/charlotte/shelby/fincastle-glen/floor-plans/linville/home-available-now-at-302-fincastle-glen-road · https://www.taylormorrison.com/make-moves/charlotte
   Not used: 304 Fincastle Glen Road (community list showed $298,990 was $318,120, but that home's own page showed $299,990 with no was-price — conflicting, so cut); the Taylor Morrison rate/buydown offer; the school line.

## Slides
1 cover · 2–4 deals · 5 compare (three kinds of builder dollars) · 6–9 tips (watch the dates; ask what it leaves out; know the lender terms; walk the amenities) · 10 CTA contact card (Denise Wilson | Broker/REALTOR®, Lifestyle International Realty — Carolinas, denisewilson.lircarolinas.com, denise.realty1@gmail.com, 704-615-7347, EHO). The email line is added to the template card in build_slides.py for this build only (TEMPLATES/bright_contemporary.py unchanged).

## Deliverables
4:5 (slide-01..10.png + slides.zip 11.9 MB) / 1:1 (slides-1x1/ + slides-1x1.zip 9.7 MB) / 9:16 (slides-9x16/ + slides-9x16.zip 14.5 MB). All zips under 25 MB, so no JPG zip. No PDF, no YouTube Short. Zero interest rates / APR / % on slides or captions; buy-downs not mentioned.
Captions: captions.md (Instagram, Facebook Page, TikTok, Facebook personal profile); fb-personal-caption.md (FB personal alone).
Build: build/build_slides.py (python3 build/build_slides.py [4x5|1x1|9x16|N]).

## Photo check
All 10 images are from the builders' own sites (build/CREDITS.txt, build/PHOTO_MANIFEST.txt). Slide 3 is a Stanley Martin elevation RENDERING of the Coventry townhomes (pill "Photo: Stanley Martin (rendering)"). Stanley Martin interiors (06, 10) are the builder's Hayworth plan photos shown on the Coventry page. No AI images. No people. House number retouched out of 02 (10511 on the porch column). Checked against TEMPLATES/photo-registry.csv: no SHA1 or source-id match; only loose hash hits (distance >= 13, unrelated photos). Registered: 30 rows (src_original, photo, slide_render x 10) appended directly to the repo registry.

## Compliance
TEMPLATES/compliance_check.py: all slide HTML PASS (contact block complete on slide 10 in all three sizes). Remaining FAIL lines are the approved Oct 31 caption-format overrides only (same as Nov 10): "Equal Housing Opportunity" in caption sections (EHO is on slide 10), "ends with a question", and "Swipe" in IG/FB Page captions (TikTok uses "Save this"; FB personal uses "Share this"). Grep check: no %, APR, rate or buydown text on any slide or caption. Fair Housing: homes, prices, amenities and terms only; no people, schools, "perfect for", safety/family-friendly/exclusive claims. No guarantees or fake urgency (dates shown are the builders' posted dates).

## Fact-check (Wed Nov 11, 2026)
- Slide 1: 3 offers in Huntersville, Pineville and Shelby, NC; David Weekley, Stanley Martin, Taylor Morrison — pages above.
- Slide 2: up to $40,000, Grace Home Lending, Nov 1–Dec 6 / close by Dec 22, present before signing — DWH promo page; ready-now townhomes from $439,382, detached garages, fenced yards, trails, gazebo, playground — North Creek Village – Townhomes page.
- Slide 3: up to $15,000 toward closing costs for a limited time; priced from $399,000; resort-style pool and cabana, scenic walking trails, double covered porches — Coventry page.
- Slide 4: 302 Fincastle Glen Road $268,990 was $281,500, Linville, 3 bed, ready 11/1/2026; 308 Fincastle Glen Road $284,990 was $295,530; butterfly garden; Food Lion; Uptown Shelby — Taylor Morrison pages.
- Slides 5–8: drawn from the posted terms above (slide 7: DWH exclusions + "not valid with any other offer"; slide 8: DWH Grace Home Lending requirement + "NOT required to use Grace Home Lending").
- Slide 9: general touring tip.
- Slide 10: contact block.

## Cut / not used
- Meritage Homes: National Sales Event (contracts Nov 2-15) is live, but every Charlotte-area Meritage community found is already in the tracker; Chambers Crossing is coming soon.
- Tri Pointe Southmont (Charlotte), Stanley Martin Woodson (Charlotte) and Stratford (Denver), Taylor Morrison Terraces at Waverly / Austin Village / Patterson Grove / Ridge at Creek Park, Lennar Northway Pointe and Alcott Village: coming soon, no offer posted.
- Empire Homes Equinox: Smart Move banner shows only a monthly-payment line (rate-based), no dollar amount — cut. Providence Towns: no offer shown.
- Stanley Martin Fallbrook Townhomes: rate-only offer — cut.
- Taylor Morrison The Coves on Lake Wylie Towns and Estates at Tramore: same master community as tracker rows — skipped. Ridge at Sugar Creek, Terraces at the Exchange, Senata, Indian Trail Townhomes, Stafford at Langtree, Tramore, River Falls (Tega Cay SC, also outside allowed SC towns): already in tracker.
- David Weekley The River District collections: The River District already in tracker (Toll Brothers) — skipped. Westview Towns, Central Living at Craig, McAlpine Place, Westwood Reserve: in tracker. Brightside Townes / The Retreat at Steele Creek: no quick move-ins on the offer.
- Smith Douglas, Pulte, Eastwood, Lennar (other communities): either already in tracker, offers expired Oct 31, or terms not readable on the builder site in time — not used.
- All rate, APR and buydown promotions (Denise rule).
