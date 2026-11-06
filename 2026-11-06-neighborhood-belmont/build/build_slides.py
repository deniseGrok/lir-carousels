"""Community Spotlight: Belmont, NC (ZIP 28012) — Fri Nov 6 2026 — Modern Charlotte Editorial.
NO PDF (Denise Nov 1 2026). Images: ORIGINAL GenerateImage; Real-ESRGAN x4.
Re-created Nov 6 ~7:00 AM ET after build/ (src images + HTML) was wiped by a disk cleanup ~6:30 AM ET.
Fact-check fix Nov 6: slide 8 bullet 1 tax due date (old "due by January 1" -> G.S. 105-360 wording).
To finish: put 10 new images at build/src/gen-NN-raw.jpg, then:
  python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-06-neighborhood-belmont"; PLACE = "Belmont · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Belmont", tagline="Railroad. Mills. River.",
      intro="A historic mill town on the Catawba peninsula, about ten miles west of Charlotte.", xy=(.48, .42)),
 dict(kind="info", pill="THE TOWN", h1="A PENINSULA|[o]WEST OF CHARLOTTE.[/o]", bullets=[
      "Belmont sits in eastern Gaston County on a peninsula formed by the Catawba River and the South Fork",
      "Charlotte lies about ten miles east; Gastonia, the county seat, is about five miles west",
      "Lake Wylie borders the south side of the peninsula"]),
 dict(kind="info", pill="THE HISTORY", h1="FROM GARIBALDI|[o]TO BELMONT.[/o]", bullets=[
      "In 1870, engineer John Garibaldi oversaw a rail fueling station here; the stop was called Garibaldi's Station",
      "By 1873 the Atlanta and Charlotte Airline ran through; the town was renamed Belmont in 1886 and incorporated in 1895",
      "Chronicle Mills, Belmont's first textile mill, was organized in 1901"]),
 dict(kind="info", pill="THE DISTRICT", h1="264 BUILDINGS|[o]ON THE REGISTER.[/o]", g0=.30, bullets=[
      "The Belmont Historic District joined the National Register on Dec. 27, 1996 (NRIS 96001525)",
      "It includes 264 contributing buildings along Main Street and nearby early-1900s neighborhoods",
      "National Register listing alone does not restrict private owners unless they pursue rehab tax credits"]),
 dict(kind="info", pill="THE GARDENS", h1="380 ACRES|[o]ON LAKE WYLIE.[/o]", bullets=[
      "Daniel Stowe Conservancy covers 380 acres at 6500 South New Hope Road on Lake Wylie",
      "The botanical gardens opened in 1999; the property now has more than eight miles of trails",
      "Trails are free daily 7 a.m. to 7 p.m.; The Gardens at Stowe require admission (adult $18.95 + tax)"]),
 dict(kind="info", pill="THE PARKS", h1="DOWNTOWN AND|[o]THE RIVERFRONT.[/o]", bullets=[
      "Stowe Park at 24 S. Main St. has a fountain, two play areas, a pavilion and a walking path",
      "Kevin Loftin Riverfront Park at 1400 Catawba St. sits on the Catawba River",
      "Riverfront amenities include a kayak launch, picnic shelters, a walking path and an amphitheatre"]),
 dict(kind="info", pill="THE ABBEY", h1="A CAMPUS ON|[o]THE NATIONAL REGISTER.[/o]", g0=.30, bullets=[
      "Benedictines have lived at Belmont Abbey since 1876 on Belmont-Mt. Holly Road",
      "The abbey's basilica was built in 1892 and listed on the National Register in 1973 (NRIS 73001343)",
      "The Belmont Abbey Historic District was listed on the National Register in 1993 (NRIS 93000584)"]),
 dict(kind="info", pill="MY TIP", h1="CHECK CITY LIMITS|[o]ON THE TAX BILL.[/o]", g0=.30, bullets=[
      "Gaston County bills and collects property taxes for Belmont; bills go out in July, are due Sept. 1, and can be paid without interest through Jan. 5 (G.S. 105-360)",
      "If the parcel sits inside Belmont's corporate limits, the same bill includes both county and city taxes",
      "Confirm city limits on the parcel map and the Gaston County Tax Office listing before you budget"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28012 • OCT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$513,000"), ("Price per sq. ft.", "$226"), ("Active listings", "169"), ("Median days on market", "61")],
      source="Source: Realtor.com Economic Research, ZIP 28012 (Belmont NC) monthly listing data, October 2026; viewed Nov. 6, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll walk Main Street and Stowe Park, see the Conservancy trails, and compare homes inside Belmont city limits before you make an offer.",
      body_9x16v="We'll walk Main Street and the Conservancy trails, then compare homes before an offer.",
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
                    tmp = os.path.join(B, f"bel-jpg-{fmt}-{i:02d}.jpg"); Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(jz, f"{os.path.getsize(os.path.join(D, jz))/1e6:.1f} MB")
        # NO PDF — Denise rule Nov 1 / Nov 5
        for p in glob.glob(os.path.join(D, "*.pdf")):
            os.remove(p); print("removed PDF", p)
    return res

def video(pdir=None):
    V = os.path.join(B, "v916"); shutil.rmtree(V, ignore_errors=True); os.makedirs(V)
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
        build(pdir=a[1], outroot=os.path.join(B, "preview"))
    else: build()
