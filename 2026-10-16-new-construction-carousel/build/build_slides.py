# Oct 16, 2026 new construction carousel. DRAFT — AWAITING DENISE APPROVAL.
# Adapted from 2026-10-15-new-construction-carousel/build-teal/build_slides.py (nc_style teal/gold, Denise Oct 15 2026).
# Offers verified on builder sites Oct 16, 2026 (~4:10-4:30 AM ET). Builder photos only, credited "Photo: <Builder>".
import sys, os, subprocess; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from nc_style import PALETTES, page, shot, CONTACT_BLOCK
from PIL import Image
D = "/workspace/lir-ai-team/content-research/carousels/2026-10-16-new-construction-carousel"; B = D + "/build"
P = PALETTES["teal"]; TAG = "NEW BUILD DEALS<br>NC + SC"
VER = "<div class='fine' style='font-size:30px;margin-top:6px'>Verified on builder site Oct 16, 2026. Terms subject to change.</div>"
def ul(x): return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"
def deal(name, who, offer, bullets, hs=None, os_=118):
    hs = hs or (96 if len(name) <= 16 else 80)
    return (f"<h1 style='font-size:{hs}px'>{name}</h1><div class='sub'>{who}</div>"
            f"<div class='offer' style='font-size:{os_}px;line-height:.98;margin-top:18px'>{offer}</div>" + ul(bullets) + VER)
I = lambda n: f"file://{B}/img/{n}"
S = [
 (I("cover_delwebb.jpg"), "Photo: Del Webb", "<h1 style='font-size:132px'>8 new-build<br><em>deals.</em><br>Verified Oct 16.</h1><p class='b'>4 in North Carolina, 4 in South Carolina. Each checked on the builder's own website on Oct 16, 2026.</p>" + ul(["Compare the full monthly payment", "Check every deadline and lender rule"])),
 (I("delwebb.jpg"), "Photo: Del Webb", deal("Carolina Riverside.", "Del Webb · Belmont, NC · 55+", "$35,000 off<br>+ a golf cart.", ["Compass, 2014 Belmont View Dr: now $491,353", "Golf cart voucher on quick move-ins", "Agree 9/1–11/30, close by 12/31/2026"])),
 (I("stanleymartin.jpg"), "Photo: Stanley Martin Homes", deal("Retreat at Laurelbrook.", "Stanley Martin · Sherrills Ford, NC · 55+", "Rates from 4.50%<br>(6.473% APR).", ["On select homes; terms not stated online", "Move-in-ready homes from $299,000", "Ranch-style plans near Lake Norman"])),
 (I("toll.jpg"), "Photo: Toll Brothers", deal("Bethany Farms.", "Toll Brothers · Simpsonville, SC", "Half off design<br>up to $50,000.", ["Plus $10,000 toward closing costs", "Deposit Oct 3–18, 2026; select homes", "Homes from $602,995 on half-acre sites"])),
 (I("lennar.jpg"), "Photo: Lennar", deal("Villas of North Valley.", "Lennar · Travelers Rest, SC", "$71K<br>price cut.", ["458 Rivergarden Dr, Cheffield, move-in ready", "Now $349,999 · 3 bed, 2 bath, 1,371 sq ft", "Single-story; deadline not stated"])),
 (I("hunterquinn.jpg"), "Photo: Hunter Quinn Homes", deal("Autumn Mill.", "Hunter Quinn Homes · Seneca, SC", "Up to $15,000<br>rate buydown.", ["Select quick move-in homes, October offer", "Preferred lender required", "Quick move-ins from $485,565"])),
 (I("ashtonwoods.jpg"), "Photo: Ashton Woods", deal("Hammock Walk at Nexton.", "Ashton Woods · Summerville, SC", "Up to $10,000<br>toward closing.", ["Villas from $279,990 (1050 Dusk Dr)", "Contract 9/15–10/31, close by 11/30/2026", "Certain quick move-in homes only"])),
 (I("kb.jpg"), "Photo: KB Home", deal("Richland Reserve.", "KB Home · Raleigh, NC", "4.99% (5.781% APR)<br>5/1 FHA ARM.", ["Townhomes from $289,095", "Sign by Oct 31, 2026; KBHS Home Loans", "Owner-occupied; rate can change after year 5"], os_=96)),
 (I("cc.jpg"), "Photo: Caviness & Cates", deal("Blakefield.", "Caviness & Cates · Fayetteville, NC", "Up to $30,000<br>builder incentive.", ["Or rates from 3.25% (6.62% APR), 3-2-1 buydown", "Select move-in-ready homes; close by 11/30/26"])),
 (None, "", "<h1 style='font-size:86px'>Want the homes<br>that qualify?<br><em>Let's match you<br>to the deal.</em></h1>"
   "<div class='box' style='margin-top:26px;padding:22px 32px 22px 26px'><b>DM or comment \"DEALS\"</b><p>and we'll get started.</p></div>"
   + CONTACT_BLOCK +
   "<div class='fine' style='margin-top:18px'>Offers verified on builder websites Oct 16, 2026. Terms, pricing and availability can change.</div>"),
]
assert len(S) == 10
for img, cr, inner in S:
    low = inner.lower(); assert "illustrative" not in low and "one community per slide" not in low and "unsplash" not in low
pngs = []
only = [int(a) for a in sys.argv[1:]] or list(range(1, 11))
for i, (img, cr, inner) in enumerate(S, 1):
    if i not in only: continue
    mode = "light" if i % 2 else "dark"
    bg = P["light"] if mode == "light" else P["dark"]
    # stronger bottom scrim so footer/credit stay legible over bright photos (Oct 16 review)
    scrim = f"<style>.ph:before{{background:linear-gradient({bg} 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.62) 72%,rgba(0,0,0,.86) 100%) !important}}</style>" if img else ""
    inner = scrim + inner
    for suf, sw in (("", i < 10), ("-video", False)):
        out = f"{D}/slide-{i:02d}{suf}.png"; shot(page(P, mode, i, inner, img, cr, sw, ph=(430 if i == 1 else 470), h1=(132 if i == 1 else 150), tag=TAG), out, B, f"slide-{i:02d}{suf}")
if len(only) < 10: sys.exit()
if os.environ.get("SKIP_RENDER"): pass
pngs = [f"{D}/slide-{i:02d}.png" for i in range(1, 11)]
# PDF with a DRAFT header strip on each page
from PIL import ImageDraw, ImageFont
fnt = ImageFont.truetype(subprocess.run(["fc-match","-f","%{file}","Montserrat:extrabold"],capture_output=True,text=True).stdout, 34)
pages = []
for p in pngs:
    im = Image.open(p).convert("RGB"); c = Image.new("RGB", (1080, 1350 + 70), "#B00020"); c.paste(im, (0, 70))
    ImageDraw.Draw(c).text((540, 35), "DRAFT — AWAITING DENISE APPROVAL", fill="white", font=fnt, anchor="mm"); pages.append(c)
pages[0].save(f"{D}/2026-10-16-new-construction-carousel-DRAFT.pdf", save_all=True, append_images=pages[1:], resolution=150)
import zipfile
with zipfile.ZipFile(f"{D}/slides.zip","w",zipfile.ZIP_DEFLATED) as z:
    for p in pngs: z.write(p, os.path.basename(p))
ins, f, per, fade = [], "", 3.3, 0.5
for i in range(10):
    ins += ["-loop","1","-t",str(per),"-i",f"{D}/slide-{i+1:02d}-video.png"]
    f += f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color=0x0F4C5C,setsar=1,fps=30,format=yuv420p[v{i}];"
prev = "v0"
for i in range(1, 10): f += f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={round(i*(per-fade),2)}[x{i}];"; prev = f"x{i}"
subprocess.run(["ffmpeg","-y","-loglevel","error",*ins,"-filter_complex",f.rstrip(";"),"-map",f"[{prev}]","-c:v","libx264","-pix_fmt","yuv420p","-r","30","-movflags","+faststart",f"{D}/2026-10-16-new-construction-carousel-youtube-short.mp4"], check=True)
print("done")
