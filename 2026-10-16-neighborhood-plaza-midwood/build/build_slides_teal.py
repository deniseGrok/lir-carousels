# DRAFT — Plaza Midwood neighborhood spotlight, nc_style teal/gold. Facts fetched Oct 16 2026 ~4:40-4:50 AM ET.
import sys, os, subprocess, zipfile, json
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from nc_style import PALETTES, page, shot, CONTACT_BLOCK
from PIL import Image
N = "2026-10-16-neighborhood-plaza-midwood"
D = "/workspace/lir-ai-team/content-research/carousels/" + N
B = D + "/build"; IMG = B + "/img"
P = PALETTES["teal"]; TAG = "NEIGHBORHOOD SPOTLIGHT<br>CHARLOTTE NC"
credits = json.load(open(B + "/credits.json"))
def ul(xs): return "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
def cred(i): return credits[str(i)][0]
def img(i): return f"{IMG}/{i:02d}.jpg"
S = [
 "<h1>Murals, music<br>and a main street.<br><em>Plaza Midwood.</em></h1>"
  + ul(["Just outside Uptown, east of Hawthorne Lane",
        "Founded in 1910 as a streetcar suburb",
        "Murals on nearly every corner"]),
 "<h1>A historic<br><em>district.</em></h1>"
  + ul(["Streets laid out by the Oakland Land Company",
        "Local Historic District since 1992",
        "Covers The Plaza, Thomas Ave and parts of Pecan and Clement",
        "Overseen by the Historic District Commission"]),
 "<h1>Live music<br><em>after dark.</em></h1>"
  + ul(["Snug Harbor and Petra's: jazz, indie, rock and more",
        "Local talent and touring artists",
        "Open mic nights and drag shows at Legion Brewing"]),
 "<h1>Eat your way<br>down <em>Central.</em></h1>"
  + ul(["Villani's Bakery: Italian pastries",
        "Milkbread's walk-up window: donuts to crispy chicken",
        "Calle Sol: ceviche and empanadas",
        "Midwood Smokehouse · Supperland"]),
 "<h1>A neighborhood<br><em>beer crawl.</em></h1>"
  + ul(["Pilot Brewing",
        "Resident Brewing Company",
        "Burial Beer Co.",
        "Southern Strain Brewing Company"]),
 "<h1>Walk it,<br><em>ride it.</em></h1>"
  + ul(["Walkable, tree-lined streets",
        "Joy Rides: electric-bike rentals",
        "Veterans Park: green space for a stroll or a picnic"]),
 "<h1>Shop<br><em>local.</em></h1>"
  + ul(["House of Africa: art, clothing and home decor",
        "Betty by Moxie Mercantile boutique",
        "Pinhouse: duckpin bowling and self-pour taps",
        "Boris &amp; Natasha · Lunchbox Records"]),
 "<h1>Getting<br><em>around.</em></h1>"
  + ul(["Main roads: Central Ave, Hawthorne Lane and The Plaza",
        "Gold Line streetcar ends at Sunnyside Ave on Hawthorne Lane",
        "17 stops, 4 miles, through Center City to the Historic West End"]),
 "<h1>What homes<br><em>cost here.</em></h1>"
  + "<div class='sub'>Realtor.com · as of September 2026</div>"
  + ul(["Median list price: $820,000",
        "Median sold price: $912,500",
        "$434 per sq ft · 45 active listings",
        "Median 35 days on market"])
  + "<div class='fine'>Source: Realtor.com Economic Research, Plaza Midwood</div>",
 "<h1>Start on<br><em>Central Ave.</em></h1>"
  + "<p class='b'>Walk Central Avenue and the historic streets off The Plaza, then let's compare listings block by block.</p>"
  + CONTACT_BLOCK,
]
assert len(S) == 10
pngs = []
for i, inner in enumerate(S, 1):
    mode = "light" if i % 2 else "dark"
    ph = 400 if i in (2, 4, 7, 8, 9, 10) else (440 if i == 1 else 500)
    h1 = 112 if i == 1 else (120 if i in (9, 10) else 136)
    for suf, sw in (("", i < 10), ("-video", False)):
        out = f"{D}/slide-{i:02d}{suf}.png"
        shot(page(P, mode, i, inner, img(i), cred(i), sw, ph=ph, h1=h1, tag=TAG), out, B, f"slide-{i:02d}{suf}")
        if not suf: pngs.append(out)
ims = [Image.open(p).convert("RGB") for p in pngs]
ims[0].save(f"{D}/{N}-DRAFT.pdf", save_all=True, append_images=ims[1:], resolution=150)
with zipfile.ZipFile(f"{D}/slides.zip", "w") as z:
    for p in pngs: z.write(p, os.path.basename(p))
ins, f, per, fade = [], "", 3.3, 0.5
for i in range(10):
    ins += ["-loop", "1", "-t", str(per), "-i", f"{D}/slide-{i+1:02d}-video.png"]
    f += f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color=0x0F4C5C,setsar=1,fps=30,format=yuv420p[v{i}];"
prev = "v0"
for i in range(1, 10):
    f += f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={round(i*(per-fade),2)}[x{i}];"; prev = f"x{i}"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", f.rstrip(";"),
                "-map", f"[{prev}]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-movflags", "+faststart", f"{D}/{N}-short.mp4"], check=True)
print("DONE", len(pngs))
