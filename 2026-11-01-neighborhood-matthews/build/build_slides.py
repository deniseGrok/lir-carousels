"""Community Spotlight: Matthews, NC (ZIP 28105) — Sun Nov 1 2026 — first carousel in 'Community Spotlight — Modern Charlotte Editorial'.
Renderer: TEMPLATES/modern_editorial.py (docs TEMPLATES/MODERN_EDITORIAL.md). Images: ORIGINAL generated images (GenerateImage), prompts in
build/IMAGE_PROMPTS.md; raw outputs saved as build/src/gen-NN-raw.(png|jpg|webp), Real-ESRGAN x4 -> build/src/gen-NN.jpg.
Usage:
  python3 build/build_slides.py upscale          # ESRGAN x4 every raw that has no upscaled copy yet
  python3 build/build_slides.py                  # 4:5 + 1:1 + 9:16 sets, PDF, zips (+ JPG zips if a PNG zip > 25 MB)
  python3 build/build_slides.py video            # 9:16 video frames (temp) + youtube-short.mp4 (silent)
  python3 build/build_slides.py preview DIR      # layout test with placeholder photos from DIR/NN.(png|jpg) -> /tmp/mt-preview (never committed)
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-01-neighborhood-matthews"; PLACE = "Matthews · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Matthews", tagline="History. Market. Greenway.",
      intro="A historic railroad town in southeast Mecklenburg County, between Charlotte and Monroe.", xy=(.5, .45)),
 dict(kind="info", pill="THE ORIGINS", h1="IT STARTED AS|[o]STUMPTOWN.[/o]", bullets=[
      "Settlers clearing land for cotton left so many tree stumps that the early settlement was unofficially called Stumptown",
      "In July 1825, John Miles Fullwood became postmaster and ran a stagecoach stop, store and post office from his home",
      "Mail went to Fullwood Station, and Stumptown gradually became known as Fullwood"]),
 dict(kind="info", pill="THE RAILROAD", h1="THE TRAIN|[o]NAMED THE TOWN.[/o]", bullets=[
      "The first train rolled into town on Dec. 15, 1874",
      "The railroad named the stop Matthews, after Edward Matthews, a director of the company",
      "By 1875, mail went to Matthews Station, and the town was incorporated as Matthews in 1879"]),
 dict(kind="info", pill="TRADE STREET", h1="HISTORY ON|[o]TRADE STREET.[/o]", bullets=[
      "Ten buildings on North Trade and East Charles streets make up the Matthews Commercial Historic District, on the National Register since 1996",
      "They date from 1888 to 1939, from the Heath and Reid General Store to a former 1939 U.S. Post Office",
      "Up the street, the Matthews Heritage Museum fills the 1879 Massey-Clark House (Thursday to Saturday, free admission)"]),
 dict(kind="info", pill="THE MARKET", h1="SATURDAYS|[o]AT THE MARKET.[/o]", bullets=[
      "The Matthews Community Farmers' Market sets up at 188 N. Trade St. every Saturday, year-round",
      "Main-season hours are 8 a.m. to noon through Nov. 21, 2026; winter hours, 9 to 11 a.m., start Dec. 5",
      "Free parking is on Trade Street, Charles Street and in the grassy lot off Cotton Gin Alley"]),
 dict(kind="info", pill="THE PARK", h1="A STAGE [o]DOWNTOWN.[/o]", bullets=[
      "Stumptown Park, two acres at 120 S. Trade St., is used year-round for concerts and special events",
      "It has a performance stage with a dance floor, a playground, a sand volleyball court and picnic areas",
      "It is open dawn to dusk, and the volleyball court and picnic area are first-come, first-served"]),
 dict(kind="info", pill="THE GREENWAY", h1="TRAILS [o]TO THE LAKE.[/o]", bullets=[
      "Four Mile Creek Greenway runs 3.3 miles, connecting downtown Matthews with Squirrel Lake Park",
      "Squirrel Lake Park covers 36 acres, with a fishing pier, walking trails and a 12-hole disc golf course",
      "The greenway also links to the Matthews Heritage Trail and the Sportsplex at Matthews"]),
 dict(kind="info", pill="MY TIP", h1="KNOW YOUR|[o]TOWN LINES.[/o]", bullets=[
      "Matthews is its own town: inside town limits, one tax bill covers Town of Matthews and Mecklenburg County taxes",
      "Confirm whether a home is inside town limits, and look up the parcel in Mecklenburg County property records",
      "Near Four Mile Creek, check the FEMA flood map before you make an offer"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28105 • SEPT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$525,500"), ("Price per sq. ft.", "$245"), ("Active listings", "117"), ("Median days on market", "46")],
      source="Source: Realtor.com Economic Research, ZIP 28105 (Matthews NC) monthly listing data, September 2026; viewed Nov. 1, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll start at the Saturday market on Trade Street, walk a stretch of the Four Mile Creek Greenway, and compare homes before you make an offer.",
      body_9x16v="We'll walk Trade Street and the greenway, then compare homes before you make an offer.",
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
            src = src_for(n, pdir); assert src, f"missing image for slide {n} (build/src/gen-{n:02d}.jpg)"
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
                    tmp = f"/tmp/mt-jpg-{fmt}-{i:02d}.jpg"; Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(jz, f"{os.path.getsize(os.path.join(D, jz))/1e6:.1f} MB")
        if fmt == "4x5":
            import img2pdf
            open(os.path.join(D, f"{NAME}-DRAFT.pdf"), "wb").write(img2pdf.convert(pngs))
    return res

def video(pdir=None):
    V = "/tmp/mt-v916"; shutil.rmtree(V, ignore_errors=True); os.makedirs(V)
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
        build(pdir=a[1], outroot="/tmp/mt-preview")
    else: build()
