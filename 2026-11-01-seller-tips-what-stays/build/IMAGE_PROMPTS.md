# GenerateImage prompts (Nov 1 2026 seller tips, "What stays, what goes")
Save each raw output (864x1152, 3:4 portrait) as build/src/gen-NN-raw.jpg, then: `python3 build/build_slides.py upscale` (Real-ESRGAN x4) and
`python3 build/build_slides.py` (renders 4:5, 1:1, 9:16 + PDFs + zips). Inspect each raw at full size first; regenerate on artifacts, dull light,
busy left side, readable text/logos/house numbers, palms/Spanish moss/ocean.

Shared style suffix (append to every prompt): "Ultra-sharp photorealistic photograph, bright warm golden-hour sunlight, high-end real estate
lifestyle magazine look, crystal-clear detail, shallow depth of field, clean uncluttered composition, main subject on the RIGHT third, calm simple
softly lit space on the LEFT half for text overlay, North Carolina Piedmont setting, no people facing camera, no readable text, no logos, no signs,
no brand names, no house numbers, no palm trees, no Spanish moss, no ocean. Vertical 3:4."

01 (cover, what stays / what goes): "Bright elegant dining room in a Charlotte-area home, a statement brass chandelier and large sunlit windows on the right, two neatly taped plain cardboard moving boxes on the hardwood floor, warm cream wall in soft shade on the left."
03 (fixtures usually stay): "Sunlit living room corner with a modern ceiling fan, a wall-mounted brass light sconce and linen roller shades on tall windows on the right side, soft warm plaster wall on the left."
04 (the list goes outside, too): "Backyard of a traditional brick Carolina home at golden hour, a small painted wooden storage shed with flower beds and low landscape path lights on the right, deep green hardwood trees and lawn in soft shadow on the left."
05 (smart devices count, too): "Close-up of a hand adjusting a sleek round smart thermostat on a warm white hallway wall, the thermostat screen shows only a soft abstract glow with no digits or text, subject on the right, sunlit blurred hallway on the left."
06 (taking it? put it in writing): "Close-up of a beautiful vintage crystal-and-brass pendant light hanging in a sunlit foyer on the right, soft cream wall and staircase blurred in the background on the left."
07 (leased items don't convey): "Two-story Carolina craftsman-style home at golden hour with dark solar panels on the roof on the right, tall pines and hardwoods in soft shade on the left, manicured lawn."
08 (personal items are separate): "Bright modern kitchen with a freestanding stainless steel refrigerator and sheer linen curtains on a window on the right, soft warm cabinetry in shade on the left, no magnets or papers on the fridge."
09 (match the listing to the contract): "Hands holding a pen over a clipboard with a blank checklist (lines and boxes only, no readable words) in a sunlit living room, subject on the right, soft blurred sofa and window light on the left."
10 (LET'S TALK background, will be blurred): "Bright warm airy living room with sunlit windows, soft neutral sofa and green plant, gentle golden light, empty and uncluttered, no people."
