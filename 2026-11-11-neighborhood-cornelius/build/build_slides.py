"""Community Spotlight: Cornelius, NC (Lake Norman, ZIP 28031) — Wed Nov 11 2026 — Modern Charlotte Editorial.
NO PDF (Denise Nov 1 2026). Images: ORIGINAL GenerateImage (prompts in build/image-prompts.json); Real-ESRGAN x4.
Slide 7 has dated events (Christmas Parade Sat Dec 5, 2026) -> post before Dec 5, 2026.
To finish: put 10 images at build/src/gen-NN-raw.<ext>, then:
  python3 build/finish.py check && python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-11-neighborhood-cornelius"; PLACE = "Cornelius · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Cornelius", tagline="Lake. Trails. Arts.",
      intro="A Mecklenburg County town on Lake Norman, incorporated March 4, 1905.", xy=(.5, .42)),
 dict(kind="info", pill="THE LAKE", h1="A LAKE THAT|[o]ROSE IN 1963.[/o]", bullets=[
      "Groundbreaking at Cowan's Ford Dam was Sept. 28, 1959; the lake waters rose in 1963",
      "Lake Norman covers more than 32,000 acres, making it North Carolina's largest manmade lake",
      "The town credits the Duke Power lake with giving Cornelius about 70 miles of lakeside property"]),
 dict(kind="info", pill="THE LAUNCH", h1="FOUR RAMPS|[o]AND A BEACH.[/o]", bullets=[
      "Ramsey Creek Park is a 43-acre Mecklenburg County park on Lake Norman at 18441 Nantz Road in Cornelius",
      "It has four boat ramps with docks, a fishing pier, picnic shelters, nature trails and an enclosed dog park",
      "The lakefront beach has seasonal swimming and posted county fees; check the county schedule before visiting"]),
 dict(kind="info", pill="THE SHORE PARK", h1="104 ACRES|[o]ON THE SHORE.[/o]", bullets=[
      "Jetton Park is a 104-acre Mecklenburg County park at 19000 Jetton Road, on the shores of Lake Norman",
      "It has a playground, large decks, a sandy beach area, tennis courts and walking and biking trails, including a 1.5-mile trail",
      "Waterfront Hall at Jetton Park can be rented for events of up to 80 guests, with views of the lake"]),
 dict(kind="info", pill="THE GREENWAYS", h1="CREEKSIDE TRAILS|[o]AND PONDS.[/o]", bullets=[
      "McDowell Creek Greenway links Birkdale Village, Robbins Park and West Catawba Avenue; check the town's construction detour",
      "Robbins Park on West Catawba Avenue has a nature preserve, two stocked fishing ponds with piers and a boardwalk nearly 600 feet long",
      "Antiquity Greenway links North Zion Avenue to the South Prong Rocky River Greenway in Davidson"]),
 dict(kind="info", pill="THE ORIGINS", h1="A TOWN BUILT|[o]ON COTTON.[/o]", g0=.30, bullets=[
      "Cornelius was founded in 1893 and incorporated on March 4, 1905",
      "Historians trace its start to a Davidson dispute over a town cotton weigher; the firm that opposed it moved just south of Davidson",
      "The town is named for Joseph Benjamin Cornelius, principal stockholder in the cotton mill that followed"]),
 dict(kind="info", pill="THE ARTS", h1="ARTS AND|[o]A HOLIDAY PARADE.[/o]", g0=.30, bullets=[
      "Cain Center for the Arts opened in 2023 with a 400-plus-seat theater, gallery and outdoor plaza",
      "Its Puckett Pottery House on Catawba Avenue offers ceramics facilities and an art courtyard",
      "The Cornelius Christmas Parade is Saturday, Dec. 5, 2026, at 10 a.m. ET, north along Highway 115; Town Hall festivities run until 2 p.m. ET"]),
 dict(kind="info", pill="MY TIP", h1="ASK ABOUT|[o]THE DOCK PERMIT.[/o]", g0=.30, bullets=[
      "Docks, piers, shoreline stabilization and dock maintenance on Duke Energy lake property or in the FERC Project Boundary need Duke Energy Lake Services approval",
      "Duke's lake use applications call for registered surveys, plan and profile drawings, and county or local building permits",
      "On any lakefront home, ask for the existing dock's permit records and check with Lake Services before you plan changes"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28031 • OCT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$530,000"), ("Price per sq. ft.", "$294"), ("Active listings", "182"), ("Median days on market", "71")],
      source="Source: Realtor.com Economic Research, ZIP 28031 (Cornelius NC) monthly listing data, October 2026; viewed Nov. 11, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll tour lake and in-town homes, check dock permits on any waterfront listing, and compare homes across Cornelius before you make an offer.",
      body_9x16v="We'll tour lake and in-town homes, then compare before an offer.",
      g0=.22, minTop=.24, minTop_9x16=.38, minTop_9x16v=.37),
]
# Visible source/date labels accompany historical numbers and park measurements.
SOURCES = {
 1:"Source: Town of Cornelius, Town History; viewed Nov. 11, 2026",
 2:"Sources: NC DNCR; Town of Cornelius history; viewed Nov. 11, 2026",
 3:"Source: Mecklenburg County Park & Recreation; viewed Nov. 11, 2026",
 4:"Sources: Mecklenburg County; Cornelius trails; viewed Nov. 11, 2026",
 5:"Source: Town of Cornelius greenways and Robbins Park; viewed Nov. 11, 2026",
 6:"Source: Town of Cornelius, Town History; viewed Nov. 11, 2026",
 7:"Sources: Cain Center; Old Town Cornelius; Town; viewed Nov. 11, 2026",
 8:"Source: Duke Energy Lake Services; viewed Nov. 11, 2026",
}
_original_inner = me.inner
def _sourced_inner(sl, fmt, n, total):
    body,extra = _original_inner(sl,fmt,n,total)
    if n in SOURCES:
        src='<div class="src">'+me.H.escape(SOURCES[n])+'</div>'
        if sl["kind"]=="info":body=body.replace('</ul></div>', '</ul>'+src+'</div>', 1)
        elif sl["kind"]=="cover":body=body.replace('<div class="dw">',src+'<div class="dw">',1)
        extra += '.src{font-weight:500;font-size:20px;line-height:1.3;margin-top:14px;color:#F5F0E8;text-shadow:0 1px 6px #000}'
    return body,extra
me.inner=_sourced_inner

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
                    tmp = os.path.join(B, f"cor-jpg-{fmt}-{i:02d}.jpg"); Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
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
