# Seller Tips: What stays, what goes (fixtures, exclusions, smart devices, leased items, personal property) (Sun Nov 1 2026, midday tips slot)
DRAFT, awaiting Denise's approval. Nothing has been posted, scheduled, sent, or added to Buffer. When approved: 12:30 PM ET via Buffer: Instagram (4:5 slide-NN.png), Facebook Page (1:1 slides-1x1/), TikTok (9:16 slides-9x16/).
STATUS Nov 1 ~5:00 AM ET: copy, facts, captions, stats slide data and build script are done and layout-tested; the custom-generated images (GenerateImage) are PENDING, so the slide PNGs, PDF and zips are not built yet. Prompts: build/IMAGE_PROMPTS.md. Then `python3 build/build_slides.py upscale` and `python3 build/build_slides.py`.
10 slides, Signature Authority v2 (Buyer/Seller Tips only; approved Oct 31 2026; matches 2026-10-31-buyer-tips-title-and-survey 4:5 @ 4f30971): coral SELLER TIP pill, Anton headline (white + coral line), 4 coral check bullets, cover script "what goes", slide 2 stats on navy (only slide with a source line), slide 10 LET'S TALK with Denise's real headshot cutout (TEMPLATES/denise-wilson-headshot-cutout-hires.png).

Why seller tips: midday carousel alternates daily (Oct 30 seller pre-listing inspection, Oct 31 buyer title and survey), so Nov 1 is seller tips.
Angle: what conveys with the sale (fixtures, exclusions, smart devices, leased items, personal property). New seller angle; prior: home value, out-of-state, prep before listing, reviewing offers, net proceeds, listing agreement, showings, under contract, buy and sell, pre-listing inspection.

## Images
Slides 1, 3-9 and the slide 10 background: custom-generated illustrative images (GenerateImage), not photos of a real property or person, never presented as a listing. No on-slide label. Raw 864x1152 kept as build/src/gen-NN-raw.jpg, Real-ESRGAN x4plus upscaled (TEMPLATES/tools/esrgan_upscale.py) to build/src/gen-NN.jpg, crisp() GEN grade, left navy band only, text layer rendered 2x and downscaled. See build/IMAGE_PROMPTS.md and CREDITS.txt.

## Sizes
- slide-01..10.png 1080x1350 (Instagram), 2026-11-01-seller-tips-what-stays-DRAFT.pdf, slides.zip.
- slides-1x1/ 1080x1080 (Facebook Page + personal), slides-1x1.zip, -DRAFT-1x1.pdf.
- slides-9x16/ 1080x1920 (TikTok; text clear of top 150, bottom 350, right 140), slides-9x16.zip, -DRAFT-9x16.pdf. No YouTube Short.

## Market data (Realtor.com only)
Realtor.com Economic Research, monthly metro core metrics (RDC_Inventory_Core_Metrics_Metro.csv), Charlotte-Concord-Gastonia, NC-SC (CBSA 16740), month 202609 (latest available; re-downloaded and verified Nov 1 2026 ~4:45 AM ET):
median_listing_price $424,950 (yy -3.08%); active_listing_count 11,182 (yy +10.31%); median_days_on_market 64 (yy +10.34%); price_reduced_share 26.22% (yy +0.65 pts, shown +0.7 pts).
https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro.csv (data library: https://www.realtor.com/research/data/)

## Facts and sources (verified Nov 1 2026)
A. NC Standard Form 2-T, Offer to Purchase and Contract (NC REALTORS / NC Bar; July 2026 marked changes, https://www.ncrealtors.org/wp-content/uploads/markedup0726-2-T.pdf; forms list Oct 19 2026 shows 2-T REV 8/2026): para. 2 intro: do not assume an item will or will not be included based on a statement or advertisement outside the contract (slide 9). 2(a): all existing fixtures included in the purchase price, free of liens, unless excluded in (d) or (e) (slide 3). 2(b) specified items, "if present on the Property on the date of the offer", including traditional and "smart" versions: ceiling and wall-attached fans, light fixtures, built-in appliances, blinds/shades, curtain/drapery rods, attached mirrors, surface-mounting TV brackets, thermostats, alarm/security systems incl. cameras, sensors, doorbells; storage shed; landscape trees and plants (except movable containers), landscape and foundation lighting; mailboxes; solar systems; EV chargers (slides 3, 4, 5). 2(c): before closing, seller unpairs conveying devices, deletes personal data, restores factory settings (slide 5). 2(d): leased or not-owned items (e.g., alarm and security systems) must be identified and do not convey; leased fuel tank in 7(d) does not convey (slide 7). 2(e) other excluded items; seller must repair damage caused by removal (slide 6). Para. 3: personal property listed transfers at no value; buyer advised to consult lender (slide 8).
B. NC REALTORS Form 2G, Guidelines for Completing the Offer to Purchase and Contract (July 2026 marked changes, https://www.ncrealtors.org/wp-content/uploads/markedup0726-2G.pdf): 2(d) liens for solar panels, HVAC systems and other major improvements need to be paid by seller at closing unless excluded or addressed in a custom addendum (slide 7); 2(e) if in doubt whether an excluded item is a fixture, it is advisable to list it (slide 6); para. 3 examples of personal property: curtains, draperies, free-standing appliances such as a refrigerator (slide 8).
C. NC REALTORS Legal Q&A, "Fixtures" paragraph and garage door openers (listed items convey only if present on the date of the offer): https://www.ncrealtors.org/question/fixtures-paragraph-and-garage-door-openers/ (background).
D. SC: no statewide standard contract; slide 9 says only "In SC, read your contract too" (a recommendation, no SC rule claimed).
Slides 6 ("Or swap it before you list"), 7 ("Ask your attorney early"), 9 (walk the home, note items, tell your broker) and 10 are planning recommendations in Denise's voice. Not legal or tax advice; slide 7 points sellers to an attorney.

## Compliance check (TEMPLATES/COMPLIANCE.md + compliance_check.py, run Nov 1 2026)
Layout test render (HTML text of all 10 slides, 4:5 + 9:16) and captions: no banned/flag words on any slide; slide 10 contact block PASS. Caption FAIL lines are only the approved Oct 31 format overrides: no "Equal Housing Opportunity" line (on slide 10), no closing question, "Swipe" in IG/FB/FB personal captions (TikTok caption avoids it). IG caption has no email.
- T1-T4: every fact from sources A-B read today; numbers only on slide 2 with source + month; captions carry no statistics; no guarantees ("help prevent", not "prevent"), no urgency.
- T5: generated illustrations only, no addresses, house numbers, signs or listing implied (re-check each image when generated).
- T8: form rules explained, attorney pointed to; "Not legal or tax advice" noted here.
- Fair Housing: homes, items, documents and process only; people only incidental (a hand on slides 5 and 9); no "perfect for", "safe", "family-friendly", "exclusive", schools or crime.

## Captions
See captions.md (Instagram, Facebook Page, TikTok, Facebook personal profile) in Denise's approved Oct 31 format.
