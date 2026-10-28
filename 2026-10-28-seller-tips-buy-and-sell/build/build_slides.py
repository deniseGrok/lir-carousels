# Seller tips Oct 28 2026: "Sell and buy at the same time". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-28-seller-tips-buy-and-sell"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
F="SELLER TIPS"
# Slide 10 contact block (Denise Oct 22 2026, COMPLIANCE.md R5).
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
STATS_CSS=("<style>.row{padding:26px 28px;margin-top:20px}.row .z{width:430px;font-size:31px;line-height:1.15}.row .v{font-size:74px}"
           ".row .y{font-size:32px}.tk{font-size:36px;line-height:1.3;margin-top:34px}</style>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_tips"); k.setdefault("h1",84); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
row=lambda z,v,y:f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
SL=[
S_(1,"SELLER TIPS","<h1>Sell and buy <em>at the same time.</em></h1>"+ul([
  "Two closings, one move",
  "The order you choose shapes your contract terms",
  "Here's how I'd plan it"]),band="SELLING TO BUY? <em>PLAN THE ORDER.</em>",h1=76),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  row("NEW<br>LISTINGS","3,742","−7.5% YoY")+row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+
  "<p class='tk'>More listings and longer market times than a year ago. Build room into both timelines.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"YOUR NUMBERS","<h1>Start with <em>your numbers.</em></h1>"+ul([
  "Estimate what you could net from your sale",
  "Ask your lender if you need that sale to buy",
  "Know how long you could carry two homes"]),h1=80),
S_(4,"SELL FIRST","<h1>Option 1: <em>sell first.</em></h1>"+ul([
  "You know your proceeds before you make an offer",
  "You may need a short-term place to stay",
  "You may be able to stay briefly after closing"]),h1=84),
S_(5,"BUY FIRST","<h1>Option 2: <em>buy first.</em></h1>"+ul([
  "You can move once, on your own schedule",
  "You may own two homes for a while",
  "Ask your lender what that means for you"]),h1=84),
S_(6,"NC CONTRACTS","<h1>A note is <em>not a contingency.</em></h1>"+ul([
  "In NC, noting on Form 2-T that you must sell is information for the seller",
  "NC REALTORS says it does not make the purchase contingent",
  "A true sale contingency needs an attorney-drafted addendum"]),h1=74),
S_(7,"TIMING","<h1>Give yourself <em>room.</em></h1>"+ul([
  "In NC, a longer due diligence period and later settlement date can help",
  "Aim to close your sale first, or be reasonably sure it will",
  "In SC, ask your attorney how your contract handles timing"]),h1=84),
S_(8,"STAYING AFTER CLOSING","<h1>Need a few <em>extra days?</em></h1>"+ul([
  "In NC, Form 2A8-T lets a seller stay briefly after closing",
  "The buyer has to agree, and it's for short-term stays only",
  "Check with your insurance professional first"]),h1=80),
S_(9,"BOTH CLOSINGS","<h1>Line up <em>both closings.</em></h1>"+ul([
  "Share both timelines with your agents, lender and closing attorney",
  "Put any date change in writing",
  "Keep a backup plan for moving day"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Plan the order, <em>then list.</em></h1><p class='b'>I recommend we map out both timelines before you list, because the order you choose shapes the terms of both contracts. For legal questions, talk with a real estate attorney.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
