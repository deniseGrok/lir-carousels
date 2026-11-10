"""Community Spotlight: Concord, NC (ZIP 28025) — Tue Nov 10 2026 — Modern Charlotte Editorial.
NO PDF (Denise Nov 1 2026). Images: ORIGINAL GenerateImage (prompts in build/image-prompts.json); Real-ESRGAN x4.
Slide 7 has dated events (Nov 20, Nov 21, Speedway Christmas from Nov 20) -> post before Nov 20, 2026.
To finish: put 10 images at build/src/gen-NN-raw.<ext>, then:
  python3 build/finish.py check && python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-10-neighborhood-concord"; PLACE = "Concord · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Concord", tagline="Harmony. Cotton. Racing.",
      intro="The Cabarrus County seat on the I-85 corridor, founded in 1796.", xy=(.5, .42)),
 dict(kind="info", pill="THE ORIGINS", h1="A TOWN NAMED|[o]FOR HARMONY.[/o]", bullets=[
      "Concord was founded in 1796 on a 26-acre site as the seat of the newly formed Cabarrus County, and incorporated in 1806",
      "The name means \"harmony,\" chosen after a compromise over where the county seat would go; the main street became Union Street",
      "After a fire in 1875, a new courthouse rose in 1876; today it is the Historic Cabarrus County Courthouse"]),
 dict(kind="info", pill="THE MILLS", h1="COTTON, RAIL|[o]AND MILLS.[/o]", bullets=[
      "The North Carolina Railroad ran just west of town, making Concord a cotton buying and shipping hub after the Civil War",
      "John M. Odell bought the old Concord Cotton Factory in 1877 and had added three more mills by 1892",
      "J. W. Cannon organized his first textile company in Concord in 1887 and opened a new plant near the railroad in 1892"]),
 dict(kind="info", pill="THE DISTRICT", h1="190 PROPERTIES|[o]ON NORTH UNION.[/o]", g0=.30, bullets=[
      "The North Union Street Historic District joined the National Register on April 15, 1986 (NRIS 86000789)",
      "It spans 190 properties in a 25-block area, running about a mile along tree-lined North Union Street toward downtown",
      "Styles range from Greek Revival and Italianate to Queen Anne, Colonial Revival and bungalow"]),
 dict(kind="info", pill="THE PARK", h1="238 ACRES|[o]AND A 10-ACRE LAKE.[/o]", bullets=[
      "Frank Liske Park is a 238-acre Cabarrus County park on a former working farm, with a refurbished dairy barn and silo",
      "It has a 10-acre lake for fishing and paddle boating, walking and fitness trails, a nature trail and 18-hole mini golf",
      "The city's Hector H. Henry II Greenway follows the Rocky River in three segments with boardwalks and observation decks"]),
 dict(kind="info", pill="THE SPEEDWAY", h1="RACING HERE|[o]SINCE 1960.[/o]", bullets=[
      "Charlotte Motor Speedway is on Concord Parkway South; its 1.5-mile superspeedway hosted the first World 600 on June 19, 1960",
      "The 2,000-plus-acre complex added The Dirt Track at Charlotte in 2000 and zMAX Dragway in 2008",
      "In 2018 the 2.28-mile ROVAL road course oval debuted in the Bank of America ROVAL 400"]),
 dict(kind="info", pill="THE SEASON", h1="HOLIDAYS ON|[o]UNION STREET.[/o]", g0=.30, bullets=[
      "The City of Concord's 29th Annual Tree Lighting Ceremony is Friday, Nov. 20, 6 to 9 p.m., in Downtown Concord; free",
      "The 98th Concord Christmas Parade starts Saturday, Nov. 21, at 2:30 p.m. and ends at Union Street and Corban Avenue",
      "Speedway Christmas lights run Nov. 20, 2026, through Jan. 3, 2027, at Charlotte Motor Speedway (tickets required)"]),
 dict(kind="info", pill="MY TIP", h1="CHECK FOR A|[o]LOCAL DISTRICT.[/o]", g0=.30, bullets=[
      "North and South Union Street are National Register districts; Edgewood is a locally designated historic district",
      "In Concord's local historic districts, many exterior changes need a Certificate of Appropriateness from the Historic Preservation Commission",
      "Before you offer, confirm whether the parcel is in a district and read the city's design standards (siding, windows, porches, roofs, fences, trees)"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28025 • OCT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$339,900"), ("Price per sq. ft.", "$200"), ("Active listings", "214"), ("Median days on market", "58")],
      source="Source: Realtor.com Economic Research, ZIP 28025 (Concord NC, incl. downtown) monthly listing data, October 2026; viewed Nov. 10, 2026",
      g0=.16, minTop=.22),
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll walk North Union Street and downtown, check district rules on any home you like, and compare homes across Concord before you make an offer.",
      body_9x16v="We'll walk North Union Street and downtown, then compare homes before an offer.",
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
                    tmp = os.path.join(B, f"con-jpg-{fmt}-{i:02d}.jpg"); Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
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
