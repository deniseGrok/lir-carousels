# Buyer tips Oct 31 2026: "Know what you're really buying" (title, survey, easements). theme="fullbleed_tips" (navy/coral), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 Instagram + LinkedIn) + PDF + slides.zip. Facebook 1:1 set: build_1x1.py.
# No 9:16 set and no YouTube Short (Denise Oct 24 2026). Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026).
import sys, os, zipfile
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image
N="2026-10-31-buyer-tips-title-and-survey"; B=os.path.dirname(os.path.abspath(__file__)); D=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
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
S_(1,"BUYER TIPS","<h1>Know what you're <em>really buying.</em></h1>"+ul([
  "Title, boundaries and easements come with every home",
  "What a title policy protects, and what it doesn't",
  "Here's what I'd check before closing"]),band="BUYING IN NC OR SC? <em>CHECK THE TITLE.</em>",h1=76),
S_(2,"THE MARKET",cs.FB_STATS+STATS_CSS+"<div class='lab'>CHARLOTTE METRO, NC + SC</div><h1>September <em>2026.</em></h1>"+
  row("MEDIAN<br>LIST PRICE","$424,950","−3.1% YoY")+row("PRICE PER<br>SQUARE FOOT","$217","−1.4% YoY")+
  row("NEW<br>LISTINGS","3,742","−7.5% YoY")+row("PENDING<br>LISTINGS","4,681","−5.9% YoY")+
  "<p class='tk'>Whatever the price, check the title and boundaries before you close.</p>"
  "<p class='src'>Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026</p>",h1=90),
S_(3,"TITLE","<h1>Title means <em>ownership.</em></h1>"+ul([
  "At closing, the deed shows the seller transferred ownership, or \"title,\" to you",
  "Old claims can surface later, like unpaid taxes or unpaid contractors",
  "A title search reviews the public records before you close"]),h1=84),
S_(4,"TWO POLICIES","<h1>Lender's policy <em>vs. owner's.</em></h1>"+ul([
  "Most lenders require a lender's title policy",
  "It protects the lender's loan, not your equity",
  "An owner's policy is optional and can help protect your investment"]),h1=80),
S_(5,"SHOP AROUND","<h1>You can <em>shop for title.</em></h1>"+ul([
  "Look at section C, page 2 of your Loan Estimate",
  "Your lender must give you a list of local providers",
  "Buying both policies from one provider usually costs less in total"]),h1=84),
S_(6,"THE SURVEY","<h1>Know where <em>the lines are.</em></h1>"+ul([
  "A survey can show boundaries, easements and setbacks",
  "NC's standard offer form lists a survey as a due diligence item",
  "Order it early so results arrive before your deadline"]),h1=84),
S_(7,"EASEMENTS","<h1>Read the <em>land questions.</em></h1>"+ul([
  "NC's disclosure statement (REC 4.22) asks about easements, shared driveways and encroachments",
  "It also asks about private roads and liens that could affect title",
  "SC's disclosure covers restrictive covenants and encroachments too"]),h1=80),
S_(8,"THE RULES","<h1>Read the rules <em>that come with it.</em></h1>"+ul([
  "Covenants and HOA documents can set mandatory rules for the lot or home",
  "NC's standard offer form recommends reviewing covenants, bylaws and rules",
  "Ask if the association charges fees for documents"]),h1=64),
S_(9,"ASK FIRST","<h1>Ask questions <em>before you sign.</em></h1>"+ul([
  "Ask your closing attorney to walk you through the title results",
  "Ask what any listed exceptions mean for the home",
  "Compare the survey with what you saw on your tour"]),h1=76),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 28%,rgba(0,0,0,.58) 46%,rgba(0,0,0,.9) 100%)!important}</style><h1>Clear title, <em>then commit.</em></h1><p class='b'>I recommend reviewing the title search, the survey and any HOA documents during due diligence, because they shape what you own and how you can use it. For legal questions about title, talk with a real estate attorney.</p>",contact=True,h1=74),
]
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
for i in range(1,11):
    v=f"{D}/slide-{i:02d}-video.png"
    if os.path.exists(v): os.remove(v)   # no video copies needed (no Short)
    assert Image.open(f"{D}/slide-{i:02d}.png").size==(1080,1350)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
