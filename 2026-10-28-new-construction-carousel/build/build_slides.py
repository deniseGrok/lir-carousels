# Oct 28 2026 New Construction Deal Carousel (fullbleed_teal) - two native sets: 4:5 1080x1350 (IG/LinkedIn), 1:1 1080x1080 (Facebook). No 9:16.
# Rendered through CDP (/workspace/tools/cdp.py) because headless --screenshot hangs on the box today.
import sys, os, zipfile; sys.path.insert(0,"/workspace/tools"); import cdp
from PIL import Image
N="2026-10-28-new-construction-carousel"; D=sys.argv[1]; B=os.path.dirname(os.path.abspath(__file__))
V="Builder's offer, verified on the builder's site Oct 28, 2026. Terms and eligibility set by the builder; subject to change."
TAG="NEW BUILD DEALS<br>NC + SC"; FOOT="NEW CONSTRUCTION"
L=dict(  # per-frame layout
 s45=dict(W=1080,H=1350,top=40,side=56,right=56,bot=96,ft=44,h1=84,li=30,lab=30,sub=32,note=27,band=52,fade="rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 40%,rgba(10,52,63,.5) 58%,rgba(9,46,56,.9) 100%"),
 s11=dict(W=1080,H=1080,top=34,side=50,right=50,bot=84,ft=36,h1=70,li=27,lab=27,sub=28,note=24,band=44,fade="rgba(8,40,50,.22) 0,rgba(8,40,50,0) 10%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 50%,rgba(9,46,56,.92) 100%"),
 s916=dict(W=1080,H=1920,top=260,side=60,right=150,bot=500,ft=440,h1=88,li=32,lab=31,sub=34,note=28,band=54,fade="rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 27%,rgba(10,52,63,.62) 40%,rgba(9,46,56,.88) 54%,rgba(9,46,56,.9) 74%,rgba(9,46,56,.78) 100%"),
)
def css(l):
    return f"""*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:{l['W']}px;height:{l['H']}px;overflow:hidden;background:#0F4C5C}}
.s{{position:relative;width:{l['W']}px;height:{l['H']}px;color:#fff;font-family:'Inter';font-weight:700}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}.ph:after{{content:'';position:absolute;inset:0;background:linear-gradient({l['fade']})}}
.tag{{position:absolute;top:{l['top']}px;left:{l['side']-16}px;background:#0F4C5C;color:#fff;border-bottom:4px solid #F2B705;font-family:'Montserrat';font-weight:800;font-size:{l['lab']-2}px;letter-spacing:2px;line-height:1.15;padding:12px 22px;border-radius:12px;z-index:3;box-shadow:0 4px 14px rgba(0,0,0,.2)}}
.cr{{position:absolute;top:{l['top']+6}px;right:{l['right']-16}px;background:rgba(15,76,92,.82);color:#fff;font-family:'Montserrat';font-weight:700;font-size:{l['lab']-4}px;padding:9px 18px;border-radius:10px;z-index:3}}
.c{{position:absolute;left:{l['side']}px;right:{l['right']}px;bottom:{l['bot']}px}}
h1{{font-family:'Anton';font-weight:400;font-size:{l['h1']}px;line-height:1.02;text-transform:uppercase;letter-spacing:.5px;text-shadow:0 2px 10px rgba(0,0,0,.45)}}h1 em{{font-style:normal;color:#F2B705}}
.lab{{display:inline-block;background:rgba(15,76,92,.88);padding:6px 14px;border-radius:8px;font-family:'Montserrat';font-weight:800;font-size:{l['lab']}px;letter-spacing:1.5px;color:#F2B705;margin-bottom:12px;text-transform:uppercase;text-shadow:0 2px 8px rgba(0,0,0,.6)}}
.sub{{font-family:'Montserrat';font-weight:800;font-size:{l['sub']}px;margin-top:12px;text-shadow:0 2px 8px rgba(0,0,0,.5)}}
ul{{list-style:none;margin-top:16px}}li{{font-size:{l['li']}px;line-height:1.26;padding-left:38px;position:relative;margin-bottom:10px;text-shadow:0 2px 8px rgba(0,0,0,.5)}}
li:before{{content:'';position:absolute;left:0;top:{int(l['li']*.36)}px;width:{int(l['li']*.55)}px;height:{int(l['li']*.55)}px;background:#F2B705;border-radius:3px}}
p.b{{font-size:{l['sub']}px;line-height:1.3;margin-top:14px;text-shadow:0 2px 8px rgba(0,0,0,.5)}}
.note{{font-size:{l['note']}px;line-height:1.3;font-weight:600;color:#F4F7F8;margin-top:8px;text-shadow:0 1px 6px rgba(0,0,0,.6)}}
.band{{background:#F2B705;color:#0F4C5C;font-family:'Anton';font-size:{l['band']}px;line-height:1.05;padding:10px 22px;border-radius:12px;margin-bottom:16px;display:inline-block}}.band em{{font-style:normal;color:#fff;text-shadow:0 1px 4px rgba(0,0,0,.35)}}
.cbox{{background:rgba(15,76,92,.84);border-radius:16px;border-left:10px solid #F2B705;padding:20px 28px 20px 22px;margin-top:16px;font-size:{l['li']}px;line-height:1.3;text-align:left}}.cbox b{{font-family:'Montserrat';font-weight:800}}
.ft{{position:absolute;left:{l['side']}px;right:{l['right']}px;bottom:{l['ft']}px;display:flex;justify-content:space-between;font-family:'Montserrat';font-weight:800;font-size:{l['lab']-2}px;letter-spacing:1.5px;color:#F4F7F8;text-shadow:0 2px 8px rgba(0,0,0,.5)}}"""
CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
         "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
ul=lambda xs:"<ul>"+"".join(f"<li>{x}</li>" for x in xs)+"</ul>"
def offer(lab,h1,sub,items): return f"<div class='lab'>{lab}</div><h1>{h1}</h1><div class='sub'>{sub}</div>"+ul(items)+f"<div class='note'>{V}</div>"
T="Tip from each builder's posted terms, read Oct 28, 2026. Terms and eligibility set by the builder; subject to change."
def tip(lab,h1,sub,items): return f"<div class='lab'>{lab}</div><h1>{h1}</h1><div class='sub'>{sub}</div>"+ul(items)+f"<div class='note'>{T}</div>"
S={
1:("Lennar","<div class='band'>NEW BUILDS. <em>VERIFIED OCT 28.</em></div><h1>6 builder rate deals <em>near Charlotte.</em></h1>"
   "<p class='b'>Kannapolis, Troutman, Bessemer City, Gastonia, Lincolnton and Salisbury. Each one checked on the builder's own website on Oct 28, 2026.</p>"
   +ul(["Two 5/1 FHA ARMs and a 3.99% first-year buydown","Plus 2 slides on how to compare them"])),
2:("Lennar",offer("Bakers Creek · Kannapolis, NC","<em>4.50%</em> 5/1 FHA ARM.","Lennar · select homes · 7.529% APR",
   ["Fixed at 4.500% (7.529% APR) for the first 5 years, then adjusts once a year","Sign a purchase agreement Oct 26–Nov 1, 2026; close by Nov 24, 2026","Through Lennar Mortgage, Lennar's affiliated lender"])),
3:("Lennar",offer("Sutton Village · Troutman, NC","Up to <em>$7,500</em> toward closing costs.","Lennar · select homes · Black Friday Sales Event",
   ["A closing credit of up to $7,500 (prepaids excluded), per the builder's terms","Paired with the 4.500% (7.529% APR) FHA 5/1 ARM","Purchase agreement Oct 26–Nov 1, 2026; close by Nov 24, 2026"])),
4:("Lennar",offer("Creekside Cottages · Bessemer City, NC","<em>4.50%</em> ARM + up to <em>$7,500.</em>","Lennar · select homes · 7.529% APR",
   ["Both parts require financing with Lennar Mortgage; buying with another lender is allowed, without the offer","Can't be combined with other Lennar promotions","Sign Oct 26–Nov 1, 2026; close by Nov 24, 2026"])),
5:("Mattamy Homes",offer("The Townes at Westfall · Gastonia, NC","<em>3.99%</em> first-year rate.","Mattamy Homes · select quick move-in townhomes",
   ["2/1 buydown: 3.99% (6.784% APR) year-1 payment on a 5.99% FHA fixed rate","4.99% in year 2, then the 5.99% fixed rate","Contracts Oct 2–31, 2026; close by Nov 30, 2026; Mattamy Home Funding"])),
6:("Century Communities",offer("Carpenter Farms · Lincolnton, NC","<em>4.875%</em> 5/1 FHA ARM.","Century Communities · select homes · 5.674% APR",
   ["4.875% (5.674% APR) for the first 60 months, per the builder's example","Plus up to $3,000 toward closing costs with Inspire Home Loans","Select Charlotte-division homes that close on or before Dec 31, 2026"])),
7:("Century Communities",offer("Grants Landing · Salisbury, NC","Up to <em>$3,000</em> toward closing costs.","Century Communities · select homes · with the 4.875% ARM",
   ["Requires closing a loan with Inspire Home Loans, Century's affiliated lender","ARM adjusts yearly after month 60: up to 1% a year, 5% lifetime (9.875% cap)","Contracts that close on or before Dec 31, 2026"])),
8:("Century Communities",tip("Tip · Compare","Same 5/1 ARM. <em>Different APR.</em>","Why the rate alone doesn't tell the story",
   ["Lennar: 4.500% rate, 7.529% APR. Century: 4.875% rate, 5.674% APR","Each builder's APR uses its own example price, loan and credit score","Ask each lender for a Loan Estimate on the home you want"])),
9:("Mattamy Homes",tip("Tip · Deadlines","The close-by date <em>is the real clock.</em>","Every offer here is tied to a closing date",
   ["Lennar: sign Oct 26–Nov 1, close by Nov 24, 2026","Mattamy Homes: contract by Oct 31, close by Nov 30, 2026","Century Communities: close on or before Dec 31, 2026"])),
10:("Century Communities","<h1>DM or comment <em>DEALS</em> and we'll get started.</h1><p class='b'>I'll help you compare the payment, the deadline and the lender rules on each one.</p>"
   "<div class='note'>Builder incentives can change; verify with the builder.</div>"+CONTACT),
}
def page(i,l,imgdir):
    cr,body=S[i]
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css(l)}</style></head><body><div class='s'>"
            f"<div class='ph' style=\"background-image:url('{imgdir}/{i:02d}.jpg')\"></div><div class='tag'>{TAG}</div><div class='cr'>Photo: {cr}</div>"
            f"<div class='c'>{body}</div><div class='ft'><span>{FOOT}</span><span>{i} / 10</span></div></div></body></html>")
for key,imgdir,out in (("s45","img",D),("s11","img1x1",D+"/slides-1x1")):
    os.makedirs(out,exist_ok=True); l=L[key]
    for i in S:
        hp=os.path.join(B,f"{key}-slide-{i:02d}.html"); open(hp,"w").write(page(i,l,imgdir))
        cdp.shot(hp,f"{out}/slide-{i:02d}.png",l["W"],l["H"])
    print(key,"ok")
ims=[Image.open(f"{D}/slide-{i:02d}.png").convert("RGB") for i in range(1,11)]
ims[0].save(f"{D}/{N}-DRAFT.pdf",save_all=True,append_images=ims[1:],resolution=150)
for zn,sub in (("slides.zip",""),("slides-1x1.zip","slides-1x1/")):
    with zipfile.ZipFile(f"{D}/{zn}","w") as z:
        for i in range(1,11): z.write(f"{D}/{sub}slide-{i:02d}.png",f"slide-{i:02d}.png")
print("done")
