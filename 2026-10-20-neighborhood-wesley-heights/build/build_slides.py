# Wesley Heights spotlight, theme="fullbleed_teal". Facts fetched Oct 20 2026 ~4:48-5:00 AM ET (see ../2026-10-20-neighborhood-wesley-heights.md sources).
import sys, zipfile; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, TEAL_STRONG
N="2026-10-20-neighborhood-wesley-heights"; D="/workspace/lir-ai-team/content-research/carousels/"+N; F="NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
cr2=lambda s: f"<div style='position:fixed;top:104px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"  # credit under the tag
S=[
slide(1,"WESLEY HEIGHTS","<h1>Bungalows, <em>a mile from Uptown.</em></h1>"+ul(["A historic neighborhood about one mile northwest of Trade and Tryon","Listed on the National Register of Historic Places in 1995","Its own stop on the CityLYNX Gold Line streetcar"]),band="CHARLOTTE NC. <em>WESLEY HEIGHTS.</em>",h1=76),
slide(2,"HISTORY","<h1>A livery family's <em>model farm.</em></h1>"+ul(["J. W. Wadsworth ran Charlotte's largest livery stable and helped run its first horse-drawn streetcars","His J. W. Wadsworth Model Farm on this land was known for its Holstein cattle","In 1895 his children incorporated the business as Wadsworth Sons Company"]),h1=72),
slide(3,"STREETCAR SUBURB","<h1>Built for <em>the trolley.</em></h1>"+ul(["The Wadsworth family subdivided the farm around 1910, after the West Trade Street trolley line was extended nearby","First laid out in 1911; the Charlotte Investment Company bought the land in 1920","Lots went on sale in December 1921, and houses went up starting in 1922"]),h1=78),
slide(4,"ARCHITECTURE","<h1>Craftsman, Tudor <em>and Colonial.</em></h1>"+ul(["Bungalow and Craftsman homes lead, with Tudor Revival and Colonial Revival designs","At its 1995 listing, 335 of the district's 372 buildings were counted as contributing","Duplexes and small apartment buildings mix in with single-family homes"]),h1=74),
slide(5,"STREETSCAPE","<h1>Walls, curbs <em>and canopy.</em></h1>"+ul(["Brick and cinderblock retaining walls, many of them original, line the streets","Granite curbstones edge the roadways","Mature trees shade the sidewalks over gently rolling Piedmont hills"]),h1=78),
slide(6,"LOTS AND LAYOUT","<h1>Long lots, <em>deep yards.</em></h1>"+ul(["Most lots are 55 feet wide and 150 or 187 feet deep","Homes sit back from the sidewalk; most lots have driveways, and many have or once had garages out back","Alleys run behind the lots in much of the older section"]),h1=78),
slide(7,"GOLD LINE",cr2("Mark Clifton, CC BY-SA 2.0")+"<h1>Back on <em>the streetcar.</em></h1>"+ul(["The Wesley Heights stop on West Trade Street opened August 30, 2021","The CityLYNX Gold Line runs 4 miles with 17 stops","From French Street through Center City to Sunnyside Avenue in Elizabeth"]),h1=78),
slide(8,"OUTDOORS","<h1>A greenway <em>close by.</em></h1>"+ul(["Part of the county's Irwin Creek, Stewart Creek and Wesley Heights greenway system","Its main section runs 2.7 miles, from State Street to Cedar Street","With a connection to Freedom Drive"]),h1=78),
slide(9,"THE MARKET",TEAL_STRONG+"<style>.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style><h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF OCTOBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$499,000</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$552,500</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$359</span><span class='y'>23 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>99</span><span class='y'>median</span></div>"
 +src("Realtor.com Economic Research, Wesley Heights")),
slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>Start with a streetcar ride down West Trade, then let's tour 1920s bungalows and newer homes side by side.</p>",contact=True,h1=76),
]
build(S,D,N+"-DRAFT.pdf",D+"/build")
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
