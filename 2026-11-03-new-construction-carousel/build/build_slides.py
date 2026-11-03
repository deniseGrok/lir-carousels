# Nov 3 2026 New Construction carousel — "New Construction — Bright Contemporary" (TEMPLATES/bright_contemporary.py). Three native sets: 4x5, 1x1, 9x16. No PDF (Denise, Nov 1, 2026).
import sys, os; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__))); D = os.path.dirname(os.getcwd())
V = "Builder's offer, verified on the builder's site Nov 3, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on Eastwood Homes' posted offer terms, read Nov 3, 2026. Terms and eligibility set by the builder; subject to change."
EW = "Eastwood Homes"
PKG = "Builder's offer: refrigerator, washer and dryer, and whole-house blinds"
S = [
 dict(kind="cover", credit=EW, h1size=80, h1_9x16="3 COMMUNITIES.|[y]MOVE-IN PACKAGE.[/y]", h1size_9x16=104, src="src/ml_amen_004-682c96fd5caa4.jpg", fy=.5,
      pill="NEW BUILDS. [y]VERIFIED NOV 3.[/y]", h1="3 COMMUNITIES. [y]MOVE-IN PACKAGE.[/y]",
      body="Sherrills Ford and Gastonia, NC. Each offer checked on Eastwood Homes' own website on Nov 3, 2026.",
      bullets=["Builder's offer on select homes: refrigerator, washer and dryer, and blinds",
               "Builder's terms: contracts written by Dec 31, 2026",
               "Plus 4 slides on what to ask before you sign"],
      note="Builder's offers, verified on the builder's site Nov 3, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit=EW, src="src/el_004-66b22a76b0fb3.jpg", fy=.45, pill="THE ENCLAVE AT LAURELBROOK • SHERRILLS FORD, NC", h1="A [y]MOVE-IN PACKAGE[/y] ON SELECT HOMES.",
      sub="Eastwood Homes • select homes",
      bullets=[PKG, "Planned 800-home community, per the builder's page",
               "Less than two miles from Lake Norman; pool and cabana open"], note=V),
 dict(kind="deal", credit=EW, src="src/ml_amen_014-682c971220481.jpg", fy=.5, pill="THE MEADOWS AT LAURELBROOK • SHERRILLS FORD, NC", h1="[y]FRIDGE, WASHER, DRYER[/y] AND BLINDS.",
      sub="Eastwood Homes • select homes",
      bullets=["Builder's move-in package on select homes, contracts by Dec 31, 2026",
               "Basement homesites, per the builder's page",
               "Pool, cabana, pocket parks, recreation field and pickleball courts"], note=V),
 dict(kind="deal", credit=EW, src="src/fl_0014.jpg", fy=.5, pill="FOUNDERS LANDING • GASTONIA, NC", h1="ONE-LEVEL HOMES [y]+ MOVE-IN PACKAGE.[/y]", h1_1x1="ONE-LEVEL HOMES|[y]+ MOVE-IN PACKAGE.[/y]",
      sub="Eastwood Homes • select homes • 55+ community",
      bullets=[PKG, "First-floor primary bedrooms and lawn maintenance, per the builder",
               "Minutes from shopping, dining and I-85, per the builder"], note=V),
 dict(kind="compare", credit=EW, src="src/ml_amen_5.jpg", fy=.5, pill="COMPARE • [y]ITEMS VS. DOLLARS[/y]", h1="ITEMS OR [y]DOLLARS?[/y]",
      sub="Two ways builders post incentives",
      bullets=["Today's 3: a move-in package of appliances and blinds from Eastwood Homes",
               "Other builder offers are posted as a dollar or percent toward closing",
               "Ask the builder what the package is worth on the exact home you like"],
      note="Comparison based on Eastwood Homes' posted offer, read Nov 3, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="tip", credit=EW, src="src/fl_0059.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="ASK WHICH HOMES [y]QUALIFY.[/y]",
      sub="From the builder's posted terms",
      bullets=["Eastwood lists this package on select homes, not every home",
               "Ask for the list of qualifying homes in the community you like",
               "The builder's terms say it is not valid on prior contracts"], note=T),
 dict(kind="tip", credit=EW, src="src/el_068.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="GET THE [y]DETAILS[/y] IN WRITING.",
      sub="What the builder's terms say",
      bullets=["Package lists a side-by-side refrigerator and a top-load washer and dryer",
               "Blinds cover operative windows only, per the builder",
               "Models and blind locations may change, so ask for them in writing"], note=T),
 dict(kind="tip", credit=EW, src="src/fl_0029.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="CHECK THE [y]DATES.[/y]",
      sub="What the builder posts",
      bullets=["Builder's terms: contracts written by Dec 31, 2026",
               "The builder says promotions can stop or change at any time",
               "Confirm the offer is in your purchase agreement the day you sign"], note=T),
 dict(kind="tip", credit=EW, src="src/el_073.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="ASK FOR THE [y]APR[/y] TOO.",
      sub="If a rate offer is mentioned",
      bullets=["Eastwood also mentions below-market rates on some homes",
               "Ask for the rate and the APR in writing for the exact loan",
               "Compare a Loan Estimate from a second lender, too"], note=T),
 dict(kind="cta", credit=EW, src="src/el_012-66b22ac09242e.jpg", fy=.5, h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the package, the terms and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
FIX = {"src/el_004-66b22a76b0fb3.jpg": [("h", 1524, 647, 1553, 664)], "src/fl_0014.jpg": [("c", 1008, 612, 1030, 722)]}  # house numbers retouched out (source px; blend from the clean pixels either side)
import numpy as np
from PIL import Image
def retouched(src):
    if src not in FIX: return src
    out = src.replace("src/", "img-retouched/"); os.makedirs("img-retouched", exist_ok=True)
    a = np.asarray(Image.open(src).convert("RGB")).astype(float).copy()
    for mode, x0, y0, x1, y1 in FIX[src]:
        if mode == "h":
            Lc = a[y0:y1, x0-3:x0-1].mean(1); Rc = a[y0:y1, x1+1:x1+3].mean(1)
            for k, x in enumerate(range(x0, x1)):
                t = (k + 1) / (x1 - x0 + 1); a[y0:y1, x] = Lc * (1 - t) + Rc * t
        elif mode == "c":  # clone the clean siding just to the right (same rows)
            dx = x1 - x0 + 6; a[y0:y1, x0:x1] = a[y0:y1, x0+dx:x1+dx]
        else:
            Tc = a[y0-3:y0-1, x0:x1].mean(0); Bc = a[y1+1:y1+3, x0:x1].mean(0)
            for k, y in enumerate(range(y0, y1)):
                t = (k + 1) / (y1 - y0 + 1); a[y, x0:x1] = Tc * (1 - t) + Bc * t
    Image.fromarray(a.clip(0, 255).astype("uint8")).save(out, quality=97); return out
for sl in S: sl["src"] = retouched(sl["src"])
FMTS = {"4x5": ("img45", D), "1x1": ("img1x1", D + "/slides-1x1"), "9x16": ("img9x16", D + "/slides-9x16")}
only = sys.argv[1:]  # optional: fmt or slide numbers
for fmt, (imgd, outd) in FMTS.items():
    if only and fmt not in only and not any(a.isdigit() for a in only): continue
    for n, sl in enumerate(S, 1):
        if any(a.isdigit() for a in only) and str(n) not in only: continue
        ph = f"{imgd}/{n:02d}.jpg"
        r = bc.prep_photo(sl["src"], ph, fmt, sl.get("fx", .5), sl.get(f"fy_{fmt}", sl.get("fy", .5)))
        bc.render(sl, ph, f"{outd}/slide-{n:02d}.png", fmt, n, 10, html_dir=".")
        print(fmt, n, "scale=%.2f" % r)
