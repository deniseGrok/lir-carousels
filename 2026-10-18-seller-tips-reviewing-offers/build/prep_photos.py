# Oct 18 2026 seller tips (reviewing offers). Unsplash originals (>=3000px wide, fetched with fit=max so never upscaled),
# cover-cropped to 4:5 and resized DOWN only to 1080x1350, light premium grade + sharpen. Originals cached in build/src/.
import os, urllib.request
from PIL import Image, ImageEnhance, ImageFilter
B=os.path.dirname(os.path.abspath(__file__)); S=B+"/src/"; O=B+"/img/"
P={"01":("1598228723793-52759bba239c",.5,.5),"03":("1615874694520-474822394e73",.5,.5),"04":("1556912172-45b7abe8b7e1",.45,.5),
   "05":("1613545325268-9265e1609167",0.0,.5),"06":("1564540583246-934409427776",.5,.5),"07":("1560184897-ae75f418493e",.5,.5),
   "08":("1600585152915-d208bec867a1",.5,.5),"09":("pexels-280222",.5,.5),"10":("pexels-5524166",.5,.5)}
cr=open(O+"CREDITS.txt","w")
cr.write("Photos: Unsplash License / Pexels License (no attribution required). Unsplash source files 3000-3600px wide (fetched with fit=max, never upscaled), cropped/resized down only, graded Oct 18 2026.\n02 | no photo (stats)\n")
for k,(pid,x,y) in sorted(P.items()):
    f=S+pid+".jpg"
    px=pid.startswith("pexels-")
    if not os.path.exists(f):
        n=pid.split("-")[1]
        urllib.request.urlretrieve(f"https://images.pexels.com/photos/{n}/pexels-photo-{n}.jpeg" if px else f"https://images.unsplash.com/photo-{pid}?q=92&w=3600&fit=max", f)
    im=Image.open(f).convert("RGB"); w,h=im.size; t=1080/1350
    if w/h>t: nw=int(h*t); l=int((w-nw)*x); im=im.crop((l,0,l+nw,h))
    else: nh=int(w/t); tp=int((h-nh)*y); im=im.crop((0,tp,w,tp+nh))
    assert im.width>=1080, "never upscale"
    im=im.resize((1080,1350),Image.LANCZOS)
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.02))); b=b.point(lambda v:int(v*.985)); im=Image.merge("RGB",(r,g,b))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=ImageEnhance.Color(im).enhance(.97); im=ImageEnhance.Brightness(im).enhance(1.02)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=70,threshold=2))
    im.save(O+k+".jpg",quality=93)
    if px: n=pid.split("-")[1]; cr.write(f"{k} | Pexels License (no attribution required) | https://www.pexels.com/photo/{n}/ (original {w}x{h})\n")
    else: cr.write(f"{k} | https://unsplash.com/photos/{pid} (images.unsplash.com/photo-{pid}) | source file {w}x{h}\n")
cr.close()
