# theme=fullbleed_tips (NoDa format, Denise Oct 16 2026; adapted from 2026-10-16-seller-tips-prep-before-listing/build/build_slides.py @ 9708bcd).
# Buyer Tips: Inspect before you commit (Oct 17 2026). DRAFT — AWAITING DENISE APPROVAL. All facts fetched Oct 17 2026.
import sys; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, FB_STATS
D="/workspace/lir-ai-team/content-research/carousels/2026-10-17-buyer-tips-inspections"; F="BUYER TIPS"
def slide(n,t,im,inner,ph=760,h1=78,li=34,**k):
    k.setdefault("theme","fullbleed_tips"); return _slide(n,t,im,inner,h1=h1,li=li,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STATS=("<style>.c{top:205px!important}.row{padding:14px 30px;margin-top:14px}.row .z{width:300px;font-size:32px}.row .v{font-size:84px}"
       ".lab{font-size:34px;margin-bottom:6px}h1{margin-bottom:18px}.src{margin-top:18px}</style>")
S=[
slide(1,"BUYER TIP 1","01.jpg","<h1>Book your inspection <em>right away</em></h1><p class='b' style='font-size:36px'>Once you're under contract, the clock starts. Here's how I recommend using your inspection window.</p>",band="UNDER CONTRACT? <em>INSPECT FIRST.</em>",h1=76,footer=F),
slide(2,"THE MARKET","01.jpg",FB_STATS+STATS+"<h1>SouthPark <em>right now</em></h1><div class='lab'>AS OF OCTOBER 2026</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$625,000</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>581</span><span class='y'>+13.16% YoY</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>56</span><span class='y'>median</span></div>"+
 "<div class='row'><span class='z'>SALE-TO-LIST</span><span class='v'>98%</span></div>"+
 "<p class='b'>More homes to compare than a year ago. Know the condition of the one you choose.</p>"+src("Realtor.com Economic Research, SouthPark page, Oct 2026"),h1=78,footer=F),
slide(3,"BUYER TIP 2","03.jpg","<h1>NC: use your <em>due diligence period</em></h1>"+ul(["On NC's standard contract (Form 2&#8209;T), you can end the deal for any reason during this period","That's the window for inspections, specialists and repair talks","The due diligence fee is generally non-refundable, so have inspectors lined up"]),h1=72,footer=F),
slide(4,"BUYER TIP 3","04.jpg","<h1>SC: know <em>your contract's dates</em></h1>"+ul(["Your purchase contract sets the inspection terms and deadlines","If it's contingent on a satisfactory inspection, you may be able to cancel without penalty (CFPB)","Put every deadline on your calendar the day you sign"]),h1=72,footer=F),
slide(5,"BUYER TIP 4","05.jpg","<h1>Hire a <em>licensed</em> inspector</h1>"+ul(["NC: paid home inspections require a license from the NC Home Inspector Licensure Board (G.S. 143&#8209;151.50)","SC: home inspectors must be licensed by the SC Residential Builders Commission (S.C. Code 40&#8209;59&#8209;520)","Choose someone accountable to you (CFPB)"]),h1=74,footer=F),
slide(6,"BUYER TIP 5","06.jpg","<h1>Be there <em>and ask questions</em></h1>"+ul(["Attending makes the report easier to understand (CFPB)","Ask what wasn't inspected. In SC, the report must note it (S.C. Code 40&#8209;59&#8209;560)","Take notes and photos as you walk"]),footer=F),
slide(7,"BUYER TIP 6","07.jpg","<h1>Read <em>the whole report</em></h1>"+ul(["NC: the report is due by the agreed date, or within 3 business days (G.S. 143&#8209;151.58)","NC's summary page says it plainly: it is not the entire report","Items flagged for a specialist deserve a closer look"]),footer=F),
slide(8,"BUYER TIP 7","08.jpg","<h1>Ask about <em>radon</em></h1>"+ul(["EPA recommends knowing the radon level in any home you consider buying","Ask the seller for past results. No test yet? Have it tested","EPA: fix the home if radon is 4 pCi/L or higher"]),footer=F),
slide(9,"BUYER TIP 8","09.jpg","<h1>Then <em>negotiate calmly</em></h1>"+ul(["You can ask the seller to make repairs or give a credit (CFPB)","The seller may or may not agree, depending on your contract and the market (CFPB)","Your lender may require some repairs before closing (CFPB)"]),footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 34%,rgba(0,0,0,.6) 52%,rgba(0,0,0,.88) 100%)!important}</style><h1>Pick your inspector <em>before you offer</em></h1><p class='b' style='margin-top:10px'>I recommend it so the first days of your window go to answers, not phone calls. Let's plan it together.</p>",contact=True,h1=68,footer=F),
]
build(S,D,"2026-10-17-buyer-tips-inspections-DRAFT.pdf",D+"/build")
short(D,"2026-10-17-buyer-tips-inspections-short.mp4",pad="0E1E3D")
