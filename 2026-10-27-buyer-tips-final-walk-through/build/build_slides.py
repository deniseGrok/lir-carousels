# Buyer tips Oct 27 2026: "Final walk-through: what to check". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-27-buyer-tips-final-walk-through"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
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
S_(1,"BUYER TIPS","<h1>The final <em>walk-through.</em></h1>"+ul([
  "It happens before you sign at closing",
  "It's your chance to confirm the home is as agreed",
  "Here's what I recommend you look for"]),band="BUYING? <em>CHECK FIRST.</em>",h1=80),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("MEDIAN LIST<br>PRICE","$424,950","−3.1% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+row("LISTINGS WITH<br>A PRICE CUT","26.2%","+0.7 pts YoY")+
  "<p class='tk'>Homes took longer to sell than a year earlier. Whatever the market, check the home before you sign.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"TIMING","<h1>Book it <em>close to closing.</em></h1>"+ul([
  "Schedule it shortly before your closing date",
  "Ask your agent to set the time with the seller's side",
  "Plan enough time to go room by room"]),h1=80),
S_(4,"REPAIRS","<h1>Confirm <em>agreed repairs.</em></h1>"+ul([
  "Bring the written list of repairs the seller agreed to",
  "Check each item yourself",
  "Ask for receipts or paperwork for completed work"]),h1=84),
S_(5,"SYSTEMS","<h1>Test <em>what you can.</em></h1>"+ul([
  "Run faucets, showers and toilets",
  "Turn on the heat and air, lights and fans",
  "Try the appliances that stay with the home"]),h1=84),
S_(6,"WHAT STAYS","<h1>Check <em>what stays.</em></h1>"+ul([
  "Your contract spells out what stays with the home",
  "Look for the included appliances and fixtures",
  "Note anything missing or swapped"]),h1=84),
S_(7,"NEW DAMAGE","<h1>Look for <em>new damage.</em></h1>"+ul([
  "Check walls, floors and doors after the move-out",
  "Look under sinks and at ceilings for signs of leaks",
  "Take photos of anything new"]),h1=84),
S_(8,"OUTSIDE","<h1>Walk <em>the outside too.</em></h1>"+ul([
  "Look at the yard, roofline and gutters from the ground",
  "Confirm keys, codes and garage remotes are ready",
  "Note items left behind that were to be removed"]),h1=84),
S_(9,"SPEAK UP","<h1>Something off? <em>Speak up.</em></h1>"+ul([
  "Tell your agent right away, before you sign",
  "The CFPB suggests contacting the seller right away about repairs or items not in place",
  "Your options depend on your contract, so ask your agent or closing attorney"]),h1=80),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Check it, <em>then sign.</em></h1><p class='b'>I recommend we do your final walk-through together with your repair list in hand, because it's your last look before you sign. For legal questions, talk with a real estate attorney.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short today)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
