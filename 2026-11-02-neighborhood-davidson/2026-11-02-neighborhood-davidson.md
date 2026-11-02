# Community Spotlight: Davidson, NC (ZIP 28036) — DRAFT, AWAITING DENISE APPROVAL
Built Mon Nov 2, 2026 (~4:40-5:15 AM ET). Second Community Spotlight in Denise's 'Community Spotlight — Modern Charlotte Editorial' design
(TEMPLATES/modern_editorial.py + TEMPLATES/MODERN_EDITORIAL.md; worked example 2026-11-01-neighborhood-matthews). Nothing posted or scheduled.
On approval: Buffer 4:00 PM ET, Instagram 4:5 (slide-01..10.png), Facebook Page 1:1 (slides-1x1/), TikTok 9:16 (slides-9x16/).

## STATUS
DRAFT — AWAITING DENISE APPROVAL. All 10 ORIGINAL images generated Nov 2, 2026 with GenerateImage from build/IMAGE_PROMPTS.md (in prompt order,
none regenerated); raw outputs build/src/gen-01..10-raw.jpg (864x1152, 3:4), Real-ESRGAN x4 (TEMPLATES/tools/esrgan_upscale.py) ->
build/src/gen-NN.jpg (3456x4608), then crop + crisp() grade/unsharp per size (build/img4x5, img1x1, img9x16). All three sets, PDF, zips and the
silent Short are built; every slide in every size was inspected (full slides + native-resolution crops). No image was unusable after cropping;
no stock used.
- Layout fixes after inspection: slide 10 body copy lengthened so it wraps clear of the headshot in 4:5 and 1:1 (the shorter line ran into her
  hair in 4:5); slide 3 1:1 focal point lowered (xy_1x1 .5,.85) so the campus building shows above the headline; text gradient started higher
  on slides 4 (g0 .32), 5 (.30) and 8 (.26) because the ivory headline sat on bright white siding/sky in 9:16.
- Image notes: slide 7 kayaks sit in the lower part of the image, so they read only faintly through the text gradient in every size (the pier
  and lake carry the slide); slide 2 and slide 7 are both lake-and-dock scenes; slide 4 farmhouse with a cottage on the right; slide 9 aerial
  with the lake on the horizon; slide 10 large oak on the right half behind the headshot.
- Slide 3 shows a generic red-brick columned building with a cupola. It is an illustration, not Davidson College's actual campus; the pill
  names the topic only.
- photo_registry check: weak perceptual-hash "possible matches" only (closest zone dist 11, gen-02 vs a 2026-10-15 new-construction image that
  is no longer in the working tree); all 10 are brand-new GenerateImage outputs, so treated as false positives (same as Matthews Nov 1).

## Deliverables
- slide-01..10.png 1080x1350 (4:5) + slides.zip (21.1 MB) + 2026-11-02-neighborhood-davidson-DRAFT.pdf (21.1 MB, lossless img2pdf)
- slides-1x1/ 1080x1080 + slides-1x1.zip (16.8 MB); slides-9x16/ 1080x1920 + slides-9x16.zip (26.7 MB) + slides-9x16-jpg.zip (8.1 MB, because
  the PNG zip is over 25 MB)
- youtube-short.mp4: 1080x1920 H.264 full screen, 43.0 s (9 x 4.6 s + 7.0 s end hold on the contact slide, 0.6 s crossfades, 1.03 slow push-in),
  45.8 MB, NO audio stream, header COMMUNITY SPOTLIGHT / Davidson · NC, never says swipe. youtube-caption.md has the title, description and tags.

## Slides
1 COVER: Discover Davidson · College. Lake. Greenway. · A college town on Lake Norman in northern Mecklenburg County, north of Charlotte.
2 THE LAKE — A TOWN ON LAKE NORMAN.: northern Mecklenburg County, a portion of the town extends north into Iredell County; western edge follows
  the shoreline of Lake Norman, a large reservoir on the Catawba River; an arm of the lake east of I-77 is known as Lake Davidson.
3 THE COLLEGE — THE COLLEGE CAME FIRST.: Davidson College opened in 1837, named for Revolutionary War Gen. William Lee Davidson; first 469 acres
  bought from his son, William Lee Davidson II; town incorporated as Davidson College in 1879, renamed Davidson in 1891.
4 THE HOMES — PORCHES AND OLD HOMES.: Davidson Historic District on the National Register in 2009; homes from Greek Revival and Queen Anne to
  Craftsman bungalows and 1950s modernist houses; Elm Row and Oak Row (1837 college dormitories) are the oldest buildings in the district.
5 THE TOWN GREEN — SATURDAYS ON MAIN STREET.: Town Green downtown on Main Street, library branch at 119 S. Main St.; Concerts on the Green
  second and fourth Saturdays in season, 6-8 p.m.; Davidson Farmers Market, 120 S. Main St., every Saturday through Nov. 21, 9 a.m.-noon.
6 THE GREENWAY — TRAILS THROUGH TOWN.: town greenways offer more than six miles of walkable space; sweetgum, tulip poplar, eastern red cedar
  line the 2.8-mile Randall R. Kincaid Trail; Abersham Park's paved greenway continues into 200-acre Fisher Farm Park (four miles of mountain
  bike trails).
7 LAKE ACCESS — PADDLE LAKE DAVIDSON.: two public lake-access parks, Parham Park and Lake Davidson Nature Preserve; preserve at 750 Jetton St.
  with a half-mile lakeside loop trail, picnic tables, gazebo, public launch; town canoe/kayak/paddleboard rentals April-October, Saturdays 2-5 p.m.
8 MY TIP — CHECK THE DISTRICT FIRST.: downtown, parts of the campus and North Main Street are in the local historic district; there many exterior
  changes need a Certificate of Appropriateness from the Historic Preservation Commission; National Register listing alone doesn't restrict
  private owners, so ask which district a home is in before you plan changes.
9 THE MARKET — REALTOR.COM • ZIP 28036 • SEPT. 2026 — WHAT HOMES LIST FOR.: $711,975 median list price · $327 price per sq. ft. · 112 active
  listings · 71 median days on market. Source line on slide: Realtor.com Economic Research, ZIP 28036 (Davidson NC) monthly listing data,
  September 2026; viewed Nov. 2, 2026.
10 MY RECOMMENDATION — LET'S TOUR IT TOGETHER.: "We'll walk Main Street and the Town Green, visit the lake preserve, and compare homes before you
  make an offer." (Short: "We'll walk Main Street and the lake, then compare homes before you make an offer.") + contact card (Broker/REALTOR®,
  firm, site, phone, Equal Housing Opportunity) + headshot.

## Sources (all fetched/verified Mon Nov 2, 2026, ~4:45-5:00 AM ET)
- Realtor.com Economic Research RDC_Inventory_Core_Metrics_Zip.csv (econdata.s3-us-west-2.amazonaws.com/Reports/Core/, Last-Modified
  Wed Sep 30 2026 14:41 GMT, latest month 202609), ZIP 28036 "davidson, nc", month 202609: median_listing_price 711975; median_listing_price_per_square_foot
  327; active_listing_count 112; median_days_on_market 71; quality_flag 0. ZIP 28036 also covers Davidson-addressed areas outside town limits.
- Wikipedia "Davidson, North Carolina" (geography): northern Mecklenburg, portion in Iredell County; western edge follows the Lake Norman
  shoreline, a large reservoir on the Catawba River; arm east of I-77 known as Lake Davidson (cites Town of Davidson Lake Davidson fact sheet).
  Town of Davidson Lake Davidson Nature Preserve page names the lake.
- Davidson College Library research guide "19th Century Davidson Buildings: Background" (davidson.libguides.com): 1835 Presbytery of Concord;
  Jetton Tract 269 acres + Linn Tract 200 acres bought from William Lee Davidson; began 1837; town incorporated as Davidson College 1879;
  renamed Davidson 1891. Davidson College Archives page: first students March 1837, town incorporated 1879. NRHP nomination (Mattson and
  Alexander 2008, text via livingplaces.com): 469 acres from William Lee Davidson II; college named for his father, Revolutionary War hero
  Gen. William Lee Davidson; Elm Row and Oak Row (1837) are the oldest properties; styles incl. Greek Revival, Queen Anne, Colonial Revival,
  Tudor Revival, Craftsman, Modernist (1950s Hillside Drive).
- Town of Davidson Historic Preservation page: National Register district designated 2009 (Wikipedia: added June 1, 2009, NRHP 09000381);
  local historic district = downtown, parts of the historic campus, North Main Street; Certificate of Appropriateness for many exterior
  changes reviewed by the Historic Preservation Commission; National Register listing "does not obligate or restrict a private owner".
- Town of Davidson Library page: Davidson branch on the town green at 119 S. Main Street. Town Concert Series page: Concerts on the Green, second
  and fourth Saturdays, 6-8 p.m., on the Town Green (2026 series; some dates on Sundays, hence "in season").
- Davidson Farmers Market Visit page: 120 South Main Street; 2026 prime season every Saturday April 4 - November 21, 9 a.m.-noon; winter
  season select Saturdays Dec 2026 - Mar 2027.
- Town of Davidson Greenways page: over six miles of walkable space; 2.8-mile Randall R. Kincaid Trail lined with sweetgum, tulip poplar,
  eastern red cedar. Abersham/Allison Park page: paved greenway continues into Fisher Farm Park. Fisher Farm page: 200-acre park, four miles of
  mountain bike trails.
- Town of Davidson Lake Access & Watercrafts page: two public lake-access properties (Parham Park, Lake Davidson Nature Preserve); rentals
  April-October, Saturdays 2-5 p.m. Lake Davidson Nature Preserve page: 750 Jetton St., Sterling Martin Trail (0.5 mile loop), picnic tables,
  gazebo, public lake access to launch personal watercraft.
- Cut: greenway mileage beyond "more than six" (town page says over six; the 2024 master plan says 9.12 miles), Presbyterian founding and all
  church history (Fair Housing), population/demographics, schools (incl. the school next to the preserve), mill history detail, Concerts @ the
  Circles, Christmas in Davidson, the Aug. rental hours, the watercraft rack lottery, the "historic districts appreciate faster" claim (town
  page, not a fact for a buyer slide), restaurants and shops (not verified today), distance to Charlotte (sources give 20-22 miles).

## Images
All 10 slides: ORIGINAL photorealistic generated illustrations (GenerateImage, generated Nov 2, 2026) of the kind of scene each slide describes.
No photo credits anywhere. Never labeled or presented as a specific real house, listing, address, business or landmark; topic pills only.
No readable signage, no palms/Spanish moss; people only incidental. Registered by build/finish.py in both photo-registry copies (provider
generated:GenerateImage, notes say the originals came from GenerateImage): 50 rows per copy (10 raw, 10 upscaled, 30 slide renders).

## Compliance check
TEMPLATES/compliance_check.py: slide HTML PASS (no banned words; slide-10 contact block complete in 4:5, 1:1 and 9:16). Caption FAIL lines are the
approved Oct 31 caption-format overrides only: Equal Housing Opportunity (on slide 10), last line is not a question (format ends with
signature + hashtags), "Swipe" on the IG/FB Page caption lines. TikTok uses "Save this post" (no swipe). Every fact sourced today or cut; no
guarantees, urgency, people/demographics, schools, churches, safety or "perfect for" language; Realtor.com numbers only on slide 9 with source +
month + viewed date; captions carry no stats (YouTube description carries the Realtor.com line + month + viewed date). Title Broker/REALTOR®
everywhere. Denise's licenses not checked.

## Captions for Buffer (also in captions.md)
### Instagram (4:5)
🎓 Did you know Davidson College came before the town of Davidson?

Before you house hunt in north Mecklenburg, here's how a college town on Lake Norman took shape.

🎓 Why does the college come first in Davidson's story?
🌊 Where does the town meet Lake Norman?
🏡 What's in the Davidson Historic District?
🎶 What happens on the Town Green?
🛶 Where can you launch a kayak on Lake Davidson?

Knowing a town's history, rules and outdoor spaces helps you picture everyday life before you choose a home.

A pretty Main Street is a good start. Knowing the whole town is better.

👉 Swipe through and save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#DavidsonNC #LakeNorman #CharlotteRealEstate #CharlotteNeighborhoods #CommunitySpotlight

### Facebook Page (1:1)
🎓 Did you know Davidson College came before the town of Davidson?

Before you house hunt in north Mecklenburg, here's how a college town on Lake Norman took shape.

🎓 Why does the college come first in Davidson's story?
🏡 What's in the Davidson Historic District?
🎶 What happens on the Town Green?
🛶 Where can you launch a kayak on Lake Davidson?

Knowing a town's history, rules and outdoor spaces helps you picture everyday life before you choose a home.

A pretty Main Street is a good start. Knowing the whole town is better.

👉 Swipe through and save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#DavidsonNC #LakeNorman #CharlotteRealEstate

### TikTok (9:16)
🎓 In Davidson, NC, the college came first. Then the town.

Here's the town's story in 10 slides.

🎓 College first, town second
🏡 The historic district
🎶 Saturdays on Main Street
🛶 Paddling Lake Davidson

Knowing the town helps you choose the home.

A pretty Main Street is a start. The whole town matters.

👉 Save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#DavidsonNC #LakeNorman #CharlotteRealEstate #CommunitySpotlight
