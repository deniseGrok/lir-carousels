import json
C = ("Ultra-sharp photorealistic magazine photograph, vertical 3:4, bright warm golden-hour sunlight, crisp detail, vivid but natural color, "
     "glowing highlights, nothing hazy or grey. Composition: the main subject sits on the RIGHT half of the frame; the LEFT half is calm, simple "
     "and darker (deep shade, dark green foliage or a soft shadowed wall) so text can sit on it. Setting plausible for the Charlotte, North Carolina "
     "area: hardwoods, crepe myrtles, Carolina pines, red clay brick, no palm trees, no Spanish moss, no ocean or beach. Absolutely no readable text, "
     "letters, numbers, logos, brand names, signs or house numbers anywhere.")
P = [
 (1, "Cover. A welcoming two-story Carolina home, red brick lower level with white board-and-batten siding above, black shutters, a covered front porch with "
     "two wooden rocking chairs, warm lights glowing in the windows, tidy lawn and mulched beds, mature oak and a crepe myrtle, shot from the front walk at a slight angle. "
     "The house fills the right half; the left side is the deep shade of a large magnolia and dark hedges. No people."),
 (2, "The inspection report. Close view of a light oak kitchen island in a sunlit kitchen: a closed three-ring binder and a few loose printed pages that are blurred "
     "and unreadable, a small LED flashlight, reading glasses and a pen, a mug of coffee. Objects grouped on the right half with shallow depth of field; "
     "the left side falls into a soft, shadowed navy cabinet wall. No people, no readable writing."),
 (3, "Current condition. A charming older Carolina home's front porch with slightly weathered gray painted floorboards, a white porch swing, a few worn steps "
     "and a peeling spot of paint on one railing, lived-in but cared for, potted ferns, late golden light raking across the boards. Porch detail on the right half; "
     "left side is dark green boxwood and deep shade. No people."),
 (4, "Inspecting early. A home inspector seen only from behind and small in the frame, on an aluminum ladder against a brick ranch home, checking the gutter "
     "and roof edge with a flashlight; plain work clothes, no logos, face not visible. The house and ladder on the right half, warm sunlit brick and clean "
     "gutters; left side is the dark shadow of a tall pine and shrubs."),
 (5, "Being specific. Overhead three-quarter view of a wooden dining table by a window: a person's hands only (no face) writing on a blank lined notepad, "
     "beside a yellow tape measure, a handheld moisture meter with a blank screen and a small paint chip fan with no labels. Hands and tools on the right half; "
     "left side a deep shadowed tabletop and dark wall. Notepad lines are blank, no legible words."),
 (6, "Repair, credit or price. A brand-new outdoor air conditioning condenser unit (plain, no brand marks) on a fresh concrete pad beside the red brick "
     "side wall of a home, new copper line set and neat gravel border, a few green shrubs, glowing late-day sun on the brick. Unit on the right half; left side "
     "is the dark shade of a holly hedge. No people."),
 (7, "Decision point. A bright entry foyer of a two-story Carolina home: the front door standing half open to a sunlit porch and green lawn beyond, warm "
     "golden light spilling across hardwood floors, a slim console table with a small bowl holding a set of house keys, a round mirror reflecting only light. "
     "Door and light on the right half; left side a calm, shadowed painted wall. No people."),
 (8, "Repairs verified. Close view of a freshly repaired white wooden porch column base and new painted trim on a farmhouse-style porch, crisp clean paint "
     "lines, new porch boards matching the old, a fresh caulk line, a folded painter's drop cloth and a closed paint can with no label set neatly to the side, "
     "golden sun across the wood. Column on the right half; left side is dark green foliage in deep shade. No people."),
 (9, "Slide 10 background (will be blurred behind Denise's headshot). A bright, warm, inviting living room in a Carolina home: cream sofa with soft throw "
     "pillows, light oak floors, a woven rug, a fireplace with a plain white mantel, large windows with golden-hour sun and green trees outside, a fiddle-leaf "
     "plant. Bright and airy everywhere, no dark areas. No people, no art with text, no screens."),
]
json.dump([dict(n=n, filename=f"gen-{n:02d}-raw", slide=(10 if n == 9 else n), aspect="3:4", prompt=f"{p} {C if n != 9 else C.split(' Composition:')[0] + ' ' + C.split('text can sit on it. ')[1]}") for n, p in P],
          open(__file__.replace("mk_prompts.py", "image-prompts.json"), "w"), indent=1, ensure_ascii=False)
