# Daily carousel standard (all three: new construction 7 AM, seller tips noon, neighborhood 5 PM)
Effective Oct 14, 2026, per Denise.

## COMPLIANCE + CONTACT BLOCK (Oct 22 2026, Denise; supersedes every older contact-block line below)
- Run TEMPLATES/COMPLIANCE.md + `python3 TEMPLATES/compliance_check.py <carousel-folder>` on every slide set and caption before delivery; fix every FAIL.
- Slide 10 contact block, EVERY carousel and EVERY size (4:5, 1:1, 9:16), left-aligned, one item per line:
  Denise Wilson | REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / (blank) / Equal Housing Opportunity
  (The firm line is REQUIRED: 21 NCAC 58A .0105, S.C. Code 40-57-135(E). The Oct 15/16 "no '— Carolinas' / no Lifestyle International Realty line" notes below are superseded.)
- Firm name "Lifestyle International Realty — Carolinas" + 704-615-7347 + "Equal Housing Opportunity" in every caption and every YouTube/TikTok description; every caption ends with a question.
- FB personal signature: Denise Wilson / Broker/REALTOR® / Lifestyle International Realty — Carolinas.
- Fair Housing: describe homes, places, prices, amenities; never people, demographics or who it's "perfect for"; no "safe", "family-friendly", "exclusive", crime or school claims. Never imply a generic photo is a named place. No visible house numbers or readable plates (retouch or reject).
- Denise's NC and SC licenses are confirmed: never check them.

## SIZING (Oct 22 2026, Denise): three native slide sets, each laid out for its own frame (never a crop or pad of another)
- 4:5 1080x1350 = slide-NN.png (+ slide-NN-video.png, PDF, slides.zip): Instagram + LinkedIn carousel.
- 1:1 1080x1080 = slides-1x1/slide-NN.png + slides-1x1.zip: FACEBOOK carousel (Facebook carousels are square). Tag top, text bottom-anchored (~92 px above the bottom), smaller headline (~58-64 px) and 30 px bullets so nothing is cropped or cramped; stats as a 2x2 grid; full compliance contact block on slide 10.
- 9:16 1080x1920 = slides-9x16/slide-NN.png + slides-9x16.zip: YouTube Shorts, IG/FB Reels, TikTok photo mode, Stories. Keep key text clear of the top ~250 px, bottom ~420 px and right ~140 px (tag at 270 px, text ends ~500 px above the bottom, right margin 160 px). No "swipe".
- YouTube Short / Reel: 1080x1920 H.264/AAC built from the 9:16 slides and FILLING THE FULL SCREEN edge to edge (no blurred fill, letterbox or pillarbox), 30-59 s, slow push-ins, crossfades, soft self-generated music, ends holding on the contact slide, under 100 MB; check extracted frames. Reference builds: 2026-10-22-neighborhood-wilmore/build/ (all three sets) and 2026-10-22-seller-tips-listing-agreement/build/.
- Older lines below that say "1080x1350 for every platform" or "Short padded with #0F4C5C / letterboxed" are superseded by this section.

## PHOTO HABIT (Oct 17 2026, every carousel, every routine run): FIX WEAK PHOTOS BEFORE HANDOFF. NEVER FLAG THEM FOR DENISE TO SWAP.
- Before handoff, check all 10 slides at full size (1080x1350, not just the contact sheet). Replace any photo that isn't scroll-stopping: soft, noisy, dull, snapshot-quality, cluttered (power lines, highways, parking lots), or dark.
- Do the swap yourself: full-res originals (Pexels/Unsplash/Wikimedia free license), resize down only, grade and sharpen, rebuild, re-check. The handoff never says "slide X photo could be stronger; swap if you like". Weak photos are fixed, not reported.
- Never misidentify a place. Generic photos are never labeled as a named place (e.g. tag "HISTORIC ESTATE", not "THE DUKE MANSION", unless it's a real photo of it). Avoid photos with obvious non-Charlotte giveaways (palms, Spanish moss, cobblestone old-town streets) where they'd read as the named neighborhood; crop them out or pick another.
- Credit on-slide only when the license requires it (CC BY / BY-SA: small 30px line, e.g. "Photo: Name, CC BY-SA 4.0").
- Skylines already used (don't reuse): Pexels 18931263, 16726603, 29014306, 13107825; Wikimedia "Charlotte NC Uptown.jpg" (Myers Park Oct 17).
- Save build/prep_photos.py + build/img/CREDITS.txt in every carousel folder so slides can be rebuilt.

## PHOTO REGISTRY (Oct 19 2026, every build, every routine run): NEVER REUSE A PHOTO. Denise: "I would like a new graphic that has not been used before."
- Registry: TEMPLATES/photo-registry.csv (one row per photo use: carousel, slide, kind, provider, source_id, source_url, photographer, file, sha1, phash, dhash, zone_phash, zone_dhash, added, notes). Tool: TEMPLATES/photo_registry.py.
- Before using ANY photo, check it: `python3 TEMPLATES/photo_registry.py check build/src/<original>.jpg` (or call photo_registry.check(path, src_id=...)). It compares perceptual hashes (whole image + the clean photo zone of a 4:5 crop, loose threshold), the source ID/URL, and the Unsplash upload series (same timestamp prefix).
- Any hit = look at both images side by side. Same photo, same house or room from another angle, or the same photographer series/upload batch (Unsplash id prefix, Pexels ids a few hundred apart from a used one) = reject and pick another. Hash hits that are clearly different images are fine.
- Every slide in a new carousel must be new: no photo from any earlier carousel (tips, neighborhood, new construction, demos, earlier draft versions in git history). Within one carousel, use each photo once.
- After the build passes full-size review, append the carousel's photos: `python3 TEMPLATES/photo_registry.py add <carousel-folder> <note>` (reads build/img/CREDITS.txt + build/prep_photos.py; hashes build/img/NN.jpg, slide-NN.png and the src original). Commit the updated registry with the carousel.
- Builder photos on new construction slides are logged too.

- EXACTLY 10 slides in every set (Instagram/Facebook cap carousels at 10 images; LinkedIn gets the same 10). Sizes: see SIZING (Oct 22 2026) above: 4:5 IG/LinkedIn, 1:1 Facebook, 9:16 Shorts/Reels/TikTok/Stories.
- No standalone cover slide and no standalone contact/CTA slide.
  - Slide 1 = first content slide with the hook folded in as a coral header band (e.g. "10 BUILDER OFFERS. NC + SC.").
  - Slide 10 = last content slide with the compact contact box folded in: Denise Wilson | REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / (blank) / Equal Housing Opportunity (firm line required since Oct 22 2026). (No 'Photos are illustrative' line, Denise Oct 15 2026.)
- Layouts by carousel:
  - New construction: slides 1-10 = 10 offer slides (one offer each). Hook band on offer 1, contact on offer 10. If fewer than 10 verified offers, slots 9-10 may be "How to compare offers" / "Why I recommend" content slides, still with contact folded into slide 10. Never pad with unverified offers.
  - Seller tips: slide 1 = hook band + first tip; slides 2-9 = tips and Redfin data; slide 10 = my recommendation + contact.
  - Neighborhood: slide 1 = hook band + where it sits; slides 2-9 = parks, dining, events, commute, home styles, prices (one source), etc.; slide 10 = my recommendation + contact.
- THEME (Oct 14, 2026, Denise approved): Neighborhood + Seller/Buyer tips use theme="fullbleed": photo fills the whole 1080x1350 slide, dark gradient fade toward the bottom + light top scrim, white text with shadow, coral accent words/tags/hook band, semi-transparent dark contact box on slide 10, h1 84px. Use photos >=1920px wide (Wikimedia Commons 1920px thumbs work). In build_slides.py:
    from carousel_style import slide as _slide, ul, build, short
    def slide(*a, **k): k.setdefault("theme", "fullbleed"); k.setdefault("h1", 84); return _slide(*a, **k)
  New construction: as of Oct 15, 2026 uses TEMPLATES/nc_style.py, palette "teal" (dark #0F4C5C / white / gold #F2B705) — see NEW CONSTRUCTION below. Optional palette swaps exist (palette="teal|turquoise|royal|emerald|plum|terracotta") but are not approved.
  Reference: 2026-10-14-neighborhood-noda/.
- Style (navy default): navy #0E1E3D, panel #182D57, coral #FF6A3D, Anton/Montserrat/Inter; nothing under 30px; NO "Illustrative image" labels (Denise Oct 15 2026); no builder photos.
- Social slide 1 footer may show "1 / 10 · SWIPE →"; video copies (slide-NN-video.png) and the Short never contain "swipe".
- Build with TEMPLATES/carousel_style.py: build() asserts 10 slides, band on slide 1, contact on slide 10, and min 30px bullet text; short() makes the 1080x1920 Short.
- Instagram caption: no email address (Buffer turns "@gmail.com" into a mention). Captions must say the real slide/offer count.
- Reference example: 2026-10-14-new-construction-carousel/10-slide/.

## NEW CONSTRUCTION (effective Oct 15, 2026, Denise picked palette 1)
- Build with TEMPLATES/nc_style.py: PALETTES["teal"] (dark #0F4C5C, light #FFFFFF, accent gold #F2B705). Reference build: 2026-10-15-new-construction-carousel/build-teal/build_slides.py.
- Layout: tag top-left "NEW BUILD DEALS / <REGION>" with gold underline (use "CHARLOTTE METRO" only if every offer is in the metro; else "NC + SC"); counter pill top-right "x/10"; huge Anton headline (community name); builder · city line; gold offer line; checkmark bullets; photo in lower half fading into background; footer "LIFESTYLE INTERNATIONAL REALTY CAROLINAS / EQUAL HOUSING OPPORTUNITY" + "SWIPE →" (carousel only, never in -video copies or the Short).
- Alternate light (odd) / dark (even) slides.
- 10 slides: 1 cover ("N new-build deals. Verified <Mon DD>." + 1-2 how-to-compare bullets), 2-9 one verified offer each, 10 contact: headline "Want the homes that qualify? Let's match you to the deal." + box 'DM or comment "DEALS" and we'll get started.' + Denise Wilson, REALTOR® · 704-615-7347 · denise.realty1@gmail.com · denisewilson.lircarolinas.com + "Offers verified on builder websites <date>. Terms can change." Fewer than 8 offers: fill with comparison/tip slides, never unverified offers.
- Real dates only (never "this week").
- PHOTOS (Denise, Oct 15 2026): builder's own photo ONLY, from its community/plan pages, credited "Photo: <Builder>". NO stock, Unsplash or "Illustrative image". Try hard: og:image first; if the page is JS-rendered, use `google-chrome --headless=new --dump-dom --virtual-time-budget=15000 <url>` and pull img src (Pulte = res.cloudinary.com/.../picturepark; Smith Douglas & Mungo = dlqxt4mfnxo6k.cloudfront.net, edit the trailing size e.g. /1600/1060). If none usable: img=None -> clean bold text-only slide. Cover = a credited builder photo from one of the offers, or text-only. nc_style.page() asserts the credit.
- Short: 1080x1920, slide-NN-video.png, padded with #0F4C5C. IG caption: no email.

## TIPS (Denise, Oct 15 2026)
- theme="fullbleed" in carousel_style.py. No "Illustrative image" labels; no "Photos are illustrative". Source line ONLY on the market-data slide. Contact = left-aligned CONTACT block.

## NEIGHBORHOOD SPOTLIGHT (effective Oct 15, 2026 afternoon — Denise)
- Build with TEMPLATES/nc_style.py: PALETTES["teal"] (dark #0F4C5C, light #FFFFFF, accent gold #F2B705). Alternate light (odd) / dark (even).
- Layout: tag top-left "NEIGHBORHOOD SPOTLIGHT / CHARLOTTE NC" with gold underline; counter pill "x/10"; huge Anton headlines; gold accent words; checkmark bullets; photo in lower half fading into background; footer brand + "SWIPE →" (carousel only, never in -video copies or the Short).
- Photos: free-license real neighborhood photos (Wikimedia Commons preferred), credited on-slide "Photo: <Author> (License)". NO stock, Unsplash, or "Illustrative image" labels. Try for 2000px+ sources, cover-crop to 1080x1350.
- Source/citation line ONLY on the market-data/prices slide. Keep full sources in the .md.
- Slide 10 contact: nc_style.CONTACT_BLOCK — left-aligned, one item per line: Denise Wilson | REALTOR® / denisewilson.lircarolinas.com / 704-615-7347 / (blank) / Equal Housing Opportunity. No email, no "— Carolinas", no "Photos are illustrative".
- Short: 1080x1920, slide-NN-video.png, padded with #0F4C5C. No SWIPE. IG caption: no email; credit Wikimedia in captions when required by license.
- Tips carousels stay on carousel_style.py theme="fullbleed" unless Denise says otherwise.
- Contact box (default CONTACT in carousel_style.py, Oct 15 2026): LEFT-aligned block (just inside the coral bar), one item per line, >=30px:
  Denise Wilson | REALTOR® / denisewilson.lircarolinas.com / 704-615-7347 / (blank line) / Equal Housing Opportunity. No email, no '— Carolinas'.

## NEW CONSTRUCTION: GEOGRAPHY + VERIFICATION (Denise, Oct 16 2026)
- Deals must be in the Charlotte metro ONLY. In SC, only Indian Land, Lancaster, York and Clover. No Fayetteville, Raleigh/Clayton, Columbia, Summerville/Charleston, etc.
- Anything not verifiable is not posted: no specific address, price or home unless the builder page confirms that exact home qualifies for the offer. If unsure, show only the verified community-level offer.

- (SUPERSEDED Oct 22 2026: the firm line IS required now, see COMPLIANCE + CONTACT BLOCK) Contact block (Denise, Oct 16 2026): NO 'Lifestyle International Realty' line under her name. All carousels: Denise Wilson | REALTOR® / denisewilson.lircarolinas.com / 704-615-7347 / (blank) / Equal Housing Opportunity. Left-aligned.

## (SUPERSEDED Oct 16 by photo_top) theme="fullbleed_lux"
- carousel_style.slide(..., theme="fullbleed_lux"); short(..., pad="0F4C5C"). Reference: 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py.
- Bright full-bleed photo, NO overall darkening: soft teal fade on the bottom ~60% only, behind the text. Teal #0F4C5C tags/panels, gold #F2B705 highlights, band and bullets. White text on the fade. No coral.
- PHOTO QUALITY RULE: bright, crisp, high-res (source >=2000px wide), high-end real estate only: sunlit luxury kitchens, staged living rooms, elegant baths, manicured exteriors, twilight exteriors. Free license only (Unsplash/Pexels license, CC0, or CC BY with a small on-slide credit). Reject anything dim, cluttered, low-res, dated or showing people. Match each photo to its slide topic. Review every slide: would a luxury brokerage post it? If not, swap the photo.
- No "Illustrative image" labels. Source line only on the market-data slide. Slide 10 = left-aligned CONTACT block (no brokerage line).

## (SUPERSEDED by photo_top_noir) theme="photo_top"
- Photo on the top ~50-56% (ph≈680-760; 640 for long-text slides), shown clean: NO overlay, tint or fade. Solid white text panel below (ct = ph+40), no overlap.
- Dark teal #0F4C5C headline (Anton), gold #F2B705 highlight under accent words and gold bullets, dark gray (#3A4148) body, small teal tag with gold underline. Slide 1 hook band: teal with gold accent words.
- Stats/market slide has NO photo: add carousel_style.PHOTO_NONE to inner; white page, big teal numbers, gold labels, a short takeaway line, source line at the bottom (the only slide with a source line).
- Slide 10: photo on top + recommendation + left-aligned CONTACT block (no brokerage line) in the white panel.
- Text >=32px body where it fits; check every slide for crowding or big empty gaps. Photo quality rule (above) still applies; swap any photo that looks weak shown uncovered.
- Short: short(..., pad="FFFFFF"). Reference build: 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py.

## (SUPERSEDED) theme="photo_top_noir" (Denise picked black + orange, Oct 16 2026; replaces photo_top white)
- photo_top layout: clean photo on top (no overlay), rich black #111 panel below, ivory #F5EFE3 headline, bright body #E6E0D6, burnt-orange/copper #D9773A accents (accent words, hook band, bullets, tag underline, thin line at the photo edge, footer). No white panels, no teal/gold.
- Stats slide: PHOTO_NONE; black page, big ivory numbers, orange labels, takeaway, source line (only slide with one).
- Slide 10: photo + recommendation + left-aligned CONTACT block (Denise Wilson | REALTOR® / denisewilson.lircarolinas.com / 704-615-7347 / blank / Equal Housing Opportunity).
- Photos: magazine-quality luxury (Unsplash/Pexels), pre-cropped wide to the photo area, premium lens grade (slight warmth, +5-7% contrast, -3-5% saturation, sharpen); no people or framed portraits, nothing dated or apartment-grade. short(..., pad="111111"). Reference: 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py.

## TIPS DEFAULT = theme="fullbleed_tips" (Denise Oct 16 2026; replaces photo_top_noir/photo_top/fullbleed_lux)
- Exact Oct 14 NoDa fullbleed format and colors (full-page photo, coral #FF6A3D tag/band/accent words/bullets, white text with shadow, navy #0E1E3D base).
- Photos are the focal point: minimal fade (light top scrim for the tag, dark gradient only in the bottom ~45%). On a very bright photo, a slide may start the gradient a little higher.
- Text block is BOTTOM-ANCHORED (.c bottom:96px), ending just above the footer; the photo fills the top. Never start text mid-slide with empty space below.
- Photos: crisp luxury homes, Charlotte-area where possible (Wikimedia Commons Myers Park/Dilworth/Elizabeth etc., CC0/PD/CC BY*, credit on slide when required, top-right 30px), otherwise Unsplash/Pexels interiors. No people. Light grade (+5% contrast, sharpen).
- Stats slide: FB_STATS (no photo, navy #0E1E3D page, big numbers, source line; only slide with a source).
- Slide 10: CONTACT block, left-aligned (Denise Wilson | REALTOR® / denisewilson.lircarolinas.com / 704-615-7347 / blank / Equal Housing Opportunity).
- short(..., pad="0E1E3D"). Reference: 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py.

## NEIGHBORHOOD DEFAULT = theme="fullbleed_tips" (Denise Oct 16 2026; replaces nc_style teal/gold for neighborhood)
- Same full-photo style as the approved seller tips (commit 9708bcd): full photo on EVERY slide, minimal fade, bottom-anchored text, NoDa coral/navy colors.
- Stats slide KEEPS a photo but uses a strong fade (see STRONG in 2026-10-16-neighborhood-plaza-midwood/build/build_slides.py) so numbers stay readable; source line only there.
- Photos: crisp, beautifully lit, full-res (never upscaled), light grade + sharpening. Real photos of the place if they're stunning (credit on-slide when license requires); otherwise a stunning Charlotte or topic photo that is never captioned or implied to be a specific place it isn't. No people as the focus.
- Slide 10: CONTACT block, left-aligned, no brokerage line. short(..., pad="0E1E3D").

## NEIGHBORHOOD = full-photo layout in TEAL/GOLD: theme="fullbleed_teal" (Denise Oct 16 2026; supersedes the coral/navy note above for neighborhood)
- Same full-photo, bottom-anchored layout as fullbleed_tips, recolored: gold #F2B705 hook band, accent words, bullets; teal #0F4C5C tag, fade tint, stats panels; white text. Lighter fade so photos stay clean.
- Stats slide: photo + TEAL_STRONG fade. Short pad="0F4C5C". Photo grade: clean-white autocontrast blend, gentle contrast, slight warmth, unsharp; full-res originals resized down only.
- Reference: 2026-10-16-neighborhood-plaza-midwood/build/build_slides.py.
