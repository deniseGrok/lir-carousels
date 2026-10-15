# DRAFT — AWAITING DENISE APPROVAL. Buyer Tips: Get pre-approved before you tour (Oct 15 2026). All facts re-fetched Oct 15 2026.
import sys; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short
THEME = "fullbleed"  # approved Oct 14 2026 for neighborhood + tips
def slide(n,t,im,inner,**k):
    inner+="<style>.ill{display:none!important}</style>"  # Denise Oct 15: no Illustrative image labels
    a=(n,t,im,inner); k.setdefault("theme", THEME); k.setdefault("h1", 84); return _slide(*a, **k)
D="/workspace/lir-ai-team/content-research/carousels/2026-10-15-buyer-tips-preapproval"; F="BUYER TIPS"
src=lambda s: f"<p class='src'>Source: {s}</p>"
nosrc=lambda s: ""  # Denise Oct 15: source line on slide 2 only
CF="CFPB, consumerfinance.gov"
NCR="NC REALTORS® North Carolina Buyer Advisory"
S=[
slide(1,"BUYER TIP 1","01.jpg","<h1>Know your number <em>before</em> you fall for a house</h1><p class='b'>A preapproval letter says what a lender is tentatively willing to lend. Start there, and your weekends go to homes that fit.</p>"+nosrc(CF+", Get a preapproval letter"),band="BEFORE YOU TOUR. <em>GET PRE-APPROVED.</em>",footer=F),
slide(2,"THE MARKET","02.jpg","<div class='lab'>SOUTHPARK · AS OF SEPTEMBER 2026</div>"+
 "<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$625,000</span></div>"+
 "<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$610,000</span></div>"+
 "<div class='row'><span class='z'>ACTIVE</span><span class='v'>573 homes</span></div>"+
 "<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>53 (median)</span></div>"+src("Realtor.com Economic Research, SouthPark page, Sep 2026"),ph=380,ct=330,footer=F),
slide(3,"BUYER TIP 2","03.jpg","<h1>Prequal vs. <em>preapproval</em></h1>"+ul(["Both are letters saying a lender may lend up to an amount, based on assumptions","Some lenders prequalify on what you report and preapprove only on verified info","Neither one is a guaranteed loan offer"])+nosrc(CF),footer=F),
slide(4,"BUYER TIP 3","04.jpg","<h1>Build your <em>lender packet</em></h1>"+ul(["Pay stubs for the last 30 days","W-2s and signed federal tax returns, last two years","Your two most recent bank statements","Proof of your down payment source + photo ID"])+nosrc(CF+", Create a loan application packet (needs vary by lender)"),footer=F),
slide(5,"BUYER TIP 4","05.jpg","<h1>What a strong letter <em>tells a seller</em></h1>"+ul(["Sellers frequently require one before accepting an offer","It should state the lender reviewed your credit, income and cash to close","Ask the lender what assumptions they made"])+nosrc(f"{CF}; {NCR}"),footer=F),
slide(6,"BUYER TIP 5","06.jpg","<h1>Two NC deposits <em>to plan for</em></h1>"+ul(["Earnest money: common, held in trust by an escrow agent","Due diligence fee: negotiated and paid directly to the seller","It's generally non-refundable, but credited toward the price if you close"])+nosrc(f"{NCR}; NCREC"),footer=F),
slide(7,"BUYER TIP 6","07.jpg","<h1>Your <em>closing attorney</em></h1>"+ul(["NC: a licensed NC attorney supervises residential closings","SC: a licensed SC attorney supervises residential closings"])+nosrc("CFPB; N.C.G.S. 10B-134.25; SC Bar Ethics Op. 09-01; S.C. Code 37-10-102"),footer=F),
slide(8,"BUYER TIP 7","08.jpg","<h1>Tour with a <em>written plan</em></h1>"+ul(["Set your price ceiling from your own budget, not only the letter","Tell your agent you don't want to see homes above it","List must-haves and nice-to-haves before the first showing"])+nosrc(CF+"; last tip is my own"),footer=F),
slide(9,"AVOID THIS","09.jpg","<h1>Don't <em>fall first</em></h1>"+ul(["Touring before you know your number","Letting the maximum approval set your budget","Letting your letter expire mid-search (typically 30 to 60 days)"])+nosrc(CF+"; my own tip"),footer=F),
slide(10,"MY RECOMMENDATION","10.jpg","<h1>Letter first, <em>then the tour</em></h1><p class='b'>Talk with a lender, gather your packet, and then let's plan a SouthPark tour around your number.</p><style>.cbox{text-align:center;padding:22px 30px;border-left-width:10px}</style>",contact=True,ph=380,ct=340,footer=F),
]
build(S,D,"2026-10-15-buyer-tips-preapproval-DRAFT.pdf",D+"/build")
short(D,"2026-10-15-buyer-tips-preapproval-short.mp4")
