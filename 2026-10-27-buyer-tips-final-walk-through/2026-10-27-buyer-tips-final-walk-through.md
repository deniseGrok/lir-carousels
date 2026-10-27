# DRAFT — AWAITING DENISE APPROVAL
# Buyer Tips: The final walk-through (Tue Oct 27 2026, midday tips slot)
Nothing has been posted, scheduled, sent, or added to Buffer. Planned Buffer after approval: 12:30 PM ET — Instagram + LinkedIn (4:5 slides), Facebook page (1:1 slides-1x1/).
10 slides, theme="fullbleed_tips" (navy #0E1E3D / coral #FF6A3D), full photo on every slide except the stats-only market slide (slide 2); bottom-anchored text; source line only on slide 2.
Why buyer tips: midday carousel alternates daily (Oct 25 buyer, Oct 26 seller), so Oct 27 is buyer tips (checked buyer-tips-tracker.csv and seller-tips-tracker.csv).
Angle: the buyer's final walk-through before signing at closing (timing, agreed repairs, testing systems, what stays, new move-out damage, outside items, what to do if something is off). New buyer angle. Prior buyer angles: preapproval (Oct 15), inspections (Oct 17), contract to closing (Oct 19, one closing-day line only), true monthly cost (Oct 21), buyer agreement (Oct 23), making an offer (Oct 25).

## Sizes (Denise Oct 24 2026)
- slide-01..10.png: 1080x1350 (4:5) for Instagram / LinkedIn, PDF (2026-10-27-buyer-tips-final-walk-through-DRAFT.pdf), slides.zip (15M).
- slides-1x1/slide-01..10.png: 1080x1080 native square layout for Facebook (slides-1x1.zip, 12M).
- Both zips under 25 MB, so no JPG versions needed. No 9:16 set and no YouTube Short.

## Market data (Realtor.com only)
Realtor.com Economic Research, Residential Listings Database, monthly metro core metrics (RDC_Inventory_Core_Metrics_Metro.csv), Charlotte-Concord-Gastonia, NC-SC (CBSA 16740), month 202609 (latest available; file Last-Modified Sep 30 2026 10:41 AM ET; downloaded and verified Oct 27 2026 ~4:25 AM ET; quality_flag 0):
median_listing_price $424,950 (yy -0.0308 = -3.1%); median_days_on_market 64 (yy +0.1034 = +10.3%); pending_listing_count 4,681 (yy -0.0593 = -5.9%); price_reduced_share 0.2622 = 26.2% (yy +0.0065 = +0.7 pts).
https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro.csv (data library: https://www.realtor.com/research/data/)

## Facts and sources (fetched and read Oct 27 2026, ~4:30 AM ET)
A. CFPB, Close the deal: "Before you sign any papers, do a final walk-through of the home. Make sure everything that you and the seller agreed would be repaired has been repaired and anything the seller agreed to leave in the house is in place. If it isn't, contact the seller immediately to discuss." https://www.consumerfinance.gov/owning-a-home/close/close-the-deal/ (slides 1, 4, 6, 9)
B. CFPB, What should I do before, during, and after the mortgage closing process?: inspect the home and make sure it is acceptable and any agreed-upon repairs have been completed. https://www.consumerfinance.gov/ask-cfpb/what-should-i-do-before-during-and-after-the-mortgage-closing-process-en-1907/ (slides 4, 7)
Slides 3, 5, 7, 8 and 10 are recommendations in Denise's voice (schedule close to closing, test systems, look for new damage, check outside items, walk through together), not statistics or outcomes. Slide 9 frames options as contract-dependent and points to the agent or closing attorney.
Not used / cut: NC Form 2-T / SC contract walk-through or possession clauses (not verified from official sources today, so no rule citations); specific "within 24 hours" timing; re-inspection or escrow-holdback options. Not legal advice; slide 10 points buyers to a real estate attorney.

## Compliance check (TEMPLATES/COMPLIANCE.md + compliance_check.py, run Oct 27 2026)
Result: no banned/flag words on any slide (4:5 and 1:1 HTML) or caption; slide 10 contact block PASS in both sizes; IG no email PASS. 24 FAIL lines, all the expected caption overrides (6 captions x firm name, phone, EHO, last-line question) per Denise's Oct 22 caption format; every caption body ends with a question before the signature.
- T1-T4: CFPB statements traced to A-B; numbers only on slide 2 with source + month; captions carry no numbers. No guarantees, no urgency, no "best/#1".
- T5-T7: generic Pexels photos, topic tags only, no listing/address implied; no visible house numbers (cover door-trim number painted out; all slides checked at full size, both sizes). No other firm's listing or signage.
- T8: slide 9 and slide 10 point to a closing attorney / real estate attorney. T9: no mortgage trigger terms; Denise not presented as a lender.
- F1-F6: describes homes, rooms and process only; no people, protected classes, "perfect for", "safe", "family-friendly", "exclusive", schools or crime.

## Photos
All Pexels License originals (long side 3,688-8,256 px), resized down only, light grade + sharpening (build/prep_photos.py). Every original checked with TEMPLATES/photo_registry.py check (no source-id, series or near-duplicate hits; candidate-id proximity filter of 300 vs registered Pexels ids) and registered with photo_registry.py add. See build/img/CREDITS.txt.
Photo pass before delivery: replaced cover candidate 37978211 (English stone-slate cottage, not plausibly Carolinas) with 18326829; replaced slide 10 candidates 36770377 (dark under the text gradient) and 37181607 (pale sky, foreign trim) with 5806989.

## Captions
See captions.md (Instagram, Facebook page, LinkedIn, TikTok, YouTube, Facebook personal profile).
