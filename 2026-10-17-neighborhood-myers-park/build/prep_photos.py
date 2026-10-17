# Final photo prep, Oct 17 2026. Full-res originals in src/ (Pexels originals; Wikimedia original for 08), resized DOWN only to 1080x1350 cover crop.
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p29374845.jpg",.5,.5),2:("src/p36595190.jpg",.5,.5),3:("src/p29084122.jpg",.5,.5),4:("src/p40244089.jpg",0.0,.5),
   5:("src/p30193323.jpg",.4,.5),6:("src/p34857738.jpg",.5,.5),7:("src/p33425081.jpg",.5,.5),8:("src/wm-Charlotte_NC_Uptown.jpg",.5,.5),
   9:("src/p38945371.jpg",.5,.5),10:("src/p2962739.jpg",.5,.45)}
for i,(f,x,y) in M.items():
    im=Image.open(f).convert("RGB"); r=max(1080/im.width,1350/im.height); assert r<1
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2)); im.save(f"img/{i:02d}.jpg",quality=95)
