# theme=fullbleed_tips (NoDa format, Denise Oct 16 2026; adapted from 2026-10-19-buyer-tips-contract-to-closing/build/build_slides.py
# and 2026-10-16-seller-tips-prep-before-listing). Seller Tips: Know your net (Tue Oct 20 2026). DRAFT — AWAITING DENISE APPROVAL. All facts fetched Oct 20 2026.
import sys; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, FB_STATS
D="/workspace/lir-ai-team/content-research/carousels/2026-10-20-seller-tips-net-proceeds"; F="SELLER TIPS"; NAME="2026-10-20-seller-tips-net-proceeds"
def slide(n,t,im,inner,ph=760,h1=78,li=34,**k):
    k.setdefault("theme","fullbleed_tips"); return _slide(n,t,im,inner,h1=h1,li=li,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STATS=("<style>.c{top:205px!important}.row{padding:14px 30px;margin-top:14px}.row .z{width:300px;font-size:32px}.row .v{font-size:84px}"
       ".lab{font-size:34px;margin-bottom:6px}h1{margin-bottom:18px}.src{margin-top:18px}</style>")
NB="&#8209;"  # non-breaking hyphen
S=[
slide(1,"SELLER TIP 1","01.jpg","<h1>Your price <em>isn't your net</em></h1><p class='b' style='font-size:36px'>What you walk away with is the price minus your loan payoff, closing costs and anything you agree to give. Here's how I recommend estimating it before you list.</p>",band="SELLING? <em>KNOW YOUR NET.</em>",h1=80,footer=F),
slide(2,"THE MARKET","01.jpg",FB_STATS+STATS+"<h1>Charlotte metro <em>right now</em></h1><div class='lab'>SEPTEMBER 2026 · NC + SC</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$424,950</span><span class='y'>&minus;3.1% YoY</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>11,182</span><span class='y'>+10.3% YoY</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>64</span><span class='y'>median</span></div>"+
 "<div class='row'><span class='z'>PRICE CUTS</span><span class='v'>26.2%</span><span class='y'>of listings</span></div>"+
 "<p class='b'>More competition than a year ago, and about 1 in 4 listings had a price cut. Knowing your net helps you price with confidence.</p>"+src("Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, Sep 2026"),h1=78,footer=F),
slide(3,"SELLER TIP 2","03.jpg","<h1>Request your <em>payoff early</em></h1>"+ul(["Your payoff isn't the balance on your statement. It's what it takes to pay the loan in full on a specific date","Your servicer must send it within 7 business days of a written request, with limited exceptions",f"Under NC Form 2{NB}T, loans and liens, like a home equity line, are paid at or before closing"]),h1=78,footer=F),
slide(4,"SELLER TIP 3","04.jpg","<h1>Plan for <em>transfer tax</em></h1>"+ul(["NC excise tax: $1 per $500 of the price, paid by the seller. That's $800 on a $400,000 sale","SC deed recording fee: $1.85 per $500, the seller's responsibility. That's $1,480 on a $400,000 sale","Both are paid at closing from your proceeds"]),h1=80,footer=F),
slide(5,"SELLER TIP 4","05.jpg","<h1>Expect <em>prorations</em></h1>"+ul([f"Under NC Form 2{NB}T, property taxes are prorated on a calendar{NB}year basis","You're responsible for taxes and HOA dues through the settlement date","Already paid this year's tax bill? Ask how it shows up on your settlement statement"]),h1=80,footer=F),
slide(6,"SELLER TIP 5","06.jpg","<h1>Ask about <em>HOA fees</em></h1>"+ul(["If you have an HOA, ask early for its list of resale and transfer fees",f"Under NC Form 2{NB}T, sellers pay for resale certificates, payment{NB}status letters and ownership transfer fees",f"Buyers pay for lender questionnaires and move{NB}in or working{NB}capital charges"]),h1=80,footer=F),
slide(7,"SELLER TIP 6","07.jpg","<h1>Commissions <em>are negotiable</em></h1>"+ul(["Broker commissions aren't set by law. They're negotiated and put in writing","A buyer may ask you to help with their agent's pay as a concession. That's your decision","Whatever you agree to comes out of your net, so see it on paper first"]),h1=76,footer=F),
slide(8,"SELLER TIP 7","08.jpg","<h1>Count repairs <em>and credits</em></h1>"+ul(["Repairs you agree to after inspections are part of your cost to sell","So is any closing{NB}cost help or home warranty you agree to pay for".replace("{NB}",NB),f"Under NC Form 2{NB}T, a seller{NB}paid home warranty is paid at Settlement"]),h1=78,footer=F),
slide(9,"SELLER TIP 8","09.jpg","<h1>Know the <em>tax rules</em></h1>"+ul(["Selling your main home? You may be able to exclude up to $250,000 of gain, or $500,000 filing jointly","Generally, you must have owned it and lived there 2 of the last 5 years",f"Get a Form 1099{NB}S? Report the sale even if the gain is excluded. A tax professional can help"]),h1=80,footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<style>.ph:after{background:linear-gradient(rgba(0,0,0,.28) 0,rgba(0,0,0,0) 12%,rgba(0,0,0,0) 34%,rgba(0,0,0,.6) 52%,rgba(0,0,0,.88) 100%)!important}</style><h1>Get a <em>net sheet</em> first</h1><p class='b' style='margin-top:10px'>I recommend a written estimate of your net before we set your list price, because it shows the number that matters before you decide. Let's run yours together.</p>",contact=True,h1=74,footer=F),
]
build(S,D,NAME+"-DRAFT.pdf",D+"/build")
short(D,NAME+"-short.mp4",pad="0E1E3D")
