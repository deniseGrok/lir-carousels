# Buyer tips Oct 23 2026: "Read your buyer agreement before you tour". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 IG/FB/LinkedIn), slide-NN-video.png (4:5, no SWIPE), slides-9x16/slide-NN.png
# (1080x1920 native 9:16 layout for TikTok photo mode/Stories/Short: tag below the top 250px, text ends above the bottom 420px
# and stays left of the right 140px). Plus PDF + slides.zip. Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-23-buyer-tips-buyer-agreement"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="BUYER TIPS"
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
S_(1,"BUYER TIPS","<h1>Your buyer agreement, <em>explained.</em></h1>"+ul([
  "A written buyer agreement spells out the services your agent provides and how they're paid (NAR)",
  "You'll be asked to sign one before touring a home with an agent, in person or virtually (NAR)",
  "Here's what I recommend checking first"]),band="BUYING? <em>READ IT FIRST.</em>",h1=86),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+row("LISTINGS WITH<br>A PRICE CUT","26.2%","+0.7 pts YoY")+
  row("MEDIAN<br>LIST PRICE","$424,950","−3.1% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  "<p class='tk'>More homes to choose from than a year earlier. Read your agreement before the tours start.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"BEFORE YOU TOUR","<h1>Know <em>when you sign.</em></h1>"+ul([
  "Since Aug. 17, 2024, many agents ask for a written agreement before a tour (NAR)",
  "Visiting an open house on your own doesn't require one (NAR)",
  "NC: it must be in writing by the time an offer is made, or from the start if it binds you for a set time (Rule 58A .0104)"]),h1=82),
S_(4,"HOW PAY WORKS","<h1>Pay is <em>negotiable.</em></h1>"+ul([
  "Agent compensation isn't set by law; it's negotiated (NAR)",
  "It must be clearly defined, like a flat fee or a percent, not open-ended or a range (NAR)",
  "SC: the agreement states the fee or how it's figured, and when it's earned (S.C. Code 40-57-135)"]),h1=82),
S_(5,"WHO PAYS","<h1>Ask <em>who pays.</em></h1>"+ul([
  "You're responsible for what your agreement says you'll pay (NAR)",
  "You can still request and negotiate for the seller to pay your agent (NAR)",
  "Ask how a seller-paid amount is handled before you sign"]),h1=84),
S_(6,"THE DATES","<h1>Check <em>the dates.</em></h1>"+ul([
  "NC: it runs for a definite period and ends at expiration without notice (Rule 58A .0104)",
  "SC: it sets start and end dates and ends then unless you sign a written extension (S.C. Code 40-57-135)",
  "Ask how long the term is and why"]),h1=84),
S_(7,"WHICH TYPE","<h1>Know <em>which type.</em></h1>"+ul([
  "SC: where it applies, the agreement must clearly state which type it is (S.C. Code 40-57-135)",
  "NC: an agreement that limits your right to work with other agents must be in writing from the start (Rule 58A .0104)",
  "Ask whether you can work with other agents while it's in effect"]),h1=84),
S_(8,"EXIT TERMS","<h1>Read the <em>exit terms.</em></h1>"+ul([
  "You and your agent can agree to change it; some agreements set conditions to exit (NAR)",
  "NC: any early-termination penalty must be clear and conspicuous (Rule 58A .0104)",
  "Legal questions? Ask a real estate attorney"]),h1=82),
S_(9,"DISCLOSURES","<h1>Know your <em>disclosures.</em></h1>"+ul([
  "NC: you get the \"Working with Real Estate Agents\" brochure at first substantial contact (Rule 58A .0104)",
  "NC: one firm may represent both sides only with each party's written authority (Rule 58A .0104)",
  "SC: dual agency needs your written consent before an offer is written (S.C. Code 40-57-350)"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Ask for it <em>before you tour.</em></h1><p class='b'>I recommend asking to see the buyer agreement before your first tour, so you can read every line and ask questions first. Let's go through it together.</p>",contact=True,h1=76),
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
