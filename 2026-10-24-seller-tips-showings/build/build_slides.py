# Seller tips Oct 24 2026: "Before buyers walk in" (showing-ready). theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 IG/FB/LinkedIn), slide-NN-video.png (4:5, no SWIPE), slides-9x16/slide-NN.png
# (1080x1920 native 9:16 layout for TikTok photo mode/Stories/Short: tag below the top 250px, text ends above the bottom 420px
# and stays left of the right 140px). Plus PDF + slides.zip. Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-24-seller-tips-showings"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="SELLER TIPS"
# Slide 10 contact block (Denise Oct 22 2026, COMPLIANCE.md R5): firm name line added.
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
STATS_CSS=("<style>.row{padding:26px 28px;margin-top:20px}.row .z{width:430px;font-size:31px;line-height:1.15}.row .v{font-size:74px}"
           ".row .y{font-size:32px}.tk{font-size:36px;line-height:1.3;margin-top:34px}</style>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_tips"); k.setdefault("h1",84); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
row=lambda z,v,y:f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
SL=[
S_(1,"SELLER TIPS","<h1>Before buyers <em>walk in.</em></h1>"+ul([
  "A few simple steps help buyers focus on the home, not the clutter",
  "Most take an afternoon, not a renovation",
  "Here's what I recommend before every showing"]),band="SELLING? <em>GET SHOWING-READY.</em>",h1=86),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+row("NEW<br>LISTINGS","3,742","−7.5% YoY")+
  row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+row("LISTINGS WITH<br>A PRICE CUT","26.2%","+0.7 pts YoY")+
  "<p class='tk'>Buyers have more homes to compare than a year earlier. How yours shows counts.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"FIRST LOOK","<h1>Start at <em>the curb.</em></h1>"+ul([
  "Sweep the walk, trim the shrubs and clear the porch",
  "Make sure the doorbell, lock and porch light all work",
  "An easy, tidy entry sets the tone for the tour"]),h1=84),
S_(4,"LIGHT","<h1>Let the <em>light in.</em></h1>"+ul([
  "Open blinds and curtains before each showing",
  "Turn on lamps and replace dim or burned-out bulbs",
  "Bright rooms are easier to see, in person and in photos"]),h1=84),
S_(5,"SURFACES","<h1>Clear <em>the counters.</em></h1>"+ul([
  "Put away small appliances, mail and everyday items",
  "Leave open space on counters, tables and shelves",
  "Start packing what you won't need before the move"]),h1=84),
S_(6,"VALUABLES","<h1>Lock up <em>valuables.</em></h1>"+ul([
  "Store jewelry, cash and small electronics out of sight",
  "Secure prescription medications and personal papers",
  "Ask your agent how showings and lockbox access will work"]),h1=84),
S_(7,"FRESH + CLEAN","<h1>Keep it <em>fresh.</em></h1>"+ul([
  "Clean kitchens and baths until they shine",
  "Air the house out and skip strong scents",
  "Fix small things: drips, loose handles, sticky doors"]),h1=84),
S_(8,"STEP OUT","<h1>Give buyers <em>space.</em></h1>"+ul([
  "Plan to be away so buyers can tour and talk freely",
  "Arrange care for pets, and tell your agent about any at home",
  "Set the thermostat to a comfortable temperature"]),h1=84),
S_(9,"DISCLOSURES","<h1>Prep isn't <em>disclosure.</em></h1>"+ul([
  "NC: for most home sales, owners give buyers the Commission's disclosure statement (G.S. 47E-4)",
  "NC: it's due no later than when a buyer makes an offer (G.S. 47E-5)",
  "SC: owners furnish a written disclosure statement on the Commission's form (S.C. Code 27-50-40)",
  "Questions about what to disclose? Ask your agent or a real estate attorney"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Make every <em>showing count.</em></h1><p class='b'>I recommend a walk-through with your agent before the first showing, room by room, so small fixes get done early. Let's make your plan together.</p>",contact=True,h1=76),
]
# Native 9:16 layout overrides (keep key text clear of top 250px, bottom 420px, right 140px).
V916=("<style>html,body,.s{width:1080px!important;height:1920px!important}.ph{height:1920px!important;width:1080px!important}"
      ".tag{top:270px!important}.c{left:56px!important;right:160px!important;bottom:500px!important}"
      ".ft{left:56px!important;right:160px!important;bottom:436px!important}"
      ".ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 40%,rgba(0,0,0,.5) 55%,rgba(0,0,0,.86) 76%,rgba(0,0,0,.9) 100%)!important}"
      "</style>")
V916_STATS=("<style>.s .c{top:370px!important;bottom:auto!important}.s h1{font-size:100px!important}.s .lab{font-size:32px}"
  ".s .row{padding:20px 30px;margin-top:18px}.s .row .z{font-size:30px;width:330px}.s .row .v{font-size:68px;flex:1}.s .row .y{font-size:32px;white-space:nowrap}"
  ".s .tk{font-size:36px;margin-top:30px}.s .src{font-size:30px;margin-top:18px}"
  ".row .z{width:330px!important;font-size:29px!important}.row .v{font-size:66px!important}.row .y{font-size:30px!important;white-space:nowrap}</style>")
def to916(h,i):
    h=h.replace("url('img/","url('9x16/img/").replace("</head>",V916+(V916_STATS if i==2 else "")+"</head>")
    return h
def shot(hp,op,w,hgt):
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
        f"--window-size={w},{hgt}",f"--screenshot={op}","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
os.makedirs(f"{D}/slides-9x16",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    hp=os.path.join(B,f"slide-{i:02d}-9x16.html"); open(hp,"w").write(to916(vid,i)); shot(hp,f"{D}/slides-9x16/slide-{i:02d}.png",1080,1920)
for i in range(1,11):
    for p,s in ((f"{D}/slide-{i:02d}.png",(1080,1350)),(f"{D}/slide-{i:02d}-video.png",(1080,1350)),(f"{D}/slides-9x16/slide-{i:02d}.png",(1080,1920))):
        assert Image.open(p).size==s,(p,Image.open(p).size)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
with zipfile.ZipFile(D+"/slides-9x16.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slides-9x16/slide-{i:02d}.png",f"slide-{i:02d}-9x16.png")
print("ok")
