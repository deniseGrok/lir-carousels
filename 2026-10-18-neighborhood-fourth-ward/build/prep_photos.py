# Fourth Ward photo prep, Oct 18 2026. Full-res originals in src/ (Pexels originals; Wikimedia Commons originals), resized DOWN only
# to a 1080x1350 cover crop, then graded: clean-white autocontrast blend 0.5, slight warmth, +4% contrast, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p38305737.jpg",.5,.5),2:("src/p35107480.jpg",.5,.55),3:("src/p29021440.jpg",.5,.5),4:("src/p35221620.jpg",.5,.5),
   5:("src/wm-Fourth_Ward_Park_fountain_Late_April_2025.jpg",.9,.5),6:("src/wm-Charlotte_Settlers_Cemetery.jpg",.5,.5),
   7:("src/p29649754.jpg",.5,.5),8:("src/wm-First_Presbyterian_Charlotte_NC_1.jpg",.5,.4),
   9:("src/p34625605.jpg",.5,.3),10:("src/p6696807.jpg",.5,.5)}
LIFT={4:1.18}
POP={6:(1.06,1.10),8:(1.07,1.06)}  # extra (contrast, color) for the two overcast-ish Wikimedia shots  # gentle shadow lift (gamma) for the turret photo, shot against the light
for i,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); r=max(1080/im.width,1350/im.height); assert r<1, (f,im.size)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2)); 
    if i in POP: im=ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(POP[i][0])).enhance(POP[i][1])
    if i in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[i])))
    im.save(f"img/{i:02d}.jpg",quality=95)
    print(i,f,"ok")
