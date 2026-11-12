# Nov 12 2026 New Construction carousel - Bright Contemporary. Three native sets. NO PDF.
# Theme: verified quick move-in savings, builder flex cash + amenities (NO interest rates / APR).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import bright_contemporary as bc
# Slide 10 contact card: add Denise's email (denise.realty1@gmail.com) to the template's card for this build only (template file unchanged).
import inspect as _insp
_src = _insp.getsource(bc)
_old = "denisewilson.lircarolinas.com<br>704-615-7347<br>"
assert _old in _src
exec(compile(_src.replace(_old, "denisewilson.lircarolinas.com<br>denise.realty1@gmail.com<br>704-615-7347<br>"), bc.__file__, "exec"), bc.__dict__)
import cdp as _cdp, inspect as _i2
# Nov 12: private headless Chrome (own port + fresh profile under the batch folder) so parallel batch renders don't collide.
_cs = _i2.getsource(_cdp.ensure).replace("/tmp/chr-cdp", "/workspace/carousel-batch-2026-11-12/chrome-render-nc")
_cdp.PORT = 9351; exec(compile(_cs, _cdp.__file__, "exec"), _cdp.__dict__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D = os.path.dirname(os.getcwd())
if not os.path.exists("src"):
    os.symlink("src-use", "src")
V = "Builder's offer, verified on the builder's site Nov 12, 2026. Terms and eligibility set by the builder; subject to change."
T = "Tip based on the builders' posted offer terms, read Nov 12, 2026. Terms and eligibility set by the builder; subject to change."
S = [
 dict(kind="cover", credit="David Weekley Homes", src="src/01-cover-encore-streamside-pool.jpg", fy=.6,
      pill="NEW BUILDS. [y]VERIFIED NOV 12.[/y]",
      h1="SAVINGS &|[y]AMENITIES.[/y]",
      body="3 communities in Waxhaw, Matthews and Charlotte, NC. Each offer checked on the builder's website Nov 12, 2026.",
      bullets=["Quick move-in savings and builder flex cash",
               "From David Weekley Homes and Empire Homes",
               "Plus a side-by-side compare and tips before you sign"],
      note="Builder's offers, verified on the builder's site Nov 12, 2026. Terms and eligibility set by the builder; subject to change."),
 dict(kind="deal", credit="David Weekley Homes", src="src/02-encore-streamside-street.jpg", fy=.9,
      pill="ENCORE AT STREAMSIDE • WAXHAW, NC",
      h1="UP TO [y]$40,000[/y]|IN SAVINGS.",
      sub="David Weekley Homes • 55+ community • ready-now homes from $568,900",
      bullets=["Up to $40,000 toward a home discount on select quick move-ins, financing with Grace Home Lending",
               "Purchase Nov 1-Dec 6, 2026; close by Dec 22, 2026; present the offer before signing",
               "Clubhouse, pool, pickleball courts, walking trails and a lifestyle director, per the builder"], note=V),
 dict(kind="deal", credit="David Weekley Homes", src="src/03-townes-cadia-village.jpg", fy=.5,
      pill="CADIA VILLAGE • MATTHEWS, NC",
      h1="[y]$40,000[/y] OFFER|IN MATTHEWS.", h1size_9x16=92,
      sub="David Weekley Homes • The Townes and The Reserve at Cadia Village",
      bullets=["The same up-to-$40,000 offer is listed on both Cadia Village pages, on select quick move-ins",
               "Ready now: a Townes home at $409,990 and Reserve homes from $679,990",
               "Lap pool, community gardens, walking and biking paths, and a future wellness center, per the builder"], note=V),
 dict(kind="deal", credit="Empire Homes", src="src/04-equinox-townhomes.jpg", fy=.5,
      pill="EQUINOX • CHARLOTTE, NC",
      h1="UP TO [y]$45,000[/y]|IN FLEX CASH.", h1size_9x16=92,
      sub="Empire Homes • townhomes starting from $419,900",
      bullets=["Smart Move Sales Event: up to $45,000 in Empire flex cash; amounts vary by community and home",
               "Pre-sale contracts signed by Dec 31, 2026; quick delivery home contracts by Dec 15, 2026",
               "Four-story townhomes with a private rooftop terrace, plus a community pool, near Camp North End"], note=V),
 dict(kind="compare", credit="David Weekley Homes", src="src/05-reserve-cadia-village.jpg", fy=.5,
      pill="COMPARE • 3 COMMUNITIES",
      h1="COMPARE THE|[y]FINE PRINT.[/y]",
      sub="Two builders, two kinds of builder dollars",
      bullets=["Encore at Streamside and Cadia Village: a David Weekley home discount on select quick move-ins",
               "Equinox: Empire flex cash, which may come as a price cut, option credits or closing cost help",
               "Ask each builder for the exact dollar amount on the home you want"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/06-encore-streamside-kitchen.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WATCH|[y]THE DATES.[/y]",
      sub="Sign-by and close-by dates differ",
      bullets=["David Weekley: purchase by Dec 6, 2026 and close by Dec 22, 2026",
               "Empire: quick delivery contracts by Dec 15, 2026; pre-sale contracts by Dec 31, 2026",
               "Check each home's ready date before you plan a move"], note=T),
 dict(kind="tip", credit="Empire Homes", src="src/07-equinox-rooftop-terrace.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="ASK WHAT IT|[y]LEAVES OUT.[/y]",
      sub="Every offer has limits in the fine print",
      bullets=["David Weekley's discount does not apply to options, lot premiums or other incentives",
               "David Weekley's offer is not valid with any other offer or on contracts already written",
               "Empire says incentives vary by community and home, so get your amount in writing"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/08-cadia-village-living.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="KNOW THE|[y]LENDER TERMS.[/y]",
      sub="Some incentives depend on the builder's lender",
      bullets=["David Weekley's savings require financing with Grace Home Lending",
               "Empire's maximum incentive may be tied to one of its preferred lenders",
               "Neither builder requires its lender, so compare full loan estimates side by side"], note=T),
 dict(kind="tip", credit="David Weekley Homes", src="src/09-encore-streamside-living.jpg", fy=.5,
      pill="TIP • BEFORE YOU SIGN",
      h1="WALK THE|[y]AMENITIES.[/y]",
      sub="Tour what is built, not only the plan",
      bullets=["See the clubhouse, pools and trails in person when you can",
               "Cadia Village lists a future wellness center, so ask what is open today",
               "Ask what the HOA covers and what the dues are"], note=T),
 dict(kind="cta", credit="Empire Homes", src="src/10-equinox-dining-living.jpg", fy=.5,
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
