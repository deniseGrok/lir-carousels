# Oct 23, 2026 new construction carousel. DRAFT — AWAITING DENISE APPROVAL.
# theme="fullbleed_teal" (carousel_style.py): full builder photo on every slide, light teal fade, text bottom-anchored,
# teal #0F4C5C + gold #F2B705, tag "NEW BUILD DEALS / NC + SC". Offers verified on builder sites Oct 23, 2026 (~4:15-4:40 AM ET).
# Three NATIVE sets: slide-NN.png 4:5 1080x1350 (IG/LinkedIn) + slide-NN-video.png; slides-1x1/ 1080x1080 (Facebook);
# slides-9x16/ 1080x1920 (Shorts/Reels/TikTok/Stories; key text clear of top 250, bottom 420, right 140). PDF + 3 zips.
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image, ImageDraw, ImageFont
N = "2026-10-23-new-construction-carousel"
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
cs.CONTACT = ("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
              "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
TAG = "NEW BUILD DEALS<br>NC + SC"; F = "NEW CONSTRUCTION"
CSS = ("<style>.cr{position:fixed;top:40px;right:40px;z-index:4;background:rgba(15,76,92,.78);color:#fff;font-family:'Inter';"
       "font-weight:600;font-size:30px;padding:10px 18px;border-radius:12px;border-bottom:3px solid #F2B705}"
       ".tag{line-height:1.15}.lab{color:#F2B705!important;font-size:32px;letter-spacing:1.5px;margin-bottom:6px;text-shadow:0 2px 10px rgba(0,0,0,.8)}"
       ".who{font-family:'Montserrat';font-weight:800;font-size:34px;color:#fff;margin-top:12px;text-shadow:0 2px 10px rgba(0,0,0,.7)}"
       "h1{color:#fff}h1 em{color:#F2B705}ul{margin-top:18px}li{margin-bottom:10px;font-size:32px}"
       ".ver{font-size:30px;font-weight:600;color:#E6F0F2;margin-top:8px;line-height:1.25;text-shadow:0 2px 8px rgba(0,0,0,.7)}"
       ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 36%,rgba(10,52,63,.5) 50%,rgba(9,46,56,.88) 70%,rgba(8,40,50,.95) 100%)!important}"
       "</style>")
VER = "<div class='ver'>Builder's offer, verified on the builder's site Oct 23, 2026. Terms and eligibility set by the builder; subject to change.</div>"
def cr(b): return f"<div class='cr'>Photo: {b}</div>"
def slide(n, inner, builder, **k):
    k.setdefault("theme", "fullbleed_teal"); k.setdefault("h1", 104); k.setdefault("footer", F); k.setdefault("li", 32)
    soc, vid, b, c = cs.slide(n, TAG, f"{n:02d}.jpg", CSS + cr(builder) + inner, **k)
    return soc.replace(" · SWIPE →", ""), vid, b, c
def deal(lab, offer, who, bullets, h=None):
    return f"<div class='lab'>{lab}</div><h1 style='font-size:{h or 100}px'>{offer}</h1><div class='who'>{who}</div>" + ul(bullets) + VER
SL = [
 slide(1, "<h1 style='font-size:104px'>6 builder deals<br>near <em>Charlotte.</em></h1>"
   "<p class='b' style='margin-top:14px'>Charlotte, Salisbury, Monroe and Lancaster SC. Each one checked on the builder's own website on Oct 23, 2026.</p>"
   + ul(["Closing help, rate offers or both: compare the full payment", "Several deadlines land Oct 25 and Oct 31, 2026"]),
   "Lennar", band="NEW BUILDS. <em>VERIFIED OCT 23.</em>"),
 slide(2, deal("TOLL BROTHERS AT THE RIVER DISTRICT · CHARLOTTE, NC", "Up to <em>$25,000</em><br>toward closing.", "Toll Brothers · select homes",
   ["Deposit between Oct 3 and Oct 25, 2026", "Separate 3/2/1 buydown on select homes: 4.125% in year 1 (7.345% APR)",
    "That rate rises each year to the 7.125% note rate in year 4"], h=96), "Toll Brothers"),
 slide(3, deal("WINECOFF · SALISBURY, NC", "Up to <em>$16K</em><br>toward closing.", "Smith Douglas Homes · move-in ready homes",
   ["Under contract by Oct 31, 2026", "Builder's preferred lender required", "Presales instead: up to $9,000 closing plus half off options up to $30,000"], h=104), "Smith Douglas Homes"),
 slide(4, deal("BAILEY RUN · CHARLOTTE, NC", "<em>3.99%</em> first-year<br>rate (6.784% APR).", "Mattamy Homes · 2/1 buydown, FHA",
   ["Select quick move-in townhomes", "Contract Oct 2-31, 2026 · close by Nov 30, 2026", "4.99% in year 2, then the 5.99% fixed rate; Mattamy Home Funding"], h=94), "Mattamy Homes"),
 slide(5, deal("WILLOUGHBY PARK · MONROE, NC", "<em>5.25%</em> fixed<br>(6.039% APR).", "M/I Homes · 30-yr fixed FHA, M/I Financial",
   ["Select homes · contract Oct 11-Nov 8, close by Dec 31, 2026", "Also: up to 3% of base price toward closing with M/I Financial", "Single-story ranch home designs"], h=104), "M/I Homes"),
 slide(6, deal("ROSELYN · LANCASTER, SC", "Up to <em>$7,500</em><br>toward closing.", "Lennar · select homes, with Lennar Mortgage",
   ["Plus an FHA 5/1 ARM fixed at 4.500% for 5 years (7.529% APR)", "Sign Oct 19-25, 2026 · close by Nov 24, 2026", "Ranch-style home designs; ask which homes qualify"], h=100), "Lennar"),
 slide(7, deal("THE VINES · CHARLOTTE, NC", "<em>4.500%</em> ARM<br>(7.529% APR).", "Lennar · FHA 5/1 ARM with Lennar Mortgage",
   ["Fixed for 5 years, then adjusts once a year", "Plus up to $7,500 toward closing costs", "Sign Oct 19-25, 2026 · close by Nov 24, 2026 · select homes"], h=104), "Lennar"),
 slide(8, "<div class='lab'>BEFORE YOU PICK ONE</div><h1 style='font-size:100px'>Closing help<br>or a <em>lower rate?</em></h1>"
   + ul(["Closing credit: less cash due at the closing table", "Buydown: a lower payment for the first years, then the full rate",
         "ARM: fixed for a set time, then it can adjust", "Ask for the APR and the payment after any change"]), "Mattamy Homes"),
 slide(9, "<div class='lab'>READ THE FINE PRINT</div><h1 style='font-size:100px'>Four questions<br>to <em>ask first.</em></h1>"
   + ul(["Which homes qualify for this offer?", "Is the builder's lender required?", "What are the contract and closing deadlines?", "Can two offers be combined?"]), "Mattamy Homes"),
 slide(10, "<style>.ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,.15) 26%,rgba(10,52,63,.7) 44%,rgba(9,46,56,.93) 66%,rgba(8,40,50,.96) 100%)!important}.cbox{margin-top:18px;text-align:left!important}</style>"
   "<h1 style='font-size:84px'>DM or comment <em>DEALS</em><br>and we'll get started.</h1>"
   "<p class='b' style='margin-top:14px;font-size:32px'>I'll help you compare the payment, the deadline and the lender rules on each one.</p>"
   "<div class='ver' style='margin-top:10px'>Builder incentives can change; verify with the builder.</div>",
   "M/I Homes", contact=True),
]
assert len(SL) == 10
for soc, vid, _, _ in SL:
    low = (soc + vid).lower()
    assert "illustrative" not in low and "one community per slide" not in low and "unsplash" not in low and "pexels" not in low and "swipe" not in low
# Native 9:16 overrides
V916 = ("<style>html,body,.s{width:1080px!important;height:1920px!important}.ph{height:1920px!important;width:1080px!important}"
        ".tag{top:270px!important}.cr{top:270px!important;right:160px!important}.c{left:56px!important;right:160px!important;bottom:500px!important}"
        ".ft{left:56px!important;right:160px!important;bottom:436px!important}"
        ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 18%,rgba(10,52,63,0) 34%,rgba(10,52,63,.5) 46%,rgba(9,46,56,.88) 62%,rgba(8,40,50,.92) 100%)!important}"
        ".s h1{font-size:88px!important}.s li{font-size:32px}</style>")
V916_10 = ("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 14%,rgba(10,52,63,.1) 24%,rgba(10,52,63,.6) 36%,rgba(9,46,56,.9) 52%,rgba(8,40,50,.94) 100%)!important}.s h1{font-size:76px!important}</style>")
def to916(h, i):
    return h.replace("url('img/", "url('9x16/img/").replace("</head>", V916 + (V916_10 if i == 10 else "") + "</head>")
# Native 1:1 overrides (square Facebook carousel)
V11 = ("<style>html,body,.s{width:1080px!important;height:1080px!important}.ph{height:1080px!important;width:1080px!important}"
       ".c{bottom:92px!important}.ft{bottom:36px!important}.s h1{font-size:62px!important;line-height:1.02}.s li{font-size:30px;line-height:1.22;margin-bottom:6px}"
       ".s ul{margin-top:12px}.band{font-size:44px!important;padding:10px 22px!important;margin-bottom:12px!important}.s p.b{font-size:30px;line-height:1.28;margin-top:10px}"
       ".lab{font-size:30px!important;margin-bottom:4px}.who{font-size:30px!important;margin-top:8px}.ver{font-size:30px;margin-top:6px;line-height:1.2}"
       ".cr{top:36px!important;right:36px!important}.cbox{padding:14px 26px 14px 20px!important;margin-top:10px!important;font-size:30px;line-height:1.22}"
       ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,.2) 22%,rgba(10,52,63,.65) 38%,rgba(9,46,56,.92) 58%,rgba(8,40,50,.95) 100%)!important}</style>")
V11_10 = ("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.3) 0,rgba(10,52,63,.5) 14%,rgba(10,52,63,.8) 28%,rgba(9,46,56,.93) 100%)!important}.s h1{font-size:54px!important}.s p.b{font-size:30px!important}</style>")
def to11(h, i):
    return h.replace("url('img/", "url('1x1/img/").replace("</head>", V11 + (V11_10 if i == 10 else "") + "</head>")
def shot(hp, op, w, hgt):
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
        f"--window-size={w},{hgt}",f"--screenshot={op}","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
pngs = cs.build(SL, D, f"{N}-DRAFT.pdf", B)
os.makedirs(f"{D}/slides-9x16", exist_ok=True); os.makedirs(f"{D}/slides-1x1", exist_ok=True)
for i, (soc, vid, _, _) in enumerate(SL, 1):
    hp = os.path.join(B, f"slide-{i:02d}-9x16.html"); open(hp, "w").write(to916(vid, i)); shot(hp, f"{D}/slides-9x16/slide-{i:02d}.png", 1080, 1920)
    hp = os.path.join(B, f"slide-{i:02d}-1x1.html"); open(hp, "w").write(to11(soc, i)); shot(hp, f"{D}/slides-1x1/slide-{i:02d}.png", 1080, 1080)
for i in range(1, 11):
    for p, s in ((f"{D}/slide-{i:02d}.png", (1080, 1350)), (f"{D}/slide-{i:02d}-video.png", (1080, 1350)),
                 (f"{D}/slides-9x16/slide-{i:02d}.png", (1080, 1920)), (f"{D}/slides-1x1/slide-{i:02d}.png", (1080, 1080))):
        assert Image.open(p).size == s, (p, Image.open(p).size)
for zn, fmt, an in (("slides.zip", "{D}/slide-{i:02d}.png", "slide-{i:02d}.png"), ("slides-9x16.zip", "{D}/slides-9x16/slide-{i:02d}.png", "slide-{i:02d}-9x16.png"),
                    ("slides-1x1.zip", "{D}/slides-1x1/slide-{i:02d}.png", "slide-{i:02d}-1x1.png")):
    with zipfile.ZipFile(f"{D}/{zn}", "w", zipfile.ZIP_DEFLATED) as z:
        for i in range(1, 11): z.write(fmt.format(D=D, i=i), an.format(i=i))
# PDF with a DRAFT header strip on each page
fnt = ImageFont.truetype(subprocess.run(["fc-match","-f","%{file}","Montserrat:extrabold"],capture_output=True,text=True).stdout, 34)
pages = []
for i in range(1, 11):
    im = Image.open(f"{D}/slide-{i:02d}.png").convert("RGB"); c = Image.new("RGB", (1080, 1420), "#B00020"); c.paste(im, (0, 70))
    ImageDraw.Draw(c).text((540, 35), "DRAFT — AWAITING DENISE APPROVAL", fill="white", font=fnt, anchor="mm"); pages.append(c)
pages[0].save(f"{D}/{N}-DRAFT.pdf", save_all=True, append_images=pages[1:], resolution=150)
print("ok")
