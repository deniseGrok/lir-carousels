# New Construction — Bright Contemporary (Denise Wilson, approved Oct 31, 2026)
Applies ONLY to the daily New Construction Deal Carousel (from Nov 1, 2026). Buyer/Seller Tips use Signature Authority; Neighborhood/Community Spotlight has its own design.
Reference: `new-construction-bright-contemporary/reference-sheet.png` (design system) and `example-01..10.png` (Denise's restyle of the Oct 31 Eastwood carousel, commit 96e7ec2). Open them at full size before every build.
Renderer: `bright_contemporary.py` (HTML/CSS rendered through /workspace/tools/cdp.py headless Chrome). First used: 2026-11-01-new-construction-carousel.

## Palette and type
Deep Navy #0B2E3A (tag, credit pill, gradient, contact card) · Teal/Aqua #0E7C8A · Golden Yellow #FFD200 (key number/word, check icons, tag underline, card bar) · White #FFFFFF · Charcoal #1B2A30 · Coral/red location pill (#E8412F→#F25C3A).
Headline: Anton, all caps, white, key number or word in yellow (`[y]…[/y]`), 1–2 lines. Everything else: Montserrat (800 for tag, pills, supporting line, footer; 600 for bullets; 500 for the disclaimer).

## Elements on every slide
- Top-left navy series tag "NEW BUILD DEALS / NC + SC" with a yellow underline; top-right small navy pill "Photo: <Builder>".
- One bright builder hero photo in the upper photo zone (4:5 80%, 1:1 92%, 9:16 62% of the height) with a Deep Navy gradient over the lower half; the zone fades into navy so landscape photos are not over-zoomed.
- Location pill (coral, white all-caps "<COMMUNITY> • <CITY>, NC"); cover uses a yellow pill ("NEW BUILDS. VERIFIED <DATE>."); tips use "TIP • BEFORE YOU SIGN"; comparison uses "COMPARE • …".
- Oversized headline, short white supporting line ("<Builder> • select homes"), 3 bullets with round yellow check icons, small disclaimer line.
- Bottom-left "NEW CONSTRUCTION", bottom-right "N / 10". Diagonal coral/orange, yellow and teal stripe accents in the top-left and bottom-right corners.
- Never print "One community per slide" and no "SWIPE" text on slides. Exactly 10 slides.
- Slide 10: "DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", a help line, "Builder incentives can change; verify with the builder.", and the navy contact card with a yellow left bar: Denise Wilson | Broker/REALTOR® / Lifestyle International Realty — Carolinas / denisewilson.lircarolinas.com / 704-615-7347 / (blank) / Equal Housing Opportunity. Her title is always Broker/REALTOR®.

## Sizes (native layouts, never cropped or padded from another size)
| fmt | px | use | notes |
|---|---|---|---|
| 4x5 | 1080x1350 | Instagram (slides/ root + slides.zip + PDF) | |
| 1x1 | 1080x1080 | Facebook Page + personal profile (slides-1x1/ + slides-1x1.zip) | smaller type |
| 9x16 | 1080x1920 | TikTok (slides-9x16/ + slides-9x16.zip) | text kept clear of TikTok UI: top 160 px, bottom 360 px, right 150 px |

## API
```python
import sys; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import bright_contemporary as bc
r = bc.prep_photo("src/x.jpg", "img45/01.jpg", "4x5", fx=.5, fy=.5)   # crop + grade; ESRGAN (tools/esrgan_upscale.py) when the source must be scaled >1.5x
bc.render(slide, "img45/01.jpg", "../slide-01.png", "4x5", 1, 10, html_dir=".")
```
`slide` dict: kind ('cover'|'deal'|'compare'|'tip'|'cta'), credit (builder name), pill, h1 (`[y]..[/y]` = yellow, `|` = forced line break), sub, body, bullets (3), note (disclaimer), optional long/h1size/h1_<fmt>/h1size_<fmt>/fy/fx.
Grade: autocontrast blend 0.5, brightness +4%, contrast +7%, saturation +20%, UnsharpMask radius 1.1 (no halos). Photos stay the builder's real photos; only house numbers may be retouched out (see the day's build_slides.py FIX list).
Build scripts write the HTML into build/ (compliance_check.py scans build/*.html).

## Photo rules
Credited builder photos only, the crispest and brightest available; never AI-generated or altered homes; no visible house numbers; never reuse a photo (photo_registry.py check before, registry rows after). If a builder has no usable photo, render the slide on solid navy/teal.
