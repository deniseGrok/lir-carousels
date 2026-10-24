# DRAFT — AWAITING DENISE APPROVAL
# Seller Tips: Before buyers walk in (Sat Oct 24 2026, midday tips slot)
Nothing has been posted, scheduled, sent, or added to Buffer. Planned Buffer after approval: 12:30 PM ET — Instagram + LinkedIn (4:5 slides), Facebook page (1:1 slides-1x1/).
10 slides, theme="fullbleed_tips" (navy #0E1E3D / coral #FF6A3D), full photo on every slide except the stats-only market slide (slide 2); bottom-anchored text; source line only on slide 2.
Why seller tips: midday carousel alternates daily (Oct 20 seller, 21 buyer, 22 seller, 23 buyer), so Oct 24 is seller tips (checked seller-tips-tracker.csv and buyer-tips-tracker.csv in the repo).
Angle: getting a home showing-ready before buyers walk in, plus a reminder that prep never replaces the required disclosure statement. New seller angle. Prior seller angles: home value (Oct 13), selling from out of state (Oct 14), prep before listing (Oct 16), reviewing offers (Oct 18), net proceeds (Oct 20), listing agreement (Oct 22).

## Slides
1 hook band "SELLING? GET SHOWING-READY." · 2 market stats (Realtor.com) · 3 start at the curb · 4 let the light in · 5 clear the counters · 6 lock up valuables · 7 keep it fresh · 8 give buyers space · 9 prep isn't disclosure (NC G.S. 47E-4, 47E-5; S.C. Code 27-50-40) · 10 my recommendation + contact block.

## Sizes (Denise Oct 22 2026)
- slide-01..10.png: 1080x1350 (4:5) for Instagram / LinkedIn (+ slide-NN-video.png copies without "swipe"), PDF, slides.zip.
- slides-1x1/slide-01..10.png: 1080x1080 native square layout for Facebook (slides-1x1.zip).
- slides-9x16/slide-01..10.png: 1080x1920 native layout for TikTok photo mode, Reels and Stories (tag at 270 px, text ends ~500 px above the bottom, right margin 160 px); slides-9x16.zip.
- All zips under 25 MB (4:5 16.6 MB, 1:1 12.7 MB, 9:16 21.4 MB), so no JPG versions needed.
- youtube-short.mp4: 1080x1920 H.264 + AAC, ~41.9 s, built full-frame from the 9:16 slides (no blur fill, letterbox or pillarbox), no "swipe".

## Market data (Realtor.com only)
Realtor.com Economic Research, Residential Listings Database, monthly metro core metrics (RDC_Inventory_Core_Metrics_Metro.csv), Charlotte-Concord-Gastonia, NC-SC (CBSA 16740), month 202609 (latest available; file Last-Modified Sep 30 2026 10:41 AM ET; downloaded and verified Oct 24 2026 ~4:30 AM ET):
active_listing_count 11,182 (yy +0.1031 = +10.3%); new_listing_count 3,742 (yy -0.0751 = -7.5%); median_days_on_market 64 (yy +0.1034 = +10.3%); price_reduced_share 0.2622 = 26.2% (yy +0.0065 = +0.7 pts).
https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro.csv (data library: https://www.realtor.com/research/data/)

## Facts and sources (fetched and read Oct 24 2026, ~4:30 AM ET)
A. N.C. Gen. Stat. 47E-4(a),(b): for transfers covered by G.S. 47E-1 (exclusions in 47E-2), the owner shall furnish the purchaser a residential property disclosure statement; the NC Real Estate Commission develops and requires the standard form. https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_47E/GS_47E-4.html
B. N.C. Gen. Stat. 47E-5(a): the owner shall deliver the disclosure statements no later than the time the purchaser makes an offer. https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_47E/GS_47E-5.html
C. S.C. Code 27-50-40(A): except for transactions exempted under 27-50-30, the owner shall furnish a purchaser a written disclosure statement in the form promulgated by the commission. https://www.scstatehouse.gov/code/t27c050.php
Slides 3-8 are practical recommendations in Denise's voice ("I recommend"), not factual claims; no statistics or outcomes are attached to them.
Not used / cut: NC buyer cancellation-right details (G.S. 47E-5(b)) and the NC "no representation" option (kept the slide simple); recording-device and showing-security law; any staging/photo statistics (not verified today). Not legal advice.

## Compliance check (TEMPLATES/COMPLIANCE.md + compliance_check.py, run Oct 24 2026)
- Slides: compliance_check.py on all slide HTML (4:5, video, 9:16, 1:1): no banned-word failures; slide 10 contact block PASS in every size (Denise Wilson | REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / blank / Equal Housing Opportunity).
- Captions: follow Denise's Oct 22 caption format (signature Denise Wilson / Broker/REALTOR® / Lifestyle International Realty; no phone; EHO and firm line on slide 10), which overrides the checker's caption phone, EHO, firm-name and last-line-question checks; the checker reports those 32 lines as expected FAILs. Every caption body ends with a question before the signature. IG has no email (PASS).
- T1-T4: statute statements traced to A-C; numbers only on slide 2 with source + month; captions carry no numbers. No guarantees, no urgency, no "best/#1".
- T5-T7: generic Pexels photos, topic tags only, no listing/address implied; house numbers retouched out on slides 1, 3 and 10 (checked at full size). No other firm's listing.
- T8: disclosure slide says "Ask your agent or a real estate attorney"; "Not legal advice" in the YouTube description and this file. T9: no mortgage trigger terms.
- F1-F6: describes homes, rooms and tasks only; no people, protected classes, "perfect for", "safe", "family-friendly", "exclusive", schools or crime.

## Photos
All Pexels License originals (long side 3,553-7,333 px), resized down only, light grade + sharpening (build/prep_photos.py). Every original checked with TEMPLATES/photo_registry.py check (no source-id or series hits; closest hash distance 13, reviewed) and registered with photo_registry.py add (27 rows). Rejected at review: 7098014 (foreign apartment view through window), 33738275 (non-Carolinas palace style), 8186477 (dated, ordinary kitchen), 6937796 (house numbers), 4119832 and 32956273 (ordinary). See build/img/CREDITS.txt.

## Captions
See captions.md (Instagram, Facebook page, LinkedIn, TikTok, Facebook personal profile) and youtube-caption.md.
