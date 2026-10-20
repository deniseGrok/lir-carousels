# Wesley Heights photo prep, Oct 20 2026. Full-res originals in src/ (Pexels originals; Wikimedia Commons originals or 3840px renders), resized DOWN only
# to a 1080x1350 cover crop, then graded: clean-white autocontrast blend 0.5, slight warmth, +4% contrast, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p24245769.jpg",.42,.5),2:("src/p12119561.jpg",.5,.5),3:("src/p5587932.jpg",.3,.5),4:("src/p40265537.jpg",0.85,0.5),
   5:("src/p14388869.jpg",1.0,.45),6:("src/p5071177.jpg",.5,.5),7:("src/wm-Wesley_Heights_01.jpg",.56,.5),8:("src/p36896236.jpg",.5,.5),
   9:("src/p6422929.jpg",.62,.5),10:("src/p5502227.jpg",.45,.5)}
LIFT={}
POP={}
ZOOM={5:1.22}
import os
for i,(f,x,y) in M.items():
    if not os.path.exists(f): print(i,"missing",f); continue
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); r=max(1080/im.width,1350/im.height)*ZOOM.get(i,1); assert r<1, (f,im.size)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if i in POP: im=ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(POP[i][0])).enhance(POP[i][1])
    if i in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[i])))
    im.save(f"img/{i:02d}.jpg",quality=95)
    print(i,f,"ok")
