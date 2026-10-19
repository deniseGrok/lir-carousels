# Oct 19, 2026 new construction carousel. DRAFT — AWAITING DENISE APPROVAL.
# theme="fullbleed_teal" (carousel_style.py): full builder photo on every slide, light teal fade, text bottom-anchored,
# teal #0F4C5C + gold #F2B705. Offers verified on builder sites Oct 19, 2026 (~4:20-4:40 AM ET). Builder photos only.
import sys, zipfile, os, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short
N = "2026-10-19-new-construction-carousel"
D = "/workspace/lir-ai-team/content-research/carousels/" + N
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
VER = "<div class='ver'>Verified on the builder's site Oct 19, 2026. Terms can change.</div>"
def cr(b): return f"<div class='cr'>Photo: {b}</div>"
def slide(n, img, inner, builder=None, **k):
    k.setdefault("theme", "fullbleed_teal"); k.setdefault("h1", 112); k.setdefault("footer", F); k.setdefault("li", 32)
    soc, vid, b, c = _slide(n, TAG, img, CSS + (cr(builder) if builder else "") + inner, **k)
    return soc.replace(" · SWIPE →", ""), vid, b, c
def deal(lab, offer, who, bullets, h=None):
    return f"<div class='lab'>{lab}</div><h1 style='font-size:{h or 104}px'>{offer}</h1><div class='who'>{who}</div>" + ul(bullets) + VER
S = [
 slide(1, "01.jpg", "<h1 style='font-size:104px'>8 builder deals<br>near <em>Charlotte.</em></h1>"
   "<p class='b' style='margin-top:14px'>Charlotte, Indian Trail, Mint Hill, Concord area and Gastonia. Each one checked on the builder's own website on Oct 19, 2026.</p>"
   + ul(["Compare the full monthly payment, not the headline", "Check each deadline and lender rule"]),
   builder="Empire Homes", band="NEW BUILDS. <em>VERIFIED OCT 19.</em>"),
 slide(2, "02.jpg", deal("ANDERSON STREET TOWNHOMES · NODA", "<em>$87,410</em> price cut.", "D.R. Horton · Charlotte, NC",
   ["829 Hammers Ln: now $375,000 (was $462,410)", "3 bed, 2.5 bath, 4-story townhome, 1,373 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(3, "03.jpg", deal("SONOMA HILLS · CHARLOTTE, NC", "<em>$83,090</em> price cut.", "D.R. Horton",
   ["5560 Pamplona Way: now $465,000 (was $548,090)", "Robie with basement: 5 bed, 3 bath, 2,368 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(4, "04.jpg", deal("REEDY CREEK PRESERVE · CHARLOTTE", "<em>$48,590</em> price cut.", "D.R. Horton",
   ["5117 Parker Forest Rd: now $385,000 (was $433,590)", "3 bed, 2.5 bath, 1,749 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(5, "05.jpg", deal("SKYBROOK CORNERS · HUNTERSVILLE, NC", "<em>$33,140</em> price cut.", "D.R. Horton · Concord area",
   ["1231 & 1235 White Birch Ave: $389,000 (was $422,140)", "Lansing townhome: 3 bed, 2.5 bath, 1,699 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(6, "06.jpg", deal("INDIAN TRAIL TOWNHOMES · INDIAN TRAIL, NC", "Save <em>$49,865.</em>", "Taylor Morrison",
   ["Vail II, 344 Sunland Alley: now $345,990 (was $395,855)", "3 bed, 2.5 bath, 1,906 sq ft · ready Nov to Dec 2026", "Reduced price applies to closings by Dec 31, 2026"]), builder="Taylor Morrison"),
 slide(7, "07.jpg", deal("CALICO RIDGE · INDIAN TRAIL, NC", "Up to <em>$40,000</em><br>in flex cash.", "Empire Homes · Smart Move Sales Event",
   ["Use it for design, move-in package, financing or buydown", "Plus $10,000 Empire Financing with the preferred lender", "Pre-sales by Dec 31, 2026 · quick-delivery by Dec 15"], h=100), builder="Empire Homes"),
 slide(8, "08.jpg", deal("OAK CREEK · MINT HILL, NC", "Savings up to <em>$40,000</em><br>on inventory homes.", "Empire Homes · Smart Move Sales Event",
   ["Or up to $10,000 flex cash + $10,000 Empire Financing", "Finished basements included on select homesites", "Quick-delivery contracts by Dec 15, 2026 · amounts vary"], h=92), builder="Empire Homes"),
 slide(9, "none.jpg", TEAL + "<div class='wm'>4.99%</div>" + deal("RHYNE COURT · GASTONIA, NC", "Rates from <em>4.99%</em><br>(5.864% APR).", "LGI Homes · FHA/VA 5/1 ARM",
   ["Select inventory townhomes", "Sign and close on or before Nov 14, 2026", "Requires LGI's affiliated mortgage brokers; limited funds"], h=118)),
 slide(10, "10.jpg", "<style>.ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,.15) 26%,rgba(10,52,63,.7) 44%,rgba(9,46,56,.93) 66%,rgba(8,40,50,.96) 100%)!important}.cbox{margin-top:18px}</style>"
   "<h1 style='font-size:84px'>DM or comment <em>DEALS</em><br>and we'll get started.</h1>"
   "<p class='b' style='margin-top:14px;font-size:32px'>I'll help you compare the payment, the deadline and the lender rules on each one.</p>"
   "<div class='ver' style='margin-top:10px'>Builder incentives can change; verify with the builder.</div>",
   builder="Empire Homes", contact=True),
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
