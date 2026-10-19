# Eastover photo prep, Oct 19 2026. Full-res originals in src/ (Pexels originals; Wikimedia Commons 3840px renders), resized DOWN only
# to a 1080x1350 cover crop, then graded: clean-white autocontrast blend 0.5, slight warmth, +4% contrast, UnsharpMask(1.0,70,2).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p13005859.jpg",.5,.5),2:("src/p33856985.jpg",.5,.5),3:("src/p32481181.jpg",.5,.4),4:("src/p36086367.jpg",.45,.85),
   5:("src/wm-Hamilton_Jones_III_House.jpg",.55,.5),6:("src/wm-Mint_Museum_of_Art_Randolph_Charlotte__NC_Aug_2015.jpg",.62,.5),
   7:("src/p38846728.jpg",.5,.5),8:("src/wm-Charlotte_Fire_Station_No._6.jpg",.45,.92),
   9:("src/p18819232.jpg",.5,.5),10:("src/p8583893.jpg",.45,.5)}
LIFT={}
POP={8:(1.06,1.08)}
ZOOM={4:1.22,8:1.5}  # tighter cover crops (still downscaled): slide 4 drops an overhead wire, slide 8 trims blank sky
for i,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); r=max(1080/im.width,1350/im.height)*ZOOM.get(i,1); assert r<1, (f,im.size)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if i in POP: im=ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(POP[i][0])).enhance(POP[i][1])
    if i in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[i])))
    im.save(f"img/{i:02d}.jpg",quality=95)
    print(i,f,"ok")
