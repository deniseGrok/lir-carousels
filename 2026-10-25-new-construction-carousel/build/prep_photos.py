# Oct 25 2026 NC carousel photo prep: builder photos only (credited). Native cover-crop for 4:5 and 1:1, Lanczos,
# grade: autocontrast blend 0.45, slight warmth, +4% contrast, +3% saturation, UnsharpMask (stronger when upscaled).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np
M={1:("src/mie_3237098.jpg",.5,.5),2:("src/mip_5542440.jpg",.5,.5),3:("src/mie_4739245.jpg",.5,.6),4:("src/mic_4661547.jpg",.5,.5),
   5:("src/ccb_kensington-e--_5-web-or-mls-d.jpg",.5,.5),6:("src/cco_daffodil-c2---_5-web-or-mls-d.jpg",.5,.6),7:("src/mst_clt-sts-modelbuilding-exterior2.jpg",.5,.5),
   8:("src/mhc_clt-hedgecliff-adriana-model-exterior-fr.jpg",.5,.5),9:("src/mie_3155021.jpg",.5,.5),10:("src/mst_clt-sts-aurora-2131vinyasaln-dining2.jpg",.5,.5)}
FX={}
FIX={1:[(656,734,673,783)],3:[(516,777,538,865)],4:[(1094,764,1115,818)],2:[(882,670,906,733,'b'),(1433,678,1447,727,'b'),(319,683,333,736,'b')]}  # house numbers retouched out (source px); 'b' = fill from the clean trim just below
PATCH={8:[(866,856,921,894,-35),(368,806,420,838,-35),(1622,856,1673,887,-35)],7:[(927,947,971,978,-33)]}  # house-number plaque covered with siding copied from 35 px above (3 siding courses)
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
    if i in FIX: src=retouch(src,FIX[i])
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
