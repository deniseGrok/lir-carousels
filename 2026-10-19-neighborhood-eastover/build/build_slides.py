# Eastover spotlight, theme="fullbleed_teal". Facts fetched Oct 19 2026 (see ../2026-10-19-neighborhood-eastover.md sources).
import sys, zipfile; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, TEAL_STRONG
N="2026-10-19-neighborhood-eastover"; D="/workspace/lir-ai-team/content-research/carousels/"+N; F="NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
cr=lambda s: f"<div style='position:fixed;top:40px;right:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"
cr2=lambda s: f"<div style='position:fixed;top:104px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"  # credit under a long tag
S=[
slide(1,"EASTOVER","<h1>Curving drives, <em>grand homes.</em></h1>"+ul(["A residential neighborhood southeast of Uptown, ZIP 28207","Bordered by Providence Road, Briar Creek and Randolph Road","Home to Mint Museum Randolph"]),band="CHARLOTTE NC. <em>EASTOVER.</em>",h1=78),
slide(2,"HISTORY","<h1>Planned <em>in 1927.</em></h1>"+ul(["Begun by the E. C. Griffith Company in 1927","Laid out on more than 300 acres of former dairy farmland","Planned to compete with the already established Myers Park"])),
slide(3,"STREET PLAN","<h1>Built for <em>the automobile.</em></h1>"+ul(["Curving drives by planner Earle Sumner Draper","Charlotte's first automobile suburb; earlier suburbs had streetcar service","Cherokee Road is its backbone, a gentle curve off Providence Road"]),h1=76),
slide(4,"ARCHITECTURE","<h1>Classic <em>Georgian Revival.</em></h1>"+ul(["Large Georgian Revival homes on spacious lots defined some of Eastover's earliest sections","The style was built here in both brick and weatherboard","Georgian-style homes still line Cherokee Road"]),h1=76),
slide(5,"HAMILTON JONES HOUSE","<h1>Tudor Revival <em>in stone.</em></h1>"+ul(["201 Cherokee Road; construction began in 1929","One of Charlotte's finest examples of the Tudor Revival style","Architect Martin E. Boyer, known for Colonial, Tudor and Georgian designs"]),h1=76),
slide(6,"MINT MUSEUM RANDOLPH",cr2("Mint Museum, CC BY-SA 4.0")+"<h1>North Carolina's <em>first art museum.</em></h1>"+ul(["First branch of the U.S. Mint; it opened uptown in 1836","Rebuilt here in 1934-36 on land given by E. C. Griffith","Free admission Wednesday nights, 5 to 9 PM"]),h1=64),
slide(7,"OUTDOORS","<h1>A creekside <em>walk.</em></h1>"+ul(["Briar Creek Greenway: about one paved mile from Randolph Road to Meadowbrook Road","It starts at Mint Museum Randolph and follows Briar Creek","A pedestrian bridge carries the trail across the creek"]),h1=74),
slide(8,"FIRE STATION NO. 6","<h1>A 1929 firehouse, <em>still on duty.</em></h1>"+ul(["249 S. Laurel Avenue, designed by architect C. C. Hook","One of three pre-World War II stations still working as firehouses in Charlotte","Brick and stone, arched engine bays and a green tile roof"]),h1=74),
slide(9,"THE MARKET",TEAL_STRONG+"<style>.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style><h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF OCTOBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$2,422,500</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$1,995,000</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$603</span><span class='y'>20 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>55</span><span class='y'>median</span></div>"
 +src("Realtor.com Economic Research, Eastover")),
slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>Start with a drive along Cherokee Road's curve, then let's compare historic homes and newer builds side by side.</p>",contact=True,h1=76),
]
build(S,D,N+"-DRAFT.pdf",D+"/build")
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
