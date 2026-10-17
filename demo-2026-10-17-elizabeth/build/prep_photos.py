# Demo photo prep: full-res Pexels originals in src/, resized DOWN only to a 1080x1350 cover crop, light grade + sharpen.
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
M={1:("src/p5353939.jpg",.45,.5),2:("src/p18940489.jpg",.5,.5)}
Z={2:(2700,1800,440)}  # slide 2: resize the 6000x4000 original DOWN to 2700x1800, crop from y=440 so the house sits high, above the stats
for i,(f,x,y) in M.items():
    im=Image.open(f).convert("RGB")
    if i in Z:
        w,h,t=Z[i]; assert w<im.width; im=im.resize((w,h),Image.LANCZOS); l=(w-1080)//2; im=im.crop((l,t,l+1080,t+1350))
    else:
        r=max(1080/im.width,1350/im.height); assert r<1
        im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-1080)*x); t=int((im.height-1350)*y); im=im.crop((l,t,l+1080,t+1350))
    if i==1:  # remove the small blue "ADT" yard sign (a brand name): rebuild that patch from the ledge/foundation/mulch on either side
        import numpy as np
        a=np.asarray(im).astype(float); x0,x1,y0,y1=662,716,846,992
        for yy in range(y0,y1):
            if yy<948:   # ledge + foundation: blend row by row between the clean pixels left and right of the sign
                L=a[yy,x0-3:x0].mean(0); R=a[yy,x1:x1+3].mean(0); t=np.linspace(0,1,x1-x0)[:,None]; a[yy,x0:x1]=L*(1-t)+R*t
            else:        # mulch: copy real texture from just left of the sign
                a[yy,x0:x1]=a[yy,x0-(x1-x0):x0]
        fixed=Image.fromarray(a.clip(0,255).astype("uint8"))
        from PIL import ImageDraw
        m=Image.new("L",im.size,0); ImageDraw.Draw(m).rectangle((x0+2,y0+2,x1-2,y1-2),fill=255); m=m.filter(ImageFilter.GaussianBlur(2))
        im=Image.composite(fixed,im,m)
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.015+1))); B=B.point(lambda v:int(v*0.985)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2)); im.save(f"img/{i:02d}.jpg",quality=95)
