# Buyer tips Oct 23 2026 photo prep. Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# Two crops per photo: img/NN.jpg 1080x1350 (4:5 carousel) and 9x16/img/NN.jpg 1080x1920 (TikTok/Stories/Short).
# 1:1 set reuses img/NN.jpg with background-size:cover. Grade (fullbleed_tips standard): autocontrast blend 0.35,
# +5% contrast, slight warmth, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
M={"01":("p12700464",.42,.5),"03":("p28586197",.3,.5),"04":("p15409513",.5,.5),"05":("p7045908",.35,.5),"06":("p2631746",.5,.5),
   "07":("p26595553",.5,.3),"08":("p6587896",.5,.5),"09":("p7168052",.45,.5),"10":("p4469146",.5,.5)}
# Retouch (T5: no visible house numbers): cover the address plaque on 12700464 with stone texture from just below it.
from PIL import ImageDraw
def retouch(f,im):
    if f=="p12700464":
        box=(2478,1334,2552,1372); dy=40
        patch=im.crop((box[0],box[1]+dy,box[2],box[3]+dy))
        m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((3,3,patch.size[0]-4,patch.size[1]-4),fill=255)
        from PIL import ImageFilter as _F; m=m.filter(_F.GaussianBlur(2))
        im.paste(patch,box[:2],m)
    return im
LIFT={"10":1.05}
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
    im=retouch(f,ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB"))
    grade(crop(im,1080,1350,x,y),k).save(f"img/{k}.jpg",quality=95)
    grade(crop(im,1080,1920,x,y),k).save(f"9x16/img/{k}.jpg",quality=95); print(k,f,"ok")
