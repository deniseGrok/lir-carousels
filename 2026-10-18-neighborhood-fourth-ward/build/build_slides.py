# Fourth Ward spotlight, theme="fullbleed_teal". Facts fetched Oct 18 2026 (see ../2026-10-18-neighborhood-fourth-ward.md sources).
import sys, zipfile; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, TEAL_STRONG
N="2026-10-18-neighborhood-fourth-ward"; D="/workspace/lir-ai-team/content-research/carousels/"+N; F="NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
cr=lambda s: f"<div style='position:fixed;top:40px;right:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"
cr2=lambda s: f"<div style='position:fixed;top:104px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"  # credit under a long tag
S=[
slide(1,"FOURTH WARD","<h1>Victorian homes in <em>Uptown.</em></h1>"+ul(["The historic northwest quarter of Uptown Charlotte","About 30 city blocks, anchored by Fourth Ward Park","Bordered by Tryon St., Trade St. and historic Elmwood Cemetery"]),band="CHARLOTTE NC. <em>FOURTH WARD.</em>",h1=78),
slide(2,"HISTORY","<h1>A neighborhood <em>brought back.</em></h1>"+ul(["One of four wards Charlotte created in the mid-1830s","A Junior League restoration program in 1976 sparked its revival","It began with the Berryhill House (1884, Victorian Italianate)"]),h1=76),
slide(3,"HOME STYLES","<h1>Queen Anne to <em>Craftsman.</em></h1>"+ul(["Queen Anne, Victorian Italianate and Folk Victorian homes","Craftsman bungalows and Colonial Revival too","Several homes were moved here and restored in the 1970s","Some keep their original heart pine floors and fireplaces"])),
slide(4,"QUEEN ANNE STYLE","<h1>Turrets, slate <em>and porches.</em></h1>"+ul(["Overcarsh House (1879): round corner turret, sunburst gables","Liddell-McNinch House: fish-scale and diamond slate roof","Sheppard House (1898): slate roof and stained glass"]),h1=76),
slide(5,"FOURTH WARD PARK",cr("City Dweller 2, CC BY-SA 4.0")+"<h1>Fountains under <em>the trees.</em></h1>"+ul(["About three acres at 301 N. Poplar Street","Fountains, walking paths and a playground","Ceramic birdhouses by artist Joan Bankemper"]),h1=76),
slide(6,"SETTLERS' CEMETERY",cr2("AlexiusHoratius, CC BY-SA 3.0")+"<h1>Charlotte's <em>earliest chapter.</em></h1>"+ul(["Charlotte's first city burial ground, in use by 1776","Revolutionary War leaders Thomas Polk and George Graham rest here","A quiet urban park with walkways, benches and a fountain"]),h1=76),
slide(7,"DINING","<h1>Dinner with <em>a history.</em></h1>"+ul(["Alexander Michael's: a tavern since 1983, in an 1897 store","McNinch House Restaurant: multi-course dinners in a Victorian home since 1989","Both serve Tuesday through Saturday"])),
slide(8,"LANDMARKS",cr("AlexiusHoratius, CC BY-SA 3.0")+"<h1>Steeples <em>and stone.</em></h1>"+ul(["First Presbyterian Church: Gothic Revival, on West Trade Street","St. Peter's Episcopal Church: 1890s brick and brownstone","McColl Center for Art + Innovation (1926, Gothic Revival)"])),
slide(9,"THE MARKET",TEAL_STRONG+"<style>.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style><h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF OCTOBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$345,000</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$371,000</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$408</span><span class='y'>100 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>76</span><span class='y'>median</span></div>"
 +src("Realtor.com Economic Research, Fourth Ward")),
slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>Start on West Ninth Street's Victorian blocks, then let's compare historic homes and condos side by side.</p>",contact=True,h1=76),
]
build(S,D,N+"-DRAFT.pdf",D+"/build")
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
