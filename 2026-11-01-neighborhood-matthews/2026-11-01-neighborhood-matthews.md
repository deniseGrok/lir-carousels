# Community Spotlight: Matthews, NC (ZIP 28105) — DRAFT, AWAITING DENISE APPROVAL (IMAGES PENDING)
Built Sun Nov 1, 2026 (~4:45-5:30 AM ET) by the Afternoon Neighborhood Spotlight Carousel routine. FIRST Community Spotlight in Denise's new
'Community Spotlight — Modern Charlotte Editorial' design (TEMPLATES/modern_editorial.py + TEMPLATES/MODERN_EDITORIAL.md, built today; replaces
fullbleed_teal for this carousel from Nov 1). Nothing posted or scheduled. On approval: Buffer 4:00 PM ET, Instagram 4:5 (slide-01..10.png),
Facebook Page 1:1 (slides-1x1/), TikTok 9:16 (slides-9x16/).

## STATUS
Copy, fact-check, sources, captions (IG, FB Page, TikTok, FB personal, YouTube), renderer, build/Short/finish scripts and image prompts are DONE and
layout-tested in all four formats with placeholder photos (temp only, never committed). The ORIGINAL generated images are PENDING: the
GenerateImage tool was not available to this build agent. Prompts: build/IMAGE_PROMPTS.md. Once the 10 raw images are saved as
build/src/gen-NN-raw.png, run from this folder:
  python3 build/finish.py check && python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py
then inspect every slide in every size at full size, regenerate weak images, and commit the outputs (slide PNGs, slides-1x1/, slides-9x16/,
zips, PDF, youtube-short.mp4, registry rows).

## Deliverables (after images)
- slide-01..10.png 1080x1350 (4:5) + slides.zip + 2026-11-01-neighborhood-matthews-DRAFT.pdf (lossless img2pdf)
- slides-1x1/ 1080x1080 + slides-1x1.zip; slides-9x16/ 1080x1920 (text clear of 150 top / 350 bottom / 140 right) + slides-9x16.zip
- *-jpg.zip versions automatically when a PNG zip is over 25 MB
- youtube-short.mp4: 1080x1920 H.264 full screen, ~43.0 s (9 x 4.6 s + 7.0 s end hold on the contact slide, 0.6 s crossfades, 1.03 slow push-in),
  NO audio stream, header COMMUNITY SPOTLIGHT / Matthews · NC at y=262 inside the safe zone, key text clear of top 250 / bottom 420 / right 140,
  never says swipe. youtube-caption.md has the title, description and tags.

## Slides
1 COVER: Discover Matthews · History. Market. Greenway. · A historic railroad town in southeast Mecklenburg County, between Charlotte and Monroe.
2 THE ORIGINS — IT STARTED AS STUMPTOWN.: stumps left by settlers clearing land for cotton -> unofficially Stumptown; July 1825 John Miles Fullwood
  postmaster, stagecoach stop/store/post office from his home; mail to Fullwood Station, Stumptown became Fullwood.
3 THE RAILROAD — THE TRAIN NAMED THE TOWN.: first train Dec. 15, 1874; stop named Matthews after Edward Matthews, a director of the company;
  by 1875 mail to Matthews Station; incorporated as Matthews in 1879.
4 TRADE STREET — HISTORY ON TRADE STREET.: ten buildings on N. Trade + E. Charles streets = Matthews Commercial Historic District, National
  Register 1996; 1888-1939, Heath and Reid General Store (1888) to the former 1939 U.S. Post Office; Matthews Heritage Museum in the 1879
  Massey-Clark House (Thu-Sat, free).
5 THE MARKET — SATURDAYS AT THE MARKET.: Matthews Community Farmers' Market, 188 N. Trade St., Saturdays year-round; 8 a.m.-noon through
  Nov. 21, 2026, winter 9-11 a.m. from Dec. 5; free parking Trade St., Charles St., grassy lot off Cotton Gin Alley.
6 THE PARK — A STAGE DOWNTOWN.: Stumptown Park, two acres at 120 S. Trade St., year-round concerts/special events; performance stage with dance
  floor, playground, sand volleyball court, picnic areas; dawn to dusk, volleyball court + picnic area first-come, first-served.
7 THE GREENWAY — TRAILS TO THE LAKE.: Four Mile Creek Greenway 3.3 mi connecting downtown Matthews with Squirrel Lake Park; Squirrel Lake Park
  36 acres, fishing pier, walking trails, 12-hole disc golf; links to Matthews Heritage Trail + Sportsplex at Matthews.
8 MY TIP — KNOW YOUR TOWN LINES.: inside town limits one tax bill covers Town of Matthews + Mecklenburg County taxes; confirm town limits and
  look up the parcel in county property records; near Four Mile Creek check the FEMA flood map before an offer.
9 THE MARKET — REALTOR.COM • ZIP 28105 • SEPT. 2026 — WHAT HOMES LIST FOR.: $525,500 median list price · $245 price per sq. ft. · 117 active
  listings · 46 median days on market. Source line on slide: Realtor.com Economic Research, ZIP 28105 (Matthews NC) monthly listing data,
  September 2026; viewed Nov. 1, 2026.
10 MY RECOMMENDATION — LET'S TOUR IT TOGETHER.: "We'll start at the Saturday market on Trade Street, walk a stretch of the Four Mile Creek
  Greenway, and compare homes before you make an offer." + contact card (Broker/REALTOR®, firm, site, phone, Equal Housing Opportunity) + headshot.

## Sources (all fetched/verified Sun Nov 1, 2026, ~4:40-5:10 AM ET)
- Realtor.com Economic Research RDC_Inventory_Core_Metrics_Zip.csv (econdata.s3-us-west-2.amazonaws.com/Reports/Core/, Last-Modified
  Wed Sep 30 2026 14:41 GMT, latest month 202609), ZIP 28105 "matthews, nc", month 202609: median_listing_price 525500; median_listing_price_per_square_foot
  245; active_listing_count 117; median_days_on_market 46; quality_flag 0. (ZIP 28104 is also named Matthews by Realtor.com; slide labels ZIP 28105 only.)
- Town of Matthews, "Our History" (matthewsnc.gov/pview.aspx?catid=0&id=20691): between Charlotte and Monroe; stumps -> Stumptown; July 1825
  John Miles Fullwood postmaster, stagecoach depot/store/post office from his home, mail to Fullwood Station, Stumptown became Fullwood; first train
  Dec. 15, 1874; stop named Matthews for Edward Matthews, a director in the company; by 1875 mail to Matthews Station; incorporated 1879.
  Cross-checks: CMHLC/landmarkscommission.org Reconnaissance Survey of Matthews (Carolina Central Railway, 1874; 1879 charter); NCpedia Gazetteer
  ("town in SE Mecklenburg County. Inc. 1879"); ACHP Preserve America page (southeast of Charlotte).
- NPS National Register nomination 96000928 (NARA PDF) + Wikipedia "Matthews Commercial Historic District": listed Aug 22, 1996; 157-195 and
  156-196 N. Trade St. and 118 E. Charles St.; ten buildings, 1888-1939; Heath and Reid General Store, 196 N. Trade St., 1888; former U.S. Post
  Office, 195 N. Trade St., 1939.
- Matthews Heritage Museum (matthewsheritagemuseum.org, Massey-Clark House + Visit Us pages): E.J. Funderburk built the house in 1879 for
  Dr. Henry Massey; sold to the town 1977; opened as the museum June 7, 2013; 232 N. Trade St.; Thu-Sat 10:00-4:30; free admission.
- Matthews Community Farmers' Market (matthewsfarmersmarket.com): Saturdays year-round; main season 4/11/26-11/21/26, 8 AM-12 PM; winter season
  Dec. 5, 2026-March 2027, 9-11 AM; 188 N. Trade St.; free parking on Trade St., Charles St. and the grassy lot off Cotton Gin Alley.
- Town of Matthews facility page, Stumptown Park (facilityview.aspx?fid=47): 120 S. Trade; 2-acre park used year round for concerts and special
  events; performance stage with dance floor, playground, sand volleyball court, picnic area; dawn to dusk; first-come, first-serve.
- Mecklenburg County Park and Recreation, Greenways page (Trail Mileage Summary updated March 2026): Four Mile Creek Greenway "3.3 miles
  connecting downtown Matthews with Squirrel Lake Park and from E. John Street to S. Trade Street with connections to the Matthews Heritage
  Trail and Sportsplex at Matthews". Town of Matthews greenway page: open at all times except during flood events and greenway repairs.
- Town of Matthews facility page, Squirrel Lake Park (fid=46): 36 acres, pond with fishing pier, trails, 12-hole disc golf course, greenway access.
- Tip slide: Town of Matthews Taxes/Assessments page ("This bill includes Town of Matthews and Mecklenburg County taxes"; county bills and
  collects for the town); Mecklenburg County Tax Rates page (total bill includes a municipal tax from Charlotte or one of the six county towns).
  FEMA flood map = general guidance. No claim about any specific home.
- Cut: 1880 census count (town says 191, ACHP says 181), depot build date (town: late 1880s; town heritage inventory: c. 1900), population and
  17-sq-mile figures, churches (Fair Housing), Matthews Elementary on the greenway page (schools), Summerfest May 2026 (only a pre-event
  announcement found), Beats 'n Bites (third-party listing only), "NC's Favorite Farmers Market" award (no year/source shown), the
  "producer-only" market claim (third-party listing), tax rates (numbers stay on the sourced stats slide), restaurants and shops (not verified today).

## Images
All 10 slides: ORIGINAL photorealistic generated illustrations (GenerateImage) of the kind of scene each slide describes — PENDING (see STATUS).
No photo credits anywhere. Never labeled or presented as a specific real house, listing, address, business or landmark; topic pills only.
No readable signage, no palms/Spanish moss; people only incidental. Raw build/src/gen-NN-raw.*, ESRGAN x4 build/src/gen-NN.jpg, graded lossless
per size (build/img4x5, img1x1, img9x16). Registered by build/finish.py in both photo-registry copies (provider generated:GenerateImage).

## Compliance check
TEMPLATES/compliance_check.py on the slide HTML (layout test) and captions: slides PASS (no banned words; slide-10 contact block complete in 4:5, 1:1
and 9:16). Caption FAIL lines are the approved Oct 31 caption-format overrides only: Equal Housing Opportunity (on slide 10), last line is not
a question (format ends with signature + hashtags), "Swipe" on the IG/FB Page caption lines. TikTok uses "Save this post" (no swipe). T1-T9 /
F1-F5 read against every slide: every fact sourced today or cut; no guarantees, urgency, people/demographics, schools, safety or "perfect for"
language; Realtor.com numbers only on slide 9 with source + month + viewed date; captions carry no stats (YouTube description carries the
Realtor.com line + month + viewed date as requested). Title Broker/REALTOR® everywhere. Denise's licenses not checked.

## Captions for Buffer (also in captions.md)
### Instagram (4:5)
🚂 Did you know Matthews was once called Stumptown?

Before you house hunt in southeast Mecklenburg County, here's how a stagecoach stop became a railroad town.

🪵 How did Stumptown become Matthews?
🧱 Which Trade Street buildings are on the National Register?
🥕 Where does the Saturday farmers' market set up?
🎶 Which downtown park has its own stage?
🌳 Where does the greenway lead?

Knowing a town's story, parks and layout helps you picture everyday life before you choose a home.

A charming downtown is a good start. Knowing the whole town is better.

👉 Swipe through and save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#MatthewsNC #CharlotteRealEstate #CharlotteNeighborhoods #NCRealEstate #CommunitySpotlight

### Facebook Page (1:1)
🚂 Did you know Matthews was once called Stumptown?

Before you house hunt in southeast Mecklenburg County, here's how a stagecoach stop became a railroad town.

🪵 How did Stumptown become Matthews?
🧱 Which Trade Street buildings are on the National Register?
🥕 Where does the Saturday farmers' market set up?
🌳 Where does the greenway lead?

Knowing a town's story, parks and layout helps you picture everyday life before you choose a home.

A charming downtown is a good start. Knowing the whole town is better.

👉 Swipe through and save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#MatthewsNC #CharlotteRealEstate #CharlotteNeighborhoods

### TikTok (9:16)
🚂 Matthews, NC was once called Stumptown. Really.

Here's the town's story in 10 slides.

🪵 From Stumptown to Matthews
🧱 Trade Street history
🥕 The Saturday market
🌳 The greenway to the lake

Knowing the town helps you choose the home.

A cute downtown is a start. The whole town matters.

👉 Save this post for your next home search.

💬 Thinking about buying or selling in the Charlotte Metro, NC or SC? Let's connect and discuss your next move!

Denise Wilson | Broker/REALTOR®
Lifestyle International Realty — Carolinas
📲 704-615-7347

#MatthewsNC #CharlotteRealEstate #CharlotteNeighborhoods #CommunitySpotlight
