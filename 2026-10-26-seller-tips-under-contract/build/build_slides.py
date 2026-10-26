# Seller tips Oct 26 2026: "Under contract? Here's what's next". theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-26-seller-tips-under-contract"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
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
S_(1,"SELLER TIPS","<h1>Under contract? <em>Here's what's next.</em></h1>"+ul([
  "An accepted offer is a big step, not the finish line",
  "The buyer still has steps to finish, and so do you",
  "Here's what I recommend you keep in mind"]),band="SELLING? <em>STAY STEADY.</em>",h1=80),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+row("MEDIAN DAYS<br>ON MARKET","64","+10.3% YoY")+
  row("ACTIVE<br>LISTINGS","11,182","+10.3% YoY")+row("LISTINGS WITH<br>A PRICE CUT","26.2%","+0.7 pts YoY")+
  "<p class='tk'>Fewer listings were pending than a year earlier. Once you have a buyer, the details matter.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"DEADLINES","<h1>Know <em>every date.</em></h1>"+ul([
  "Put each contract deadline on your calendar the day you sign",
  "In NC, note the due diligence date your contract lists",
  "Ask what each date means for you before it arrives"]),h1=84),
S_(4,"REPAIRS","<h1>Repair requests <em>are negotiated.</em></h1>"+ul([
  "After inspections, a buyer may ask for repairs or a price change",
  "You can agree, decline or counter",
  "Put anything you agree to in writing"]),h1=80),
S_(5,"CONDITION","<h1>Keep it <em>as it was.</em></h1>"+ul([
  "Your contract may require the home to be in substantially the same condition at closing, reasonable wear and tear excepted",
  "Keep up the yard, systems and routine care",
  "If something breaks, tell your agent right away"]),h1=84),
S_(6,"NORTH CAROLINA","<h1>NC: something <em>changed?</em></h1>"+ul([
  "Find a material inaccuracy in a disclosure statement you delivered? Promptly give the buyer a corrected statement",
  "The same applies if an event makes a statement inaccurate in a material way (G.S. 47E-7)"]),h1=80),
S_(7,"SOUTH CAROLINA","<h1>SC: keep disclosures <em>current.</em></h1>"+ul([
  "The disclosure statement goes to the buyer before the contract is signed, or as the contract says (S.C. Code 27-50-50)",
  "Find a material inaccuracy later? Promptly deliver a corrected statement or make reasonable repairs before closing (S.C. Code 27-50-60)"]),h1=80),
S_(8,"YOUR PROCEEDS","<h1>Protect <em>your proceeds.</em></h1>"+ul([
  "Treat any email that changes wiring instructions with caution",
  "Confirm by calling a number you already know, not one in the email",
  "Talk with your closing attorney before you share bank details"]),h1=80),
S_(9,"MOVING OUT","<h1>Plan <em>your move.</em></h1>"+ul([
  "Check the closing and possession terms in your contract",
  "Schedule utility changes and keep service on through closing",
  "Gather keys, codes, garage remotes and manuals"]),h1=84),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Steady to <em>closing day.</em></h1><p class='b'>I recommend we walk through your contract dates together the day it's signed, because each one shapes your next step. For legal or tax questions, talk with a real estate attorney or tax professional.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short today)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
