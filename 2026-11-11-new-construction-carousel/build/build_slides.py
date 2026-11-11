# Nov 11 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme: verified quick move-in savings, closing cost help, a reduced list price + amenities (NO interest rates / APR).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
# Slide 10 contact card: add Denise's email (denise.realty1@gmail.com) to the template's card for this build only (template file unchanged).
import inspect as _insp
_src = _insp.getsource(bc)
_old = "denisewilson.lircarolinas.com<br>704-615-7347<br>"
assert _old in _src
exec(compile(_src.replace(_old, "denisewilson.lircarolinas.com<br>denise.realty1@gmail.com<br>704-615-7347<br>"), bc.__file__, "exec"), bc.__dict__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 11, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on the builders' posted offer terms, read Nov 11, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="David Weekley Homes", src="src/01-cover-north-creek-village-twilight.jpg", fy=.55,
      pill="NEW BUILDS. [y]VERIFIED NOV 11.[/y]",
      h1="PRICE CUTS &|[y]AMENITIES.[/y]",
      body="3 builder offers in Huntersville, Pineville and Shelby, NC. Each checked on the builder's website Nov 11, 2026.",
      bullets=["Quick move-in savings, closing cost help and a reduced price",
               "From David Weekley, Stanley Martin and Taylor Morrison",
               "Plus a side-by-side compare and tips before you sign"],
      note="Builder's offers, verified on the builder's site Nov 11, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="David Weekley Homes", src="src/02-north-creek-village-townhomes.jpg", fy=.5,
      pill="NORTH CREEK VILLAGE • HUNTERSVILLE, NC",
      h1="UP TO [y]$40,000[/y]|IN SAVINGS.",
      sub="David Weekley Homes • ready-now townhomes from $439,382",
      bullets=["Up to $40,000 toward a home discount on select quick move-ins, financing with Grace Home Lending",
               "Purchase Nov 1-Dec 6, 2026; close by Dec 22, 2026; present the offer before signing",
               "Townhomes with detached garages and fenced yards; trails, a gazebo and a playground, per the builder"], note=V),
 dict(kind="deal", credit="Stanley Martin (rendering)", src="src/03-coventry-rendering.jpg", fy=.6,
      pill="COVENTRY • PINEVILLE, NC",
      h1="UP TO [y]$15,000[/y]|TOWARD CLOSING.", h1size_9x16=92,
      sub="Stanley Martin • townhomes priced from $399,000",
      bullets=["Up to $15,000 toward closing costs for a limited time, per Stanley Martin",
               "No end date is posted, so ask the builder for the full terms in writing",
               "Resort-style pool and cabana, scenic walking trails and double covered porches, per the builder"], note=V),
 dict(kind="deal", credit="Taylor Morrison", src="src/04-fincastle-glen-exterior.jpg", fy=.5,
      pill="FINCASTLE GLEN • SHELBY, NC",
      h1="SAVE [y]$12,510[/y]|ON A READY HOME.", h1size_9x16=92,
      sub="Taylor Morrison • 302 Fincastle Glen Road, now $268,990",
      bullets=["Was $281,500, now $268,990: a 3-bed Linville plan with a Nov 1, 2026 ready date",
               "Other ready homes show cuts too, like $284,990, down from $295,530",
               "A butterfly garden on site, steps from Food Lion and minutes from Uptown Shelby, per the builder"], note=V),
 dict(kind="compare", credit="David Weekley Homes", src="src/05-north-creek-village-dining.jpg", fy=.5,
      pill="COMPARE • 3 OFFERS",
      h1="COMPARE THE|[y]FINE PRINT.[/y]",
      sub="Three kinds of builder dollars",
      bullets=["North Creek Village: a home discount on select move-in ready homes, with set dates",
               "Coventry: closing cost help for a limited time, with no posted end date",
               "Fincastle Glen: a lower list price shown right on the home"], note=T),
 dict(kind="tip", credit="Stanley Martin", src="src/06-coventry-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WATCH|[y]THE DATES.[/y]",
      sub="Sign-by, close-by and limited time",
      bullets=["David Weekley: purchase by Dec 6, 2026 and close by Dec 22, 2026",
               "Stanley Martin says limited time with no end date, so ask for one",
               "Taylor Morrison lists a ready date on each home; confirm it before you plan a move"], note=T),
 dict(kind="tip", credit="Taylor Morrison", src="src/07-fincastle-glen-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="ASK WHAT IT|[y]LEAVES OUT.[/y]",
      sub="Every offer has limits in the fine print",
      bullets=["David Weekley's discount does not apply to options, lot premiums or other incentives",
               "David Weekley's offer is not valid with any other offer",
               "Get the current price and the exact dollar amount for your home in writing"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/08-north-creek-village-living.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="KNOW THE|[y]LENDER TERMS.[/y]",
      sub="Some incentives depend on the builder's lender",
      bullets=["David Weekley's savings require financing with Grace Home Lending",
               "You are not required to use that lender, but the incentive may not apply",
               "Compare full loan estimates side by side before you choose"], note=T),
 dict(kind="tip", credit="Taylor Morrison", src="src/09-fincastle-glen-living.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WALK THE|[y]AMENITIES.[/y]",
      sub="Tour what is built, not only the plan",
      bullets=["See the pool, trails and playgrounds in person when you can",
               "Ask what the HOA covers and what the dues are",
               "Confirm which amenities are finished and which are planned"], note=T),
 dict(kind="cta", credit="Stanley Martin", src="src/10-coventry-family-room.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the dollar incentives and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# House number retouched out: 02 (10511 on the porch column, vertical blend). Homes otherwise unaltered.
FIX = {"src/02-north-creek-village-townhomes.jpg": [("v", 1116, 540, 1140, 665)]}
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
