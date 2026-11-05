# Nov 5 2026 New Construction carousel — Bright Contemporary. Three native sets. NO PDF.
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
# use curated src-use as src/
if not os.path.exists("src"):
    os.symlink("src-use", "src")
elif os.path.islink("src") or os.path.isdir("src"):
    pass
V = "Builder's offer, verified on the builder's site Nov 5, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on Lennar's posted Black Friday Sales Event terms, read Nov 5, 2026. Terms and eligibility set by the builder; subject to change."
LN = "Lennar"
RATE = "Builder's offer: 3.990% FHA 5/1 ARM (7.053% APR) on select homes"
S = [
 dict(kind="cover", credit=LN, src="src/01.jpg", fy=.55, fy_1x1=.7, fy_4x5=.6,
      pill="NEW BUILDS. [y]VERIFIED NOV 5.[/y]", h1="[y]3.990%[/y] FHA 5/1 ARM|(7.053% APR).",
      body="4 Lennar communities in Maiden, Shelby and Newton, NC. Each offer checked on the builder's website Nov 5, 2026.",
      bullets=["Builder's promotional FHA 5/1 ARM: 3.990% (7.053% APR), fixed for 5 years",
               "Builder's terms: sign Nov 2-8, 2026, close by Nov 24, 2026",
               "Plus tips on the fine print before you sign"],
      note="Builder's offers, verified on the builder's site Nov 5, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit=LN, src="src/02.jpg", fy=.5, pill="SHANNON WOODS WALK & ENCLAVE • MAIDEN, NC",
      h1="LARGEST PLANS|[y]+ 3.990%.[/y]", h1size_9x16=88,
      sub="Lennar • select homes",
      bullets=[RATE,
               "Floorplans about 2,016 to 3,269 sq. ft., per the builder",
               "Community pool, cabana, clubhouse and fitness center, per the builder"], note=V),
 dict(kind="deal", credit=LN, src="src/03.jpg", fy=.5, pill="SHANNON WOODS MEADOWS • MAIDEN, NC",
      h1="SINGLE-FAMILY|[y]+ 3.990%.[/y]",
      sub="Lennar • select homes",
      bullets=[RATE,
               "Floorplans about 1,864 to 2,706 sq. ft., per the builder",
               "Clubhouse with a swimming pool, per the builder"], note=V),
 dict(kind="deal", credit=LN, src="src/04.jpg", fy=.45, pill="CLEVELAND HILL • SHELBY, NC",
      h1="FROM THE|[y]LOW $200s.[/y]",
      sub="Lennar • select homes",
      bullets=[RATE,
               "Plans from about 1,043 sq. ft., base price from $240,000, per the builder",
               "Onsite playground; downtown Shelby about 2.5 miles, per the builder"], note=V),
 dict(kind="deal", credit=LN, src="src/05.jpg", fy=.5, pill="BUFFALO RIDGE • NEWTON, NC",
      h1="SINGLE-FAMILY|[y]+ 3.990%.[/y]",
      sub="Lennar • select homes",
      bullets=[RATE,
               "Plans about 1,956 to 2,578 sq. ft., base price from $275,000, per the builder",
               "Builder's terms: Lennar Mortgage required for the rate"], note=V),
 dict(kind="tip", credit=LN, src="src/06.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN",
      h1="THE RATE|[y]ADJUSTS.[/y]",
      sub="From the builder's posted terms",
      bullets=["3.990% stays fixed for the first five years",
               "Starting in year six, the rate adjusts once a year",
               "Ask for the rate, the APR and the adjustment terms in writing"], note=T),
 dict(kind="tip", credit=LN, src="src/07.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN",
      h1="ASK WHICH|[y]HOMES QUALIFY.[/y]", h1size_9x16=88,
      sub="From the builder's posted terms",
      bullets=["The offer is on select new homes, not every homesite",
               "Contracts must be signed Nov 2-8 and close by Nov 24, 2026",
               "Limited funds; the rate may change or run out"], note=T),
 dict(kind="tip", credit=LN, src="src/08.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN",
      h1="LENNAR|[y]MORTGAGE.[/y]",
      sub="From the builder's posted terms",
      bullets=["The rate offer requires financing through Lennar Mortgage",
               "You can still buy with another lender, without this rate",
               "Compare both paths before you lock anything in"], note=T),
 dict(kind="tip", credit=LN, src="src/09.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN",
      h1="NOT|[y]COMBINABLE.[/y]",
      sub="From the builder's posted terms",
      bullets=["This promotion may not be combined with other Lennar offers",
               "Incentives can affect the loan amount",
               "Get the written terms for the home you want"], note=T),
 dict(kind="cta", credit=LN, src="src/10.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the rate, the APR and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# house-number retouch placeholders (inspect after first render)
FIX = {}
import numpy as np
from PIL import Image
def retouched(src):
    if src not in FIX: return src
    out = src.replace("src/", "img-retouched/"); os.makedirs("img-retouched", exist_ok=True)
    a = np.asarray(Image.open(src).convert("RGB")).astype(float).copy()
    for mode, x0, y0, x1, y1 in FIX[src]:
        Tc = a[y0-3:y0-1, x0:x1].mean(0); Bc = a[y1+1:y1+3, x0:x1].mean(0)
        for k, y in enumerate(range(y0, y1)):
            t = (k + 1) / (y1 - y0 + 1); a[y, x0:x1] = Tc * (1 - t) + Bc * t
    Image.fromarray(a.clip(0, 255).astype("uint8")).save(out, quality=97); return out
for sl in S: sl["src"] = retouched(sl["src"])
FMTS = {"4x5": ("img45", D), "1x1": ("img1x1", D + "/slides-1x1"), "9x16": ("img9x16", D + "/slides-9x16")}
only = sys.argv[1:]
for fmt, (imgd, outd) in FMTS.items():
    if only and fmt not in only and not any(a.isdigit() for a in only): continue
    os.makedirs(outd, exist_ok=True); os.makedirs(imgd, exist_ok=True)
    for n, sl in enumerate(S, 1):
        if any(a.isdigit() for a in only) and str(n) not in only: continue
        ph = f"{imgd}/{n:02d}.jpg"
        r = bc.prep_photo(sl["src"], ph, fmt, sl.get("fx", .5), sl.get(f"fy_{fmt}", sl.get("fy", .5)))
        bc.render(sl, ph, f"{outd}/slide-{n:02d}.png", fmt, n, 10, html_dir=".")
        print(fmt, n, "scale=%.2f" % r)
