# Oct 22, 2026 new construction carousel. DRAFT — AWAITING DENISE APPROVAL.
# theme="fullbleed_teal" (carousel_style.py): full builder photo on every slide, light teal fade, text bottom-anchored,
# teal #0F4C5C + gold #F2B705. Offers verified on builder sites Oct 22, 2026 (~4:20-4:50 AM ET). Builder photos only.
import sys, zipfile, os, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short
N = "2026-10-22-new-construction-carousel"
D = "/workspace/repos/lir-carousels/" + N
TAG = "NEW BUILD DEALS<br>NC + SC"; F = "NEW CONSTRUCTION"
CSS = ("<style>.cr{position:fixed;top:40px;right:40px;z-index:4;background:rgba(15,76,92,.78);color:#fff;font-family:'Inter';"
       "font-weight:600;font-size:30px;padding:10px 18px;border-radius:12px;border-bottom:3px solid #F2B705}"
       ".tag{line-height:1.15}.lab{color:#F2B705!important;font-size:32px;letter-spacing:1.5px;margin-bottom:6px}"
       ".who{font-family:'Montserrat';font-weight:800;font-size:34px;color:#fff;margin-top:12px;text-shadow:0 2px 10px rgba(0,0,0,.7)}"
       "h1{color:#fff}h1 em{color:#F2B705}ul{margin-top:18px}li{margin-bottom:10px;font-size:32px}"
       ".ver{font-size:30px;font-weight:600;color:#E6F0F2;margin-top:8px;text-shadow:0 2px 8px rgba(0,0,0,.7)}"
       ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 44%,rgba(10,52,63,.5) 58%,rgba(9,46,56,.86) 76%,rgba(8,40,50,.94) 100%)!important}"
       "</style>")
TEAL = "<style>.ph{display:none!important}html,body,.s{background:radial-gradient(circle at 80% 18%,#16627A 0,#0F4C5C 55%,#0B3D4A 100%)!important}.wm{position:fixed;left:44px;top:150px;font-family:'Anton';font-size:330px;line-height:1;color:rgba(255,255,255,.07);letter-spacing:2px}.gl{position:fixed;left:56px;top:540px;width:160px;height:8px;background:#F2B705;border-radius:4px}</style>"
VER = "<div class='ver'>Verified on the builder's site Oct 22, 2026. Terms can change.</div>"
def cr(b): return f"<div class='cr'>Photo: {b}</div>"
def slide(n, img, inner, builder=None, **k):
    k.setdefault("theme", "fullbleed_teal"); k.setdefault("h1", 112); k.setdefault("footer", F); k.setdefault("li", 32)
    soc, vid, b, c = _slide(n, TAG, img, CSS + (cr(builder) if builder else "") + inner, **k)
    return soc.replace(" · SWIPE →", ""), vid, b, c
def deal(lab, offer, who, bullets, h=None):
    return f"<div class='lab'>{lab}</div><h1 style='font-size:{h or 104}px'>{offer}</h1><div class='who'>{who}</div>" + ul(bullets) + VER
S = [
 slide(1, "01.jpg", "<h1 style='font-size:104px'>7 builder deals<br>near <em>Charlotte.</em></h1>"
   "<p class='b' style='margin-top:14px'>Waxhaw, Belmont, Charlotte, Clover SC, Huntersville, Monroe and Midland. Each one checked on the builder's own website on Oct 22, 2026.</p>"
   + ul(["Compare the full monthly payment, not the headline", "Check each deadline and lender rule"]),
   builder="Mattamy Homes", band="NEW BUILDS. <em>VERIFIED OCT 22.</em>"),
 slide(2, "02.jpg", deal("THE BLUFFS AT WESLEY CHAPEL · WAXHAW, NC", "50% off design<br>up to <em>$100,000.</em>", "Toll Brothers · select homes",
   ["Design Studio options at half price on select homes", "Deposit between Oct 3 and Oct 25, 2026", "Not every home qualifies; ask which ones do"], h=98), builder="Toll Brothers"),
 slide(3, "03.jpg", deal("REDHAWK · BELMONT, NC", "<em>$70K</em> price cut.", "Lennar · move-in ready home",
   ["1310 Swift Lane: now $475,000", "Hunter plan: 4 bed, 3.5 bath, 2,790 sq ft", "Builder lists no end date; confirm before you sign"], h=112), builder="Lennar"),
 slide(4, "04.jpg", deal("GRIFFITH LAKES · CHARLOTTE, NC", "50% off design<br>up to <em>$50,000.</em>", "Toll Brothers · select homes",
   ["Deposit between Oct 3 and Oct 25, 2026", "Separate 5.49% (6.27% APR) on select quick-delivery homes", "Rate: sign Oct 8 or later, close by Dec 18, 2026"], h=98), builder="Toll Brothers"),
 slide(5, "05.jpg", deal("ARBOR CHASE · CLOVER, SC", "<em>3.99%</em> first-year<br>rate (6.784% APR).", "Mattamy Homes · 2/1 buydown, FHA",
   ["Select quick move-in townhomes", "Contract Oct 2-31, 2026 · close by Nov 30, 2026", "Payment rises in year 2, then sets at the 5.99% rate"], h=96), builder="Mattamy Homes"),
 slide(6, "06.jpg", deal("WHITAKER POINTE · HUNTERSVILLE, NC", "Up to <em>3%</em><br>toward closing.", "M/I Homes · with M/I Financial",
   ["Contract by Nov 8, close by Dec 31, 2026", "Also: 5.25% (6.039% APR) 30-yr fixed FHA on select homes", "Amount varies by home"], h=110), builder="M/I Homes"),
 slide(7, "07.jpg", deal("TWINLEAF MEADOWS · MONROE, NC", "Rates from <em>4.75%</em><br>(6.602% APR).", "D.R. Horton · FHA 5/1 ARM with DHI Mortgage",
   ["Fixed for 5 years, then adjusts once a year", "1001 Grace Valley Dr: $459,000 (was $465,290)", "Builder says home savings end Nov 1, 2026"], h=100), builder="D.R. Horton"),
 slide(8, "none.jpg", TEAL + "<div class='wm' style='font-size:300px'>55+</div>" + deal("DEL WEBB CAROLINA RIDGE · MIDLAND, NC", "Golf cart<br><em>included.</em>", "Del Webb · 55+ community",
   ["A voucher for a golf cart on new home purchases", "Through Oct 31, 2026 · close by May 31, 2027", "Hometown Heroes: an additional $2,000 off"], h=118)),
 slide(9, "09.jpg", "<div class='lab'>BEFORE YOU PICK ONE</div><h1 style='font-size:96px'>Three kinds of<br><em>rate offers.</em></h1>"
   + ul(["2/1 buydown: lower payment for 2 years, then the full rate", "ARM: fixed for a set time, then it can adjust", "Fixed: the same rate for the life of the loan", "Ask for the APR and the payment after any change"]), builder="Mattamy Homes"),
 slide(10, "10.jpg", "<style>.ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,.15) 26%,rgba(10,52,63,.7) 44%,rgba(9,46,56,.93) 66%,rgba(8,40,50,.96) 100%)!important}.cbox{margin-top:18px;text-align:left!important}</style>"
   "<h1 style='font-size:84px'>DM or comment <em>DEALS</em><br>and we'll get started.</h1>"
   "<p class='b' style='margin-top:14px;font-size:32px'>I'll help you compare the payment, the deadline and the lender rules on each one.</p>"
   "<div class='ver' style='margin-top:10px'>Builder incentives can change; verify with the builder.</div>",
   builder="Toll Brothers", contact=True),
]
assert len(S) == 10
for soc, vid, _, _ in S:
    low = (soc + vid).lower()
    assert "illustrative" not in low and "one community per slide" not in low and "unsplash" not in low
    assert "swipe" not in vid.lower() and "swipe" not in soc.lower()
only = [int(a) for a in sys.argv[1:]]
if only:
    from carousel_style import render
    import shutil
    for i in only:
        soc, vid, _, _ = S[i-1]
        for suf, h in (("", soc), ("-video", vid)):
            hp = f"{D}/build/slide-{i:02d}{suf}.html"; open(hp, "w").write(h)
            subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
                "--window-size=1080,1350",f"--screenshot={D}/slide-{i:02d}{suf}.png","--allow-file-access-from-files",f"file://{hp}"], check=True, capture_output=True)
    sys.exit()
build(S, D, N + "-DRAFT.pdf", D + "/build")
short(D, N + "-youtube-short.mp4", pad="0F4C5C")
with zipfile.ZipFile(D + "/slides.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for i in range(1, 11): z.write(f"{D}/slide-{i:02d}.png", f"slide-{i:02d}.png")
print("done")
# PDF with a DRAFT header strip on each page (same as Oct 16 NC PDF)
from PIL import Image, ImageDraw, ImageFont
fnt = ImageFont.truetype(subprocess.run(["fc-match","-f","%{file}","Montserrat:extrabold"],capture_output=True,text=True).stdout, 34)
pages = []
for i in range(1, 11):
    im = Image.open(f"{D}/slide-{i:02d}.png").convert("RGB"); c = Image.new("RGB", (1080, 1420), "#B00020"); c.paste(im, (0, 70))
    ImageDraw.Draw(c).text((540, 35), "DRAFT — AWAITING DENISE APPROVAL", fill="white", font=fnt, anchor="mm"); pages.append(c)
pages[0].save(f"{D}/{N}-DRAFT.pdf", save_all=True, append_images=pages[1:], resolution=150)
print("pdf done")
