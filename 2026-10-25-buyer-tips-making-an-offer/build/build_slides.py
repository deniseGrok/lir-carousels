# Buyer tips Oct 25 2026: "Before you make an offer". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-25-buyer-tips-making-an-offer"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
F="BUYER TIPS"
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
S_(1,"BUYER TIPS","<h1>Before you <em>make an offer.</em></h1>"+ul([
  "Your offer is a written proposal: price, dates and terms",
  "The seller can accept it, reject it or counter",
  "Here's what I recommend you check first"]),band="BUYING? <em>WRITE IT RIGHT.</em>",h1=84),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("MEDIAN<br>LIST PRICE","$424,950","−3.1% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  row("LISTINGS WITH<br>A PRICE CUT","26.2%","+0.7 pts YoY")+row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+
  "<p class='tk'>Homes are taking longer to sell than a year earlier. Clear terms still matter.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"IN WRITING","<h1>Put it <em>in writing.</em></h1>"+ul([
  "NC: a home sale contract must be in writing to be enforceable",
  "SC: a contract to sell land must be in writing and signed (S.C. Code 32-3-10)",
  "List any items you expect to stay with the home in your offer"]),h1=84),
S_(4,"PRICE","<h1>Know your <em>number.</em></h1>"+ul([
  "Review recent nearby sales of similar homes with your agent",
  "Weigh condition, updates and time on the market",
  "Decide your top price before you write, not in the moment"]),h1=84),
S_(5,"DUE DILIGENCE","<h1>NC: know the <em>DD fee.</em></h1>"+ul([
  "On NC's standard contract, it's paid directly to the seller",
  "It buys a set period when you can end the contract for any reason",
  "It's non-refundable unless the seller breaches, and is typically credited to you at closing",
  "No law requires one; the fee and the period are negotiated"]),h1=80),
S_(6,"EARNEST MONEY","<h1>Earnest money, <em>explained.</em></h1>"+ul([
  "NC: not required, but common; it shows good faith",
  "A broker must deposit it within three banking days after acceptance",
  "End the contract before due diligence expires, and it should be refunded",
  "After that, it's usually forfeited unless the seller can't or won't perform"]),h1=80),
S_(7,"SOUTH CAROLINA","<h1>Buying <em>in SC?</em></h1>"+ul([
  "Licensees must put every offer in writing and promptly present it (S.C. Code 40-57-135)",
  "Rejected without a counter? You get a signed rejection form within 48 hours",
  "Earnest money checks a broker holds go into a trust account within 48 hours of written acceptance, weekends and bank holidays excluded (S.C. Code 40-57-136)"]),h1=80),
S_(8,"ACCEPTANCE","<h1>When it's <em>a contract.</em></h1>"+ul([
  "NC: the seller must sign your offer without changes, and you must be told",
  "Any change is a counteroffer you can accept, reject or counter",
  "Until you're notified, you can still withdraw your offer",
  "Ask for a signed copy of the contract"]),h1=80),
S_(9,"MULTIPLE OFFERS","<h1>If others <em>are offering.</em></h1>"+ul([
  "NC: until the seller signs and tells you, they can accept another offer, even if yours came first",
  "The seller's broker can't share other buyers' price and terms without their permission",
  "Don't assume your offer gets special consideration"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Every term <em>counts.</em></h1><p class='b'>I recommend we go through your offer line by line, because price is only one term. For contract or legal questions, a real estate attorney can help.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short today)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
