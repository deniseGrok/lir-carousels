# Elizabeth photo prep (rebuild Oct 21 2026 ~6:45 AM ET): replaced slides 1, 2, 4, 10; re-cropped real Independence Park photos 5, 6 (credit moved below the tag).
# Full-res originals in src/, resized DOWN only to 1080x1350 cover crop; grade: autocontrast blend 0.5, slight warmth, +4% contrast, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os, sys
M={1:("src/p16501696.jpg",.5,.5),2:("src/p31719341.jpg",.5,.25),4:("src/p12196697.jpg",.35,.5),10:("src/p29007362.jpg",.5,.5),
   5:("src/wm-Independence_Park_near_7th_St_and_Hawthorne_Ave_looking_towards_Charlottetown_Ave_Early_August_2025.jpg",.5,.5),
   6:("src/wm-Independence_Park_walking_paths_along_Park_Dr_Lamar_Dr_Early_August_2025.jpg",.5,.5)}
LIFT={10:1.18}; ZOOM={}
for i,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); r=max(1080/im.width,1350/im.height)*ZOOM.get(i,1); assert r<1, (f,im.size)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if i in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[i])))
    im.save(f"img/{i:02d}.jpg",quality=95); print(i,f,"ok")
