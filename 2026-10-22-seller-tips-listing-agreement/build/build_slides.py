# Seller tips Oct 22 2026: "Read your listing agreement before you sign". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 IG/FB/LinkedIn), slide-NN-video.png (4:5, no SWIPE), slides-9x16/slide-NN.png
# (1080x1920 native 9:16 layout for TikTok photo mode/Stories/Short: tag below the top 250px, text ends above the bottom 420px
# and stays left of the right 140px). Plus PDF + slides.zip. Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-22-seller-tips-listing-agreement"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="SELLER TIPS"
# Slide 10 contact block (Denise Oct 22 2026, COMPLIANCE.md R5): firm name line added.
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
STATS_CSS=("<style>.row{padding:18px 28px}.row .z{width:430px;font-size:30px;line-height:1.15}.row .v{font-size:66px}"
           ".row .y{font-size:32px}.tk{font-size:34px;line-height:1.3;margin-top:26px}</style>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_tips"); k.setdefault("h1",84); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
row=lambda z,v,y:f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
SL=[
S_(1,"SELLER TIPS","<h1>Know what <em>you're signing.</em></h1>"+ul([
  "Your listing agreement is your contract with the brokerage firm that markets your home",
  "It sets the term, the services, how the firm is paid and how it ends",
  "Here's what I recommend checking before you sign"]),band="SELLING? <em>READ IT FIRST.</em>",h1=86),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+row("NEW<br>LISTINGS","3,742","−7.5% YoY")+
  row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+row("MEDIAN LIST<br>PRICE PER SQ FT","$217","−1.4% YoY")+
  "<p class='tk'>Homes took longer to sell than a year earlier. Know your listing term before you sign.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"IN WRITING","<h1>Get it <em>in writing.</em></h1>"+ul([
  "NC: a listing agreement must be in writing and signed when it's formed (NCREC Rule 58A .0104)",
  "SC: it must be in writing and spell out the firm's duties, pay and dates (S.C. Code 40-57-135)",
  "SC: you get a copy at signing or right after"])),
S_(4,"THE DATES","<h1>Check the <em>dates.</em></h1>"+ul([
  "NC: it runs for a definite period and ends at expiration without notice (Rule 58A .0104)",
  "SC: it sets start and end dates and ends on the expiration date unless you sign a written extension (S.C. Code 40-57-135)",
  "Ask how long the term is and why"])),
S_(5,"HOW PAY WORKS","<h1>Commissions are <em>negotiable.</em></h1>"+ul([
  "Commissions aren't set by law; they're negotiated and put in writing (NAR)",
  "SC: the agreement states the fee or how it's figured, when it's earned and how it's shared with cooperating brokers (S.C. Code 40-57-135)",
  "Read the pay section line by line"]),h1=80),
S_(6,"BUYER-AGENT PAY","<h1>Decide on <em>buyer-agent pay.</em></h1>"+ul([
  "Since Aug. 17, 2024, offers of compensation to buyer agents can't be shown on an MLS (NAR settlement practice changes)",
  "With your approval, an offer can still be shared in other marketing, like flyers and brokerage websites",
  "Seller concessions can still appear on an MLS but can't be tied to paying a buyer's agent"]),h1=80),
S_(7,"EXIT TERMS","<h1>Read the <em>exit terms.</em></h1>"+ul([
  "NC: any early-termination penalty must be clear and conspicuous in the agreement (Rule 58A .0104)",
  "Ask what happens if your plans change before the end date",
  "Get the answer in writing before you sign"])),
S_(8,"DUAL AGENCY","<h1>Ask about <em>dual agency.</em></h1>"+ul([
  "NC: one firm may represent both buyer and seller only with each party's written authority (Rule 58A .0104)",
  "SC: the agreement explains the firm's policy on dual agency, designated agency and transaction brokerage (S.C. Code 40-57-135)",
  "Know your options before an offer comes in"])),
S_(9,"DISCLOSURES","<h1>Know your <em>disclosure forms.</em></h1>"+ul([
  "NC: you get the \"Working with Real Estate Agents\" brochure at first substantial contact (Rule 58A .0104)",
  "SC: you get the Disclosure of Brokerage Relationships form at the first practical opportunity (S.C. Code 40-57-370)",
  "NC listing agreements include a fair housing nondiscrimination clause (Rule 58A .0104)"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Read it <em>before you sign.</em></h1><p class='b'>I recommend asking for the listing agreement ahead of time so you can read every page and ask questions first. Let's go through yours together.</p>",contact=True,h1=78),
]
# Native 9:16 layout overrides (keep key text clear of top 250px, bottom 420px, right 140px).
V916=("<style>html,body,.s{width:1080px!important;height:1920px!important}.ph{height:1920px!important;width:1080px!important}"
      ".tag{top:270px!important}.c{left:56px!important;right:160px!important;bottom:500px!important}"
      ".ft{left:56px!important;right:160px!important;bottom:436px!important}"
      ".ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 40%,rgba(0,0,0,.5) 55%,rgba(0,0,0,.86) 76%,rgba(0,0,0,.9) 100%)!important}"
      "</style>")
V916_STATS=("<style>.s .c{top:370px!important;bottom:auto!important}.s h1{font-size:100px!important}.s .lab{font-size:32px}"
  ".s .row{padding:20px 30px;margin-top:18px}.s .row .z{font-size:30px;width:400px}.s .row .v{font-size:76px}.s .row .y{font-size:32px;white-space:nowrap}"
  ".s .tk{font-size:36px;margin-top:30px}.s .src{font-size:30px;margin-top:18px}</style>")
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
