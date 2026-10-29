# Buyer tips Oct 29 2026: "Check flood risk before you buy". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-29-buyer-tips-flood-risk"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
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
S_(1,"BUYER TIPS","<h1>Check the flood map <em>first.</em></h1>"+ul([
  "Look up the flood zone for any address",
  "Know what your insurance does and doesn't cover",
  "Here's what I'd check, step by step"]),band="BUYING IN NC OR SC? <em>CHECK THE MAP.</em>",h1=76),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("MEDIAN<br>LIST PRICE","$424,950","−3.1% YoY")+row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+
  row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+row("PRICE-REDUCED<br>SHARE","26.2%","+0.7 pts YoY")+
  "<p class='tk'>More homes to choose from and more time on the market. Use that time to check each home's flood risk.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"LOOK IT UP","<h1>Look up <em>the flood zone.</em></h1>"+ul([
  "FEMA's Flood Map Service Center lets you search any address",
  "In NC, the state Flood Risk Information System (FRIS) has maps too",
  "Check early, ideally during your due diligence period"]),h1=80),
S_(4,"THE ZONES","<h1>Know what <em>the letters mean.</em></h1>"+ul([
  "Zones starting with A or V are high-risk areas",
  "Shaded Zone X is moderate risk; unshaded Zone X is minimal",
  "FEMA notes floods can happen anywhere, even in lower-risk zones"]),h1=76),
S_(5,"YOUR LENDER","<h1>High-risk zone? <em>Ask your lender.</em></h1>"+ul([
  "With a government-backed mortgage, flood insurance is required in a high-risk zone",
  "Some lenders require it in other areas too",
  "Ask early so the cost is part of your monthly budget"]),h1=74),
S_(6,"YOUR POLICY","<h1>Homeowners insurance <em>isn't flood insurance.</em></h1>"+ul([
  "Most homeowners policies don't cover flood damage",
  "Flood coverage is a separate policy, through the NFIP or a private insurer",
  "Ask a licensed insurance agent to quote the home you're considering"]),h1=70),
S_(7,"TIMING","<h1>Mind the <em>30-day wait.</em></h1>"+ul([
  "A new NFIP policy usually takes effect 30 days after purchase",
  "There's no wait when it's bought while making a new mortgage",
  "Line it up with your lender and agent before closing"]),h1=84),
S_(8,"NC DISCLOSURES","<h1>Read the <em>flood questions.</em></h1>"+ul([
  "NC's disclosure statement (REC 4.22) asks about flood zones, past flood damage and claims",
  "It also asks about current flood insurance and elevation certificates",
  "A \"No\" means the owner has no actual knowledge, not that there's no problem"]),h1=80),
S_(9,"ASK FOR IT","<h1>Ask for <em>the paperwork.</em></h1>"+ul([
  "Ask if there's an elevation certificate for the home",
  "In NC, the disclosure form notes an existing flood policy may be assignable to a buyer",
  "In SC, ask the seller directly and check the FEMA map yourself"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Check the map, <em>then commit.</em></h1><p class='b'>I recommend checking the flood zone and getting an insurance quote early in due diligence, because flood risk can change your monthly cost and what your lender requires. For coverage questions, talk with a licensed insurance agent.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
