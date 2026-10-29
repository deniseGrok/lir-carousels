# Oct 29 2026 NC carousel photo prep: builder photos only (all credited 'Photo: Lennar', from each community's own Lennar page). Native cover-crop for 4:5 and 1:1, Lanczos,
# grade: autocontrast blend 0.45, slight warmth, +4% contrast, +3% saturation, UnsharpMask (stronger when upscaled; KB web photos are 1200x800).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={1:("src/sv_pic2.jpg",.5,.5),2:("src/sr_blake_kit.jpg",.5,.5),3:("src/cc_mpc.jpg",.5,.5),4:("src/sv_west_great.jpg",.5,.5),
   5:("src/ns_fire.jpg",.5,.5),6:("src/ac_dream13.jpg",.5,.5),7:("src/ns_verona_great.jpg",.5,.5),
   8:("src/sv_chad_liv.jpg",.5,.5),9:("src/ns_cp2.jpg",.5,.5),10:("src/ns_lake.jpg",.12,.5)}
FX={}
# house numbers retouched out; rects given in 4:5 output px, mapped back to source px (so both sizes are clean); 'v' = blend from the clean trim above/below
FIX45={3:[(460,786,478,862,'v')]}
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
