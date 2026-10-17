# Oct 17, 2026 new construction carousel. DRAFT — AWAITING DENISE APPROVAL.
# theme="fullbleed_teal" (carousel_style.py): full builder photo on every slide, light teal fade, text bottom-anchored,
# teal #0F4C5C + gold #F2B705. Offers verified on builder sites Oct 17, 2026 (~4:15-5:00 AM ET). Builder photos only.
import sys, zipfile, os, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short
N = "2026-10-17-new-construction-carousel"
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
VER = "<div class='ver'>Verified on the builder's site Oct 17, 2026. Terms can change.</div>"
def cr(b): return f"<div class='cr'>Photo: {b}</div>"
def slide(n, img, inner, builder=None, **k):
    k.setdefault("theme", "fullbleed_teal"); k.setdefault("h1", 112); k.setdefault("footer", F); k.setdefault("li", 32)
    return _slide(n, TAG, img, CSS + (cr(builder) if builder else "") + inner, **k)
def deal(lab, offer, who, bullets, h=None):
    return f"<div class='lab'>{lab}</div><h1 style='font-size:{h or 104}px'>{offer}</h1><div class='who'>{who}</div>" + ul(bullets) + VER
S = [
 slide(1, "01.jpg", "<h1 style='font-size:104px'>8 builder deals<br>near <em>Charlotte.</em></h1>"
   "<p class='b' style='margin-top:14px'>7 in North Carolina, 1 in York, SC. Each one checked on the builder's own website on Oct 17, 2026.</p>"
   + ul(["Compare the full monthly payment, not the headline", "Check each deadline and lender rule"]),
   builder="Pulte Homes", band="NEW BUILDS. <em>VERIFIED OCT 17.</em>"),
 slide(2, "02.jpg", deal("ARBOR VILLAGE · MATTHEWS, NC", "<em>$101K</em> in savings.", "Dream Finders Homes",
   ["4009 Grommet Ct: now $444,990 (was $546,500)", "Red Oak plan, move-in ready · 4 bed, 3 bath", "Deadline not stated"]), builder="Dream Finders Homes"),
 slide(3, "03.jpg", deal("ESPLANADE AT NORTHGATE · 55+", "Save <em>$82,625.</em>", "Taylor Morrison · Indian Trail, NC",
   ["Bali, 106 Northgate Blvd: now $374,990, ready now", "Malta, 110 Northgate Blvd: $399,990 (save $79,625)", "Final 2 homes · deadline not stated"]), builder="Taylor Morrison"),
 slide(4, "04.jpg", deal("FERGUS CROSSING · YORK, SC", "<em>$53,140</em> price cut.", "D.R. Horton",
   ["950 Two Brothers Ln: now $325,000 (was $378,140)", "4 bed, 2.5 bath, 2,174 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(5, "05.jpg", deal("CASWELL · NODA, CHARLOTTE", "Save up to <em>$50,000.</em>", "Empire Homes · Smart Move Sales Event",
   ["Price cuts, option credits or closing costs; varies by home", "Pre-sale by 12/31/26; quick delivery by 12/15/26", "Rooftop-terrace townhomes; final opportunities"]), builder="Empire Homes"),
 slide(6, "06.jpg", deal("CARDINAL CREEK · CHARLOTTE, NC", "<em>$39,590</em> price cut.", "D.R. Horton",
   ["12133 Barred Owl Ct: now $375,000 (was $414,590)", "4 bed, 2.5 bath, 1,613 sq ft", "Builder says savings end Nov 1, 2026"]), builder="D.R. Horton"),
 slide(7, "07.jpg", deal("GALLOWAY TOWNS · CHARLOTTE, NC", "<em>$35,000</em> in savings.", "Pulte Homes",
   ["Cooper, Lot 00312: now $420,460 (was $455,460)", "Promo rate 4.75% (5.830% APR) 7/6 ARM", "Est. completion Oct 2026 · deadline not stated"]), builder="Pulte Homes"),
 slide(8, "08.jpg", deal("PAW CREEK · CHARLOTTE, NC", "Up to <em>$16,000</em><br>toward closing.", "Smith Douglas Homes",
   ["Inventory homes, plus blinds and appliance package", "Or presales: $7,500 + half off options up to $15,000", "Under contract by Oct 31, 2026 · preferred lender"], h=100), builder="Smith Douglas Homes"),
 slide(9, "none.jpg", TEAL + "<div class='wm'>4.99%</div>" + deal("ASCOT WOODS · CHARLOTTE, NC", "Rates from <em>4.99%</em><br>(5.864% APR).", "LGI Homes · FHA/VA 5/1 ARM",
   ["Select inventory homes; homes from $395,900", "Sign and close on or before Nov 14, 2026", "Requires LGI's affiliated mortgage brokers"], h=118)),
 slide(10, "10.jpg", "<style>.ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,.15) 26%,rgba(10,52,63,.7) 44%,rgba(9,46,56,.93) 66%,rgba(8,40,50,.96) 100%)!important}.cbox{margin-top:18px}</style>"
   "<h1 style='font-size:84px'>DM or comment <em>DEALS</em><br>and we'll get started.</h1>"
   "<p class='b' style='margin-top:14px;font-size:32px'>I'll help you compare the payment, the deadline and the lender rules on each one.</p>"
   "<div class='ver' style='margin-top:10px'>Builder incentives can change; verify with the builder.</div>",
   builder="Pulte Homes", contact=True),
]
assert len(S) == 10
for soc, vid, _, _ in S:
    low = (soc + vid).lower()
    assert "illustrative" not in low and "one community per slide" not in low and "unsplash" not in low
    assert "swipe" not in vid.lower()
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
