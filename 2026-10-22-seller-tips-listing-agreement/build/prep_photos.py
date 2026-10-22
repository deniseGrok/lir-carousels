# Seller tips Oct 22 2026 photo prep. Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# Two crops per photo: img/NN.jpg 1080x1350 (4:5 carousel) and 9x16/img/NN.jpg 1080x1920 (TikTok/Stories/Short).
# Grade (fullbleed_tips standard): autocontrast blend 0.35, +5% contrast, slight warmth, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
M={"01":("p12148363",.5,.45),"03":("p8850629",.5,.4),"04":("p2343469",.5,.5),"05":("p34037811",.45,.5),"06":("p14598479",.55,.5),
   "07":("p4654982",.4,.5),"08":("p18032330",.5,.5),"09":("p4740488",.55,.5),"10":("p14998093",.5,.4)}
LIFT={"01":1.06}
def grade(im,k):
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.35)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    return im
def crop(im,W,H,x,y):
    r=max(W/im.width,H/im.height); assert r<1,(im.size,W,H)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-W)*x); t=int((im.height-H)*y)
    return im.crop((l,t,l+W,t+H))
os.makedirs("img",exist_ok=True); os.makedirs("9x16/img",exist_ok=True)
for k,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    grade(crop(im,1080,1350,x,y),k).save(f"img/{k}.jpg",quality=95)
    grade(crop(im,1080,1920,x,y),k).save(f"9x16/img/{k}.jpg",quality=95); print(k,f,"ok")
