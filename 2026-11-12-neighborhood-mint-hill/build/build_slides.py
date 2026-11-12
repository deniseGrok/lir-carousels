"""Community Spotlight: Mint Hill, NC (Mecklenburg County, ZIP 28227) — Thu Nov 12 2026 — Modern Charlotte Editorial.
NO PDF (Denise Nov 1 2026). Images: ORIGINAL GenerateImage (prompts in build/image-prompts.json); Real-ESRGAN x4.
Slide 7 has dated events (Christmas Parade and Tree Lighting Sat Dec 5, 2026; Mingle & Jingle Dec 11-12, 2026) -> post before Dec 5, 2026.
To finish: put 10 images at build/src/gen-NN-raw.<ext>, then:
  python3 build/finish.py check && python3 build/build_slides.py upscale && python3 build/build_slides.py && python3 build/build_slides.py video && python3 build/finish.py
"""
import os, sys, glob, zipfile, subprocess, shutil
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import modern_editorial as me
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); SRC = os.path.join(B, "src")
NAME = "2026-11-12-neighborhood-mint-hill"; PLACE = "Mint Hill · NC"

SL = [
 dict(kind="cover", discover="Discover", name="Mint Hill", tagline="Parks. History. Hometown events.",
      intro="A Mecklenburg County town whose current charter was ratified March 11, 1971.", xy=(.5, .42)),
 dict(kind="info", pill="THE ROOTS", h1="SETTLED|[o]AROUND 1750.[/o]", bullets=[
      "The Town's history page traces Mint Hill to a community founded around 1750, known then as Clear Creek",
      "Town officials gave up an earlier charter in 1910 so Mecklenburg County would build a road through Mint Hill",
      "The General Assembly ratified the Town's new charter on March 11, 1971 (Session Law 1971-73)"]),
 dict(kind="info", pill="THE VILLAGE", h1="A HISTORIC|[o]VILLAGE TO WALK.[/o]", bullets=[
      "The Carl J. McEwen Historic Village sits at 7601 Matthews-Mint Hill Road, kept by the Mint Hill Historical Society",
      "It includes a restored Country Doctor's Office, the Ira V. Ferguson Country Store, a gold assay office and a blacksmith shop",
      "Tours are by appointment through the Historical Society, with posted admission"]),
 dict(kind="info", pill="THE BIG PARK", h1="50-PLUS ACRES|[o]OF PLAY.[/o]", bullets=[
      "Mint Hill Veterans Memorial Park at 8850 Fairview Road opened in 1997 and covers more than 50 acres",
      "It has five tennis courts, two pickleball courts, a nine-hole disc golf course, three picnic shelters and a one-mile nature trail",
      "The park is home to the N.C. Korean War Veterans Memorial, which honors the 788 North Carolinians killed or missing in that war"]),
 dict(kind="info", pill="THE NEWER PARK", h1="28 ACRES|[o]ON BRIEF ROAD.[/o]", bullets=[
      "Mint Hill Founders Park at 9801 Brief Road is a 28-acre property the Town bought in 2014 with a 50% state PARTF grant",
      "It has an inclusive playground with separate play areas by age, and a 1.3-acre dog park with small and large dog sections",
      "Over a mile of trails is open in daylight; the playground and dog park are lit and open 7 a.m. to 10:30 p.m."]),
 dict(kind="info", pill="THE WOODS", h1="SHADE, TRAILS|[o]AND A NATURE CENTER.[/o]", g0=.30, bullets=[
      "Park on Wilgrove, off Wilgrove-Mint Hill Road, was the Town's first municipal park in 1974, with a wooded perimeter walking trail",
      "Stevens Creek Nature Center and Preserve, a Mecklenburg County site at 15700 Thompson Road, has native animals and an exhibit hall",
      "The Town's splash pad at the Mint Hill Community Center is seasonal and closed Oct. 1 to Memorial Day"]),
 dict(kind="info", pill="THE SEASON", h1="A PARADE AND|[o]A CHRISTMAS MARKET.[/o]", g0=.30, bullets=[
      "The Christmas Parade and Tree Lighting is Saturday, Dec. 5, 2026, 5:30 to 9 p.m. ET, traveling down Matthews-Mint Hill Road",
      "After the parade, the Tree Lighting Ceremony at Town Hall has food trucks and entertainment",
      "Mingle & Jingle is Dec. 11, 2026 (5 to 9 p.m. ET) and Dec. 12, 2026 (11 a.m. to 9 p.m. ET) at the Community Center, with 30-plus market vendors"]),
 dict(kind="info", pill="MY TIP", h1="ASK WHO SERVES|[o]THE ADDRESS.[/o]", g0=.30, bullets=[
      "The Town's utilities page lists Charlotte Water, Piedmont Natural Gas and two electric providers: Duke Energy and Union Power",
      "For homes on a private well or septic system, Mecklenburg County Environmental Health keeps well and septic permit records",
      "On any home, ask which providers serve the address and request recent bills before you make an offer"]),
 dict(kind="stats", pill="THE MARKET", kicker="REALTOR.COM • ZIP 28227 • OCT. 2026", h1="WHAT HOMES [o]LIST FOR.[/o]", h1_9x16="WHAT HOMES|[o]LIST FOR.[/o]", h1_9x16v="WHAT HOMES|[o]LIST FOR.[/o]",
      lines_9x16=2, lines_9x16v=2,
      cards=[("Median list price", "$429,000"), ("Price per sq. ft.", "$221"), ("Active listings", "201"), ("Median days on market", "64")],
      source="Source: Realtor.com Economic Research, ZIP 28227 (Mint Hill mailing ZIP; Realtor.com labels it Charlotte NC) monthly listing data, October 2026; viewed Nov. 12, 2026",
      g0=.16, minTop=.22, xy=(.5, .5)),  # gen-09.jpg pre-cropped to the lower 60% (residential foreground)
 dict(kind="cta", pill="MY RECOMMENDATION", h1="LET'S TOUR IT|[o]TOGETHER.[/o]",
      body="We'll tour homes across Mint Hill, confirm the utilities at each address, and compare homes before you make an offer.",
      body_9x16v="We'll tour Mint Hill homes, then compare before an offer.",
      g0=.22, minTop=.24, minTop_9x16=.38, minTop_9x16v=.37),
]
# Visible source/date labels accompany historical numbers and park measurements.
SOURCES = {
 1:"Source: NC Session Law 1971-73; viewed Nov. 12, 2026",
 2:"Sources: Town of Mint Hill history; NC Session Law 1971-73; viewed Nov. 12, 2026",
 3:"Source: Mint Hill Historical Society; viewed Nov. 12, 2026",
 4:"Source: Town of Mint Hill Parks & Recreation; viewed Nov. 12, 2026",
 5:"Source: Town of Mint Hill, Founders Park; viewed Nov. 12, 2026",
 6:"Sources: Town of Mint Hill; Mecklenburg County Park & Rec; viewed Nov. 12, 2026",
 7:"Source: Mint Hill Events (Town of Mint Hill events); viewed Nov. 12, 2026",
 8:"Sources: Town of Mint Hill utilities; Mecklenburg County Environmental Health; viewed Nov. 12, 2026",
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
                    tmp = os.path.join(B, f"mh-jpg-{fmt}-{i:02d}.jpg"); Image.open(p).convert("RGB").save(tmp, quality=92, subsampling=0)
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
