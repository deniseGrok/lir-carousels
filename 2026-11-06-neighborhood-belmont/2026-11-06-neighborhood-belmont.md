# Community Spotlight: Belmont, NC (ZIP 28012) — BLOCKED: NEEDS NEW IMAGES BEFORE DENISE CAN APPROVE
Built Fri Nov 6, 2026 (~4:30-5:30 AM ET). Fifth Community Spotlight in Denise's 'Community Spotlight — Modern Charlotte Editorial' design
(TEMPLATES/modern_editorial.py + TEMPLATES/MODERN_EDITORIAL.md). First Gaston County town in the series. Nothing posted or scheduled.
On approval: Buffer 4:00 PM ET, Instagram 4:5 (slide-01..10.png), Facebook Page 1:1 (slides-1x1/), TikTok 9:16 (slides-9x16/). NO PDF.

## STATUS
BLOCKED — see "## BLOCKED" below (source images lost in the 6:30 AM ET cleanup; slide 7 image wrong). Originally: all 10 ORIGINAL images generated Nov 6, 2026 with GenerateImage; Real-ESRGAN x4 then crop + crisp grade per size.
9:16 set only reached slide 3 before the run was interrupted; no video yet.
- Slide 7 uses evergreen Belmont Abbey National Register landmark facts (not holiday events) for longer shelf life.
- Slide 5 Conservancy garden admission (adult $18.95 + tax) verified Nov 6, 2026; fees can change.
- Images are generic illustrations, never a specific real house, business, mill or landmark; pills name topics only.
- Title Broker/REALTOR®. No interest rates → no APR. No photo credits.

## Place
Belmont, NC · ZIP 28012 · Gaston County. PLACE label "Belmont · NC". Tagline: "Railroad. Mills. River."

## Deliverables
- slide-01..10.png 1080x1350 + slides.zip (NO PDF)
- slides-1x1/ + slides-1x1.zip; slides-9x16/ + slides-9x16.zip (+ JPG zip if PNG zip over 25 MB)
- youtube-short.mp4 1080x1920 H.264, silent, slow push-in + crossfades, ends on contact slide; youtube-caption.md
- captions.md (IG / FB Page / TikTok / FB personal)

## Sources (verified Fri Nov 6, 2026) — full notes in `_research/2026-11-06-spotlight.md`
- Location: Belmont Historic District NR nomination GS0024 (eastern Gaston peninsula, Catawba + South Fork; ~10 mi west of Charlotte; Gastonia ~5 mi west); City of Belmont About (Lake Wylie south).
- History: NR nomination — Garibaldi's Station 1870; Atlanta & Charlotte Airline by 1873; renamed Belmont 1886; incorporated 1895; Chronicle Mills 1901. Do NOT use City About "1871".
- District: NPGallery NRIS 96001525 listed Dec 27 1996; 264 contributing buildings; NR listing alone does not restrict private owners (City Historic District page).
- Gardens: danielstoweconservancy.org — 380 acres, gardens opened 1999, 8+ mi trails free daily 7 a.m.–7 p.m.; Gardens admission adult $18.95 + tax.
- Parks: cityofbelmont.org — Stowe Park 24 S Main; Kevin Loftin Riverfront Park 1400 Catawba (kayak launch, amphitheatre, shelters).
- Abbey (slide 7 evergreen): Benedictines since 1876; Basilica built 1892; Belmont Abbey Cathedral NRHP Apr 11 1973 (NRIS 73001343); Abbey Historic District NRHP Jul 14 1993 (NRIS 93000584). Landmark/architecture only — no faith lifestyle or school-quality claims.
- Tip: City FAQ — Gaston County bills/collects; bills include county + city taxes if inside municipal limits; confirm Belmont corporate limits + Gaston Tax Office. Due date per G.S. 105-360 (due Sept. 1; payable at par before Jan. 6), NOT the City FAQ's "due by January 1".
- Market: Realtor.com Economic Research ZIP 28012 October 2026: median list $513,000, $226/sqft, 169 active, 61 median DOM, quality_flag 0; viewed Nov 6 2026.

## Cuts
City About "1871"; bellus mon etymology; Dutch fort 1750s; holiday events on slide 7; schools/demographics/crime/faith lifestyle; named restaurants; rates/APR; other ZIPs.

## Compliance
TEMPLATES/compliance_check.py on slide HTML. Approved Oct 31 caption format overrides the checker's EHO, last-line-question and Swipe flags.
No interest rates shown. Title Broker/REALTOR®. Licenses not checked. Fair Housing clean (places/amenities/process only).

## BLOCKED (Fri Nov 6, 2026 ~7:00 AM ET)
1. A disk cleanup at ~6:30 AM ET deleted every build/ folder in the repo (and /tmp). For Belmont that removed all 10 generated source images (build/src/gen-NN-raw.jpg + upscales) and the slide HTML. They were never committed, so they cannot be restored. The 9:16 set stopped at slide 3, so 9:16 slides 4–10, slides-9x16.zip and youtube-short.mp4 cannot be built without new images. build_slides.py, finish.py and make_youtube_short.py were re-created verbatim (temp paths moved from /tmp into build/), with the slide 8 fix below.
2. Slide 7 image is factually wrong: it shows a grey-stone Gothic church with a square crenellated tower. The real Mary Help of Christians Basilica is red brick with a tall central spire. Shown under bullets that name the Basilica, it would read as the landmark (COMPLIANCE T5). It needs a new image: a real licensed photo of the basilica, or a neutral image with no identifiable church (oak-lined campus lawn / brick walk).
3. The existing 4:5 slide-01..10.png and slides-1x1/ renders still show the OLD slide 8 tax line and the wrong slide 7 image. Do not post them. They are left uncommitted and will be replaced by the rebuild.
To finish once 10 images are in build/src/gen-NN-raw.jpg: python3 build/finish.py check; python3 build/build_slides.py upscale; python3 build/build_slides.py; python3 build/build_slides.py video; python3 build/finish.py.

## Fact-check (Denise rule Nov 5; re-verified live Fri Nov 6, 2026 ~6:35–6:50 AM ET)
- Slide 1/2: eastern Gaston County; peninsula formed by the Catawba River + South Fork; ~10 mi west of Charlotte; Gastonia (county seat) 5 mi west — Belmont Historic District NR nomination GS0024 (_research/GS0024-full.txt, lines 288–294, 4426–4427; https://files.nc.gov/ncdcr/nr/GS0024.pdf via City link). Lake Wylie to the south — https://www.cityofbelmont.org/about/
- Slide 3: 1870 Garibaldi (supervising engineer, Mecklenburg Iron Works) oversaw the new rail facilities (fueling station + bridge), stop called Garibaldi / Garibaldi's Station; Atlanta & Charlotte Airline completed by 1873; renamed Belmont 1886; incorporated 1895; Chronicle Mills organized 1901, no textile mill in Belmont in 1900 — NR nomination lines 4490–4497, 4557, 4645–4654; City About (1886, 1895, 1901).
- Slide 4: NRHP Dec 27, 1996, NRIS 96001525; 264 contributing buildings; no restrictions from NR listing unless pursuing rehab tax credits — https://www.cityofbelmont.org/belmont-historic-district/ ; https://npgallery.nps.gov/AssetDetail/NRIS/96001525
- Slide 5: 380 acres, 6500 South New Hope Road, Lake Wylie, gardens opened 1999, 8+ mi trails — https://danielstoweconservancy.org/about-us/ ; Trailhead Store + trails open daily 7 a.m.–7 p.m., free; only The Gardens require admission; adult $18.95 + tax — https://danielstoweconservancy.org/visit/hoursandadmission/
- Slide 6: Stowe Park, 24 S Main Street: large fountain, two play units, pavilion, walking path — https://www.cityofbelmont.org/stowe-park/ ; Kevin Loftin Riverfront Park, 1400 Catawba Street: kayak launch ramp, picnic shelters, walking path, amphitheatre — https://www.cityofbelmont.org/kevin-loftin-riverfront-park/
- Slide 7: monks at Belmont Abbey since 1876; basilica built 1892, on the National Register; 100 Belmont-Mt. Holly Road — https://belmontabbeycollege.edu/about-us/monastery-basilica/ ; Belmont Abbey Cathedral NRIS 73001343 published 4/11/1973 — https://npgallery.nps.gov/AssetDetail/NRIS/73001343 ; Belmont Abbey Historic District NRIS 93000584 published 7/14/1993 — https://npgallery.nps.gov/AssetDetail/NRIS/93000584 . TEXT OK; IMAGE WRONG (see BLOCKED).
- Slide 8: CORRECTED bullet 1. Old: "Gaston County bills and collects property taxes for Belmont; bills go out in July and are due by January 1". New: "Gaston County bills and collects property taxes for Belmont; bills go out in July, are due Sept. 1, and can be paid without interest through Jan. 5 (G.S. 105-360)". Sources: City FAQ (Gaston bills/collects, July bills, county + city on one bill inside corporate limits) _research/city-taxes-faq.html; G.S. 105-360(a) https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-360.html (due Sept 1; at par before Jan 6).
- Slide 9: Realtor.com Economic Research ZIP CSV re-downloaded Nov 6 (https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Zip.csv), 202610 / 28012: $513,000 median list, $226/sq ft, 169 active, 61 median DOM, quality_flag 0. All match.
- Slide 10: contact block per R5 (Broker/REALTOR®, firm, website, phone, EHO).
- Captions: no numbers except the sourced stats line in the YouTube description; FB personal caption reworked to the approved warm first-person format ("Friends, if you're house hunting…", "share this with anyone…", "Message me anytime").
- Cut (from research): City About "1871"; "bellus mon" etymology; holiday events; schools/demographics/crime/faith lifestyle; named restaurants.
