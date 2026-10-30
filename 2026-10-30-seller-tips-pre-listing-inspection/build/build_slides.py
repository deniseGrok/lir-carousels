# Seller tips Oct 30 2026: "Inspect it before you list" (pre-listing inspection). theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-30-seller-tips-pre-listing-inspection"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
F="SELLER TIPS"
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
STATS_CSS=("<style>.row{padding:26px 28px;margin-top:20px}.row .z{width:430px;font-size:31px;line-height:1.15}.row .v{font-size:74px}"
           ".row .y{font-size:32px}.tk{font-size:34px;line-height:1.28;margin-top:28px}</style>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_tips"); k.setdefault("h1",84); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
row=lambda z,v,y:f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
SL=[
S_(1,"SELLER TIPS","<h1>Inspect it <em>before you list.</em></h1>"+ul([
  "See your home the way a buyer's inspector will",
  "Decide what to fix, credit or price in",
  "Here's how I'd use a pre-listing inspection"]),band="SELLING IN NC OR SC? <em>KNOW FIRST.</em>",h1=78),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  row("PRICE-REDUCED<br>SHARE","26.2%","+0.7 pts YoY")+row("MEDIAN LIST<br>PRICE / SQ FT","$217","−1.4% YoY")+
  "<p class='tk'>More homes to compare. Knowing your home's condition early helps you plan price and prep.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"WHAT IT IS","<h1>An inspection, <em>on your schedule.</em></h1>"+ul([
  "You hire a licensed home inspector before the home goes on the market",
  "NC and SC both license home inspectors",
  "It's a snapshot of the home's condition, not a warranty"]),h1=78),
S_(4,"WHY IT HELPS","<h1>Fewer surprises <em>after the offer.</em></h1>"+ul([
  "Buyers usually hire their own inspector once you're under contract",
  "Finding issues first gives you time to get repair bids",
  "You get to plan instead of reacting on a deadline"]),h1=78),
S_(5,"THE BIG ITEMS","<h1>Start with <em>the big systems.</em></h1>"+ul([
  "Roof, foundation and other structural parts",
  "Heating, cooling, plumbing and electrical",
  "These are items NC and SC disclosure forms ask about too"]),h1=80),
S_(6,"YOUR OPTIONS","<h1>Fix it, credit it <em>or price it in.</em></h1>"+ul([
  "Repair items before listing, with licensed contractors where required",
  "Or get written bids buyers can review",
  "Or set your price with the issue in mind"]),h1=76),
S_(7,"DISCLOSURE","<h1>Once you know, <em>it counts.</em></h1>"+ul([
  "NC and SC disclosure forms ask what the owner actually knows",
  "In NC, brokers must disclose material facts they know, whatever the form says",
  "Ask a real estate attorney how a report affects your disclosures"]),h1=84),
S_(8,"SHARE IT","<h1>Consider sharing <em>the report.</em></h1>"+ul([
  "NC law lets an owner attach a home inspector's written report to the disclosure statement",
  "It also limits an owner's liability for errors in that report when the owner reasonably relied on it",
  "Keep receipts and warranties for any repairs you make"]),h1=80),
S_(9,"BUYERS STILL LOOK","<h1>It doesn't replace <em>the buyer's inspection.</em></h1>"+ul([
  "Buyers can still hire their own inspector",
  "SC law keeps the buyer's duty to inspect the property",
  "NC's disclosure form tells buyers it isn't a substitute for inspections"]),h1=70),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Know first, <em>then list.</em></h1><p class='b'>I recommend considering a pre-listing inspection, because it lets you decide on repairs, price and disclosures with time to think, not on a buyer's deadline. For legal questions about your disclosures, talk with a real estate attorney.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
