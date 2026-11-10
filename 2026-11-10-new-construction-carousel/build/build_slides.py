# Nov 10 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme: verified quick move-in savings, flex cash toward closing costs, a design/starting point credit + amenities (NO interest rates / APR).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 10, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on the builders' posted offer terms, read Nov 10, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="Classica Homes", src="src/01-cover-davidson-retreat-front.jpg", fy=.55,
      pill="NEW BUILDS. [y]VERIFIED NOV 10.[/y]",
      h1="SAVINGS &|[y]AMENITIES.[/y]",
      body="3 builder offers in Charlotte and Davidson, NC. Each checked on the builder's website Nov 10, 2026.",
      bullets=["Quick move-in savings, flex cash and a design credit",
               "From David Weekley, Meritage and Classica",
               "Plus a side-by-side compare and tips before you sign"],
      note="Builder's offers, verified on the builder's site Nov 10, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="David Weekley (rendering)", src="src/02-mcalpine-place-rendering.jpg", fy=.5,
      pill="MCALPINE PLACE • CHARLOTTE, NC",
      h1="UP TO [y]$40,000[/y]|IN SAVINGS.",
      sub="David Weekley Homes • paired villas from $396,990",
      bullets=["Up to $40,000 toward a home discount on select quick move-ins, financing with Grace Home Lending",
               "Purchase Nov 1-Dec 6, 2026; close by Dec 22, 2026; present the offer before signing",
               "New paired villas in east Charlotte with an outdoor gathering space and shade structure, per the builder"], note=V),
 dict(kind="deal", credit="Meritage Homes", src="src/03-russell-grove-exterior.jpg", fy=.5,
      pill="RUSSELL GROVE • CHARLOTTE, NC",
      h1="UP TO [y]$30,000[/y]|IN FLEX CASH.",
      sub="Meritage Homes • single-family homes from $415,550",
      bullets=["Flex cash toward closing costs on eligible homes, using MTH Mortgage and Carefree Title",
               "Contracts Nov 2-15, 2026; close by Dec 20, 2026; amounts vary by home, per Meritage",
               "Lawn maintenance included; a future pool and cabana plus a tot lot, per Meritage"], note=V),
 dict(kind="deal", credit="Classica Homes", src="src/04-davidson-retreat-kitchen.jpg", fy=.5,
      pill="DAVIDSON RETREAT • DAVIDSON, NC",
      h1="[y]$40,000[/y] STARTING|POINT CREDIT.", h1size_9x16=92,
      sub="Classica Homes • custom homes from $1,359,900",
      bullets=["$40,000 credit for structural options, Design Studio selections, or off the home price, per Classica",
               "Six estate-sized homesites; each plan has a 3-car side-load garage",
               "Steps from the Davidson Greenway and minutes from historic Downtown Davidson, per Classica"], note=V),
 dict(kind="compare", credit="Meritage Homes", src="src/05-russell-grove-living.jpg", fy=.5,
      pill="COMPARE • 3 OFFERS",
      h1="COMPARE THE|[y]FINE PRINT.[/y]",
      sub="Three kinds of builder dollars",
      bullets=["McAlpine Place: a home discount on select move-in ready homes, with set dates",
               "Russell Grove: flex cash at closing, tied to the builder's lender and title company",
               "Davidson Retreat: a credit built into the starting price for options or price"], note=T),
 dict(kind="tip", credit="Meritage Homes", src="src/06-russell-grove-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WATCH|[y]TWO DATES.[/y]",
      sub="A sign-by date and a close-by date",
      bullets=["Meritage: contract Nov 2-15, 2026 and close by Dec 20, 2026",
               "David Weekley: purchase by Dec 6, 2026 and close by Dec 22, 2026",
               "Ask the builder which homes can close inside the window"], note=T),
 dict(kind="tip", credit="Classica Homes", src="src/07-davidson-retreat-kitchen-2.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="ASK WHAT IT|[y]LEAVES OUT.[/y]",
      sub="Every offer has limits in the fine print",
      bullets=["David Weekley's discount does not apply to options, lot premiums or other incentives",
               "Meritage says flex cash amounts vary and may not be available on every purchase",
               "Get the exact dollar amount for your home in writing"], note=T),
 dict(kind="tip", credit="Meritage Homes", src="src/08-russell-grove-great-room.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="KNOW THE|[y]LENDER TERMS.[/y]",
      sub="Many incentives depend on the builder's lender",
      bullets=["Both offers ask you to finance with the builder's affiliated lender",
               "You may use another lender or pay cash, but the incentive may not apply",
               "Compare full loan estimates side by side before you choose"], note=T),
 dict(kind="tip", credit="Meritage Homes", src="src/09-russell-grove-dining.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WALK THE|[y]AMENITIES.[/y]",
      sub="Tour what is built, not only the plan",
      bullets=["Some amenities are listed as future or coming soon",
               "Ask what the HOA covers and what the dues are",
               "Confirm which amenities are finished and which are planned"], note=T),
 dict(kind="cta", credit="Classica Homes", src="src/10-davidson-retreat-kitchen-3.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the dollar incentives and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# House numbers retouched out: 01 (128 on the stucco wall, vertical blend) and 03 (5211 on the porch column, vertical blend). Homes otherwise unaltered.
FIX = {"src/01-cover-davidson-retreat-front.jpg": [("v", 908, 728, 926, 782)],
       "src/03-russell-grove-exterior.jpg": [("v", 408, 770, 423, 828)]}
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
