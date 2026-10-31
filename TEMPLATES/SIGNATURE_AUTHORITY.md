# Buyer & Seller Tips — Signature Authority (v2, Oct 31 2026)
Denise's design. Match her example slides in `TEMPLATES/signature-authority-examples/` (10 x 4:5 examples incl. cover + Let's Talk,
the template guide `01M69GSVS8MQX2QDJ5K4ZNG71K.png`, and her real-headshot 1:1 slide `01M69GT5HEGMY2SCQ8B8KKJKS7.png`).
Original template sheet: `TEMPLATES/signature-authority-template.png`. Renderer: `TEMPLATES/signature_authority.py` (v2).
Worked example: `2026-10-31-buyer-tips-title-and-survey/build/build_slides.py`.
v1 (even charcoal overlay, sage text, 1:1 + 9:16) was replaced Oct 31 2026 because Denise wanted it closer to her examples.

## Look (4:5 1080x1350)
- Photo: crystal-clear, vivid, golden-hour/sunlit photo (Denise Oct 31 2026: "dull" → match `signature-authority-examples/brightness-reference-2026-10-31/example-01..10.png`). Pick highest-res originals (ideally 4000px+), sharp subject, warm light, glowing windows, nothing grey/hazy/flat; subject on the RIGHT half and a darker or mid-tone left side so the text sits on it. 4:5 grade `crisp()` at final size: Lanczos downscale → levels stretch → exposure + shadow lift → clarity (large-radius local contrast) → vibrance → golden warmth → fine unsharp mask (threshold 3, no halos); photo saved lossless as `build/img/NN.png`. Per-slide tweaks: `crisp=dict(expo=, shadows=, warmth=, vib=, contrast=)` (e.g. warmth=.25 on a pale blue sky so it doesn't turn mint).
- Text crispness (4:5 photo slides): the text + gradient layer is rendered at 2x on a transparent page, Lanczos-downscaled and composited over the graded photo. PDF is lossless (img2pdf) when installed.
- Overlay (4:5 `BRIGHT` css): ONLY a soft left navy (#0E3042) band behind the text: .84 at the left edge → .44 at 40% → .14 at 50% → clear by 57%, so the right ~43% of the photo is untouched; no top fade; a short navy fade (240px) at the bottom for the footer; subtle text shadow on headline/body/bullets/footer. Cover: soft radial navy glow behind the title block + light left band. No even dark overlay, no grey veil. Per-slide override: `css_4x5=".gl{...}"`. (1:1 / 9:16 still use the earlier overlay and `warm()` grade until Denise approves the bright 4:5 look.)
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

Sizes (Denise approved the design Oct 31 2026): `sa.build(..., fmt="4x5" | "1x1" | "9x16")`. 4x5 1080x1350 Instagram (`slide-NN.png`, PDF, `slides.zip`);
1x1 1080x1080 Facebook Page (`slides-1x1/`, `slides-1x1.zip`, `<name>-DRAFT-1x1.pdf`); 9x16 1080x1920 native TikTok (`slides-9x16/`, `slides-9x16.zip`,
`<name>-DRAFT-9x16.pdf`), with text kept out of the TikTok UI zones (top 150, bottom 350, right 140; footer at bottom 360 / right 160; Denise's face kept left of x 940).
Size layouts live in `OVR` in the renderer. Per-slide tweaks: `xy_1x1` / `xy_9x16` and `css_1x1` / `css_9x16`. Captions: TEMPLATES/CAPTION_FORMAT.md.

## Custom generated images (Oct 31 2026, Denise approved)
Allowed for photo slides when stock is dull: GenerateImage prompts for ultra-sharp, photorealistic, bright golden-hour magazine light, subject on the RIGHT with a calm, simple left side (dark foliage or soft wall) for the text, Carolinas-plausible (no palms, Spanish moss or ocean), no readable text, logos, signs or house numbers. People only incidental (from behind, hands), never implying who a home is for and never posed as a client or as Denise. Inspect at full size and regenerate on artifacts. Raw output is 864x1152 (3:4): keep it as build/src/gen-NN-raw.jpg, upscale 4x with Real-ESRGAN x4plus (ONNX at /workspace/models/RealESRGAN_x4plus.fp16.onnx, script TEMPLATES/tools/esrgan_upscale.py, blend 80/20 with Lanczos) to build/src/gen-NN.jpg, then render with a gentler grade (crisp=dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)). Record them in CREDITS.txt and the carousel notes as custom-generated illustrative images (not a specific property; no on-slide label), and register them in photo-registry.csv with provider "generated".

Other sizes (Oct 31 2026): pass bright_all=True on a photo slide to give 1:1 and 9:16 the same bright finishing as 4:5 (OVR size layout + BRIGHT_FMT gradients; 9:16 uses a soft ellipse behind the text block since the text runs ~85% wide). Set xy_1x1 / xy_9x16 focal points per slide (3:4 generated images: 9:16 keeps only the middle 75% of the width, so x≈.72-.95 keeps a right-side subject). 9:16 CTA slide hides the page counter (it sat on Denise's blazer).
