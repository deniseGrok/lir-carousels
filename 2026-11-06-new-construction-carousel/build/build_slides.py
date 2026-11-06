# Nov 6 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme: verified price cuts & closing credits (NO interest rates / APR).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 6, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on common new-construction incentive terms, read Nov 6, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="David Weekley Homes", src="src/01-cover-encore-harmony.jpg",
      fy=.55, fy_1x1=.7, fy_4x5=.6,
      pill="NEW BUILDS. [y]VERIFIED NOV 6.[/y]",
      h1="PRICE CUTS &|[y]CLOSING CREDITS.[/y]",
      body="5 builder offers in Harrisburg, Concord, Charlotte and Waxhaw, NC. Each offer checked on the builder's website Nov 6, 2026.",
      bullets=["Verified dollar price cuts, closing credits and design credits",
               "Communities from David Weekley, Pulte, Tri Pointe and Classica",
               "Plus tips on Was/Now pricing, credits vs cuts, and preferred-lender terms"],
      note="Builder's offers, verified on the builder's site Nov 6, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="David Weekley Homes", src="src/02-encore-pool-cabana.jpg", fy=.45,
      pill="ENCORE AT HARMONY • HARRISBURG, NC",
      h1="UP TO [y]$40,000[/y]|HOME DISCOUNT.",
      sub="David Weekley Homes • select Charlotte-area quick move-ins",
      bullets=["Builder's offer: up to $40,000 toward a home discount on select quick move-ins",
               "Contracts Nov 1-Dec 6, 2026; close by Dec 22, 2026; Grace Home Lending",
               "55+ community with a shared pool, cabana and outdoor gathering space, per the builder"], note=V),
 dict(kind="deal", credit="Pulte Homes", src="src/03-cannon-run-exterior.jpg", fy=.5,
      pill="CANNON RUN • CONCORD, NC",
      h1="BUILDER'S BEST|[y]PRICE CUTS.[/y]",
      sub="Pulte Homes • quick move-in examples",
      bullets=["Verified Was→Now savings of about $35,000 to $76,000 on select QMIs",
               "Examples: $37,916 and $35,000 off posted Was prices, checked Nov 6",
               "Onsite pool with cabana, per the builder"], note=V),
 dict(kind="deal", credit="Tri Pointe Homes", src="src/04-ascend-exterior.jpg", fy=.5,
      pill="ASCEND • CHARLOTTE / BALLANTYNE, NC",
      h1="UP TO [y]$55,000[/y]|CLOSING CREDIT.", h1size_9x16=92,
      sub="Tri Pointe Homes • eligible MIR and ready-to-build",
      bullets=["Up to $55,000 toward closing costs, price reduction, move-in package and/or Design Studio",
               "Purchase Oct 1-Dec 30, 2026; finance through Tri Pointe Connect",
               "3-story townhomes near GoBallantyne, per the builder"], note=V),
 dict(kind="deal", credit="Tri Pointe Homes", src="src/05-oldtown-exterior.jpg", fy=.5,
      pill="OLD TOWN VILLAGE • WAXHAW, NC",
      h1="UP TO [y]$10,000[/y]|CLOSING CREDIT.",
      sub="Tri Pointe Homes • eligible MIR and ready-to-build",
      bullets=["Up to $10,000 toward closing costs, price reduction and/or Design Studio",
               "Purchase Oct 1-Dec 30, 2026; finance through Tri Pointe Connect",
               "Walkable to historic downtown Waxhaw, per the builder"], note=V),
 dict(kind="deal", credit="Classica Homes", src="src/06-carrington-street.jpg", fy=.55,
      pill="ENCLAVE AT CARRINGTON • CHARLOTTE, NC",
      h1="[y]$40,000[/y] STARTING|[y]POINT CREDIT.[/y]", h1size_9x16=88,
      sub="Classica Homes • included in starting price",
      bullets=["$40,000 Starting Point Credit for design, structural options, or deduct from home cost",
               "Boutique 11-homesite enclave near Piper Glen, per the builder",
               "You choose how to use the credit, per Classica's pricing page"], note=V),
 dict(kind="tip", credit="Pulte Homes", src="src/07-cannon-run-pool.jpg", fy=.45,
      pill="TIP • BEFORE YOU SIGN",
      h1="GET THE|[y]WAS / NOW[/y]|IN WRITING.",
      sub="Before you rely on a price-cut badge",
      bullets=["Ask for the Was price, the Now price and the savings amount in writing",
               "Confirm which homesites still carry the Builder's Best Price badge",
               "Savings can change as inventory moves - verify the day you write"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/08-encore-cabana.jpg", fy=.45,
      pill="TIP • BEFORE YOU SIGN",
      h1="CREDIT VS|[y]PRICE CUT.[/y]",
      sub="Run both nets before you choose",
      bullets=["A closing credit and a price cut do not always leave the same cash at the table",
               "Ask the lender to show the net for each path on the same Loan Estimate",
               "Some credits only apply when you use the builder's preferred lender"], note=T),
 dict(kind="tip", credit="Tri Pointe Homes", src="src/09-ascend-lot5.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="COMPARE|[y]LOAN ESTIMATES.[/y]", h1size_9x16=88,
      sub="Preferred-lender credits need a side-by-side",
      bullets=["Many closing credits require the builder's preferred lender",
               "Compare a preferred-lender Loan Estimate with an outside lender's",
               "Pick the path with the clearer net - not just the bigger headline credit"], note=T),
 dict(kind="cta", credit="Tri Pointe Homes", src="src/10-oldtown-plan4a.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the dollar incentives and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
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
