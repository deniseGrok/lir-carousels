# Community Spotlight — Modern Charlotte Editorial (Denise's design, in use from Nov 1 2026)
Design reference: `TEMPLATES/community-spotlight-modern-editorial/reference-sheet.png` + `example-01..08.png` (commit dd5bef1).
Renderer: `TEMPLATES/modern_editorial.py`. First worked example: `2026-11-01-neighborhood-matthews/build/build_slides.py`.
Applies ONLY to the Neighborhood / Community Spotlight carousel (replaces fullbleed_teal there). New Construction uses Bright Contemporary;
Buyer/Seller Tips use Signature Authority.

## Palette
Deep Teal #183C46 (pills, gradients, footer) · Terracotta #C66C4E (highlight words, bullets, footer panel) · Warm Ivory #F5F0E8 (headlines/text) ·
Charcoal #293338 (contrast) · thin gold edge #D9A84E (pill border, CTA card bar, swoosh start).

## Type (sizes for 1080 width)
- Playfair Display Black Italic, ALL CAPS headlines ~88-110 px (4:5 100, 1:1 88, 9:16 110); highlight words `[o]..[/o]` get a warm
  orange-to-terracotta fill; thin gold-to-terracotta swoosh under every headline.
- Montserrat: section pill 26-30 px ExtraBold; body/bullets 27-33 px Medium; stat values 76-88 px ExtraBold; footer 23-25 px ExtraBold.
- Cover: "Discover" Playfair SemiBold Italic + neighborhood name Playfair ExtraBold (~134-164 px, auto-fit to one line), terracotta italic
  three-word tagline, one-line intro, DENISE WILSON / Broker/REALTOR® | LIFESTYLE INTERNATIONAL REALTY, "1 / 10 →" (no footer bar, as in the sheet).
- Headline auto-fit: the JS fitter shrinks the headline to its max lines (2 by default; `lines`, `lines_<fmt>`), then shrinks body text until the
  block clears `minTop` (fraction of height) so it never collides with the pill. Card text on slide 10 shrinks until it clears the headshot.

## Layout
- Full-bleed bright photo on every slide (no photo credits: images are original GenerateImage illustrations).
- Rounded deep-teal section pill top-left with a thin gold edge (THE ORIGINS, THE RAILROAD, THE MARKET, THE PARK, MY TIP, THE MARKET,
  MY RECOMMENDATION...). Cover pill: terracotta pin + COMMUNITY SPOTLIGHT / CHARLOTTE METRO • NC + SC.
- Text bottom-left over a deep-teal gradient (starts at `g0`: 4:5 .40, 1:1 .30, 9:16 .36; stats .16, CTA .22).
- Exactly 3 terracotta square bullets per info slide.
- Footer bar: deep teal with gold hairline, NEIGHBORHOOD SPOTLIGHT left; terracotta panel with two diagonal stripes on the right holding "N / 10".
- Slide 9: kicker "REALTOR.COM • ZIP ##### • MON. YYYY", headline, four translucent teal stat cards (median list price, price per sq. ft.,
  active listings, median days on market), source line with month + viewed date. Realtor.com numbers ONLY here.
- Slide 10: "LET'S TOUR IT / TOGETHER." + one-line plan, left contact card with gold bar: Denise Wilson | Broker/REALTOR® /
  Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / (gap) / EHO icon + Equal Housing Opportunity;
  hi-res headshot `TEMPLATES/denise-wilson-headshot-cutout-hires.png` on the right, standing on the footer. Title is ALWAYS Broker/REALTOR®.
- Margins: 42-56 px sides, pill 34-40 px from top (4:5/1:1).

## Formats
| fmt | size | notes |
|---|---|---|
| 4x5 | 1080x1350 | Instagram (Buffer) + PDF |
| 1x1 | 1080x1080 | Facebook Page (Buffer) |
| 9x16 | 1080x1920 | TikTok: pill at 166 px, footer bar sits 350 px above the bottom, text right edge 150 px in |
| 9x16v | 1080x1920 | YouTube Short frames only (temp): COMMUNITY SPOTLIGHT / <place> header at y=262, pill at 380, footer 420 px up, right 150 px |

## Images (generated)
- Prompt each slide's scene in 3:4 portrait (subject in the upper 55%, calm lower 40%, nothing key near the side edges), bright golden hour,
  blue sky, lush greenery + flowers, magazine quality; no readable text/signs/logos/house numbers, no palms/Spanish moss/ocean; people only
  incidental, varied, never stereotyped, never implying who an area suits (Fair Housing). Never present an image as a specific real house,
  listing, address, business or landmark: pills name topics, not places pictured.
- `me.upscale(raw, up)` = Real-ESRGAN x4 (`TEMPLATES/tools/esrgan_upscale.py`, /workspace/models/RealESRGAN_x4plus.fp16.onnx), then
  `me.prep_photo(up, png, fmt, x, y)` crops at the focal point, Lanczos to full res and applies `crisp()` (levels, exposure + shadow lift,
  clarity, vibrance, warmth, fine unsharp mask). Photo saved lossless; text layer rendered at 2x (transparent, CDP) and composited.
- Register every raw, upscaled source and slide render in TEMPLATES/photo-registry.csv (both copies); never reuse an image.
- Inspect every slide in every size at full size; regenerate dull/soft/odd images.

## Rendering
`me.render(slide, out_png, fmt, n, total, photo_png, html_dir)` writes `<fmt>-slide-NN.html` (compliance_check.py scans `build/*.html`) and the PNG.
Uses headless Chrome over CDP (`/workspace/tools/cdp.py`, port 9333) and fonts from /usr/share/fonts/truetype/sand-box/google (Playfair Display,
Montserrat variable TTFs, loaded with @font-face).
