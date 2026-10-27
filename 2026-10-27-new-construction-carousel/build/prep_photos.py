# Oct 27 2026 NC carousel photo prep: builder photos only (credited KB Home / Mattamy Homes). Native cover-crop for 4:5 and 1:1, Lanczos,
# grade: autocontrast blend 0.45, slight warmth, +4% contrast, +3% saturation, UnsharpMask (stronger when upscaled; KB web photos are 1200x800).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={1:("src/kbv_2338ext.jpg",.5,.5),2:("src/kbv_1910ext.jpg",.5,.5),3:("src/kbm_2338.jpg",.5,.5),4:("src/kbw_2539.jpg",.5,.5),
   5:("src/kbb_1808.jpg",.5,.5),6:("src/mwa_clt-way-caswellend-model-exteriorfrontday1.jpg",.5,.5),7:("src/mwa_clt-way-caswellend-model-greatroom-kitchen.jpg",.5,.5),
   8:("src/kbv_porch.jpg",.5,.5),9:("src/kbw_0093.jpg",.5,.5),10:("src/mwa_clt-way-caswellend-model-kitchen.jpg",.5,.5)}
FX={}
# house numbers retouched out; rects given in 4:5 output px, mapped back to source px (so both sizes are clean); 'v' = blend from the clean trim above/below
FIX45={1:[(412,790,434,868,'v')],9:[(916,870,932,922,'v')],2:[(786,780,812,856,'v')],3:[(594,840,618,938,'v')]}
def retouch(im,rects):
    a=np.asarray(im).astype(float).copy()
    for x0,y0,x1,y1 in rects:
        top=a[y0-3:y0-1,x0:x1].mean(0); bot=a[y1+1:y1+3,x0:x1].mean(0)
        for k,y in enumerate(range(y0,y1)):
            t=(k+1)/(y1-y0+1); a[y,x0:x1]=top*(1-t)+bot*t
    return Image.fromarray(a.clip(0,255).astype('uint8'))
SIZES={"img":(1080,1350),"img1x1":(1080,1080)}
for i,(f,x,y) in M.items():
    src=ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    if i in FIX45:
        r=max(1080/src.width,1350/src.height); l=(round(src.width*r)-1080)*x; t=(round(src.height*r)-1350)*y
        for x0,y0,x1,y1,mode in FIX45[i]:
            src=retouch(src,[tuple(int(v) for v in ((x0+l)/r,(y0+t)/r,(x1+l)/r+1,(y1+t)/r+1))])
    for d,(W,H) in SIZES.items():
        r=max(W/src.width,H/src.height); im=src.resize((round(src.width*r),round(src.height*r)),Image.LANCZOS)
        xx=FX.get((i,d),x); l=int((im.width-W)*xx); t=int((im.height-H)*y); im=im.crop((l,t,l+W,t+H))
        im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.45)
        R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
        im=ImageEnhance.Contrast(im).enhance(1.04); im=ImageEnhance.Color(im).enhance(1.03)
        im=im.filter(ImageFilter.UnsharpMask(1.4 if r>1.4 else 1.0, 90 if r>1.4 else 60, 2))
        im.save(f"{d}/{i:02d}.jpg",quality=94)
    print(i,f,src.size,"scale4:5=%.2f"%max(1080/src.width,1350/src.height))
