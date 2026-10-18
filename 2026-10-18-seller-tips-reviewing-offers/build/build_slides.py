# theme=fullbleed_tips (NoDa format, Denise Oct 16 2026; adapted from 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py @ 9708bcd
# and 2026-10-17-buyer-tips-inspections). Seller Tips: Review the whole offer (Oct 18 2026). DRAFT — AWAITING DENISE APPROVAL. All facts fetched Oct 18 2026.
import sys; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, FB_STATS
D="/workspace/lir-ai-team/content-research/carousels/2026-10-18-seller-tips-reviewing-offers"; F="SELLER TIPS"; NAME="2026-10-18-seller-tips-reviewing-offers"
def slide(n,t,im,inner,ph=760,h1=78,li=34,**k):
    k.setdefault("theme","fullbleed_tips"); return _slide(n,t,im,inner,h1=h1,li=li,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STATS=("<style>.c{top:205px!important}.row{padding:14px 30px;margin-top:14px}.row .z{width:300px;font-size:32px}.row .v{font-size:84px}"
       ".lab{font-size:34px;margin-bottom:6px}h1{margin-bottom:18px}.src{margin-top:18px}</style>")
NB="&#8209;"  # non-breaking hyphen
S=[
slide(1,"SELLER TIP 1","01.jpg","<h1>Review <em>the whole offer</em></h1><p class='b' style='font-size:36px'>Price is one line. Fees, deposits, dates and contingencies shape what you actually get. Here's how I recommend reading each offer.</p>",band="GOT AN OFFER? <em>READ PAST THE PRICE.</em>",h1=78,footer=F),
slide(2,"THE MARKET","01.jpg",FB_STATS+STATS+"<h1>SouthPark <em>right now</em></h1><div class='lab'>AS OF OCTOBER 2026</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$625,000</span></div>"+
 "<div class='row'><span class='z'>SALE-TO-LIST</span><span class='v'>98%</span><span class='y'>1.54% under ask</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>56</span><span class='y'>median</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>581</span><span class='y'>+13.16% YoY</span></div>"+
 "<p class='b'>Offers are landing close to asking, so the terms can matter as much as the price.</p>"+src("Realtor.com Economic Research, SouthPark page, Oct 2026"),h1=78,footer=F),
slide(3,"SELLER TIP 2","03.jpg","<h1>NC: weigh the <em>due diligence fee</em></h1>"+ul([f"On NC's Form 2{NB}T, it's paid to you and due on the Effective Date","It's yours from that date and credited to the buyer at closing","It's non-refundable unless the contract says otherwise or you materially breach"]),h1=72,footer=F),
slide(4,"SELLER TIP 3","04.jpg","<h1>Check the <em>earnest money</em></h1>"+ul(["NC: it goes to the escrow agent within five days of the Effective Date","NC: if the buyer ends the deal during due diligence, it's refunded to them",f"SC: a broker holds it in a separate trust account until closing or termination (S.C. Code 40{NB}57{NB}136)"]),h1=74,footer=F),
slide(5,"SELLER TIP 4","05.jpg","<h1>Ask how <em>they'll pay</em></h1>"+ul([f"Cash offer? NC's Form 2{NB}T advises sellers to get proof of funds before signing","A preapproval letter helps, but it isn't a guaranteed loan offer (CFPB)",f"NC's Form 2{NB}T has no loan or appraisal contingency. The buyer's due diligence period covers that"]),h1=78,footer=F),
slide(6,"SELLER TIP 5","06.jpg","<h1>Read <em>the contingencies</em></h1>"+ul(["NC: the standard contract isn't contingent on the buyer selling their home. That takes a custom addendum",f"SC: every term and condition belongs in the written offer (S.C. Code 40{NB}57{NB}135)","Know exactly which conditions you're agreeing to"]),h1=78,footer=F),
slide(7,"SELLER TIP 6","07.jpg","<h1>Match the <em>dates</em> to your move</h1>"+ul(["NC: settlement happens no later than the contract date, at a time and place the buyer picks","Possession transfers at closing unless an addendum says otherwise",f"Need a few days after closing? Ask about a Seller Possession After Closing Agreement (Form 2A8{NB}T)"]),h1=74,footer=F),
slide(8,"SELLER TIP 7","08.jpg","<h1>Add up <em>the concessions</em></h1>"+ul([f"NC: seller concessions sit on page 1 of Form 2{NB}T, as dollars or a percent","Buyer agent compensation (Form 220) is a concession too, in addition to those","Ask for a net sheet on each offer so you compare what you'd keep"]),h1=78,footer=F),
slide(9,"SELLER TIP 8","09.jpg","<h1>Multiple offers? <em>You decide</em></h1>"+ul(["There's no \"first in the door\" rule. You choose which offer to work with (NCREC)","You can ask some or all buyers for their highest and best (NCREC)","Any change you make is a counteroffer, and it rejects the original offer (NCREC)"]),h1=74,footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 34%,rgba(0,0,0,.6) 52%,rgba(0,0,0,.88) 100%)!important}</style><h1>Compare offers <em>side by side</em></h1><p class='b' style='margin-top:10px'>I recommend one page per offer with your estimated net, so you decide on the full picture. Let's review yours together.</p>",contact=True,h1=72,footer=F),
]
build(S,D,NAME+"-DRAFT.pdf",D+"/build")
short(D,NAME+"-short.mp4",pad="0E1E3D")
