import json
C = ("Ultra-sharp photorealistic magazine photograph, vertical 3:4, bright warm golden-hour sunlight, crystal-clear crisp detail, vivid but natural color, "
     "glowing highlights, nothing hazy or grey. Composition: the main subject sits on the RIGHT half of the frame; the LEFT half is calm, simple "
     "and darker (deep shade, dark green foliage or a soft shadowed wall) so text can sit on it. Setting plausible for the Charlotte, North Carolina "
     "area: hardwoods, crepe myrtles, Carolina pines, red clay brick, no palm trees, no Spanish moss, no ocean or beach. Absolutely no readable text, "
     "letters, numbers, logos, brand names, signs, house numbers, or screens showing any content anywhere.")
C10 = C.split(" Composition:")[0] + " " + C.split("text can sit on it. ")[1]
P = [
 (1, "Cover. A handsome two-story Carolina home at golden hour: painted white brick, a deep-teal front door with brass hardware, a covered porch with a "
     "pair of lanterns glowing, boxwoods and a crepe myrtle, a brick front walk. Shot from the walk at a slight angle; the house fills the right half; the left "
     "side is the deep shade of a large Southern magnolia. No people."),
 (2, "How the scam works. A tidy home office desk by a sunlit window: a closed silver laptop, a smartphone lying face-down, a few plain white envelopes "
     "with no writing, reading glasses and a mug of coffee. Objects grouped on the right half with shallow depth of field; left side is a shadowed "
     "dark-green painted wall. No people."),
 (3, "Set the plan early. Overhead three-quarter view of a light oak kitchen table in warm morning sun: a spiral notepad with only blank lined paper, "
     "a pen resting on it, a smartphone face-down, a small ceramic bowl of clementines, a coffee cup. Items on the right half; left side falls into soft "
     "deep shadow. No people."),
 (4, "Call a number you trust. In a bright Carolina living room, a person seen from behind and slightly to the side stands at a tall window holding a "
     "phone to their ear, face turned away and not visible, casual sweater, golden light on hardwood floors and green trees outside. Person small and "
     "incidental on the right half; left half a shadowed wall. Phone back faces camera with no logo."),
 (5, "Pause on any change. A classic craftsman-style front porch at golden hour with a closed solid red front door, white trim, a simple brass door knob, "
     "a potted fern, painted gray porch floorboards, warm sun raking across. Door on the right half; left side the deep shade of a dark holly hedge. No people, "
     "no house numbers."),
 (6, "Keep money talk off email. Close view on a walnut desk in warm light: a closed laptop with a small solid brass padlock resting on its lid, a leather "
     "folio closed beside it, a fountain pen. Subject on the right half with shallow depth of field; left side dark and softly shadowed. No people, "
     "no logos on the laptop."),
 (7, "Confirm it arrived. A bright, upscale conference room in a small Carolina law office: a long polished wood table, leather chairs, a closed navy "
     "folder and a pen on the table, a tall window with afternoon sun and green oak trees outside, built-in bookshelves with plain spines blurred. "
     "Table and window on the right half; left side a shadowed paneled wall. No people, no readable book titles."),
 (8, "Act fast. In a sunlit modern farmhouse kitchen, a person seen in profile from the shoulders down, face not shown, stands at a white quartz "
     "island holding a phone to their ear with one hand and a closed folder in the other; a calm, focused posture. Person incidental on the right half; "
     "left side a dark-green shadowed cabinet wall. No visible screen content."),
 (9, "Slide 10 background (will be blurred behind Denise's headshot). A bright, airy Carolina sunroom: white-painted brick wall, a cream linen sofa with "
     "sage and coral pillows, a jute rug, a large potted olive tree, tall windows with golden-hour sun and green pines outside. Bright everywhere, no dark "
     "areas. No people, no art with text, no screens."),
]
out = [dict(slide=(10 if n == 9 else n), filename=f"tips-{n:02d}.png", aspect_ratio="3:4", prompt=f"{p} {C if n != 9 else C10}") for n, p in P]
json.dump(out, open("/workspace/carousel-batch-2026-11-12/tips-image-prompts.json", "w"), indent=1, ensure_ascii=False)
json.dump(out, open(__file__.replace("mk_prompts.py", "image-prompts.json"), "w"), indent=1, ensure_ascii=False)
print(len(out))
