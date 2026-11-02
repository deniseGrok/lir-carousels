# Nov 2 2026 New Construction carousel — "New Construction — Bright Contemporary" (TEMPLATES/bright_contemporary.py). Three native sets: 4x5, 1x1, 9x16. No PDF (Denise, Nov 1, 2026).
import sys, os; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__))); D = os.path.dirname(os.getcwd())
V = "Builder's offer, verified on the builder's site Nov 2, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on Eastwood Homes' posted offer, read Nov 2, 2026. Terms and eligibility set by the builder; subject to change."
EW = "Eastwood Homes"
PKG = "Builder's offer: side-by-side refrigerator, washer and dryer, and window blinds"
S = [
 dict(kind="cover", credit=EW, h1size=80, h1_9x16="4 COMMUNITIES.|[y]MOVE-IN PACKAGE.[/y]", h1size_9x16=104, src="src/ap_0009-reedit.jpg", fy=.5,
      pill="NEW BUILDS. [y]VERIFIED NOV 2.[/y]", h1="4 COMMUNITIES. [y]MOVE-IN PACKAGE.[/y]",
      body="Huntersville, Monroe and Troutman, NC. Each offer checked on Eastwood Homes' own website on Nov 2, 2026.",
      bullets=["Builder's offer on select homes: refrigerator, washer and dryer, and blinds",
               "4 Charlotte-area communities from Eastwood Homes",
               "Plus 4 slides on what to ask before you sign"],
      note="Builder's offers, verified on the builder's site Nov 2, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit=EW, src="src/er_004-6a0b37599340c.jpg", fy=.5, pill="ENCLAVE AT RIVERDALE • HUNTERSVILLE, NC", h1="A [y]MOVE-IN PACKAGE[/y] ON SELECT HOMES.",
      sub="Eastwood Homes • select homes",
      bullets=[PKG, "Ranch, two-story and three-story plans, per the builder's page",
               "Wooded community minutes from Birkdale Village"], note=V),
 dict(kind="deal", credit=EW, src="src/ap_004-6abd69f3954b7.jpg", fy=.5, pill="ASHTON PARK • MONROE, NC", h1="[y]FRIDGE, WASHER, DRYER[/y] AND BLINDS.",
      sub="Eastwood Homes • select homes",
      bullets=["Builder's move-in package on select homes, for a limited time",
               "72 homes with wooded homesites, per the builder's page",
               "Walking trails and a dog park; under 1 mile from the 74 Bypass"], note=V),
 dict(kind="deal", credit=EW, src="src/nc_53028978147.jpg", fy=.55, pill="NORMAN CREEK • TROUTMAN, NC", h1="APPLIANCES [y]+ BLINDS[/y] ON SELECT HOMES.",
      sub="Eastwood Homes • select homes",
      bullets=[PKG, "Pool and cabana listed on the builder's page (may still be under construction)",
               "Easy access to Lake Norman and I-77, per the builder"], note=V),
 dict(kind="deal", credit=EW, src="src/nct_001-6a916410b97e8.jpg", fy=.5, pill="NORMAN CREEK TOWNHOMES • TROUTMAN, NC", h1="TOWNHOMES WITH A [y]MOVE-IN PACKAGE.[/y]",
      sub="Eastwood Homes • select townhomes",
      bullets=[PKG, "Pool and cabana listed on the builder's page (may still be under construction)",
               "Builder's page notes easy access to Lake Norman and I-77"], note=V),
 dict(kind="compare", credit=EW, src="src/nc_amenity_img-8016.jpg", fy=.5, pill="COMPARE • [y]ITEMS VS. DOLLARS[/y]", h1="ITEMS OR [y]DOLLARS?[/y]",
      sub="Two ways builders post incentives",
      bullets=["Today's 4: a move-in package of appliances and blinds from Eastwood Homes",
               "Other builder offers are posted as a dollar or percent toward closing",
               "Ask the builder what the package is worth on the exact home you like"],
      note="Comparison based on Eastwood Homes' posted offer, read Nov 2, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="tip", credit=EW, src="src/ap_016-69f22d58a5772.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="ASK WHICH HOMES [y]QUALIFY.[/y]",
      sub="From the builder's posted offer",
      bullets=["Eastwood lists this package on select homes, not every home",
               "Ask for the list of qualifying homes in the community you like",
               "Make sure the offer is written into your purchase agreement"], note=T),
 dict(kind="tip", credit=EW, src="src/er_028-6a0b388f4822c.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="GET THE [y]DETAILS[/y] IN WRITING.",
      sub="Questions to ask the builder",
      bullets=["Which refrigerator, washer and dryer come with the home",
               "Which windows and rooms get blinds",
               "Whether the package can combine with other builder offers"], note=T),
 dict(kind="tip", credit=EW, src="src/nc_52356138245.jpg", fy=.55, pill="TIP • BEFORE YOU SIGN", h1="CHECK THE [y]DATES.[/y]",
      sub="What the builder posts",
      bullets=["Eastwood says \"for a limited time\"; no end date is posted on its offers page",
               "Builder offers can change, so confirm the offer the day you sign",
               "Compare a Loan Estimate from a second lender, too"], note=T),
 dict(kind="cta", credit=EW, src="src/er_016-6a0b37ecb920c.jpg", fy=.5, h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the package, the terms and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
FIX = {"src/ap_0009-reedit.jpg": [(1692, 1052, 1714, 1174)], "src/nc_52356138245.jpg": [(1430, 940, 1449, 1008)]}  # house numbers retouched out (source px; horizontal blend from the clean column either side)
import numpy as np
from PIL import Image
def retouched(src):
    if src not in FIX: return src
    out = src.replace("src/", "img-retouched/"); os.makedirs("img-retouched", exist_ok=True)
    a = np.asarray(Image.open(src).convert("RGB")).astype(float).copy()
    for x0, y0, x1, y1 in FIX[src]:
        Lc = a[y0:y1, x0-3:x0-1].mean(1); Rc = a[y0:y1, x1+1:x1+3].mean(1)
        for k, x in enumerate(range(x0, x1)):
            t = (k + 1) / (x1 - x0 + 1); a[y0:y1, x] = Lc * (1 - t) + Rc * t
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
