"""Community Spotlight: Fort Mill, SC (ZIP 29715) — Tue Nov 3 2026 — Modern Charlotte Editorial (third set; worked examples Matthews Nov 1, Davidson Nov 2).
Renderer: TEMPLATES/modern_editorial.py (docs TEMPLATES/MODERN_EDITORIAL.md). Images: ORIGINAL generated images (GenerateImage), prompts in
build/IMAGE_PROMPTS.md; raw outputs saved as build/src/gen-NN-raw.(png|jpg|webp), Real-ESRGAN x4 -> build/src/gen-NN.jpg.
Usage:
  python3 build/build_slides.py upscale          # ESRGAN x4 every raw that has no upscaled copy yet
  python3 build/build_slides.py                  # 4:5 + 1:1 + 9:16 sets, PDF, zips (+ JPG zips if a PNG zip > 25 MB)
  python3 build/build_slides.py video            # 9:16 video frames (temp) + youtube-short.mp4 (silent)
  python3 build/build_slides.py preview DIR      # layout test with placeholder photos from DIR/NN.(png|jpg) -> /tmp/fm-preview (never committed)
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-03-neighborhood-fort-mill"; PLACE = "Fort Mill · SC"

SL = [
 dict(kind="cover", discover="Discover", name="Fort Mill", tagline="Mill. Main. Greenway.",
      intro="A historic mill town in northeastern York County, just south of the North Carolina line.", xy=(.5, .45)),
 dict(kind="info", pill="THE TOWN", h1="JUST ACROSS|[o]THE STATE LINE.[/o]", bullets=[
      "Fort Mill sits in northeastern York County, South Carolina, just south of the North Carolina line",
      "Charlotte lies to the north and Rock Hill to the south",
      "From I-77 at Exit 85, SC 160 heads east into town"]),
 dict(kind="info", pill="THE HISTORY", h1="A FORT AND|[o]A GRIST MILL.[/o]", bullets=[
      "The name joins a colonial-era fort with a grist mill on Steele Creek, known as Webb's Mill",
      "The South Carolina General Assembly chartered the town on Feb. 12, 1873",
      "Fort Mill Manufacturing Co. was chartered in 1887 and later became part of Springs Cotton Mills"]),
 dict(kind="info", pill="THE BUILDINGS", h1="BRICK FRONTS|[o]ON MAIN STREET.[/o]", g0=.30, bullets=[
      "The Fort Mill Downtown Historic District joined the National Register on June 11, 1992",
      "Its one- and two-story masonry storefronts were built between 1860 and 1940",
      "Look for corbelled brick and recessed panels at 210, 223 and 225 Main St., all from around 1900"]),
 dict(kind="info", pill="THE GREENWAY", h1="2,100 ACRES|[o]OF GREENWAY.[/o]", bullets=[
      "The Anne Springs Close Greenway opened in 1995 and covers more than 2,100 acres in Fort Mill",
      "Its 40 miles of trails pass Lake Haigler, the Steele Creek swinging bridge and historic Nation Ford Road",
      "Day admission is $17 per adult and $8 for ages 3 to 12; trails are open 7 a.m. to sunset"]),
 dict(kind="info", pill="THE PARK", h1="A PARK ON|[o]WHITE STREET.[/o]", bullets=[
      "Walter Y. Elisha Park covers 12 acres at 345 N. White St., between Ardrey and Sidney Johnson streets",
      "It has a 0.6-mile walking trail, a playground, eight arbor swings, an amphitheater and open lawn",
      "A trail links it to Harris Street, and it hosts the annual South Carolina Strawberry Festival"]),
 dict(kind="info", pill="MAIN STREET", h1="HOLIDAYS|[o]DOWNTOWN.[/o]", g0=.30, bullets=[
      "The Third Thursday Art Crawl turns downtown shops into pop-up galleries, next on Nov. 19, 4 to 8 p.m.",
      "The free Christmas Village and Tree Lighting is Dec. 3, 5 to 8 p.m., at Walter Y. Elisha Park",
      "The 79th annual Fort Mill Christmas Parade steps off Dec. 5 at 11 a.m. in historic downtown"]),
 dict(kind="info", pill="MY TIP", h1="ASK ABOUT|[o]THE 4% RATIO.[/o]", g0=.30, bullets=[
      "In S.C., a legal residence is assessed at 4% of fair market value; most other real property is at 6%",
      "The 4% ratio isn't automatic: each new owner applies with the York County Assessor's Office",
      "Apply before the first tax penalty date of the first year you claim it, with proof of domicile ready"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 29715 • SEPT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$460,031"), ("Price per sq. ft.", "$216"), ("Active listings", "205"), ("Median days on market", "67")],
      source="Source: Realtor.com Economic Research, ZIP 29715 (Fort Mill SC) monthly listing data, September 2026; viewed Nov. 3, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll walk Main Street, visit the Greenway and Elisha Park, and compare homes before you make an offer.",
      body_9x16v="We'll walk Main Street and the Greenway, then compare homes before an offer.",
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
                    tmp = f"/tmp/fm-jpg-{fmt}-{i:02d}.jpg"; Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(jz, f"{os.path.getsize(os.path.join(D, jz))/1e6:.1f} MB")
        if fmt == "4x5":
            import img2pdf
            open(os.path.join(D, f"{NAME}-DRAFT.pdf"), "wb").write(img2pdf.convert(pngs))
    return res

def video(pdir=None):
    V = "/tmp/fm-v916"; shutil.rmtree(V, ignore_errors=True); os.makedirs(V)
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
        build(pdir=a[1], outroot="/tmp/fm-preview")
    else: build()
