# DRAFT — Ballantyne neighborhood spotlight, rebuilt teal/gold nc_style (Denise Oct 15 PM).
# Facts from Oct 15 morning fetch. Cut: Trampled by Turtles Oct 17 (timing risk).
import sys, os, subprocess, zipfile, json
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from nc_style import PALETTES, page, shot, CONTACT_BLOCK
from PIL import Image
D = "/workspace/lir-ai-team/content-research/carousels/2026-10-15-neighborhood-ballantyne"
B = D + "/build"; IMG = B + "/img-hq"
P = PALETTES["teal"]; TAG = "NEIGHBORHOOD SPOTLIGHT<br>CHARLOTTE NC"
credits = json.load(open("/tmp/ball_credits.json"))
def ul(xs): return "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
def cred(i): return credits[str(i)][0]
def img(i): return f"{IMG}/{i:02d}.jpg"
S = [
 (img(1), cred(1), "<h1>A city within<br>the city.<br><em>Ballantyne.</em></h1>"
  + ul(["535-acre campus of offices, parks, dining and live music",
        "100+ acres of green space, 20+ miles of paths",
        "The Bowl: a new dining district on Bowl Street"])),
 (img(2), cred(2), "<h1>The Bowl.<br><em>New living room.</em></h1>"
  + ul(["Dining, retail and entertainment at 15119 Bowl Street",
        "Garden rooms, sidewalk seating, rooftop decks",
        "A central green; paths to Ballantyne's Backyard and the TD Amp"])),
 (img(3), cred(3), "<h1>100+ acres<br>of <em>backyard.</em></h1>"
  + ul(["Ballantyne's Backyard: a former golf course, now a community park",
        "Trails, rolling hills, catch-and-release ponds",
        "Stream Park: 6 acres with a playground, pavilion, stream and hammocks"])),
 (img(4), cred(4), "<h1>20+ miles<br>of <em>paths.</em></h1>"
  + ul(["Walking paths and bike lanes across the campus",
        "The Fit Trail, with fitness stations",
        "Trails around Hawkins and Crawford Ponds",
        "Carolina Thread Trail via McAlpine Creek Greenway"])),
 (img(5), cred(5), "<h1>Dinner on<br><em>Bowl Street.</em></h1>"
  + ul(["North Italia · Flower Child",
        "Olde Mecklenburg Brewery · Postino",
        "Brasserie Copain · Harriet's Hamburgers",
        "Plus Honeysuckle Gelato and PopUp Bagels"])),
 (img(6), cred(6), "<h1>More local<br><em>flavor.</em></h1>"
  + ul(["Tabla Indian Restaurant",
        "Crispy Banh Mi: Vietnamese specialties",
        "Gallery Restaurant at The Ballantyne hotel",
        "Hestia Rooftop · Fiore lounge"])),
 (img(7), cred(7), "<h1>A stage<br><em>in the park.</em></h1>"
  + ul(["TD Amp Ballantyne: 5,000-capacity outdoor venue",
        "Concerts, festivals and fitness classes",
        "Open daily to stroll when no event is on"])),  # Trampled by Turtles Oct 17 CUT
 (img(8), cred(8), "<h1>Roads +<br><em>transit.</em></h1>"
  + ul(["I-485 Express Lanes opened Feb. 2026 across south Charlotte",
        "Six new roads + intersection upgrades on campus",
        "CATS Route 43: eight stops on the Ballantyne campus",
        "Three LYNX stops planned on campus (2030 transit plan)"])),
 (img(9), cred(9), "<h1>Two sides,<br><em>two prices.</em></h1>"
  + "<div class='sub'>Realtor.com · as of September 2026</div>"
  + ul(["West: median list $418,750 · median sold $405,000",
        "East: median list $621,888 · median sold $657,000"])
  + "<div class='fine'>Source: Realtor.com Economic Research, Ballantyne West + East</div>"),
 (img(10), cred(10), "<h1>Spend a Saturday<br><em>here first.</em></h1>"
  + "<p class='b'>Walk Ballantyne's Backyard, have dinner on Bowl Street, then let's compare West and East listings side by side.</p>"
  + CONTACT_BLOCK),
]
assert len(S) == 10
pngs = []
for i, (im, cr, inner) in enumerate(S, 1):
    mode = "light" if i % 2 else "dark"
    # more text on 4,6,8 and contact -> slightly smaller photo / h1
    ph = 420 if i in (4, 6, 8, 10) else (460 if i in (1, 9) else 520)
    h1 = 120 if i in (1, 10) else (132 if i in (3, 4, 9) else 140)
    for suf, sw in (("", i < 10), ("-video", False)):
        out = f"{D}/slide-{i:02d}{suf}.png"
        shot(page(P, mode, i, inner, im, cr, sw, ph=ph, h1=h1, tag=TAG), out, B, f"slide-{i:02d}{suf}")
        if not suf: pngs.append(out)
ims = [Image.open(p).convert("RGB") for p in pngs]
ims[0].save(f"{D}/2026-10-15-neighborhood-ballantyne-DRAFT.pdf", save_all=True, append_images=ims[1:], resolution=150)
with zipfile.ZipFile(f"{D}/slides.zip", "w") as z:
    for p in pngs: z.write(p, os.path.basename(p))
# Short
ins, f, per, fade = [], "", 3.3, 0.5
for i in range(10):
    ins += ["-loop", "1", "-t", str(per), "-i", f"{D}/slide-{i+1:02d}-video.png"]
    f += f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color=0x0F4C5C,setsar=1,fps=30,format=yuv420p[v{i}];"
prev = "v0"
for i in range(1, 10):
    f += f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={round(i*(per-fade),2)}[x{i}];"; prev = f"x{i}"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", f.rstrip(";"),
                "-map", f"[{prev}]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-movflags", "+faststart", f"{D}/2026-10-15-neighborhood-ballantyne-short.mp4"], check=True)
print("DONE", len(pngs))
