# Nov 8 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme (rev. Nov 8 afternoon): Fort Mill / Grahym removed (outside allowed SC towns).
# Slide 2 is now Pulte West End Heights, Charlotte NC, Was-to-Now price cuts. No interest rates / APR.
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 8, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on the builders' posted offer terms, read Nov 8, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="Classica Homes", src="src/01-cover-stephens-farm-front.jpg", fy=.55,
      pill="NEW BUILDS. [y]VERIFIED NOV 8.[/y]",
      h1="CREDITS &|[y]AMENITIES.[/y]",
      body="3 builder offers in Charlotte and Huntersville, NC. Each checked on the builder's website Nov 8, 2026.",
      bullets=["A price cut, quick move-in savings and a design credit",
               "From Pulte, David Weekley and Classica",
               "Plus a side-by-side compare and tips before you sign"],
      note="Builder's offers, verified on the builder's site Nov 8, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="Pulte Homes", src="src/02-west-end-exterior.jpg", fy=.42,
      pill="WEST END HEIGHTS • CHARLOTTE, NC",
      h1="UP TO [y]$73,000[/y]|OFF THE PRICE.", h1size_9x16=92,
      sub="Pulte Homes • Evans quick move-in townhomes",
      bullets=["Was-to-Now prices on Available Now homes, including $472,605 now $399,605",
               "Other posted Evans cuts run from $61,000 to $72,000, checked on Pulte's site Nov 8, 2026",
               "40 townhomes just west of Uptown; Stewart Creek and Irwin Creek Greenways nearby, per Pulte"],
      note="Prices posted on Pulte's West End Heights page Nov 8, 2026. Availability and price can change."),
 dict(kind="deal", credit="David Weekley Homes", src="src/03-craig-exterior.jpg", fy=.45,
      pill="CENTRAL LIVING AT CRAIG • CHARLOTTE, NC",
      h1="UP TO [y]$40,000[/y]|IN SAVINGS.",
      sub="David Weekley Homes • select quick move-in townhomes",
      bullets=["Up to $40,000 toward a home discount on select quick move-ins, financing with Grace Home Lending",
               "Purchase Nov 1-Dec 6, 2026; close by Dec 22, 2026; present the offer before signing",
               "Three-story townhomes in the Cotswold area; Evergreen Nature Preserve about 2 miles away, per the builder"], note=V),
 dict(kind="deal", credit="Classica Homes", src="src/04-stephens-farm-aerial.jpg", fy=.5,
      pill="STEPHENS FARM • HUNTERSVILLE, NC",
      h1="[y]$40,000[/y] STARTING|POINT CREDIT.", h1size_9x16=92,
      sub="Classica Homes • custom homes priced from $1,606,900",
      bullets=["$40,000 credit included in the starting price for structural options, Design Studio, or off the price, per Classica",
               "42 acres with 22 acres of preserved land and a 1.5-acre central park, per Classica",
               "Buckeye Cove Nature Preserve about 500 feet from the entrance, per Classica"], note=V),
 dict(kind="compare", credit="Pulte Homes", src="src/05-west-end-kitchen.jpg", fy=.45,
      pill="COMPARE • 3 OFFERS",
      h1="COMPARE THE|[y]FINE PRINT.[/y]",
      sub="Three kinds of builder dollars",
      bullets=["West End Heights: a posted price cut already in the asking price",
               "Central Living at Craig: a home discount on select move-in ready homes, with set dates",
               "Stephens Farm: a credit built into the starting price for options or price"], note=T),
 dict(kind="tip", credit="Pulte Homes", src="src/06-west-end-living.jpg", fy=.48,
      pill="TIP • BEFORE YOU SIGN",
      h1="READ THE|[y]WAS AND NOW.[/y]",
      sub="A price cut is already the price",
      bullets=["Pulte shows a previous price and the price it is asking now",
               "Ask what that current price includes before options",
               "Confirm the home is still offered at that price before you sign"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/07-craig-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="PRESENT IT|[y]FIRST.[/y]",
      sub="Some offers must be shown before you sign",
      bullets=["David Weekley's terms say the offer must be presented before signing",
               "Not valid with other offers or on contracts already written, per the builder",
               "Bring the offer page to your first visit and get it in writing"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/08-craig-living.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="KNOW THE|[y]LENDER TERMS.[/y]",
      sub="Many incentives depend on the builder's lender",
      bullets=["Ask which incentives require the builder's affiliated lender",
               "David Weekley's disclosure says buyers are not required to use its lender",
               "Compare full loan estimates side by side before you choose"], note=T),
 dict(kind="tip", credit="Classica Homes", src="src/09-stephens-farm-park-area.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WALK THE|[y]AMENITIES.[/y]",
      sub="Tour what is built, not only the plan",
      bullets=["Visit the parks, trails and common areas in person",
               "Ask what the HOA covers and what the dues are",
               "Confirm which amenities are finished and which are planned"], note=T),
 dict(kind="cta", credit="Classica Homes", src="src/10-stephens-farm-pavilion.jpg", fy=.5,
      h1="DM OR COMMENT [y]DEALS[/y] AND WE'LL GET STARTED.", long=True,
      body="I'll help you compare the communities, the dollar incentives and the fine print on each one.",
      note="Builder incentives can change; verify with the builder."),
]
# House numbers retouched out. Homes otherwise unaltered.
# 02 West End Heights (1920x1280): vertical plaques 1017 (siding), 1013 and 1009 (brick), 1005 (siding).
FIX = {"src/01-cover-stephens-farm-front.jpg": [("v", 1246, 824, 1264, 882)],
       "src/02-west-end-exterior.jpg": [("v", 324, 922, 352, 992), ("v", 702, 912, 732, 996),
                                        ("v", 1078, 932, 1106, 996), ("v", 1440, 916, 1460, 982)],
       "src/03-craig-exterior.jpg": [("vclone-36", 1564, 934, 1616, 970), ("vclone-36", 1070, 902, 1112, 938), ("vclone-36", 586, 912, 632, 948)]}
import numpy as np
from PIL import Image
def retouched(src):
    if src not in FIX: return src
    out = src.replace("src/", "img-retouched/"); os.makedirs("img-retouched", exist_ok=True)
    a = np.asarray(Image.open(src).convert("RGB")).astype(float).copy()
    for mode, x0, y0, x1, y1 in FIX[src]:
        if mode.startswith("vclone-"):
            dy = int(mode.split("-")[1]); a[y0:y1, x0:x1] = a[y0+dy:y1+dy, x0:x1].copy()
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
import zipfile
from PIL import Image as _Image
if not only:
    pairs = [("slides.zip", D), ("slides-1x1.zip", D + "/slides-1x1"), ("slides-9x16.zip", D + "/slides-9x16")]
    for zp, folder in pairs:
        path = os.path.join(D, zp)
        with zipfile.ZipFile(path, "w") as z:
            for i in range(1, 11):
                z.write(os.path.join(folder, f"slide-{i:02d}.png"), f"slide-{i:02d}.png")
        mb = os.path.getsize(path) / 1e6
        print(zp, f"{mb:.1f} MB")
        if mb > 25:
            jz = path.replace(".zip", "-jpg.zip")
            with zipfile.ZipFile(jz, "w") as z:
                for i in range(1, 11):
                    tmp = f"nc-jpg-{i:02d}.jpg"
                    _Image.open(os.path.join(folder, f"slide-{i:02d}.png")).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(os.path.basename(jz), f"{os.path.getsize(jz)/1e6:.1f} MB")
