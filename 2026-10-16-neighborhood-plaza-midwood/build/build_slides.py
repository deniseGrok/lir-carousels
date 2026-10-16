# Plaza Midwood spotlight, theme="fullbleed_teal" (seller-tips layout in teal/gold; Denise Oct 16 2026). Facts fetched Oct 16 2026; copy unchanged.
import sys, shutil, glob, zipfile, os; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul, build, short, TEAL_STRONG
N="2026-10-16-neighborhood-plaza-midwood"; D="/workspace/lir-ai-team/content-research/carousels/"+N; F="NEIGHBORHOOD SPOTLIGHT"
for f in glob.glob(D+"/build/img-teal/*"): shutil.copy(f, D+"/build/img/"+os.path.basename(f))
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
src=lambda s: f"<p class='src'>Source: {s}</p>"
STRONG="<style>.ph:after{background:linear-gradient(rgba(0,0,0,.35) 0,rgba(0,0,0,.2) 18%,rgba(0,0,0,.55) 36%,rgba(0,0,0,.88) 60%,rgba(0,0,0,.94) 100%)!important}.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style>"
S=[
slide(1,"PLAZA MIDWOOD","<h1>Murals, music and a main street. <em>Plaza Midwood.</em></h1>"+ul(["Just outside Uptown, east of Hawthorne Lane","Founded in 1910 as a streetcar suburb","Murals on nearly every corner"]),band="CHARLOTTE NC. <em>PLAZA MIDWOOD.</em>",h1=76),
slide(2,"HISTORIC DISTRICT","<h1>A historic <em>district.</em></h1>"+ul(["Streets laid out by the Oakland Land Company","Local Historic District since 1992","Covers The Plaza, Thomas Ave and parts of Pecan and Clement","Overseen by the Historic District Commission"])),
slide(3,"LIVE MUSIC","<h1>Live music <em>after dark.</em></h1>"+ul(["Snug Harbor and Petra's: jazz, indie, rock and more","Local talent and touring artists","Open mic nights and drag shows at Legion Brewing"])),
slide(4,"DINING","<h1>Eat your way down <em>Central.</em></h1>"+ul(["Villani's Bakery: Italian pastries","Milkbread's walk-up window: donuts to crispy chicken","Calle Sol: ceviche and empanadas","Midwood Smokehouse · Supperland"])),
slide(5,"BREWERIES","<h1>A neighborhood <em>beer crawl.</em></h1>"+ul(["Pilot Brewing","Resident Brewing Company","Burial Beer Co.","Southern Strain Brewing Company"])),
slide(6,"OUTDOORS","<h1>Walk it, <em>ride it.</em></h1>"+ul(["Walkable, tree-lined streets","Joy Rides: electric-bike rentals","Veterans Park: green space for a stroll or a picnic"])),
slide(7,"SHOPPING","<h1>Shop <em>local.</em></h1>"+ul(["House of Africa: art, clothing and home decor","Betty by Moxie Mercantile boutique","Pinhouse: duckpin bowling and self-pour taps","Boris &amp; Natasha · Lunchbox Records"])),
slide(8,"GETTING AROUND","<h1>Getting <em>around.</em></h1>"+ul(["Main roads: Central Ave, Hawthorne Lane and The Plaza","Gold Line streetcar ends at Sunnyside Ave on Hawthorne Lane","17 stops, 4 miles, through Center City to the Historic West End"])),
slide(9,"THE MARKET",TEAL_STRONG+STRONG.replace(STRONG.split("}")[0]+"}","<style>")+"<h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF SEPTEMBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$820,000</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$912,500</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$434</span><span class='y'>45 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>35</span><span class='y'>median</span></div>"
 +src("Realtor.com Economic Research, Plaza Midwood")),
slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Start on <em>Central Ave.</em></h1><p class='b'>Walk Central Avenue and the historic streets off The Plaza, then let's compare listings block by block.</p>",contact=True,h1=76),
]
build(S,D,N+"-DRAFT.pdf",D+"/build")
short(D,N+"-short.mp4",pad="0F4C5C")
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
