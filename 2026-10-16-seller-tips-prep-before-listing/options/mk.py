import subprocess,os
O=os.getcwd()
S1=dict(tag="SELLER TIP 1",band="Listing soon? <em>Prep first.</em>",h="Fix the small stuff <em>before</em> buyers see it",body="<p>Most of what buyers notice can be handled before the sign goes up. Here's the prep order I recommend.</p>",img="01.jpg",n="1")
S4=dict(tag="SELLER TIP 3",band="",h="Clear, clean, <em>then paint</em>",body="<ul><li>Pack what you won't need before moving day</li><li>Deep-clean kitchens, baths and windows</li><li>Minor cosmetic updates like paint, fixtures and landscaping typically pay off (Realtor.com)</li></ul>",img="04.jpg",n="4")
BASE="""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;font-family:'Inter';overflow:hidden}
.ph{position:absolute;left:0;right:0;top:0;background-size:cover;background-position:center}
h1{font-family:'Playfair Display','Georgia',serif;font-weight:600;line-height:1.08}
.tag{font-family:'Montserrat';font-weight:700;font-size:30px;letter-spacing:4px;text-transform:uppercase}
.band{font-family:'Montserrat';font-weight:700;font-size:32px;letter-spacing:3px;text-transform:uppercase;margin-bottom:18px}
p,li{font-size:34px;line-height:1.4}ul{list-style:none}li{padding-left:40px;position:relative;margin-bottom:12px}
li:before{content:'';position:absolute;left:0;top:20px;width:20px;height:2px}
.ft{position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-family:'Montserrat';font-weight:600;font-size:30px;letter-spacing:3px}
.rule{width:90px;height:3px;margin:0 0 22px}"""
OPT={
"A":("Warm neutral: greige panel, charcoal, brushed brass","""
.s{background:#E9E2D6}.ph{height:760px}.c{position:absolute;left:64px;right:64px;top:800px;color:#2E2B28}
.tag{position:absolute;top:44px;left:44px;background:rgba(233,226,214,.92);color:#2E2B28;padding:12px 22px}
h1{font-size:66px;color:#2E2B28}h1 em{font-style:italic;color:#9C7A3C}.band{color:#9C7A3C}.rule{background:#9C7A3C}
li:before{background:#9C7A3C}.ft{color:#5B544C;border-top:1px solid #CFC5B5;padding-top:14px}"""),
"B":("Photo-dominant: full photo, small frosted card, cream text, champagne","""
.s{background:#222}.ph{height:1350px}.c{position:absolute;left:48px;right:48px;bottom:120px;padding:38px 44px;color:#F6F0E4;
background:rgba(30,28,25,.42);backdrop-filter:blur(18px) saturate(1.1);border-radius:6px;border:1px solid rgba(246,240,228,.25)}
.tag{position:absolute;top:44px;left:44px;color:#F6F0E4;background:rgba(30,28,25,.35);backdrop-filter:blur(10px);padding:12px 22px}
h1{font-size:60px;color:#F6F0E4}h1 em{font-style:italic;color:#E2CFA4}.band{color:#E2CFA4}.rule{background:#E2CFA4}
p,li{font-size:32px}li:before{background:#E2CFA4}.ft{color:#F6F0E4;text-shadow:0 1px 8px rgba(0,0,0,.8)}.ft span{background:rgba(30,28,25,.35);padding:6px 12px;border-radius:4px}"""),
"C":("Magazine: espresso band, ivory text, muted gold line","""
.s{background:#2B241F}.ph{height:720px}.c{position:absolute;left:64px;right:64px;top:770px;color:#F3ECDF}
.ph:after{content:'';position:absolute;left:0;right:0;bottom:0;height:4px;background:#B8995A}
.tag{position:absolute;top:44px;left:44px;background:#2B241F;color:#F3ECDF;padding:12px 22px;border-bottom:3px solid #B8995A}
h1{font-size:66px;color:#F3ECDF}h1 em{font-style:italic;color:#C9AE73}.band{color:#C9AE73}.rule{background:#B8995A}
li:before{background:#B8995A}.ft{color:#BFB3A0;border-top:1px solid #4A4038;padding-top:14px}"""),
"D":("Natural: sage panel, cream type, olive accent","""
.s{background:#7E8A6E}.ph{height:740px}.c{position:absolute;left:64px;right:64px;top:790px;color:#F7F2E7}
.tag{position:absolute;top:44px;left:44px;background:#F7F2E7;color:#4E5841;padding:12px 22px}
h1{font-size:66px;color:#F7F2E7}h1 em{font-style:italic;color:#EADBB5}.band{color:#EADBB5}.rule{background:#EADBB5}
li:before{background:#EADBB5}.ft{color:#E9E4D6;border-top:1px solid #9AA58A;padding-top:14px}"""),
}
for k,(desc,css) in OPT.items():
  for S in (S1,S4):
    band=f"<div class='band'>{S['band']}</div>" if S['band'] else ""
    html=f"""<!doctype html><html><head><meta charset='utf-8'><style>{BASE}{css}</style></head><body><div class='s'>
<div class='ph' style="background-image:url('{S['img']}')"></div><div class='tag'>{S['tag']}</div>
<div class='c'>{band}<div class='rule'></div><h1>{S['h']}</h1><div style='margin-top:22px'>{S['body']}</div></div>
<div class='ft'><span>SELLER TIPS</span><span>{S['n']} / 10</span></div></div></body></html>"""
    hp=f"{O}/opt-{k}-slide{S['n']}.html"; open(hp,"w").write(html)
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--hide-scrollbars","--force-device-scale-factor=1","--window-size=1080,1350",f"--screenshot={O}/option-{k}-slide{S['n']}.png","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
from PIL import Image,ImageDraw,ImageFont
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",34) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
W,H=540,675; c=Image.new("RGB",(4*W+5*20,2*H+3*20+80),"#F2EFEA"); d=ImageDraw.Draw(c)
for j,(k,(desc,_)) in enumerate(OPT.items()):
  x=20+j*(W+20); d.text((x,18),f"Option {k}",fill="#222",font=f)
  for r,n in enumerate(("1","4")): c.paste(Image.open(f"{O}/option-{k}-slide{n}.png").resize((W,H)),(x,80+r*(H+20)))
c.save(f"{O}/compare.png"); print("ok")
