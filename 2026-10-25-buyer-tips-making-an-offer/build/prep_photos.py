# Buyer tips Oct 25 2026 photo prep. Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# One crop per photo: img/NN.jpg 1080x1350 (4:5 carousel). The 1:1 set reuses img/NN.jpg with background-size:cover.
# Grade (fullbleed_tips standard): autocontrast blend 0.35, slight warmth, +5% contrast, UnsharpMask(1.0,70,2).
# No 9:16 set and no Short (Denise Oct 24 2026).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={"01":("p4030036",.5,.5),"03":("p16641323",.45,.5),"04":("p6035306",.5,.5),"05":("p4800175",.62,.5),"06":("p39404263",.55,.5),
   "07":("p4682075",.5,.5),"08":("p14495942",.5,.5),"09":("p31602311",.4,.5),"10":("p10855266",.5,.5)}
LIFT={}
# Retouch (T5: no visible house numbers), on the 1080x1350 crop before grading: number plaques painted out with
# adjacent trim/post copied over them (slide 01 Pexels 4030036 beam over the door, plus a brand yard sign painted out with shrub; slide 04 Pexels 6035306 porch beam; slide 07 Pexels 4682075 porch post).
from PIL import ImageDraw
RT={"01":[((731,615,772,639),(-44,0)),((325,819,355,861),(0,-44))],"04":[((668,590,724,622),(-72,0))],"07":[((772,748,802,832),(0,96))]}
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
