# Elizabeth spotlight photo-fix rebuild (Oct 21 2026 ~6:50 AM ET), theme="fullbleed_teal". Re-renders slides 1, 2, 4, 10 (new photos) and 5, 6 (credit moved
# below the tag so it no longer overlaps it). Slides 3, 7, 8, 9 are unchanged from the approved 5 AM build (that build/ folder was not kept).
# Text is identical to the approved slides. Then rebuilds the PDF and slides.zip from all 10 PNGs.
import sys, os, zipfile, subprocess; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide as _slide, ul
from PIL import Image
N="2026-10-21-neighborhood-elizabeth"; D=sys.argv[1] if len(sys.argv)>1 else "/workspace/lir-ai-team/content-research/carousels/"+N
B=os.path.dirname(os.path.abspath(__file__)); F="NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
cr2=lambda s: f"<div style='position:fixed;top:124px;left:40px;font-size:30px;font-weight:600;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.8)'>Photo: {s}</div>"
S={
1:slide(1,"ELIZABETH","<h1>Oaks and porches, <em>near Uptown.</em></h1>"+ul(["A historic neighborhood whose western edge sits about one mile east of Uptown","Charlotte's second streetcar suburb, laid out between 1891 and 1915","Listed on the National Register of Historic Places in 1989"]),band="CHARLOTTE NC. <em>ELIZABETH.</em>",h1=76),
2:slide(2,"HISTORY","<h1>Named for <em>a college.</em></h1>"+ul(["Elizabeth College, a Lutheran college for women, began building here in 1897","Its 20-acre site with a grove sat at the end of a new street opened by the Highland Park Company","The college moved to Salem, Virginia, in 1915"]),h1=78),
4:slide(4,"ARCHITECTURE","<h1>Bungalows, Tudor <em>and Colonial.</em></h1>"+ul(["More than half the houses are bungalows, with Craftsman, Colonial Revival and Tudor Revival touches","Spanish Mission and Italian Renaissance Revival designs appear too","1920s and 1930s duplexes and small apartment buildings sit on nearly every street"]),h1=74),
5:slide(5,"INDEPENDENCE PARK",cr2("City Dweller 2, CC BY-SA 4.0")+"<h1>Charlotte's <em>first public park.</em></h1>"+ul(["Established in 1905 on the former site of the city waterworks","Designed by John Nolen, one of his earliest commissions, years before his 1911 plan for Myers Park","Hawthorne Lane splits the park into two sections"]),h1=78),
6:slide(6,"PARK TODAY",cr2("City Dweller 2, CC BY-SA 4.0")+"<h1>Renewed <em>in 2023.</em></h1>"+ul(["The 34-acre park reopened in June 2023 after a nearly $6 million county renovation","A 12-foot-wide greenway ties into Hawthorne Lane and the Little Sugar Creek Greenway","A perennial garden, nature playground, trails, picnic pavilion and athletic fields"]),h1=80),
10:slide(10,"MY RECOMMENDATION","<style>.ph:after{background:linear-gradient(rgba(8,40,50,.22) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 34%,rgba(10,52,63,.55) 52%,rgba(9,46,56,.86) 100%)!important}</style><h1>Let's walk it <em>together.</em></h1><p class='b'>Ride the streetcar to Hawthorne Lane, then let's tour bungalows, Tudors and duplexes on the tree-lined side streets.</p>",contact=True,h1=76),
}
for i,(soc,vid,_,_) in S.items():
    for suffix,h in (("",soc),("-video",vid)):
        hp=os.path.join(B,f"slide-{i:02d}{suffix}.html"); open(hp,"w").write(h)
        subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1","--window-size=1080,1350",
            f"--screenshot={D}/slide-{i:02d}{suffix}.png","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
ims=[Image.open(f"{D}/slide-{i:02d}.png").convert("RGB") for i in range(1,11)]
ims[0].save(f"{D}/{N}-DRAFT.pdf",save_all=True,append_images=ims[1:],resolution=150)
with zipfile.ZipFile(D+"/slides.zip","w") as z:
    for i in range(1,11): z.write(f"{D}/slide-{i:02d}.png",f"slide-{i:02d}.png")
print("ok")
