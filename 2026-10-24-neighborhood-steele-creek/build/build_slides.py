# Steele Creek neighborhood spotlight Oct 24 2026. theme="fullbleed_teal" (teal #0F4C5C / gold #F2B705), 10 slides.
# Renders: slide-NN.png (1080x1350, 4:5 IG/FB/LinkedIn), slide-NN-video.png (4:5, no SWIPE), slides-9x16/slide-NN.png
# + slides-1x1/slide-NN.png (1080x1080 native square layout for the Facebook carousel, Denise Oct 22 2026: tag top, text
# bottom-anchored, smaller headline and bullets so nothing is cropped or cramped).
# (1080x1920 native 9:16 layout for the Short/Reel, TikTok photo mode, Stories: header tag below the top 250px, text ends above
# the bottom 420px and stays left of the right 140px). Plus PDF + slides.zip + slides-9x16.zip.
# Compliance: TEMPLATES/COMPLIANCE.md (Oct 22 2026): slide 10 contact block with firm line + EHO; no people/demographics/schools.
import sys, os, zipfile, subprocess
sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
from carousel_style import ul
from PIL import Image

sys.path.insert(0,"/workspace/tools"); import cdp
_run=subprocess.run
def _patched(args,*a,**k):
    if args and args[0]=="google-chrome":
        ws=[x for x in args if x.startswith("--window-size=")][0].split("=")[1].split(","); op=[x for x in args if x.startswith("--screenshot=")][0].split("=",1)[1]
        hp=[x for x in args if x.startswith("file://")][0][7:]; cdp.shot(hp,op,int(ws[0]),int(ws[1])); return None
    return _run(args,*a,**k)
subprocess.run=_patched; cs.subprocess.run=_patched
N="2026-10-24-neighborhood-steele-creek"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/repos/lir-carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="NEIGHBORHOOD SPOTLIGHT"
cs.CONTACT=("<div class='cbox'><b>Denise Wilson | REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>"
            "denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>")
def S_(n,tag,inner,**k):
    k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F)
    return cs.slide(n,tag,f"{n:02d}.jpg",inner,**k)
cr=lambda s: f"<div class='cr' style='position:fixed;top:124px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.85);background:rgba(8,40,50,.62);padding:4px 14px;border-radius:10px'>Photo: {s}</div>"
row=lambda z,v,y="":f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>"
STATS_CSS=("<style>.row{padding:18px 28px}.row .z{width:380px;font-size:30px;line-height:1.15}.row .v{font-size:66px}"
           ".tk{font-size:34px;line-height:1.3;margin-top:24px}</style>")
SL=[
S_(1,"STEELE CREEK",cr("Lake Wylie · bobcapra, CC BY 2.0")+"<h1>Lake views on Charlotte's <em>southwest side.</em></h1>"+ul([
  "A Charlotte community in ZIP codes 28273 and 28278",
  "One of Mecklenburg County's original 15 townships",
  "Its western edge meets Lake Wylie, pictured here"]),band="CHARLOTTE NC. <em>STEELE CREEK.</em>",h1=78),
S_(2,"HISTORY",cr("Bagatar, CC BY-SA 3.0")+"<h1>Roots older than <em>the county.</em></h1>"+ul([
  "Steele Creek Presbyterian Church was organized in 1760, two years before Mecklenburg County was formed",
  "Its Gothic Revival brick sanctuary was completed in 1889",
  "The sanctuary and cemetery were listed on the National Register of Historic Places in 1991"])),
S_(3,"HISTORIC LANDMARK",cr("Bagatar, CC BY-SA 3.0")+"<h1>A burial ground <em>from the 1760s.</em></h1>"+ul([
  "The cemetery beside the 1889 sanctuary dates to about 1763",
  "A dry-laid stone wall with iron gates surrounds it",
  "It holds the graves of 13 Revolutionary War soldiers"])),
S_(4,"THE LAKE",cr("Lake Wylie · bobcapra, CC BY 2.0")+"<h1>Lake Wylie, <em>since 1904.</em></h1>"+ul([
  "First formed in 1904 by a dam on the Catawba River near Fort Mill, S.C.",
  "A rebuilt dam in 1924 grew it to about 13,443 acres and 325 miles of shoreline",
  "Renamed in 1960 for Dr. W. Gil Wylie"])),
S_(5,"OUTDOORS","<h1>1,100 acres <em>on the water.</em></h1>"+ul([
  "McDowell Nature Preserve is a Mecklenburg County preserve on the Lake Wylie shore",
  "More than seven miles of hiking trails, a nature center and a campground",
  "Boat launch at Copperhead Island, pictured here"]),h1=78),
S_(6,"STATE LINE",cr("Carowinds · Dough4872, CC BY-SA 4.0")+"<h1>Fun on <em>both sides of the line.</em></h1>"+ul([
  "Carowinds opened March 31, 1973, and straddles the North Carolina and South Carolina line",
  "A golden state line runs through the park",
  "Nearby, Charlotte Premium Outlets opened in 2014 at I-485 and Steele Creek Road"]),h1=76),
S_(7,"THE HOMES","<h1>From farmland <em>to new homes.</em></h1>"+ul([
  "Much of Steele Creek stayed rural farmland until the 2000s",
  "I-485, a widened NC 49 and a new Buster Boyd Bridge brought new homes and shopping",
  "Newer subdivisions and mixed-use developments now fill much of the area"])),
S_(8,"MY TIP","<h1>Near the lake? <em>Ask about the dock.</em></h1>"+ul([
  "On Duke Energy lakes, Duke controls the lakebed and permits docks and shoreline work",
  "Ask whether an existing dock was permitted and can be transferred to you",
  "Unpermitted changes may become the new owner's problem to fix"]),h1=76),
S_(9,"THE MARKET",cs.TEAL_STRONG+STATS_CSS+"<div class='lab'>REALTOR.COM · ZIP 28278 · SEPT. 2026</div><h1>What homes <em>list for.</em></h1>"+
  row("MEDIAN LIST<br>PRICE","$561,250")+row("PRICE PER<br>SQ. FT.","$214")+row("ACTIVE<br>LISTINGS","212")+row("MEDIAN DAYS<br>ON MARKET","65")+
  "<p class='src'>Source: Realtor.com Economic Research, ZIP 28278 (Charlotte NC) monthly listing data, September 2026; viewed Oct. 24, 2026</p>",h1=72),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 48%,rgba(9,46,56,.88) 100%)!important}</style><h1>Let's tour it <em>together.</em></h1><p class='b'>We'll compare a newer home inland with one near the lake, and I'll check any dock permits before you make an offer.</p>",contact=True,h1=76),
]
# Native 9:16 layout overrides (key text clear of top 250px, bottom 420px, right 140px).
V916=("<style>html,body,.s{width:1080px!important;height:1920px!important}.ph{height:1920px!important;width:1080px!important}"
      ".tag{top:270px!important}.cr{top:356px!important;left:56px!important}.c{left:56px!important;right:160px!important;bottom:500px!important}"
      ".ft{left:56px!important;right:160px!important;bottom:436px!important}"
      ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 18%,rgba(10,52,63,0) 38%,rgba(10,52,63,.5) 52%,rgba(9,46,56,.86) 72%,rgba(8,40,50,.9) 100%)!important}"
      "</style>")
V916_STATS=("<style>.s .c{top:380px!important;bottom:auto!important}.s h1{font-size:96px!important}.s .lab{font-size:30px}"
  ".s .row{padding:20px 30px;margin-top:16px}.s .row .z{font-size:30px;width:380px}.s .row .v{font-size:76px}"
  ".s .src{font-size:30px;margin-top:22px}"
  ".ph:after{background:linear-gradient(rgba(8,40,50,.4) 0,rgba(8,40,50,.55) 15%,rgba(10,52,63,.8) 30%,rgba(9,46,56,.9) 60%,rgba(8,40,50,.93) 100%)!important}</style>")
V916_10=("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 14%,rgba(10,52,63,0) 28%,rgba(10,52,63,.55) 42%,rgba(9,46,56,.88) 62%,rgba(8,40,50,.9) 100%)!important}</style>")
def to916(h,i):
    extra=V916+(V916_STATS if i==9 else "")+(V916_10 if i==10 else "")
    return h.replace("url('img/","url('9x16/img/").replace("</head>",extra+"</head>")

# Native 1:1 (1080x1080) layout overrides for the square Facebook carousel.
V11=("<style>html,body,.s{width:1080px!important;height:1080px!important}.ph{height:1080px!important;width:1080px!important}"
     ".c{bottom:92px!important}.ft{bottom:36px!important}.s h1{font-size:62px!important}.s li{font-size:30px;line-height:1.22;margin-bottom:8px}"
     ".s ul{margin-top:14px}.band{font-size:46px!important;padding:10px 22px!important;margin-bottom:12px!important}.s p.b{font-size:31px;line-height:1.28;margin-top:12px}"
     ".cbox{padding:16px 26px 16px 20px!important;margin-top:12px!important;font-size:30px;line-height:1.24}"
     ".ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 14%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 50%,rgba(9,46,56,.88) 100%)!important}</style>")
V11_STATS=("<style>.s .c{top:auto!important;bottom:92px!important}.s h1{font-size:64px!important}.s .lab{font-size:30px;margin-bottom:6px}"
  ".s .grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}.s .row{margin-top:0!important;padding:16px 22px!important;flex-direction:column;align-items:flex-start}"
  ".s .row .z{width:auto!important;font-size:30px!important}.s .row .v{font-size:64px!important}.s .row .y{display:none}.s .src{font-size:30px;margin-top:16px}"
  ".ph:after{background:linear-gradient(rgba(8,40,50,.25) 0,rgba(8,40,50,.15) 14%,rgba(10,52,63,.6) 30%,rgba(9,46,56,.9) 50%,rgba(8,40,50,.93) 100%)!important}</style>")
V11_10=("<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 10%,rgba(10,52,63,.35) 22%,rgba(10,52,63,.7) 36%,rgba(9,46,56,.9) 100%)!important}.s h1{font-size:58px!important}</style>")
def to11(h,i):
    if i==9:
        h=h.replace("<div class='row'>","<div class='grid'><div class='row'>",1).replace("<p class='src'>","</div><p class='src'>",1)
    extra=V11+(V11_STATS if i==9 else "")+(V11_10 if i==10 else "")
    return h.replace("url('img/","url('1x1/img/").replace("</head>",extra+"</head>")
def shot(hp,op,w,hgt):
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
        f"--window-size={w},{hgt}",f"--screenshot={op}","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
pngs=cs.build(SL,D,f"{N}-DRAFT.pdf",B)
os.makedirs(f"{D}/slides-9x16",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    hp=os.path.join(B,f"slide-{i:02d}-9x16.html"); open(hp,"w").write(to916(vid,i)); shot(hp,f"{D}/slides-9x16/slide-{i:02d}.png",1080,1920)
# Short/Reel frames: same native 9:16 layout + "NEIGHBORHOOD SPOTLIGHT / Steele Creek · Charlotte NC" header inside the safe zone
# (header at 270px, tag pushed to 410px, credit to 496px; key text still ends 500px above the bottom). Kept in build/video-9x16/.
HDR=("<div class='vh' style='position:fixed;top:262px;left:56px;right:160px;z-index:50;font-family:Montserrat,Inter,sans-serif'>"
     "<div style='display:inline-block;background:#F2B705;color:#0F4C5C;font-weight:800;font-size:34px;letter-spacing:3px;padding:8px 18px;border-radius:8px'>NEIGHBORHOOD SPOTLIGHT</div>"
     "<div style='margin-top:10px;color:#fff;font-weight:800;font-size:46px;text-shadow:0 2px 10px rgba(0,0,0,.85)'>Steele Creek · Charlotte NC</div></div>")
VH=("<style>.tag{top:410px!important}.cr{top:496px!important}.s .c{max-height:none}</style>")
VH9=("<style>.s .c{top:560px!important}.s h1{font-size:84px!important}.s .row{padding:16px 30px!important;margin-top:12px!important}.s .row .v{font-size:70px!important}</style>")
os.makedirs(B+"/video-9x16",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    h=to916(vid,i).replace("</head>",VH+(VH9 if i==9 else "")+"</head>").replace("</body>",HDR+"</body>")
    hp=os.path.join(B,f"slide-{i:02d}-9x16-video.html"); open(hp,"w").write(h); shot(hp,f"{B}/video-9x16/slide-{i:02d}.png",1080,1920)
os.makedirs(f"{D}/slides-1x1",exist_ok=True)
for i,(soc,vid,_,_) in enumerate(SL,1):
    hp=os.path.join(B,f"slide-{i:02d}-1x1.html"); open(hp,"w").write(to11(soc,i)); shot(hp,f"{D}/slides-1x1/slide-{i:02d}.png",1080,1080)
for i in range(1,11):
    assert Image.open(f"{D}/slides-1x1/slide-{i:02d}.png").size==(1080,1080)
    for p,s in ((f"{D}/slide-{i:02d}.png",(1080,1350)),(f"{D}/slide-{i:02d}-video.png",(1080,1350)),(f"{D}/slides-9x16/slide-{i:02d}.png",(1080,1920))):
        assert Image.open(p).size==s,(p,Image.open(p).size)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
with zipfile.ZipFile(D+"/slides-9x16.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slides-9x16/slide-{i:02d}.png",f"slide-{i:02d}-9x16.png")
with zipfile.ZipFile(D+"/slides-1x1.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slides-1x1/slide-{i:02d}.png",f"slide-{i:02d}-1x1.png")
print("ok")
