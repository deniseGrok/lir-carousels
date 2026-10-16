# theme=fullbleed_tips (NoDa format, Denise Oct 16 2026). Seller Tips: Prep before you list (Oct 16 2026). theme="photo_top" (Denise Oct 16 2026). Facts fetched Oct 16 2026; copy unchanged.
import sys, shutil, glob; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, FB_STATS
D="/workspace/lir-ai-team/content-research/carousels/2026-10-16-seller-tips-prep-before-listing"; F="SELLER TIPS"
for f in glob.glob(D+"/build/img-fb/*.jpg"): shutil.copy(f, D+"/build/img/"+f.split("/")[-1])
def slide(n,t,im,inner,ph=760,h1=78,li=34,**k):
    k.setdefault("theme","fullbleed_tips"); return _slide(n,t,im,inner,h1=h1,li=li,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STATS=("<style>.c{top:150px!important}.row{padding:14px 30px;margin-top:14px}.row .z{width:300px;font-size:32px}.row .v{font-size:84px}"
       ".lab{font-size:34px;margin-bottom:6px}h1{margin-bottom:18px}.src{margin-top:18px}</style>")
S=[
slide(1,"SELLER TIP 1","01.jpg","<div class='ill' style='display:block!important;position:fixed;top:40px;right:40px;left:auto;font-size:30px'>Photo: RoxylovesHistory (CC BY-SA 4.0)</div><h1>Fix the small stuff <em>before</em> buyers see it</h1><p class='b' style='font-size:36px'>Most of what buyers notice can be handled before the sign goes up. Here's the prep order I recommend.</p>",band="LISTING SOON? <em>PREP FIRST.</em>",ph=680,h1=72,footer=F),
slide(2,"THE MARKET","02.jpg",FB_STATS+STATS+"<h1>SouthPark <em>right now</em></h1><div class='lab'>AS OF SEPTEMBER 2026</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$625,000</span></div>"+
 "<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$610,000</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>573</span><span class='y'>+17.90% YoY</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>53</span><span class='y'>median</span></div>"+
 "<p class='b'>More listings than a year ago means buyers have more to compare.</p>"+src("Realtor.com Economic Research, SouthPark page, Sep 2026"),h1=78,footer=F),
slide(3,"SELLER TIP 2","03.jpg","<h1>Walk it <em>like a buyer</em></h1>"+ul(["Start at the curb, then the front door, then every room","Write down scuffs, drips, sticky doors and dead bulbs","Ask a friend to do the same walk. Fresh eyes catch more"]),footer=F),
slide(4,"SELLER TIP 3","04.jpg","<h1>Clear, clean, <em>then paint</em></h1>"+ul(["Pack what you won't need before moving day","Deep-clean kitchens, baths and windows","Minor cosmetic updates like paint, fixtures and landscaping typically pay off (Realtor.com)"]),ph=720,footer=F),
slide(5,"SELLER TIP 4","05.jpg","<h1>Find problems <em>before the buyer does</em></h1>"+ul(["Consider a pre-listing inspection","Fix anything leaking, broken or unsafe","Skip the big remodel: major renovations rarely return full cost (Realtor.com)"]),ph=720,footer=F),
slide(6,"SELLER TIP 5","06.jpg","<h1>NC disclosures: <em>start them now</em></h1>"+ul(["NC owners give buyers the Residential Property and Owners' Association Disclosure Statement (G.S. 47E&#8209;4)","Plus the Mineral and Oil and Gas Rights Disclosure (G.S. 47E&#8209;4.1)","Gather HOA dues, repair records and warranties while you prep"]),ph=680,h1=70,li=34,footer=F),
slide(7,"SELLER TIP 6","07.jpg","<h1>SC sellers <em>and older homes</em></h1>"+ul(["SC: owners deliver a written disclosure statement before the contract is signed (S.C. Code 27&#8209;50&#8209;50)","Built before 1978? Federal rules require a lead-based paint disclosure, EPA's pamphlet, and a 10-day inspection window buyers can waive (EPA)"]),ph=720,h1=72,li=34,footer=F),
slide(8,"SELLER TIP 7","08.jpg","<h1>Get it <em>photo-ready</em></h1>"+ul(["Open the blinds and turn on every light","Clear counters, tables and the fridge door","Tidy the yard and front entry. That's usually the first photo"]),footer=F),
slide(9,"SELLER TIP 8","09.jpg","<h1>Price from <em>the solds</em></h1>"+ul(["Start with recent nearby sales of similar homes, not list prices","Factor in the condition after your prep","Pricing accuracy directly affects buyer interest and days on market (Realtor.com)"]),ph=720,footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 34%,rgba(0,0,0,.6) 52%,rgba(0,0,0,.88) 100%)!important}</style><h1>Start prep <em>30 days out</em></h1><p class='b' style='margin-top:10px'>Walk it, fix it and start your disclosures. Then let's price it from the solds together.</p>",contact=True,ph=660,h1=68,footer=F),
]
build(S,D,"2026-10-16-seller-tips-prep-before-listing-DRAFT.pdf",D+"/build")
short(D,"2026-10-16-seller-tips-prep-before-listing-short.mp4",pad="0E1E3D")
