# Buyer & Seller Tips — Signature Authority (v2, Oct 31 2026)
Denise's design. Match her example slides in `TEMPLATES/signature-authority-examples/` (10 x 4:5 examples incl. cover + Let's Talk,
the template guide `01M69GSVS8MQX2QDJ5K4ZNG71K.png`, and her real-headshot 1:1 slide `01M69GT5HEGMY2SCQ8B8KKJKS7.png`).
Original template sheet: `TEMPLATES/signature-authority-template.png`. Renderer: `TEMPLATES/signature_authority.py` (v2).
Worked example: `2026-10-31-buyer-tips-title-and-survey/build/build_slides.py`.
v1 (even charcoal overlay, sage text, 1:1 + 9:16) was replaced Oct 31 2026 because Denise wanted it closer to her examples.

## Look (4:5 1080x1350)
- Photo: warm, sunlit, golden, vivid lifestyle photo (living rooms, kitchens, desks with a model house and keys, a calculator, porches). Grade `warm()`: lift + golden balance + saturation. Never dim; swap dim photos.
- Overlay: ONLY a left navy (#0E3042) gradient behind the text (≈.93 at the left edge → clear by ~75% width), a light top fade, and a navy fade at the bottom for the footer. No even dark overlay.
- Tag pill top-left: `BUYER TIP` sage (#A9C9B8) with navy text / `SELLER TIP` coral (#E38B6C), Montserrat Bold ~38px.
- Headline: Anton, ~92px, all caps; line 1 white, line 2 coral (`"Line one|line two"`).
- Body: Montserrat Medium ~33px, 1-2 sentences, max ~600px wide.
- Bullets: exactly 4 short lines (≈ ≤30 characters, one line each), Montserrat SemiBold ~32px, big filled coral check bubbles (52px). Sage bubbles are an option on buyer slides (`bubble=` per slide).
- Footer every slide: short coral rule + `BUYER & SELLER TIPS` left, `N / 10 →` right.
- Margins ~58px left/right (as in the examples).

## Slide types
1. `sa.cover`: navy box top-left "BUYER & SELLER TIPS / CHARLOTTE METRO • NC + SC"; bold Anton lead ~104px (e.g. "REAL ESTATE" or today's topic "KNOW WHAT YOU'RE"); big coral script line (Great Vibes; "Tips" / "really buying"); "Practical advice for BUYERS / SELLERS"; bottom-left "DENISE WILSON / BROKER/REALTOR® | LIFESTYLE INTERNATIONAL REALTY"; "1 / 10 →".
2. `sa.stats`: stats only on navy (no photo), Realtor.com metro numbers with month + source line.
3-9. `sa.edu`: tag + 2-line headline + 1-2 sentence body + 4 bullets over a warm photo.
10. `sa.cta`: "LET'S TALK / BUYING OR SELLING? I'M HERE TO HELP." + coral script "Denise Wilson", Broker/REALTOR®, Lifestyle International Realty — Carolinas, 704-615-7347, denisewilson.lircarolinas.com, Equal Housing Opportunity logo + text. Denise's REAL headshot on the right (`TEMPLATES/denise-wilson-headshot-cutout-hires.png`, cut out with rembg u2net_human_seg + edge cleanup from the hi-res portrait she sent Oct 31; crop of only her, branding excluded: `denise-wilson-headshot-hires-crop.png`; placed `right:-60px; bottom:0; height:1000px`) over a bright, warm, blurred living room. The source portrait has "DW AI COMPANION" text, a robot, a "DENISE AI STRATEGIST" nameplate, mug and notebook: never let any of that show; always use the crop/cutout. The older low-res `denise-wilson-headshot-cutout.png` / `-crop.png` (from her 1:1 example) are superseded. Never generate or alter her face; never use the woman in the 4:5 example (may be AI-generated).

## Sizes
- v2 lays out 4:5 only (slide-NN.png, PDF, slides.zip). After Denise approves the design, add 1:1 (Facebook) and, when she asks, 9:16 (TikTok, safe zones: top 150, bottom 250, right 120) in the same look.

## Rules
Photos: no people as the subject, no house numbers/signs, check `photo_registry.py check` (and the Pexels ±500 id rule), register after build. Compliance: TEMPLATES/COMPLIANCE.md + compliance_check.py (no guarantees/urgency; sourced, dated numbers; firm name, phone and EHO on slide 10).

Title on slides (Denise, Oct 31 2026): always "Broker/REALTOR®" (cover byline in caps "BROKER/REALTOR®", slide 10 card "Broker/REALTOR®"), matching the caption signature.
