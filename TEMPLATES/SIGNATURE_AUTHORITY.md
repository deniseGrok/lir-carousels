# Buyer & Seller Tips — Signature Authority (Denise's design template, received Oct 31 2026)
Reference sheet: `TEMPLATES/signature-authority-template.png`. Renderer: `TEMPLATES/signature_authority.py` (theme name `signature_authority`).
First used: `2026-10-31-buyer-tips-title-and-survey/` (see its `build/build_slides.py` as the worked example). Use for all future buyer/seller tips days.

## Colors
- Deep Navy `#0E3042`: primary, footer rule, stat cards, contact icons, tag text
- Soft Teal / Sage `#9BB7AE`: BUYER tags, accents, sub-labels
- Coral-Copper `#E38B6C`: SELLER tags, highlight words, check-circle icons, script accents, page arrow
- Warm White `#F5F3EE`: contact card / clean backgrounds
- Charcoal overlay `#11212A`: 60-80% over full-bleed photos where text sits, fading lighter over the open photo so it stays bright

## Typography
- Series tag pill, top-left: Montserrat SemiBold, all caps (`BUYER TIP` teal pill / `SELLER TIP` coral pill; slide 10 uses `LET'S TALK`)
- Headline: Bebas Neue, all caps, white; highlight words in coral (markup `[[words]]`, `|` = line break)
- Body: Montserrat Regular, sentence case, 1-2 sentences
- Bullets: 3-4, Montserrat Medium, coral check-circle icons
- Script accent: Great Vibes, coral (cover "Tips"-style line, name on contact card)
- Footer on every slide: `BUYER & SELLER TIPS` left, `N / 10 →` right, Montserrat SemiBold, teal hairline above

## Formats (standing rules)
- 4:5 1080x1350 -> `slide-NN.png`, PDF, `slides.zip` (Instagram + LinkedIn); ~110-120px safe margins
- 1:1 1080x1080 -> `slides-1x1/`, `slides-1x1.zip` (Facebook)
- 9:16 1080x1920 -> `slides-9x16/`, `slides-9x16.zip` ONLY when Denise asks (TikTok; first requested Oct 31 2026). TikTok safe zones: top 150+, bottom 250+ (footer sits at 262), right 120+ (140 used)

## Slide types
1. Cover (`sa.cover`): bold Bebas lead + coral script line + "Practical advice for BUYERS/SELLERS" + optional outlined topic kicker
2. Stats (`sa.stats`): Realtor.com metro numbers with month + source line; photo behind 80% charcoal
3-9. Educational (`sa.edu`): headline + 1-2 sentence copy + 3-4 bullets
10. CTA (`sa.cta`): "LET'S TALK" + Warm White contact card: Denise Wilson (script), BROKER/REALTOR®, Lifestyle International Realty — Carolinas, 704-615-7347, denisewilson.lircarolinas.com (her established web address, used on prior slide 10s), Equal Housing Opportunity + EHO house icon. No headshot is on file: use a bright interior photo, never a generated/fake person. If Denise supplies a real headshot, add it to the card.

## Photography
Bright, natural light, warm, uncluttered, never dark; no people/demographics; homes, interiors, exteriors, details. Check every photo in `TEMPLATES/photo-registry.csv` (photo_registry.py check) and register after build. Graded per format from build/src originals (downscale only).

## Compliance
NC/SC Real Estate Commission + Fair Housing (TEMPLATES/COMPLIANCE.md, compliance_check.py): no guarantees/urgency, sourced and dated numbers, no "swipe" on 9:16, firm name + phone + EHO on slide 10.
