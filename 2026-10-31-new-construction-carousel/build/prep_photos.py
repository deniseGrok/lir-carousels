# Oct 31 2026 NC carousel photo prep: builder photos on slides 2-5, 7-9; slides 1, 6, 10 replaced Oct 31 with free-license Unsplash/Pexels originals (src/; pexels-7914572 has 3 unit-number plaques retouched out in the saved src) (credited Eastwood Homes; each from the community page on eastwoodhomes.com). Native cover-crop for 4:5 and 1:1, Lanczos,
# grade: autocontrast blend 0.45, slight warmth, +4% contrast, +3% saturation, UnsharpMask (stronger when upscaled).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={1:("src/photo-1647579350413-a6ada4e480ed.jpg",.84,.5),2:("src/ro_club.jpg",.5,.5),3:("src/cf_patterson.jpg",.5,.5),4:("src/cw_008.jpg",.5,.5),
   5:("src/rc_016.jpg",.5,.5),6:("src/pexels-7914572.jpg",.5,1.0),7:("src/bc_towns.jpg",.5,.5),
   8:("src/gs_kitchen.jpg",.5,.5),9:("src/ro_lounge.jpg",.5,.5),10:("src/photo-1784810801262-d0d27227a480.jpg",.75,.5)}
FX={(1,"img1x1"):.8,(10,"img1x1"):.95}
FY={(6,"img1x1"):.55}
# house numbers retouched out; rects given in 4:5 output px, mapped back to source px (so both sizes are clean); 'v' = blend from the clean trim above/below
FIX45={4:[(992,876,1052,904,'h'),(908,984,932,1002,'v')],5:[(740,754,766,828,'v')],
       7:[(158,650,212,682,'v'),(824,703,866,728,'v')]}  # house numbers retouched out
def retouch(im,rects):
    a=np.asarray(im).astype(float).copy()
    for x0,y0,x1,y1 in rects:
        top=a[y0-3:y0-1,x0:x1].mean(0); bot=a[y1+1:y1+3,x0:x1].mean(0)
        for k,y in enumerate(range(y0,y1)):
            t=(k+1)/(y1-y0+1); a[y,x0:x1]=top*(1-t)+bot*t
    return Image.fromarray(a.clip(0,255).astype('uint8'))
def retouch_h(im,rects):  # blend from the clean columns left/right (for horizontal trim)
    a=np.asarray(im).astype(float).copy()
    for x0,y0,x1,y1 in rects:
        L=a[y0:y1,x0-3:x0-1].mean(1); R=a[y0:y1,x1+1:x1+3].mean(1)
        for k,x in enumerate(range(x0,x1)):
            t=(k+1)/(x1-x0+1); a[y0:y1,x]=L*(1-t)+R*t
    return Image.fromarray(a.clip(0,255).astype('uint8'))
SIZES={"img":(1080,1350),"img1x1":(1080,1080)}
for i,(f,x,y) in M.items():
    src=ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    if i in FIX45:
        r=max(1080/src.width,1350/src.height); l=(round(src.width*r)-1080)*x; t=(round(src.height*r)-1350)*y
        for x0,y0,x1,y1,mode in FIX45[i]:
            src=(retouch_h if mode=='h' else retouch)(src,[tuple(int(v) for v in ((x0+l)/r,(y0+t)/r,(x1+l)/r+1,(y1+t)/r+1))])
    for d,(W,H) in SIZES.items():
        r=max(W/src.width,H/src.height); im=src.resize((round(src.width*r),round(src.height*r)),Image.LANCZOS)
        xx=FX.get((i,d),x); l=int((im.width-W)*xx); t=int((im.height-H)*FY.get((i,d),y)); im=im.crop((l,t,l+W,t+H))
        im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.45)
        R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
        im=ImageEnhance.Contrast(im).enhance(1.04); im=ImageEnhance.Color(im).enhance(1.03)
        im=im.filter(ImageFilter.UnsharpMask(1.4 if r>1.4 else 1.0, 90 if r>1.4 else 60, 2))
        im.save(f"{d}/{i:02d}.jpg",quality=94)
    print(i,f,src.size,"scale4:5=%.2f"%max(1080/src.width,1350/src.height))
