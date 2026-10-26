# Seller tips Oct 26 2026 photo prep. Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# One crop per photo: img/NN.jpg 1080x1350 (4:5 carousel). The 1:1 set reuses img/NN.jpg with background-size:cover.
# Grade (fullbleed_tips standard): autocontrast blend 0.35, slight warmth, +5% contrast, UnsharpMask(1.0,70,2).
# Oct 26 photo pass: slides 1, 5, 6, 9 replaced with brighter, crisper Pexels originals (>=3000px).
# No 9:16 set and no Short (Denise Oct 24 2026).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={"01":("p10258631",.42,.5),"03":("p10827394",.35,.5),"04":("p6510970",.45,.5),"05":("p20806614",.5,.5),"06":("p17158688",.5,.5),
   "07":("p37153448",.5,.5),"08":("p15668080",.5,.5),"09":("p16581570",.5,.5),"10":("p8134748",.55,.5)}
LIFT={"04":1.12,"08":1.1,"07":1.06,"05":1.18,"09":1.1}
# Retouch (T5: no visible house numbers): none needed in the final set (checked at full size).
from PIL import ImageDraw
RT={}
# (paint_num kept from an earlier cover candidate; not used in the final set)
def paint_num(im):
    from PIL import ImageStat
    box=(588,612,632,636); ref=im.crop((box[0],box[1]-2,box[2],box[1]+1))
    col=tuple(int(v) for v in ImageStat.Stat(im.crop((640,615,650,632))).median)
    patch=Image.new("RGB",(box[2]-box[0],box[3]-box[1]),col)
    m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((2,2,patch.size[0]-3,patch.size[1]-3),fill=255); m=m.filter(ImageFilter.GaussianBlur(2))
    im.paste(patch,box[:2],m); return im
def retouch(k,im):
    for box,(dx,dy) in RT.get(k,[]):
        patch=im.crop((box[0]+dx,box[1]+dy,box[2]+dx,box[3]+dy))
        m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((2,2,patch.size[0]-3,patch.size[1]-3),fill=255)
        m=m.filter(ImageFilter.GaussianBlur(1.5)); im.paste(patch,box[:2],m)
    return im
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
os.makedirs("img",exist_ok=True)
for k,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    grade(retouch(k,crop(im,1080,1350,x,y)),k).save(f"img/{k}.jpg",quality=95); print(k,f,"ok")
