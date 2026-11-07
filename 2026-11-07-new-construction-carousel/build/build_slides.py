# Nov 7 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme: verified design savings, builder-wide QMI savings, upgrade packages, allowances + amenities (NO interest rates / APR).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 7, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on the builders' posted offer terms, read Nov 7, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="Classica Homes", src="src/01-cover-riverchase-pool.jpg", fy=.6,
      pill="NEW BUILDS. [y]VERIFIED NOV 7.[/y]",
      h1="SAVINGS &|[y]AMENITIES.[/y]",
      body="4 builder offers in Mint Hill, Huntersville and the Charlotte area, NC, plus Lancaster, SC. Each checked on the builder's website Nov 7, 2026.",
      bullets=["Design savings, quick move-in savings, upgrade packages and a lot allowance",
               "From David Weekley, Epcon, Madison-Simmons and Classica",
               "Plus tips on caps, deadlines, upgrade lists and allowances"],
      note="Builder's offers, verified on the builder's site Nov 7, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="David Weekley Homes", src="src/02-whitley-exterior.jpg", fy=.35,
      pill="WHITLEY PRESERVE • MINT HILL, NC",
      h1="UP TO [y]$20,000[/y]|DESIGN SAVINGS.", h1size_9x16=92,
      sub="David Weekley Homes • Park Collection, to-be-built homes",
      bullets=["Half off up to $40,000 in Design Center selections and flex options (max $20,000)",
               "Purchase Oct 1-Dec 31, 2026; present the offer before signing; lot premiums excluded",
               "Park, walking trails, pavilion and playground; walk or bike to Downtown Mint Hill, per the builder"], note=V),
 dict(kind="deal", credit="Epcon Communities", src="src/03-epcon-courtyard-exterior.jpg", fy=.45,
      pill="EPCON COMMUNITIES • CHARLOTTE AREA, NC",
      h1="UP TO [y]$40,000[/y]|IN SAVINGS.",
      sub="Epcon Communities • select Charlotte-area homes",
      bullets=["Up to $40,000 on select quick move-ins; up to $10,000 on select to-be-built homes",
               "Agreements accepted by Nov 30, 2026; quick move-ins close by Dec 15, 2026",
               "Single-level ranch homes with garden courtyards; several Epcon Charlotte communities are 55+"], note=V),
 dict(kind="deal", credit="Madison-Simmons Homes", src="src/04-maxwell-front.jpg", fy=.4,
      pill="TOWNES AT MAXWELL • HUNTERSVILLE, NC",
      h1="[y]$15K[/y] IN BUILDER|UPGRADES.",
      sub="Madison-Simmons Homes • Videri phase townhomes",
      bullets=["Videri phase homes from $509,990 with an additional $15K in builder incentive upgrades",
               "35 townhomes near downtown Huntersville with garage, balcony and green space, per the builder",
               "No end date posted; confirm current incentives with the builder"], note=V),
 dict(kind="deal", credit="Classica Homes", src="src/05-riverchase-clubhouse.jpg", fy=.55,
      pill="RIVERCHASE ESTATES • LANCASTER, SC",
      h1="[y]$100,000[/y] LOT|ALLOWANCE.", h1size_9x16=92,
      sub="Classica Homes • Custom Portfolio homes",
      bullets=["$100,000 Lot Development Allowance included in the starting price, per Classica",
               "Homesites sold separately; 1-acre wooded homesites along the Catawba River",
               "Clubhouse, resort pool with lap lanes, tennis and pickleball courts, fitness center, trails"], note=V),
 dict(kind="tip", credit="David Weekley Homes", src="src/06-whitley-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="HALF OFF|HAS A [y]CAP.[/y]",
      sub="Do the math on design savings",
      bullets=["Half off up to $40,000 in selections tops out at a $20,000 credit",
               "Selections above the cap are paid by you, per the builder's terms",
               "Ask which items count and whether lot premiums are excluded"], note=T),
 dict(kind="tip", credit="Epcon Communities", src="src/07-epcon-courtyard.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="TWO DATES|[y]MATTER.[/y]",
      sub="The sign-by date and the close-by date",
      bullets=["Many offers set a date to sign and a separate date to close",
               "Ask what happens to the incentive if closing moves past the close-by date",
               "Get both dates written into your purchase agreement"], note=T),
 dict(kind="tip", credit="Madison-Simmons Homes", src="src/08-maxwell-balcony.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="ITEMIZE THE|[y]UPGRADES.[/y]",
      sub="Know what an upgrade package includes",
      bullets=["Ask for a written list of each upgrade and its value",
               "Ask if any of it can go toward closing costs instead; the builder decides",
               "An upgrade adds value to you only if you would have chosen it"], note=T),
 dict(kind="tip", credit="Classica Homes", src="src/09-riverchase-pool-lap.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="READ THE|[y]ALLOWANCE.[/y]",
      sub="Know where the allowance ends",
      bullets=["Ask exactly what site work the allowance is meant to cover",
               "Get a written estimate of any costs above the allowance",
               "Confirm whether the homesite price is separate from the home price"], note=T),
 dict(kind="cta", credit="David Weekley Homes", src="src/10-whitley-pavilion.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the dollar incentives and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# House-number plaques (04) and clubhouse address number (05, stone patch cloned from the left) retouched out (horizontal blend from the fascia on both sides). Homes otherwise unaltered.
FIX = {"src/04-maxwell-front.jpg": [("h", 122, 700, 169, 724), ("h", 804, 694, 847, 715), ("h", 1447, 693, 1490, 715)],
       "src/05-riverchase-clubhouse.jpg": [("clone-46", 732, 447, 774, 467)]}
import numpy as np
from PIL import Image
def retouched(src):
    if src not in FIX: return src
    out = src.replace("src/", "img-retouched/"); os.makedirs("img-retouched", exist_ok=True)
    a = np.asarray(Image.open(src).convert("RGB")).astype(float).copy()
    for mode, x0, y0, x1, y1 in FIX[src]:
        if mode.startswith("clone-"):
            dx = int(mode.split("-")[1]); a[y0:y1, x0:x1] = a[y0:y1, x0-dx:x1-dx].copy()
        elif mode == "h":
            for y in range(y0, y1):
                Lc = a[y, x0-4:x0-1].mean(0); Rc = a[y, x1+1:x1+4].mean(0)
                for k, x in enumerate(range(x0, x1)):
                    t = (k + 1) / (x1 - x0 + 1); a[y, x] = Lc * (1 - t) + Rc * t
        else:
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
