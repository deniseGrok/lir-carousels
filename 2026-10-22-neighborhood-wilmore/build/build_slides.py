# Wilmore neighborhood spotlight Oct 22 2026. theme="fullbleed_teal" (teal #0F4C5C / gold #F2B705), 10 slides.
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
N="2026-10-22-neighborhood-wilmore"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
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
S_(1,"WILMORE","<h1>Bungalows and curves, <em>near Uptown.</em></h1>"+ul([
  "Dilworth's sister neighborhood, just across the rail line, southwest of Uptown",
  "One of Charlotte's first streetcar suburbs",
  "A Charlotte Local Historic District since 2010"]),band="CHARLOTTE NC. <em>WILMORE.</em>",h1=78),
S_(2,"HISTORY","<h1>Named for <em>two farms.</em></h1>"+ul([
  "Developer F. C. Abbott combined the names of two former owners, Wilson and Moore",
  "Abbott's company published the plat of Wilmore in 1914",
  "The first bungalows went up in the late 1910s, and the neighborhood took shape in the 1920s"])),
S_(3,"GOLD RUSH",cr("James St. John, CC BY 2.0")+"<h1>Built on <em>gold-rush ground.</em></h1>"+ul([
  "Wilmore grew on farmland and the land around the Rudisill Gold Mine",
  "The Rudisill was one of the most productive mines of the country's first gold rush",
  "Mint Street was built to link the mines with the Mint on West Trade Street"]),h1=78),
S_(4,"STREET PLAN","<h1>A grid, <em>then curves.</em></h1>"+ul([
  "The 1914 plan set straight streets near the railroad and curving streets past Mint Street",
  "West Park, West Kingston, West Boulevard and West Worthington echo Dilworth's street names",
  "Spruce Street, Dunkirk Drive and Merriman Avenue curve over a hillcrest toward Irwin Creek"]),h1=80),
S_(5,"ARCHITECTURE","<h1>Bungalows with <em>full-width porches.</em></h1>"+ul([
  "Most buildings are Bungalow style, with low overhanging roofs, full-width front porches and Craftsman details",
  "A wide range of styles and materials overall",
  "Mainly single-family homes, plus duplexes, apartment buildings and commercial buildings"]),h1=76),
S_(6,"HISTORIC DISTRICT","<h1>Plan exterior <em>changes early.</em></h1>"+ul([
  "Wilmore is one of Charlotte's eight Local Historic Districts, designated in 2010",
  "Exterior changes, including windows, doors, fencing and tree removal, need Historic District Commission approval",
  "That approval, a Certificate of Appropriateness, comes before any work begins"]),h1=78),
S_(7,"WILMORE CENTENNIAL PARK",cr("City Dweller 2, CC BY-SA 4.0")+"<h1>A park on <em>South Tryon.</em></h1>"+ul([
  "Wilmore Centennial Park at South End sits at S. Tryon Street and Kingston Avenue",
  "A large open lawn faces Uptown, with seating, art display areas and a natural play area",
  "Built by Mecklenburg County Park and Recreation with Beacon Partners"])),
S_(8,"LYNX BLUE LINE",cr("City Dweller 2, CC BY-SA 4.0")+"<h1>Light rail <em>next door.</em></h1>"+ul([
  "Wilmore's eastern edge follows Camden Road and the rail line",
  "Blue Line stations: Bland St. (1511 Camden Rd.) and East/West Blvd. (1821 Camden St.)",
  "The line runs north through Uptown to UNC Charlotte and south to I-485/South Blvd."])),
S_(9,"THE MARKET",cs.TEAL_STRONG+STATS_CSS+"<div class='lab'>REALTOR.COM · THROUGH SEPT. 2026</div><h1>What homes <em>list for.</em></h1>"+
  row("MEDIAN LIST<br>PRICE","$644,900")+row("LIST PRICE<br>PER SQ FT","$444")+row("HOMES<br>FOR SALE","18")+row("MEDIAN DAYS<br>ON MARKET","112")+
  "<p class='src'>Source: Realtor.com Economic Research, Wilmore, Charlotte NC; data through Sept. 2026, viewed Oct. 22, 2026</p>",h1=76),
S_(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 30%,rgba(10,52,63,.55) 48%,rgba(9,46,56,.88) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>Ride the Blue Line to East/West Blvd., then let's compare bungalows on the straight streets with homes on the curving ones. Planning exterior changes? We'll check the historic district rules first.</p>",contact=True,h1=76),
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
