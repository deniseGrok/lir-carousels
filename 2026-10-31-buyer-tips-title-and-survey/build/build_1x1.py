# Native 1:1 (1080x1080) Facebook feed set from the 4:5 social slides (Denise Oct 22 2026: FB carousels square). Buyer tips Oct 31 2026 (title and survey).
import os,re,subprocess,zipfile
from PIL import Image
B=os.path.dirname(os.path.abspath(__file__)); D=os.path.dirname(B); O=D+"/slides-1x1"; os.makedirs(O,exist_ok=True)
SQ=("<style>html,body,.s{width:1080px!important;height:1080px!important}.ph{width:1080px!important;height:1080px!important}"
    ".tag{top:34px!important;left:40px!important;font-size:26px!important;padding:10px 20px!important}"
    ".c{top:auto!important;bottom:84px!important;left:52px!important;right:52px!important}"
    ".s h1{font-size:H1PXpx!important}.s ul{margin-top:14px!important}.s li{font-size:LIPXpx!important;line-height:1.24!important;margin-bottom:9px!important;padding-left:36px!important}"
    ".s li:before{top:10px!important;width:16px!important;height:16px!important}.s p.b{font-size:28px!important;margin-top:12px!important}"
    ".ft{bottom:30px!important;left:52px!important;right:52px!important;font-size:24px!important}"
    ".s .band{font-size:44px!important;padding:10px 22px!important;margin-bottom:12px!important}"
    ".s .cbox{font-size:25px!important;padding:16px 26px 16px 20px!important;margin-top:12px!important}"
    ".ph:after{background:linear-gradient(rgba(0,0,0,.3) 0,rgba(0,0,0,0) 14%,rgba(0,0,0,0) 30%,rgba(0,0,0,.6) 50%,rgba(0,0,0,.9) 100%)!important}"
    "</style>")
ST=("<style>.s .c{top:auto!important;bottom:92px!important}.s .lab{font-size:28px!important;margin-bottom:8px!important}.s .row{padding:13px 28px!important;margin-top:11px!important}"
    ".s .row .z{font-size:28px!important;width:420px!important}.s .row .v{font-size:60px!important}.s .row .y{font-size:30px!important}"
    ".s .tk{font-size:30px!important;margin-top:20px!important}.s .src{font-size:24px!important;margin-top:10px!important}"
    ".ph:after{background:linear-gradient(rgba(0,0,0,.4) 0,rgba(0,0,0,.6) 25%,rgba(0,0,0,.85) 60%,rgba(0,0,0,.92) 100%)!important}</style>")
# Lighter 1:1 fade (photo brightness 1.1, softer gradient, stronger text shadow) on every photo slide so the square set stays bright (LT below).
LITE=("<style>.ph{filter:brightness(1.1) saturate(1.04)}"
      ".ph:after{background:linear-gradient(rgba(0,0,0,.18) 0,rgba(0,0,0,0) 10%,rgba(0,0,0,0) 42%,rgba(0,0,0,.42) 60%,rgba(0,0,0,.8) 100%)!important}"
      "h1,li,.ft{text-shadow:0 2px 12px rgba(0,0,0,.85),0 0 3px rgba(0,0,0,.6)!important}</style>")
H1={1:68,2:78,4:64,5:60,6:58,7:68,8:64,9:64,10:60}; LI={3:26,4:26,5:26,6:26,7:26,8:26,9:26}; LT=(1,3,4,5,6,7,8,9,10)
for i in range(1,11):
    h=open(f"{B}/slide-{i:02d}.html").read()
    css=SQ.replace("H1PX",str(H1.get(i,70))).replace("LIPX",str(LI.get(i,28)))+(ST if i==2 else "")+(LITE if i in LT else "")
    h=h.replace("</head>",css+"</head>",1)
    if i==10: h=h.replace("</div></div><div class='ft'>","</div></div><div class='ft'>")  # keep contact block
    hp=f"{B}/slide-{i:02d}-1x1.html"; open(hp,"w").write(h)
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
      "--window-size=1080,1080",f"--screenshot={O}/slide-{i:02d}.png","--allow-file-access-from-files",f"file://{hp}"],check=True,capture_output=True)
    assert Image.open(f"{O}/slide-{i:02d}.png").size==(1080,1080)
with zipfile.ZipFile(D+"/slides-1x1.zip","w") as z:
    for i in range(1,11): z.write(f"{O}/slide-{i:02d}.png",f"slide-{i:02d}-1x1.png")
print("ok")
