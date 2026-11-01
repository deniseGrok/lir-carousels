# Nov 1 2026 New Construction carousel — "New Construction — Bright Contemporary" (TEMPLATES/bright_contemporary.py). Three native sets: 4x5, 1x1, 9x16.
import sys, os; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__))); D = os.path.dirname(os.getcwd())
V = "Builder's offer, verified on the builder's site Nov 1, 2026. Terms and eligibility set by the builder; subject to change."
EW, MI = "Eastwood Homes", "M/I Homes"
S = [
 dict(kind="cover", credit=MI, h1size=82, h1_9x16="5 COMMUNITIES.|[y]2 BUILDERS.[/y]", h1size_9x16=112, src="src/ag_4573203.jpg", fy=.55, pill="NEW BUILDS. [y]VERIFIED NOV 1.[/y]", h1="5 COMMUNITIES. [y]2 BUILDERS.[/y]",
      body="Denver, Stanley, Gastonia, Concord and Locust, NC. Each offer checked on the builder's own website on Nov 1, 2026.",
      bullets=["Up to $5,000 or $3,500 toward closing costs on select Eastwood Homes quick move-ins",
               "Up to 3% of base price toward closing costs on select M/I Homes",
               "Plus 3 slides to compare offers before you sign"],
      note="Builders' offers, verified on the builders' sites Nov 1, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit=EW, src="src/rk_nbhd001.jpg", fy=.5, pill="ROCK CREEK • DENVER, NC", h1="UP TO [y]$5,000[/y] TOWARD CLOSING.",
      sub="Eastwood Homes • select quick move-in homes",
      bullets=["Up to $5,000 in closing costs with an Eastwood Homes preferred lender",
               "Contracts written on or after Jan 1, 2026; not valid on prior contracts",
               "Builder's page lists wooded homesites minutes from Lake Norman"], note=V),
 dict(kind="deal", credit=EW, src="src/ca_003-68dbdf34087f0.jpg", fy=.5, pill="CARRINGTON • STANLEY, NC", h1="UP TO [y]$3,500[/y] TOWARD CLOSING.",
      sub="Eastwood Homes • select quick move-in homes",
      bullets=["Up to $3,500 in closing costs with an Eastwood Homes preferred lender",
               "Applies to select quick move-in homes; not valid on prior contracts",
               "Builder lists a playground plus a planned pool, cabana and pickleball"], note=V),
 dict(kind="deal", credit=MI, src="src/br_5404035.jpg", fy=.55, pill="BOULDER RIDGE • GASTONIA, NC", h1="UP TO [y]3%[/y] TOWARD CLOSING.",
      sub="M/I Homes • select homes",
      bullets=["Up to 3% of base price toward closing costs with M/I Financial",
               "Contract by Dec 1, 2026 and close by Dec 31, 2026",
               "Builder lists ranch and 2-story plans near Crowders Mountain"], note=V),
 dict(kind="deal", credit=MI, src="src/ap_4739251.jpg", fy=.55, pill="ANNSBOROUGH PARK • CONCORD, NC", h1="UP TO [y]3%[/y] OF BASE PRICE.",
      sub="M/I Homes • select homes",
      bullets=["Toward closing costs, prepaids or a rate buydown with M/I Financial",
               "Contract by Dec 1, 2026 and close by Dec 31, 2026",
               "Pool, clubhouse and pickleball courts listed on the builder's page"], note=V),
 dict(kind="deal", credit=MI, src="src/ag_3907706.jpg", fy=.55, pill="AMBER GLEN • LOCUST, NC", h1="UP TO [y]3%[/y] FOR CLOSING COSTS.",
      sub="M/I Homes • select homes",
      bullets=["Up to 3% of base price with M/I Financial; the amount may vary by home",
               "Not usable as a price reduction, per the builder's terms",
               "Builder lists 5-bedroom plans, about 2,700 to 3,500+ sq ft"], note=V),
 dict(kind="compare", credit=MI, src="src/ap_4774541.jpg", fy=.5, pill="COMPARE • [y]DOLLARS VS. PERCENT[/y]", h1="[y]$5,000[/y] OR [y]3%[/y]?",
      sub="Two ways today's builders post closing help",
      bullets=["A dollar cap: Eastwood lists up to $3,500 or $5,000 with its preferred lender",
               "A percent: M/I lists up to 3% of base price with M/I Financial",
               "Ask each builder for the dollar figure on the exact home you like"],
      note="Comparison based on each builder's posted offer terms, read Nov 1, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="tip", credit=EW, src="src/rk_012-6a79d8772985f.jpg", fy=.5, pill="TIP • BEFORE YOU SIGN", h1="ASK WHAT IT [y]COVERS.[/y]",
      sub="From the builders' posted terms",
      bullets=["M/I's credit can go to closing costs, prepaids or a rate buydown, not a price cut",
               "M/I's terms exclude home inspection and radon fees",
               "Both offers use the builder's lender, so compare a second Loan Estimate"],
      note="Tip based on M/I Homes' and Eastwood Homes' posted offer terms, read Nov 1, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="tip", credit=MI, src="src/br_4957984.jpg", fy=.55, pill="TIP • BEFORE YOU SIGN", h1="CHECK THE [y]DATES.[/y]",
      sub="What each builder posts",
      bullets=["M/I Homes: contract by Dec 1, 2026 and close by Dec 31, 2026",
               "Eastwood Homes: contracts on or after Jan 1, 2026; no end date posted",
               "Eastwood says its promotions can change or stop at any time"],
      note="Tip based on M/I Homes' and Eastwood Homes' posted offer terms, read Nov 1, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="cta", credit=EW, src="src/ca_002-68dbd386e02c0.jpg", fy=.5, h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the credit, the lender terms and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# house numbers retouched out of the source (rects in source px; horizontal blend from the clean trim either side)
FIX = {"src/rk_nbhd001.jpg": [(2287, 1400, 2319, 1542)], "src/ag_4573203.jpg": [(1446, 780, 1460, 833)],
       "src/br_5404035.jpg": [(1347, 857, 1363, 915)], "src/br_4957984.jpg": [(1195, 770, 1210, 831)], "src/ag_3907706.jpg": [(1445, 841, 1464, 889)],
       "src/ca_003-68dbdf34087f0.jpg": [(1066, 838, 1086, 922)], "src/ap_4739251.jpg": [(709, 905, 728, 998)], "src/ca_002-68dbd386e02c0.jpg": [(698, 866, 714, 954)]}
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
