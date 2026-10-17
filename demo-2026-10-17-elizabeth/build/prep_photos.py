# Demo photo prep: full-res Pexels originals in src/, resized DOWN only to a 1080x1350 cover crop, light grade + sharpen.
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p5353939.jpg",.45,.5),2:("src/p37860098.jpg",.5,.5)}
for i,(f,x,y) in M.items():
    im=Image.open(f).convert("RGB"); r=max(1080/im.width,1350/im.height); assert r<1
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    if i==2:  # soften the small out-of-area street-name sign ("Weaver Ave", Mount Gretna PA) so the slide never shows a wrong place name
        from PIL import ImageDraw
        box=(470,505,640,600); reg=im.crop(box); b=reg.filter(ImageFilter.GaussianBlur(14))
        # pull the patch toward the surrounding wood/leaf tones so no bright rectangle remains
        b=Image.blend(b,Image.new("RGB",b.size,(78,70,58)),0.55).filter(ImageFilter.GaussianBlur(6))
        m=Image.new("L",reg.size,0); ImageDraw.Draw(m).ellipse((12,10,reg.width-12,reg.height-10),fill=255); m=m.filter(ImageFilter.GaussianBlur(12))
        im.paste(Image.composite(b,reg,m),box[:2])
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2)); im.save(f"img/{i:02d}.jpg",quality=95)
