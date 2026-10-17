# DRAFT — Myers Park neighborhood spotlight, theme="fullbleed_teal" (Denise Oct 16 2026 neighborhood default). Facts fetched Oct 17 2026 ~4:44-4:58 AM ET.
import sys, zipfile; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, TEAL_STRONG
N="2026-10-17-neighborhood-myers-park"; D="/workspace/lir-ai-team/content-research/carousels/"+N; F="NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STRONG="<style>.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style>"
S=[
slide(1,"MYERS PARK","<h1>Oak canopy and historic homes. <em>Myers Park.</em></h1>"+ul(["Just south of Uptown Charlotte","Planned in the early 1900s on former cotton farmland","Laid out by planners John Nolen and Earle Sumner Draper"]),band="CHARLOTTE NC. <em>MYERS PARK.</em>",h1=76),
slide(2,"HOME STYLES","<h1>Homes with <em>a history.</em></h1>"+ul(["1920s Colonial Revival and Tudor Revival homes","Bungalow and Craftsman styles too","A historic district on the National Register of Historic Places"])),
slide(3,"TREE CANOPY","<h1>Streets under <em>the oaks.</em></h1>"+ul(["A canopy of oaks more than 100 years old","Mansions and gardens along Queens Road West","The 2.85-mile Booty Loop for walking, running and cycling"])),
slide(4,"THE DUKE MANSION","<h1>A historic <em>estate.</em></h1>"+ul(["The Duke Mansion: listed on the National Register","20 individually decorated guest rooms","4.5 acres of gardens, free to stroll during daylight hours"])),
slide(5,"WING HAVEN","<h1>Wing Haven's <em>three gardens.</em></h1>"+ul(["Wing Haven Garden &amp; Bird Sanctuary","Elizabeth Lawrence House &amp; Garden","SEED Wildlife &amp; Children's Garden","On Ridgewood Avenue, open Wednesday to Saturday, 10 a.m. to 5 p.m."])),
slide(6,"OUTDOORS","<h1>Greenway at <em>the edge.</em></h1>"+ul(["Little Sugar Creek Greenway runs along the western edge","Right next to Freedom Park","Tree-lined, walkable streets throughout"])),
slide(7,"DINING","<h1>Porches, plates <em>and pours.</em></h1>"+ul(["Selwyn Avenue Pub: a Myers Park porch since 1990","Napa on Providence: dinner on Perrin Place","Dot Dot Dot: a speakeasy at nearby Park Road Shopping Center"])),
slide(8,"CLOSE TO IT ALL","<h1>Close to <em>it all.</em></h1>"+ul(["Uptown Charlotte sits just to the north","Main routes: Providence Road, Kings Drive and Queens Road","Theatre Charlotte on Queens Road","Mint Museum Randolph nearby"])),
slide(9,"THE MARKET",TEAL_STRONG+STRONG+"<h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF OCTOBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$2,111,250</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$1,276,500</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$530</span><span class='y'>90 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>50</span><span class='y'>median</span></div>"
 +src("Realtor.com Economic Research, Myers Park")),
slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Let's tour it <em>together.</em></h1><p class='b'>Start with a drive down Queens Road West, then let's compare homes street by street.</p>",contact=True,h1=76),
]
build(S,D,N+"-DRAFT.pdf",D+"/build")
short(D,N+"-short.mp4",pad="0F4C5C")
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("DONE")
