"""Community Spotlight: Davidson, NC (ZIP 28036) — Mon Nov 2 2026 — Modern Charlotte Editorial (second set; worked example 2026-11-01-neighborhood-matthews).
Renderer: TEMPLATES/modern_editorial.py (docs TEMPLATES/MODERN_EDITORIAL.md). Images: ORIGINAL generated images (GenerateImage), prompts in
build/IMAGE_PROMPTS.md; raw outputs saved as build/src/gen-NN-raw.(png|jpg|webp), Real-ESRGAN x4 -> build/src/gen-NN.jpg.
Usage:
  python3 build/build_slides.py upscale          # ESRGAN x4 every raw that has no upscaled copy yet
  python3 build/build_slides.py                  # 4:5 + 1:1 + 9:16 sets, PDF, zips (+ JPG zips if a PNG zip > 25 MB)
  python3 build/build_slides.py video            # 9:16 video frames (temp) + youtube-short.mp4 (silent)
  python3 build/build_slides.py preview DIR      # layout test with placeholder photos from DIR/NN.(png|jpg) -> /tmp/dv-preview (never committed)
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-02-neighborhood-davidson"; PLACE = "Davidson · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Davidson", tagline="College. Lake. Greenway.",
      intro="A college town on Lake Norman in northern Mecklenburg County, north of Charlotte.", xy=(.5, .45)),
 dict(kind="info", pill="THE LAKE", h1="A TOWN ON|[o]LAKE NORMAN.[/o]", bullets=[
      "Davidson sits in northern Mecklenburg County, and a portion of the town extends north into Iredell County",
      "The town's western edge follows the shoreline of Lake Norman, a large reservoir on the Catawba River",
      "An arm of the lake on the east side of I-77 is known as Lake Davidson"]),
 dict(kind="info", pill="THE COLLEGE", h1="THE COLLEGE|[o]CAME FIRST.[/o]", xy_1x1=(.5, .85), bullets=[
      "Davidson College opened in 1837, named for Revolutionary War Gen. William Lee Davidson",
      "Its first 469 acres were bought from his son, William Lee Davidson II",
      "The town incorporated as Davidson College in 1879 and changed its name to Davidson in 1891"]),
 dict(kind="info", pill="THE HOMES", h1="PORCHES AND|[o]OLD HOMES.[/o]", g0=.32, bullets=[
      "The Davidson Historic District was added to the National Register of Historic Places in 2009",
      "Its homes range from Greek Revival and Queen Anne to Craftsman bungalows and 1950s modernist houses",
      "Elm Row and Oak Row, two 1837 college dormitories, are the oldest buildings in the district"]),
 dict(kind="info", pill="THE TOWN GREEN", h1="SATURDAYS|[o]ON MAIN STREET.[/o]", g0=.30, bullets=[
      "The Town Green is downtown on Main Street, home to the Davidson library branch at 119 S. Main St.",
      "In season, the town's Concerts on the Green play second and fourth Saturdays, 6 to 8 p.m.",
      "The Davidson Farmers Market sets up at 120 S. Main St. every Saturday through Nov. 21, 9 a.m. to noon"]),
 dict(kind="info", pill="THE GREENWAY", h1="TRAILS|[o]THROUGH TOWN.[/o]", bullets=[
      "Town greenways offer more than six miles of walkable space",
      "Sweetgum, tulip poplar and eastern red cedar line the 2.8-mile Randall R. Kincaid Trail",
      "Abersham Park's paved greenway continues into 200-acre Fisher Farm Park, with four miles of mountain bike trails"]),
 dict(kind="info", pill="LAKE ACCESS", h1="PADDLE|[o]LAKE DAVIDSON.[/o]", bullets=[
      "The town has two public lake-access parks: Parham Park and the Lake Davidson Nature Preserve",
      "The preserve, at 750 Jetton St., has a half-mile lakeside loop trail, picnic tables, a gazebo and a public launch",
      "Town canoe, kayak and paddleboard rentals run April through October, Saturdays 2 to 5 p.m."]),
 dict(kind="info", pill="MY TIP", h1="CHECK THE|[o]DISTRICT FIRST.[/o]", g0=.26, bullets=[
      "Downtown, parts of the campus and North Main Street are in Davidson's local historic district",
      "There, many exterior changes need a Certificate of Appropriateness from the Historic Preservation Commission",
      "National Register listing alone doesn't restrict private owners, so ask which district a home is in before you plan changes"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28036 • SEPT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$711,975"), ("Price per sq. ft.", "$327"), ("Active listings", "112"), ("Median days on market", "71")],
      source="Source: Realtor.com Economic Research, ZIP 28036 (Davidson NC) monthly listing data, September 2026; viewed Nov. 2, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll walk Main Street and the Town Green, visit the lake preserve, and compare homes before you make an offer.",
      body_9x16v="We'll walk Main Street and the lake, then compare homes before you make an offer.",
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
                    tmp = f"/tmp/dv-jpg-{fmt}-{i:02d}.jpg"; Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(jz, f"{os.path.getsize(os.path.join(D, jz))/1e6:.1f} MB")
        if fmt == "4x5":
            import img2pdf
            open(os.path.join(D, f"{NAME}-DRAFT.pdf"), "wb").write(img2pdf.convert(pngs))
    return res

def video(pdir=None):
    V = "/tmp/dv-v916"; shutil.rmtree(V, ignore_errors=True); os.makedirs(V)
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
        build(pdir=a[1], outroot="/tmp/dv-preview")
    else: build()
