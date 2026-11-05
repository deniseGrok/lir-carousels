"""Community Spotlight: Huntersville, NC (ZIP 28078) — Wed Nov 5 2026 — Modern Charlotte Editorial.
NO PDF (Denise Nov 1 2026). Images: ORIGINAL GenerateImage; Real-ESRGAN x4.
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-05-neighborhood-huntersville"; PLACE = "Huntersville · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Huntersville", tagline="Lake. Rails. Village.",
      intro="A northern Mecklenburg town on Lake Norman, shaped by the railroad and a lifestyle village.", xy=(.48, .42)),
 dict(kind="info", pill="THE TOWN", h1="NORTH OF|[o]CHARLOTTE.[/o]", bullets=[
      "Huntersville sits in northern Mecklenburg County along I-77, north of Charlotte",
      "Lake Norman forms much of its western edge",
      "From Uptown, I-77 North reaches the main exits in about 20 to 25 minutes off-peak"]),
 dict(kind="info", pill="THE HISTORY", h1="CRAIGHEAD|[o]TO HUNTERSVILLE.[/o]", bullets=[
      "The settlement was once called Craighead before the railroad era",
      "It was renamed for Rev. Humphrey Hunter when the railroad arrived in the 1800s",
      "The town was incorporated in 1873 along the Atlantic, Tennessee and Ohio Railroad"]),
 dict(kind="info", pill="THE LAKE", h1="LAKE NORMAN|[o]ON THE WEST.[/o]", bullets=[
      "Duke Power filled Lake Norman in 1963 by damming the Catawba River at Cowans Ford",
      "It is North Carolina's largest man-made lake, with about 520 miles of shoreline",
      "Public access near town includes boat launches and lakeside parks along the western edge"]),
 dict(kind="info", pill="THE VILLAGE", h1="BIRKDALE|[o]ON GILEAD ROAD.[/o]", g0=.30, bullets=[
      "Birkdale Village opened in 2003 on about 52 acres of a former horse farm off Gilead Road",
      "It mixes shops, restaurants, offices and apartments around a central plaza",
      "The open lawn and amphitheater host outdoor movies and seasonal events"]),
 dict(kind="info", pill="THE GREENWAY", h1="TORRENCE|[o]CREEK TRAILS.[/o]", bullets=[
      "Torrence Creek Greenway links neighborhoods near Exit 23 with wooded creek corridors",
      "Tributary Greenway II continues the network toward Huntersville's western side",
      "Together they form part of Mecklenburg County's growing greenway system"]),
 dict(kind="info", pill="THE HOUSE", h1="HUGH TORRANCE|[o]HOUSE AND STORE.[/o]", g0=.30, bullets=[
      "The Hugh Torrance House and Store stands on Gilead Road as one of the area's oldest standing structures",
      "It joined the National Register of Historic Places on Sept. 14, 1992",
      "Guided tours share early Piedmont trade and farm life on a limited seasonal schedule"]),
 dict(kind="info", pill="MY TIP", h1="ASK ABOUT|[o]LAKE AND HOA RULES.[/o]", g0=.30, bullets=[
      "Homes near Lake Norman may have dock, pier or shoreline rules from the HOA or Duke Energy",
      "Confirm floodplain status and any shoreline buffer before you offer",
      "Ask for the HOA packet early so you know fees, rental rules and exterior guidelines"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28078 • OCT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$571,250"), ("Price per sq. ft.", "$229"), ("Active listings", "282"), ("Median days on market", "64")],
      source="Source: Realtor.com Economic Research, ZIP 28078 (Huntersville NC) monthly listing data, October 2026; viewed Nov. 5, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll walk Birkdale, see the greenways and compare Lake Norman-area homes before you make an offer.",
      body_9x16v="We'll walk Birkdale and the greenways, then compare homes before an offer.",
      g0=.22, minTop=.24, minTop_9x16=.38, minTop_9x16v=.37),
]
for s in SL: s["place"] = PLACE
FMT_DIR = {"4x5": D, "1x1": os.path.join(D, "slides-1x1"), "9x16": os.path.join(D, "slides-9x16")}

def src_for(n, pdir=None):
    if pdir:
        for e in ("png", "jpg", "jpeg", "webp"):
            p = os.path.join(pdir, f"{n:02d}.{e}")
            if os.path.exists(p): return p
        return None
    p = os.path.join(SRC, f"gen-{n:02d}.jpg")
    return p if os.path.exists(p) else None

def upscale():
    for raw in sorted(glob.glob(os.path.join(SRC, "gen-??-raw.*"))):
        n = int(os.path.basename(raw)[4:6]); out = os.path.join(SRC, f"gen-{n:02d}.jpg")
        if not os.path.exists(out): print("ESRGAN", raw); me.upscale(raw, out)

def build(fmts=("4x5", "1x1", "9x16"), pdir=None, outroot=None):
    res = {}
    for fmt in fmts:
        od = os.path.join(outroot, fmt) if outroot else FMT_DIR[fmt]; os.makedirs(od, exist_ok=True)
        idir = os.path.join(outroot or B, f"img{fmt}"); os.makedirs(idir, exist_ok=True)
        hd = os.path.join(outroot, "html") if outroot else B; pngs = []
        for n, sl in enumerate(SL, 1):
            src = src_for(n, pdir); assert src, f"missing image for slide {n}"
            x, y = sl.get(f"xy_{fmt}", sl.get("xy", (.5, .5)))
            ph = os.path.join(idir, f"{n:02d}.png"); me.prep_photo(src, ph, fmt, x, y, **sl.get("grade", {}))
            out = os.path.join(od, f"slide-{n:02d}.png"); fit = me.render(sl, out, fmt, n, len(SL), ph, hd)
            print(fmt, n, fit); pngs.append(out)
        res[fmt] = pngs
        if outroot: continue
        zp = {"4x5": "slides.zip", "1x1": "slides-1x1.zip", "9x16": "slides-9x16.zip"}[fmt]
        with zipfile.ZipFile(os.path.join(D, zp), "w") as z:
            for i, p in enumerate(pngs, 1): z.write(p, f"slide-{i:02d}.png")
        mb = os.path.getsize(os.path.join(D, zp)) / 1e6; print(zp, f"{mb:.1f} MB")
        if mb > 25:
            jz = zp.replace(".zip", "-jpg.zip")
            with zipfile.ZipFile(os.path.join(D, jz), "w") as z:
                for i, p in enumerate(pngs, 1):
                    tmp = f"/tmp/hv-jpg-{fmt}-{i:02d}.jpg"; Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(jz, f"{os.path.getsize(os.path.join(D, jz))/1e6:.1f} MB")
        # NO PDF — Denise rule Nov 1 / Nov 5
        for p in glob.glob(os.path.join(D, "*.pdf")):
            os.remove(p); print("removed PDF", p)
    return res

def video(pdir=None):
    V = "/tmp/hv-v916"; shutil.rmtree(V, ignore_errors=True); os.makedirs(V)
    for n, sl in enumerate(SL, 1):
        src = src_for(n, pdir); x, y = sl.get("xy_9x16", sl.get("xy", (.5, .5)))
        ph = os.path.join(V, f"ph-{n:02d}.png"); me.prep_photo(src, ph, "9x16v", x, y, **sl.get("grade", {}))
        print("9x16v", n, me.render(sl, os.path.join(V, f"slide-{n:02d}.png"), "9x16v", n, len(SL), ph, V))
    subprocess.run([sys.executable, os.path.join(B, "make_youtube_short.py"), D, V], check=True)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["upscale"]: upscale()
    elif a[:1] == ["video"]: video()
    elif a[:1] == ["preview"]:
        build(pdir=a[1], outroot="/tmp/hv-preview")
    else: build()
