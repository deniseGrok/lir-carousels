import sys,os; sys.path.insert(0,"/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from carousel_style import slide, ul, render
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
D="/workspace/lir-ai-team/content-research/carousels/2026-10-16-seller-tips-prep-before-listing"; O=os.getcwd()
for n in ("01","04"):
    im=Image.open(f"{D}/build/img-lux/{n}.jpg").convert("RGB")
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.035+2))); b=b.point(lambda v:int(v*0.96))
    im=Image.merge("RGB",(r,g,b)); im=ImageEnhance.Contrast(im).enhance(1.07); im=ImageEnhance.Color(im).enhance(0.97); im=ImageEnhance.Sharpness(im).enhance(1.25)
    im.save(f"img/{n}.jpg",quality=93)
P={"1 Navy + champagne":("#0B1F3A","#F5EFE3","#D4B483","#C9D0DA"),"2 Black + blush":("#111111","#F5EFE3","#E8B4B8","#CFCAC4"),"3 Emerald + brass":("#0F3D2E","#F4ECDC","#B08D57","#CFDBD3")}
def ov(bg,tx,ac,mu): return (f"<style>html,body,.s{{background:{bg}!important}}.s{{color:{tx}}}h1{{color:{tx}!important}}"
  f"h1 em{{color:{ac}!important;background:none!important;font-style:normal}}li,p.b{{color:{mu}!important}}li:before{{background:{ac}!important}}"
  f".tag{{background:{bg}!important;color:{tx}!important;border-bottom:4px solid {ac}!important}}.band{{background:{ac}!important;color:{bg}!important}}.band em{{color:{bg}!important}}"
  f".ft{{color:{ac}!important;border-top:1px solid {ac}55!important}}.ph{{border-bottom:4px solid {ac}}}</style>")
labels=[];files=[]
for k,(bg,tx,ac,mu) in P.items():
    o=ov(bg,tx,ac,mu); tag=k.split()[0]
    S=[slide(1,"SELLER TIP 1","01.jpg",o+"<h1>Fix the small stuff <em>before</em> buyers see it</h1><p class='b' style='font-size:36px'>Most of what buyers notice can be handled before the sign goes up. Here's the prep order I recommend.</p>",band="LISTING SOON? <em>PREP FIRST.</em>",ph=780,ct=820,h1=72,li=34,theme="photo_top",footer="SELLER TIPS"),
       slide(4,"SELLER TIP 3","04.jpg",o+"<h1>Clear, clean, <em>then paint</em></h1>"+ul(["Pack what you won't need before moving day","Deep-clean kitchens, baths and windows","Minor cosmetic updates like paint, fixtures and landscaping typically pay off (Realtor.com)"]),ph=800,ct=840,h1=78,li=34,theme="photo_top",footer="SELLER TIPS")]
    out=render([(s[0],0,0,0) for s in S],O,O,prefix=f"palette-{tag}")
    for src,n in zip(out,("1","4")): dst=f"{O}/palette-{tag}-slide{n}.png"; os.replace(src,dst); files.append(dst)
    labels.append(k)
fp="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; f=ImageFont.truetype(fp,34) if os.path.exists(fp) else ImageFont.load_default()
W,H=540,675; c=Image.new("RGB",(3*W+4*20,2*H+3*20+80),"#EDEAE4"); d=ImageDraw.Draw(c)
for j,k in enumerate(labels):
    x=20+j*(W+20); d.text((x,20),k,fill="#111",font=f); t=k.split()[0]
    for r,n in enumerate(("1","4")): c.paste(Image.open(f"{O}/palette-{t}-slide{n}.png").resize((W,H)),(x,80+r*(H+20)))
c.save(f"{D}/options/palette-compare.png"); print("\n".join(files))
