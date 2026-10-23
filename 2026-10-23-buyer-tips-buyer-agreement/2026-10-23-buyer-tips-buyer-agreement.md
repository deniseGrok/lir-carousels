# DRAFT — AWAITING DENISE APPROVAL
# Buyer Tips: Read your buyer agreement before you tour (Fri Oct 23 2026, midday tips slot)
Nothing has been posted, scheduled, sent, or added to Buffer. Planned Buffer after approval: 12:30 PM ET — Instagram + LinkedIn (4:5 slides), Facebook page (1:1 slides-1x1/).
10 slides, theme="fullbleed_tips" (navy #0E1E3D / coral #FF6A3D), full photo on every slide except the stats-only market slide (slide 2); bottom-anchored text; source line only on slide 2.
Why buyer tips: midday carousel alternates daily (Oct 19 buyer, 20 seller, 21 buyer, 22 seller), so Oct 23 is buyer tips (checked buyer-tips-tracker.csv and seller-tips-tracker.csv in the repo and in content-research).
Angle: what to check in a written buyer agreement before the first tour. New buyer angle. Prior buyer angles: pre-approval (Oct 15), inspections (Oct 17), contract to closing (Oct 19), true monthly cost (Oct 21). Companion to the Oct 22 seller listing-agreement post, written from the buyer's side.

## Slides
1 hook band "BUYING? READ IT FIRST." + what a buyer agreement is (NAR) · 2 market stats (Realtor.com) · 3 when you sign · 4 pay is negotiable · 5 who pays · 6 the dates · 7 which type · 8 exit terms · 9 disclosures / dual agency · 10 my recommendation + contact block.

## Sizes (Denise Oct 22 2026)
- slide-01..10.png: 1080x1350 (4:5) for Instagram / LinkedIn (+ slide-NN-video.png copies without "swipe"), PDF, slides.zip.
- slides-1x1/slide-01..10.png: 1080x1080 native square layout for Facebook (slides-1x1.zip).
- slides-9x16/slide-01..10.png: 1080x1920 native layout for TikTok photo mode, Reels and Stories (tag at 270 px, text ends ~500 px above the bottom, right margin 160 px); slides-9x16.zip.
- youtube-short.mp4: 1080x1920 H.264 + AAC, ~41.9 s, built full-frame from the 9:16 slides (no blur fill, letterbox or pillarbox), no "swipe".

## Market data (Realtor.com only)
Realtor.com Economic Research, Residential Listings Database, monthly metro core metrics (RDC_Inventory_Core_Metrics_Metro.csv), Charlotte-Concord-Gastonia, NC-SC (CBSA 16740), month 202609 (latest available; file Last-Modified Sep 30 2026; downloaded and verified Oct 23 2026 ~4:35 AM ET):
active_listing_count 11,182 (yy +0.1031 = +10.3%); price_reduced_share 0.2622 = 26.2% (yy +0.0065 = +0.7 pts); median_listing_price $424,950 (yy -0.0308 = -3.1%); median_days_on_market 64 (yy +0.1034 = +10.3%).
https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro.csv (data library: https://www.realtor.com/research/data/)

## Facts and sources (all fetched and read Oct 23 2026, ~4:30-4:40 AM ET)
A. NAR, "Consumer Guide to Written Buyer Agreements": as of Aug 17 2024 buyers will be asked to sign a written buyer agreement before touring a home with an agent, in person or virtually; not needed to visit an open house on your own or ask about services; the agreement outlines the services and what the agent will be paid; compensation is negotiable and not set by law; must be clearly defined (e.g., $0, flat fee, percent, hourly) and not open-ended or a range; you are responsible for paying as outlined but can still request, negotiate for and receive compensation for your agent from the seller; you and your agent can mutually agree to change it; agreements may have conditions to exit; consult an attorney about state law. https://www.nar.realtor/the-facts/consumer-guide-written-buyer-agreements
   (Slide 3 "many agents" follows NAR's wording: a "nationwide requirement for many real estate professionals".)
B. 21 NCAC 58A .0104 (NCREC): (a) buyer agreements must be express, in writing and signed no later than the time an offer is made; an agreement that binds the buyer for a period of time or restricts the buyer's right to work with other agents must be in writing from formation; every written agreement is for a definite period and terminates without prior notice at expiration; early-termination penalty set out clearly and conspicuously; (c) "Working with Real Estate Agents" at first substantial contact; (d)+(i) a broker may not represent another party in the same transaction without the written authority of each party; a firm representing more than one party is a dual agent. http://reports.oah.state.nc.us/ncac/title%2021%20-%20occupational%20licensing%20boards%20and%20commissions/chapter%2058%20-%20real%20estate%20commission/subchapter%20a/21%20ncac%2058a%20.0104.pdf
C. S.C. Code 40-57-135(I)(2): a buyer's representation agreement must be in writing with (b) the fee or method of calculating it, (c) how and when compensation is earned, (f) specific beginning and ending dates, (h) terminates on the definite expiration date unless a written extension is signed, (i) must clearly state, if applicable, whether it is "exclusive agency" or "exclusive right to represent". https://www.scstatehouse.gov/code/t40c057.php
D. S.C. Code 40-57-350(I)(1): a firm may act as a disclosed dual agent only with prior informed, written consent; the dual agency agreement must be signed by the buyer before writing an offer. Same URL.
Not used / cut: specific NC/SC form numbers and protection-period terms (not verified today); typical compensation amounts (no verifiable standard). Not legal advice.

## Compliance check (TEMPLATES/COMPLIANCE.md + compliance_check.py, run Oct 23 2026)
- Slides: compliance_check.py on all slide HTML (4:5, video, 9:16, 1:1): no banned words; slide 10 contact block complete in every size (Denise Wilson | REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / blank / Equal Housing Opportunity), confirmed at full size. Slide 7 was reworded ("Know which type") so the statute term "exclusive" does not appear on slides or captions.
- Captions: follow Denise's Oct 22 caption format (signature Denise Wilson / Broker/REALTOR® / Lifestyle International Realty; no phone; EHO and firm line on slide 10), which overrides the checker's caption phone, EHO and last-line-question checks. The checker therefore reports those caption lines (plus its exact "— Carolinas" firm-name string, YouTube Title/Tags sections) as expected FAILs; every caption ends its body with a question before the signature.
- T1-T4: every rule statement traced to A-D; numbers only on slide 2 with source + month; captions carry no numbers. No guarantees, no urgency, no "best/#1".
- T5-T7: generic Pexels photos, topic tags only, no listing/address implied; the cover's address plaque was retouched out; no visible house numbers (checked at full size). No other firm's listing; no builder incentives.
- T8: rules described as what they say + "ask"/"I recommend"; "Legal questions? Ask a real estate attorney" on slide 8; "Not legal advice" in the YouTube description and this file. T9: no mortgage trigger terms.
- F1-F6: describes documents, rules and rooms only; no people, protected classes, "perfect for", "safe", "family-friendly", "exclusive", schools or crime.

## Photos
All Pexels License originals (>=4000 px), resized down only, light grade + sharpening (build/prep_photos.py). Every original checked with TEMPLATES/photo_registry.py check (no source-id or series hits; closest hash hits reviewed side by side and confirmed different images) and registered with photo_registry.py add. Rejected at full-size review: 4030036 (house number), 4682075 (house number), 31748131 (overcast, dull), 7174386 (wall AC units, busy), 15062127 (plain), 7174113 (dated), 7587864 (dark), 29012619 (muted), 7836571 (casual, not luxury), 3935320 (ordinary). See build/img/CREDITS.txt.

## Captions
See captions.md (Instagram, Facebook page, LinkedIn, TikTok, Facebook personal profile) and youtube-caption.md.
