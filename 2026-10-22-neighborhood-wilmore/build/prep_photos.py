# Wilmore spotlight (Oct 22 2026) photo prep, theme fullbleed_teal. Full-res originals in src/, resized DOWN only.
# Three crops per photo: img/NN.jpg 1080x1350 (4:5 IG/LinkedIn carousel), 9x16/img/NN.jpg 1080x1920 (Short/Reel/TikTok/Stories),
# 1x1/img/NN.jpg 1080x1080 (square Facebook carousel, Denise Oct 22 2026).
# Grade (fullbleed_teal standard): autocontrast blend 0.45, slight warmth, +4% contrast, UnsharpMask(1.0,70,2); LIFT = gamma brighten.
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
M={"01":("p38604168",.45,.5),"02":("p34531575",.5,.6),"03":("wm-Gold_nugget_(Australia)_4_(16848647509)",.45,.5),
   "04":("p5580657",.5,.7),"05":("p5900802",.5,.5),"06":("p7487005",.35,.5),
   "07":("wm-Wilmore_Centennial_Park_viewed_from_South_Tryon_Early_May_2024",.42,.6),
   "08":("wm-South_End_Rail_Trail_at_Bland_St_Station_March_2024",.5,.5),"09":("p33327057",.5,.2),"10":("p32342611",.5,.55)}
LIFT={"01":1.12,"04":1.08,"06":1.12,"10":1.1}
def grade(im,k):
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.45)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    return im
def crop(im,W,H,x,y):
    r=max(W/im.width,H/im.height); assert r<1,(im.size,W,H)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-W)*x); t=int((im.height-H)*y)
    return im.crop((l,t,l+W,t+H))
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("img",exist_ok=True); os.makedirs("9x16/img",exist_ok=True); os.makedirs("1x1/img",exist_ok=True)
# Retouch (no visible house numbers, COMPLIANCE.md T5): slide 1 source has "19" on the door trim; cover it with the trim directly above.
FIX={"01":[((3368,2975,3452,3080),(3368,3092))]}
BLUR={"09":[(2380,3780,2640,3930)]}   # slide 9 source: blur the parked car's license plate (no readable plates, T5)
for k,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    for b in BLUR.get(k,[]): im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(18)),b[:2])
    for box,src in FIX.get(k,[]):
        w,h=box[2]-box[0],box[3]-box[1]; mk=Image.new("L",(w,h),0); mk.paste(255,(8,8,w-8,h-8)); mk=mk.filter(ImageFilter.GaussianBlur(5))
        im.paste(im.crop((src[0],src[1],src[0]+w,src[1]+h)),box[:2],mk)
    grade(crop(im,1080,1350,x,y),k).save(f"img/{k}.jpg",quality=95)
    grade(crop(im,1080,1920,x,y),k).save(f"9x16/img/{k}.jpg",quality=95); grade(crop(im,1080,1080,x,y),k).save(f"1x1/img/{k}.jpg",quality=95); print(k,f,"ok")
