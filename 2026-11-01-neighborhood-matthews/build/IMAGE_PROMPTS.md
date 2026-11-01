# GenerateImage prompts — Community Spotlight: Matthews, NC (Sun Nov 1 2026)
STATUS: PENDING. The GenerateImage tool was not available to the routine's build agent, so no images exist yet; nothing below has been generated.
Whoever has GenerateImage: generate each prompt as a 3:4 PORTRAIT image (e.g. 864x1152 or larger), save the raw output as
`build/src/gen-NN-raw.png` (or .jpg/.webp; NN = 01..10), inspect it at full size, then run from the carousel folder:
`python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py`.

Reject and regenerate on: dull/hazy/grey light, softness, warped or readable text/signs/logos/house numbers, extra or broken limbs, odd
architecture (melted windows, impossible rooflines, floating stairs), palm trees, Spanish moss, ocean/beach, any person posed or facing camera.
These images are ILLUSTRATIONS of the kind of scene each slide describes. They are never labeled or presented as a specific real house,
listing, address, business or landmark (slides carry topic pills only: THE ORIGINS, THE RAILROAD, TRADE STREET...).

Composition for every image (the renderer crops it to 4:5, 1:1 and 9:16): main subject and the brightest detail in the UPPER 55% of the frame
and roughly centered; the LOWER 40% calm and simple (lawn, path, pavement, soft foliage) because a deep-teal gradient and the text sit there;
nothing important near the left/right edges (9:16 crops ~8% off each side).

Shared style suffix (append to every prompt):
"Ultra-sharp photorealistic photograph, bright warm golden-hour sunlight, clear deep-blue sky with a few soft white clouds, lush green trees
and colorful flowers, crystal-clear detail, high-end lifestyle magazine look, North Carolina Piedmont small town setting, vertical 3:4.
No readable text, no signs, no logos, no brand names, no house numbers, no license plates, no palm trees, no Spanish moss, no ocean.
People, if any, small and incidental in the background, seen from behind or at a distance, never posed, never the focus."

01 COVER (Discover Matthews): "A charming historic small-town main street in the North Carolina Piedmont at golden hour: a row of one- and
two-story red-brick storefronts from around 1900 with canvas awnings and black lamp posts, large shade trees, hanging flower baskets and planters
of pink and white blooms, wide clean sidewalk, the street receding toward lush trees, blue sky; lower third is sunlit sidewalk and planters."

02 THE ORIGINS (Stumptown, 1820s stagecoach stop): "Rolling North Carolina Piedmont farmland at golden hour: a split-rail fence and a few
weathered old tree stumps in a meadow of wildflowers in the foreground-middle, a small 19th-century white clapboard farmhouse with a porch in the
far distance among tall hardwood trees, warm sunlight, blue sky; lower part is a calm sunlit grassy meadow."

03 THE RAILROAD (first train 1874): "A single railroad track curving gently through a lush green North Carolina town edge at golden hour,
tall hardwood trees on both sides, wildflowers and Queen Anne's lace along the gravel ballast, a vintage black railroad signal post, long warm
light, blue sky; no train, no buildings with signs; lower part is the sunlit gravel and grass beside the rails."

04 TRADE STREET (1888-1939 brick storefronts): "Close, slightly angled view of a beautifully kept late-1800s red-brick commercial building with
corbeled decorative brickwork along the roofline, tall arched upper windows and a striped canvas awning over a glass storefront with a warm glow,
potted flowers on the sidewalk, a lamp post and a shade tree, golden-hour sun, blue sky; no readable signage; lower part is clean brick sidewalk."

05 THE MARKET (Saturday farmers' market): "A bright outdoor small-town farmers' market on a grassy green at golden morning light: rows of plain
white canopy tents, wooden tables with baskets of colorful fresh vegetables, apples, pumpkins and cut flowers in the foreground-middle, a few
shoppers small and out of focus in the background seen from behind, big shade trees, blue sky; no signs or price tags; lower part is soft grass."

06 THE PARK (downtown park with a performance stage): "A small downtown town park at golden hour: a covered open-air performance stage with a
simple gabled roof and string lights at the back of a wide sunlit lawn, a brick patio with a few picnic tables, big leafy shade trees and flower
beds, blue sky; empty stage, no banners, no text; lower part is soft green lawn."

07 THE GREENWAY (creek trail to a lake park): "A paved greenway trail curving beside a gentle clear creek in lush North Carolina woods at golden
hour, a small wooden footbridge, ferns, black-eyed Susans and purple coneflowers along the path, sunbeams through tall hardwoods, a glimpse of a
calm pond with a wooden fishing pier in the distance, blue sky; lower part is the sunlit paved path."

08 MY TIP (know your town lines): "A welcoming front porch of a traditional Carolina craftsman-style home at golden hour, white columns, two wooden
rocking chairs, a glossy dark-green front door with a lantern, blue and white hydrangeas and boxwoods along brick steps, dappled sunlight, blue sky
through trees; no house number, no mailbox number; lower part is the sunlit brick steps and garden."

09 THE MARKET (stats; text covers the lower 75%): "Elevated view at golden hour over a leafy North Carolina town of traditional houses with
pitched roofs nestled among dense green and early-autumn trees, no steeples, no signs, no water towers, warm light, deep-blue sky with soft
clouds filling the top third; the lower two thirds is calm continuous tree canopy and rooftops."

10 MY RECOMMENDATION (contact slide; Denise's headshot is added on the right): "A sunlit brick sidewalk in a historic small-town downtown at golden
hour leading into the distance, black lamp posts, planters overflowing with pink and white flowers, big shade trees, soft-focus brick storefronts
with awnings on the left, blue sky; the RIGHT half of the lower two thirds calm and simple (soft trees, sidewalk) because her photo goes there."

Focal-point overrides go in build_slides.py as xy=(x, y) / xy_1x1 / xy_9x16 per slide after viewing the crops.
