# 2-slide DEMO (Denise, Oct 17 5:17 PM): same fullbleed_teal style as the Myers Park build (0923caa), but only 2 slides.
import sys, os, subprocess; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
import carousel_style as cs
cs.N = 2   # page counter reads "1 / 2", "2 / 2" (build() is not used because it enforces 10 slides + contact block)
from carousel_style import slide as _slide, ul, TEAL_STRONG
D = "/workspace/lir-ai-team/content-research/carousels/demo-2026-10-17-elizabeth"; F = "NEIGHBORHOOD SPOTLIGHT"
def slide(n,t,inner,**k): k.setdefault("theme","fullbleed_teal"); k.setdefault("h1",80); k.setdefault("footer",F); return _slide(n,t,f"{n:02d}.jpg",inner,**k)
S = [
 slide(1,"ELIZABETH","<h1>A historic <em>district.</em></h1>"+ul(["The Elizabeth Historic District joined the National Register of Historic Places on January 3, 1989"]),
       band="CHARLOTTE NC. <em>ELIZABETH.</em>"),
 slide(2,"THE MARKET",TEAL_STRONG+"<style>.ph:after{background:linear-gradient(rgba(8,40,50,.16) 0,rgba(8,40,50,0) 12%,rgba(10,52,63,0) 30%,rgba(10,52,63,.62) 45%,rgba(9,46,56,.88) 58%,rgba(8,40,50,.93) 100%)!important}.row .z{width:300px;font-size:32px}.row{padding:12px 28px}</style><h1>What homes <em>cost here.</em></h1><div class='lab'>REALTOR.COM · AS OF OCTOBER 2026</div>"
 +"<div class='row'><span class='z'>MEDIAN LIST</span><span class='v'>$701,000</span></div>"
 +"<div class='row'><span class='z'>MEDIAN SOLD</span><span class='v'>$870,000</span></div>"
 +"<div class='row'><span class='z'>PER SQ FT</span><span class='v'>$346</span><span class='y'>40 active listings</span></div>"
 +"<div class='row'><span class='z'>DAYS ON MKT</span><span class='v'>71</span><span class='y'>median</span></div>"
 +"<p class='src'>Source: Realtor.com Economic Research, Elizabeth</p>"),
]
for i,(soc,vid,_,_) in enumerate(S,1):
    hp=f"{D}/build/slide-{i:02d}.html"; open(hp,"w").write(soc); op=f"{D}/slide-{i:02d}.png"
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
        "--window-size=1080,1350",f"--screenshot={op}","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
