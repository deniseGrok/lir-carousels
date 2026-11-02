# GenerateImage prompts (Nov 2 2026 buyer tips, "Insure it before you close")
Save each raw output (3:4 portrait) as build/src/gen-NN-raw.jpg, then: `python3 build/build_slides.py upscale` (Real-ESRGAN x4) and
`python3 build/build_slides.py` (renders 4:5, 1:1, 9:16 + zips; any PDF is deleted automatically). Inspect each raw at full size first;
regenerate on artifacts, dull light, busy left side, readable text/logos/house numbers, palms/Spanish moss/ocean. Register every image in
TEMPLATES/photo-registry.csv (provider "generated"), never reuse one.

Shared style suffix (append to every prompt): "Ultra-sharp photorealistic photograph, bright warm golden-hour sunlight, high-end real estate
lifestyle magazine look, crystal-clear detail, shallow depth of field, clean uncluttered composition, main subject on the RIGHT third, calm simple
softly lit space on the LEFT half for text overlay, North Carolina Piedmont setting, no people facing camera, no readable text, no logos, no signs,
no brand names, no house numbers, no palm trees, no Spanish moss, no ocean. Vertical 3:4."

01 (cover, insure it before you close): "Front porch of a classic two-story Carolina home at golden hour, a set of house keys resting on a white porch railing in sharp focus on the right, warm painted siding and porch columns, soft green lawn and hardwood trees blurred on the left."
03 (your lender will ask for it): "Sunlit kitchen island with a closed plain manila folder, a pen and a pair of reading glasses on the right side of a light quartz counter, soft cream cabinetry blurred on the left, no paper text visible."
04 (shop it early): "Hands holding a smartphone showing only a soft abstract blank screen glow, seated at a sunlit wooden table on a screened porch, subject on the right, soft green backyard trees blurred on the left."
05 (ask about past claims): "Close-up of a well-kept asphalt shingle roof edge and clean gutter of a brick Carolina home in bright golden-hour light on the right, clear soft blue sky on the left."
06 (replacement cost or cash value): "Bright mudroom or utility room with a modern water heater and neatly organized shelves on the right, warm white walls and soft window light on the left, clean and new-looking."
07 (know your deductibles): "Two-story Carolina traditional home with a gray shingle roof under a bright clear late-afternoon sky, tall hardwoods swaying lightly, house on the right, open sky and lawn on the left, no house numbers."
08 (know what's not covered): "Gentle creek with smooth stones winding behind a backyard lawn at golden hour in the Carolina Piedmont, wooden footbridge on the right, soft trees and light on the left."
09 (in an HOA? see its policy): "Row of elegant brick townhomes with white trim and small landscaped front gardens at golden hour, buildings on the right, sunlit tree-lined sidewalk softly blurred on the left, no numbers or signs."
10 (LET'S TALK background, will be blurred): "Bright warm airy living room with sunlit windows, soft neutral sofa and green plant, gentle golden light, empty and uncluttered, no people."
