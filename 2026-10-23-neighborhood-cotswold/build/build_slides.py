# Cotswold neighborhood spotlight Oct 23 2026. theme="fullbleed_teal" (teal #0F4C5C / gold #F2B705), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 IG/FB/LinkedIn), slide-NN-video.png (4:5, no SWIPE), slides-9x16/slide-NN.png
# + slides-1x1/slide-NN.png (1080x1080 native square layout for the Facebook carousel, Denise Oct 22 2026: tag top, text
# bottom-anchored, smaller headline and bullets so nothing is cropped or cramped).
# (1080x1920 native 9:16 layout for the Short/Reel, TikTok photo mode, Stories: header tag below the top 250px, text ends above
# the bottom 420px and stays left of the right 140px). Plus PDF + slides.zip + slides-9x16.zip.
# Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026): slide 10 contact block with firm line + EHO; no people/demographics/schools.
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-23-neighborhood-cotswold"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="NEIGHBORHOOD SPOTLIGHT"
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
cr=lambda s: f"<div class='cr' style='position:fixed;top:124px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.85);background:rgba(8,40,50,.62);padding:4px 14px;border-radius:10px'>Photo: {s}</div>"
row=lambda z,v,y="":f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
STATS_CSS=("<style>.row{padding:18px 28px}.row .z{width:380px;font-size:30px;line-height:1.15}.row .v{font-size:66px}"
           ".tk{font-size:34px;line-height:1.3;margin-top:24px}</style>")
SL=[
S_(1,"COTSWOLD",cr("Castle Combe, England · Saffron Blaze, CC BY-SA 3.0")+"<h1>An English name, <em>mid-century streets.</em></h1>"+ul([
  "A Charlotte neighborhood in ZIP 28211, along Randolph and Sharon Amity Roads",
  "Named for the Cotswolds region of England, pictured here",
  "Many homes date from the 1950s and 1960s"]),band="CHARLOTTE NC. <em>COTSWOLD.</em>",h1=78),
S_(2,"HISTORY","<h1>It started as <em>farmland.</em></h1>"+ul([
  "Cotswold began in the early 1950s as a planned shopping and residential community on the outskirts of Charlotte",
  "The site was farmland known as Faulkner Plantation",
  "The first phase was announced in December 1952, and work began 13 days later"])),
S_(3,"MID-CENTURY DESIGN","<h1>Mid-century <em>from day one.</em></h1>"+ul([
  "The first phase was an apartment complex designed by mid-century modern architect C. W. Connelly",
  "By June 1954 it was mostly complete, and two-thirds of the units were already rented",
  "In 1978 the apartments were converted to condominiums"])),
S_(4,"SHOPPING HISTORY","<h1>One of Charlotte's <em>first suburban malls.</em></h1>"+ul([
  "A Harris Supermarket opened first, in October 1958",
  "The full center held its grand opening in summer 1963 as Cotswold Mall, at Randolph and Sharon Amity Roads",
  "In the early 2000s the enclosed section became an open-air center, today's Cotswold Village"]),h1=76),
S_(5,"THE HOMES","<h1>Ranches, split-levels <em>and remodels.</em></h1>"+ul([
  "Brick ranch and split-level homes from the 1950s and 1960s line many streets",
  "Many original homes have been remodeled",
  "Newer custom homes now share some of the same blocks"]),h1=76),
S_(6,"MY TIP","<h1>Research <em>the house itself.</em></h1>"+ul([
  "Mecklenburg County parcel records show a home's build year and recorded plat",
  "Ask which updates were made, and whether they were permitted",
  "Compare original and remodeled homes by price per square foot, not just list price"])),
S_(7,"GETTING AROUND","<h1>Close-in <em>and connected.</em></h1>"+ul([
  "Randolph Road and Sharon Amity Road are the main corridors",
  "Randolph Road heads west toward Uptown",
  "Neighbors include Myers Park, Oakhurst, Randolph Park and Sherwood Forest"])),
S_(8,"OUTDOORS","<h1>A greenway <em>off Randolph.</em></h1>"+ul([
  "Briar Creek Greenway has a 1.0-mile section between Randolph Road and Meadowbrook Road",
  "Parking for that section is at 115 Museum Plaza",
  "It's part of a county system with 85.5 miles of greenway trails (Mecklenburg County, March 2026)"])),
S_(9,"THE MARKET",cs.TEAL_STRONG+STATS_CSS+"<div class='lab'>REALTOR.COM · AS OF OCT. 2026</div><h1>What homes <em>list and sell for.</em></h1>"+
  row("MEDIAN LIST<br>PRICE","$862,000")+row("MEDIAN SOLD<br>PRICE","$975,000")+row("HOMES<br>FOR SALE","70")+row("MEDIAN DAYS<br>ON MARKET","94")+
  "<p class='src'>Source: Realtor.com Economic Research, Cotswold, Charlotte NC; key indicators as of October 2026, viewed Oct. 23, 2026</p>",h1=72),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 48%,rgba(9,46,56,.88) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>We'll start at Cotswold Village, then compare an original ranch with a remodeled one a few streets away. I'll pull the parcel records before we go.</p>",contact=True,h1=76),
]
# Native 9:16 layout overrides (key text clear of top 250px, bottom 420px, right 140px).
V916=("<style>html,body,.s{width:1080px!important;height:1920px!important}.ph{height:1920px!important;width:1080px!important}"
      ".tag{top:270px!important}.cr{top:356px!important;left:56px!important}.c{left:56px!important;right:160px!important;bottom:500px!important}"
      ".ft{left:56px!important;right:160px!important;bottom:436px!important}"
      ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 18%,rgba(10,52,63,0) 38%,rgba(10,52,63,.5) 52%,rgba(9,46,56,.86) 72%,rgba(8,40,50,.9) 100%)!important}"
      "</style>")
V916_STATS=("<style>.s .c{top:380px!important;bottom:auto!important}.s h1{font-size:96px!important}.s .lab{font-size:30px}"
  ".s .row{padding:20px 30px;margin-top:16px}.s .row .z{font-size:30px;width:380px}.s .row .v{font-size:76px}"
  ".s .src{font-size:30px;margin-top:22px}"
  ".ph:after{background:linear-gradient(rgba(8,40,50,.4) 0,rgba(8,40,50,.55) 15%,rgba(10,52,63,.8) 30%,rgba(9,46,56,.9) 60%,rgba(8,40,50,.93) 100%)!important}</style>")
V916_10=("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 14%,rgba(10,52,63,0) 28%,rgba(10,52,63,.55) 42%,rgba(9,46,56,.88) 62%,rgba(8,40,50,.9) 100%)!important}</style>")
def to916(h,i):
    extra=V916+(V916_STATS if i==9 else "")+(V916_10 if i==10 else "")
    return h.replace("url('img/","url('9x16/img/").replace("</head>",extra+"</head>")

# Native 1:1 (1080x1080) layout overrides for the square Facebook carousel.
V11=("<style>html,body,.s{width:1080px!important;height:1080px!important}.ph{height:1080px!important;width:1080px!important}"
     ".c{bottom:92px!important}.ft{bottom:36px!important}.s h1{font-size:62px!important}.s li{font-size:30px;line-height:1.22;margin-bottom:8px}"
     ".s ul{margin-top:14px}.band{font-size:46px!important;padding:10px 22px!important;margin-bottom:12px!important}.s p.b{font-size:31px;line-height:1.28;margin-top:12px}"
     ".cbox{padding:16px 26px 16px 20px!important;margin-top:12px!important;font-size:30px;line-height:1.24}"
     ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 14%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 50%,rgba(9,46,56,.88) 100%)!important}</style>")
V11_STATS=("<style>.s .c{top:auto!important;bottom:92px!important}.s h1{font-size:64px!important}.s .lab{font-size:30px;margin-bottom:6px}"
  ".s .grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}.s .row{margin-top:0!important;padding:16px 22px!important;flex-direction:column;align-items:flex-start}"
  ".s .row .z{width:auto!important;font-size:30px!important}.s .row .v{font-size:64px!important}.s .row .y{display:none}.s .src{font-size:30px;margin-top:16px}"
  ".ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,.15) 14%,rgba(10,52,63,.6) 30%,rgba(9,46,56,.9) 50%,rgba(8,40,50,.93) 100%)!important}</style>")
V11_10=("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 10%,rgba(10,52,63,.35) 22%,rgba(10,52,63,.7) 36%,rgba(9,46,56,.9) 100%)!important}.s h1{font-size:58px!important}</style>")
def to11(h,i):
    if i==9:
        h=h.replace("<div class='row'>","<div class='grid'><div class='row'>",1).replace("<p class='src'>","</div><p class='src'>",1)
    extra=V11+(V11_STATS if i==9 else "")+(V11_10 if i==10 else "")
    return h.replace("url('img/","url('1x1/img/").replace("</head>",extra+"</head>")
def shot(hp,op,w,hgt):
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
        f"--window-size={w},{hgt}",f"--screenshot={op}","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
os.makedirs(f"{D}/slides-9x16",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    hp=os.path.join(B,f"slide-{i:02d}-9x16.html"); open(hp,"w").write(to916(vid,i)); shot(hp,f"{D}/slides-9x16/slide-{i:02d}.png",1080,1920)
os.makedirs(f"{D}/slides-1x1",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    hp=os.path.join(B,f"slide-{i:02d}-1x1.html"); open(hp,"w").write(to11(soc,i)); shot(hp,f"{D}/slides-1x1/slide-{i:02d}.png",1080,1080)
for i in range(1,11):
    assert Image.open(f"{D}/slides-1x1/slide-{i:02d}.png").size==(1080,1080)
    for p,s in ((f"{D}/slide-{i:02d}.png",(1080,1350)),(f"{D}/slide-{i:02d}-video.png",(1080,1350)),(f"{D}/slides-9x16/slide-{i:02d}.png",(1080,1920))):
        assert Image.open(p).size==s,(p,Image.open(p).size)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
with zipfile.ZipFile(D+"/slides-9x16.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slides-9x16/slide-{i:02d}.png",f"slide-{i:02d}-9x16.png")
with zipfile.ZipFile(D+"/slides-1x1.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slides-1x1/slide-{i:02d}.png",f"slide-{i:02d}-1x1.png")
print("ok")
