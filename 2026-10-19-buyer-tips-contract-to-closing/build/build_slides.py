# theme=fullbleed_tips (NoDa format, Denise Oct 16 2026; adapted from 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py @ 9708bcd
# and 2026-10-18-seller-tips-reviewing-offers). Buyer Tips: From contract to keys (Oct 19 2026). DRAFT — AWAITING DENISE APPROVAL. All facts fetched Oct 19 2026.
import sys; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, FB_STATS
D="/workspace/lir-ai-team/content-research/carousels/2026-10-19-buyer-tips-contract-to-closing"; F="BUYER TIPS"; NAME="2026-10-19-buyer-tips-contract-to-closing"
def slide(n,t,im,inner,ph=760,h1=78,li=34,**k):
    k.setdefault("theme","fullbleed_tips"); return _slide(n,t,im,inner,h1=h1,li=li,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STATS=("<style>.c{top:205px!important}.row{padding:14px 30px;margin-top:14px}.row .z{width:300px;font-size:32px}.row .v{font-size:84px}"
       ".lab{font-size:34px;margin-bottom:6px}h1{margin-bottom:18px}.src{margin-top:18px}</style>")
NB="&#8209;"  # non-breaking hyphen
S=[
slide(1,"BUYER TIP 1","01.jpg","<h1>From contract <em>to keys</em></h1><p class='b' style='font-size:36px'>The weeks between an accepted offer and closing day shape how smoothly you move in. Here's how I recommend using them.</p>",band="UNDER CONTRACT? <em>PLAN THE CLOSE.</em>",h1=80,footer=F),
slide(2,"THE MARKET","01.jpg",FB_STATS+STATS+"<h1>Charlotte <em>right now</em></h1><div class='lab'>AS OF OCTOBER 2026</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$421,450</span></div>"+
 "<div class='row'><span class='z'>SALE-TO-LIST</span><span class='v'>99%</span><span class='y'>1.16% under ask</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>63</span><span class='y'>median</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>6,000</span><span class='y'>+13.79% YoY</span></div>"+
 "<p class='b'>More homes to choose from than a year ago, and offers still land close to asking. Plan your closing as carefully as your offer.</p>"+src("Realtor.com Economic Research, Charlotte, NC, Oct 2026"),h1=78,footer=F),
slide(3,"BUYER TIP 2","03.jpg","<h1>Check your <em>rate lock</em></h1>"+ul(["A lock keeps your rate from changing until closing, if you close in time and your application doesn't change","Locks typically run 30, 45 or 60 days. Make sure yours covers your closing date","Extending a lock can be expensive, so ask about it up front"]),h1=80,footer=F),
slide(4,"BUYER TIP 3","04.jpg","<h1>Keep your <em>finances steady</em></h1>"+ul(["Even a locked rate can change if your loan amount, credit score or verified income changes","A new loan or a missed payment can move your credit score","I recommend checking with your lender before any big purchase or job change"]),h1=78,footer=F),
slide(5,"BUYER TIP 4","05.jpg","<h1>Get a copy of <em>the appraisal</em></h1>"+ul([f"On a first{NB}lien mortgage, your lender must give you a free copy of every appraisal","It's due promptly when it's done, or three business days before closing, whichever is earlier","You may be asked to waive that timing. Think it over before you agree"]),h1=74,footer=F),
slide(6,"BUYER TIP 5","06.jpg","<h1>Line up <em>insurance early</em></h1>"+ul(["Lenders generally require proof of homeowner's insurance","Standard policies don't cover flood or earthquake damage, though you may be able to add it","You can shop for your own policy and compare it with your Loan Estimate"]),h1=80,footer=F),
slide(7,"BUYER TIP 6","07.jpg","<h1>Read your <em>Closing Disclosure</em></h1>"+ul(["Your lender must give it to you at least three business days before closing","Compare it with your Loan Estimate: loan type, rate, monthly payment and fees","By law, only certain costs can change. Ask about anything that did"]),h1=74,footer=F),
slide(8,"BUYER TIP 7","08.jpg","<h1>Verify every <em>wire</em></h1>"+ul(["An email with last-minute changes to wire instructions may be a scam","Confirm by phone with trusted contacts, using numbers you saved in advance","Never use phone numbers or links from the email itself"]),h1=80,footer=F),
slide(9,"BUYER TIP 8","09.jpg","<h1>Get ready for <em>closing day</em></h1>"+ul(["Bring your ID, your Closing Disclosure and your payment or proof of wire","Take all the time you need to read every document",f"NC: keys, codes and garage openers are delivered at Closing unless an agreement says otherwise (Form 2{NB}T)"]),h1=76,footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 34%,rgba(0,0,0,.6) 52%,rgba(0,0,0,.88) 100%)!important}</style><h1>Build one <em>closing calendar</em></h1><p class='b' style='margin-top:10px'>I recommend putting your rate lock, appraisal, insurance and Closing Disclosure dates on one calendar the day you go under contract. Let's map yours together.</p>",contact=True,h1=72,footer=F),
]
build(S,D,NAME+"-DRAFT.pdf",D+"/build")
short(D,NAME+"-short.mp4",pad="0E1E3D")
