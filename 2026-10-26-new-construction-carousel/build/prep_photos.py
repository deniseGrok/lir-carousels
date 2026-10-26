# Oct 26 2026 NC carousel photo prep: builder photos only (credited). Native cover-crop for 4:5 and 1:1, Lanczos,
# grade: autocontrast blend 0.45, slight warmth, +4% contrast, +3% saturation, UnsharpMask (stronger when upscaled).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np, os
Image.MAX_IMAGE_PIXELS=None
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={1:("src/tcx_01-130093835.jpg",.5,.5),2:("src/tmi_04-ALC09444.jpg",.5,.5),3:("src/tcx_Context_at_Oakhurst-Wright_Kitchen.jpg",.5,.5),4:("src/tel_04-ALC00247.jpg",.5,.5),
   5:("src/tam_06-Patio.jpg",.5,.5),6:("src/mch_thetownesatcheyney-briana-kitchen.jpg",.5,.5),7:("src/mbp_bpl-prescottmodel-greatroom-kitchen.jpg",.5,.5),
   8:("src/cbs_calderwood-c-lot-1_35-print-001.jpg",.5,.5),9:("src/csm_daffodil-f2-lot-1_5.jpg",.5,.5),10:("src/tmi_44-ALC09689.jpg",.5,.5)}
FX={}
FIX={}; PATCH={}
# house numbers retouched out; rects given in 4:5 output px, mapped back to source px (so both sizes are clean)
# 'v' = blend down the white trim from the clean trim above/below; ('h',dx) = copy the same trim band from dx px to the side
FIX45={1:[(593,891,610,942,'v')],4:[(334,663,376,681,('h',-46))],10:[(809,829,823,877,'v')],8:[(879,822,898,875,'v')]}
def retouch(im,rects):
    a=np.asarray(im).astype(float).copy()
    for rr in rects:
        x0,y0,x1,y1=rr[:4]
        if len(rr)>4: a[y0:y1,x0:x1]=a[y1+1:y1+3,x0:x1].mean(0); continue
        top=a[y0-3:y0-1,x0:x1].mean(0); bot=a[y1+1:y1+3,x0:x1].mean(0)
        for k,y in enumerate(range(y0,y1)):
            t=(k+1)/(y1-y0+1); a[y,x0:x1]=top*(1-t)+bot*t
    return Image.fromarray(a.clip(0,255).astype('uint8'))
SIZES={"img":(1080,1350),"img1x1":(1080,1080)}
for i,(f,x,y) in M.items():
    src=ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    if src.width>4200: src=src.resize((4096,round(src.height*4096/src.width)),Image.LANCZOS)
    if i in FIX: src=retouch(src,FIX[i])
    if i in FIX45:
        r=max(1080/src.width,1350/src.height); l=(round(src.width*r)-1080)*x; t=(round(src.height*r)-1350)*y
        for x0,y0,x1,y1,mode in FIX45[i]:
            X0,Y0,X1,Y1=[int(v) for v in ((x0+l)/r,(y0+t)/r,(x1+l)/r+1,(y1+t)/r+1)]
            if mode=='v': src=retouch(src,[(X0,Y0,X1,Y1)])
            else: dx=int(mode[1]/r); src.paste(src.crop((X0+dx,Y0,X1+dx,Y1)),(X0,Y0))
    for x0,y0,x1,y1,dy in PATCH.get(i,[]): src.paste(src.crop((x0,y0+dy,x1,y1+dy)),(x0,y0))
    for d,(W,H) in SIZES.items():
        r=max(W/src.width,H/src.height); im=src.resize((round(src.width*r),round(src.height*r)),Image.LANCZOS)
        xx=FX.get((i,d),x); l=int((im.width-W)*xx); t=int((im.height-H)*y); im=im.crop((l,t,l+W,t+H))
        im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.45)
        R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
        im=ImageEnhance.Contrast(im).enhance(1.04); im=ImageEnhance.Color(im).enhance(1.03)
        im=im.filter(ImageFilter.UnsharpMask(1.2 if r>1.2 else 1.0, 80 if r>1.2 else 60, 2))
        im.save(f"{d}/{i:02d}.jpg",quality=94)
    print(i,f,src.size,"scale4:5=%.2f"%max(1080/src.width,1350/src.height))
