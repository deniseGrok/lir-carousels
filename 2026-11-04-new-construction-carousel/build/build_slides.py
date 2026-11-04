# Nov 4 2026 New Construction carousel — "New Construction — Bright Contemporary" (TEMPLATES/bright_contemporary.py). Three native sets: 4x5, 1x1, 9x16. No PDF (Denise, Nov 1, 2026).
import sys, os; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__))); D = os.path.dirname(os.getcwd())
V = "Builder's offer, verified on the builder's site Nov 4, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on Meritage Homes' posted sales event terms, read Nov 4, 2026. Terms and eligibility set by the builder; subject to change."
MH = "Meritage Homes"
OFF = "Builder's offer: up to $30,000 in flex cash on eligible homes"
S = [
 dict(kind="cover", credit=MH, src="src/brighton-springs__11__aded6aa5bc.jpg", fy=.55, fy_1x1=.8, fy_4x5=.7,
      pill="NEW BUILDS. [y]VERIFIED NOV 4.[/y]", h1="UP TO [y]$30,000[/y]|IN FLEX CASH.",
      body="7 Meritage Homes communities in Charlotte, Mooresville, Stanley and Gastonia, NC, and York, SC. Each offer checked on the builder's website Nov 4, 2026.",
      bullets=["Builder's offer on eligible homes: toward closing costs or a lower rate",
               "Builder's terms: contracts Nov 2-15, 2026, closing by Dec 20, 2026",
               "Plus a tip on the fine print before you sign"],
      note="Builder's offers, verified on the builder's site Nov 4, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit=MH, src="src/brighton-springs__05__8761c8c0c7.jpg", fy=.5, pill="BRIGHTON SPRINGS • YORK, SC", h1="RANCH AND TWO-STORY|[y]+ FLEX CASH.[/y]", h1size_9x16=92,
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Washer, dryer, refrigerator and whole-home blinds included, per the builder",
               "Onsite trails and a pavilion, per the builder's page"], note=V),
 dict(kind="deal", credit=MH, src="src/crossrail-station__00__f13871f56d.jpg", fy=.5, pill="CROSSRAIL STATION • MOORESVILLE, NC", h1="NEW TOWNHOMES|[y]+ FLEX CASH.[/y]",
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Three two-story townhome floorplans, per the builder",
               "Washer, dryer, fridge and whole-home blinds included, per the builder"], note=V),
 dict(kind="deal", credit=MH, src="src/galloway-ridge__06__3710e40257.jpg", fy=.5, pill="GALLOWAY RIDGE • CHARLOTTE, NC", h1="NORTHWEST CHARLOTTE|[y]TOWNHOMES.[/y]", h1size_9x16=92,
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Move-in ready townhomes with washer, dryer, fridge and blinds, per the builder",
               "Community pool, per the builder's page"], note=V),
 dict(kind="deal", credit=MH, src="src/harper-landing__08__476789e799.jpg", fy=.5, pill="HARPER LANDING • STANLEY, NC", h1="UP TO [y]$30,000[/y]|FLEX CASH.",
      sub="Meritage Homes • eligible homes",
      bullets=["Builder's terms: contracts Nov 2-15, 2026, closing by Dec 20, 2026",
               "Ranch and two-story homes, per the builder",
               "Washer, dryer, fridge and whole-home blinds included, per the builder"], note=V),
 dict(kind="deal", credit=MH, src="src/rocky-river-towns__05__e177fdd45a.jpg", fy=.5, pill="ROCKY RIVER TOWNS • CHARLOTTE, NC", h1="MOVE-IN READY|[y]TOWNHOMES.[/y]",
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Open-concept townhome floorplans, per the builder",
               "Washer, dryer, fridge and whole-home blinds included, per the builder"], note=V),
 dict(kind="deal", credit=MH, src="src/avalon__05__e7a8df6588.jpg", fy=.45, pill="AVALON • GASTONIA, NC", h1="[y]FLEX CASH[/y]|IN GASTONIA.",
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Planned community with parks and walking trails, per the builder",
               "A future pool and cabana are planned, per the builder"], note=V),
 dict(kind="deal", credit=MH, src="src/nolen-farm__07__3a226ec26a.jpg", fy=.5, pill="NOLEN FARM • GASTONIA, NC", h1="FENCED YARDS|[y]+ FLEX CASH.[/y]",
      sub="Meritage Homes • eligible homes",
      bullets=[OFF, "Washer, dryer, fridge, blinds and whole-home fencing, per the builder",
               "Pool, splash pad and sports courts, per the builder's page"], note=V),
 dict(kind="tip", credit=MH, src="src/avalon__04__0e1af26e45.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="ASK HOW THE|[y]3% CAP[/y] APPLIES.",
      sub="From the builder's posted terms",
      bullets=["Lender-tied credits are capped at 3% of base price plus lot premium",
               "Flex cash requires the builder's preferred lender and title company",
               "Amounts vary by home; ask for the rate and APR in writing"], note=T),
 dict(kind="cta", credit=MH, src="src/crossrail-station__02__c76260c56f.jpg", fy=.5, h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the terms and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# house numbers retouched out (source px; vertical blend from the clean trim above and below)
FIX = {"src/crossrail-station__00__f13871f56d.jpg": [("v", 1328, 1308, 1352, 1410)],
       "src/galloway-ridge__06__3710e40257.jpg": [("v", 711, 751, 726, 825), ("v", 1546, 671, 1559, 751)],
       "src/harper-landing__08__476789e799.jpg": [("v", 828, 684, 843, 741)],
       "src/brighton-springs__05__8761c8c0c7.jpg": [("v", 769, 580, 785, 652)],
       "src/brighton-springs__11__aded6aa5bc.jpg": [("v", 913, 562, 930, 620)],
       "src/avalon__05__e7a8df6588.jpg": [("v", 800, 806, 822, 884)],
       "src/rocky-river-towns__05__e177fdd45a.jpg": [("v", 796, 702, 812, 774)],
       "src/nolen-farm__07__3a226ec26a.jpg": [("v", 915, 760, 937, 838)]}
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
