"""Signature Authority renderer, v2 (Oct 31 2026): matches Denise's example slides in TEMPLATES/signature-authority-examples/
(10 x 4:5 examples + template guide + 1:1 headshot slide). Spec: TEMPLATES/SIGNATURE_AUTHORITY.md.

Look: warm, sunlit lifestyle photo stays vivid; a LEFT navy gradient behind the text fades to the clear photo on the right,
plus a navy fade at the bottom for the footer (no even dark overlay). Anton headline: line 1 white, line 2 coral.
Big Montserrat body, 4 short bullets with big filled check bubbles, sage BUYER TIP / coral SELLER TIP pill top-left,
footer "BUYER & SELLER TIPS" + "N / 10 →".

Usage (from a carousel's build/build_slides.py):
    import sys; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import signature_authority as sa
    SL = [sa.cover(...), sa.stats(...), sa.edu(...)*7, sa.cta(...)]
    sa.build(SL, carousel_dir, build_dir, pdf_name, series="buyer")     # 4:5 1080x1350 only (slide-NN.png, PDF, slides.zip)
1:1 / 9:16 are NOT laid out in v2 yet; add them only after Denise approves the 4:5 design.
"""
import os, html, subprocess, zipfile
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
Image.MAX_IMAGE_PIXELS = None

NAVY, NAVY_RGB, SAGE, CORAL, WHITE = "#0E3042", "14,48,66", "#A9C9B8", "#E38B6C", "#F5F3EE"
W, H = 1080, 1350
L = 58            # left margin (examples sit ~40-60px in)
GF = "/usr/share/fonts/truetype/sand-box/google"
TPL = os.path.dirname(os.path.abspath(__file__))
HEADSHOT = os.path.join(TPL, "denise-wilson-headshot-cutout-hires.png")   # real headshot, background removed (Denise's hi-res portrait sent Oct 31; crop: denise-wilson-headshot-hires-crop.png)
FONTS = (f"@font-face{{font-family:Anton;src:url('file://{GF}/Anton/Anton-Regular.ttf')}}"
         f"@font-face{{font-family:Mont;src:url('file://{GF}/Montserrat/Montserrat-VariableFont_wght.ttf');font-weight:100 900}}"
         f"@font-face{{font-family:Script;src:url('file://{GF}/Great Vibes/GreatVibes-Regular.ttf')}}")

def check(color):
    return (f"<svg viewBox='0 0 40 40' class='ck'><circle cx='20' cy='20' r='20' fill='{color}'/>"
            "<path d='M11 20.5l6 6 12-13' fill='none' stroke='#fff' stroke-width='4.2' stroke-linecap='round' stroke-linejoin='round'/></svg>")
EHO = ("<svg viewBox='0 0 48 46' class='eho'><path d='M24 2L1 20h6v24h34V20h6z' fill='none' stroke='#fff' stroke-width='3.4' stroke-linejoin='round'/>"
       "<rect x='14' y='22' width='20' height='4.4' fill='#fff'/><rect x='14' y='31' width='20' height='4.4' fill='#fff'/></svg>")

def warm(im, bright=1.06, sat=1.12, gold=1.0):
    """Warm, sunlit, vivid grade (never dark): lift, golden balance, +saturation, light sharpen."""
    im = Image.blend(im, ImageOps.autocontrast(im, cutoff=0.4), 0.3)
    R, G, B = im.split()
    R = R.point(lambda v: min(255, int(v*(1+.05*gold)+4*gold))); G = G.point(lambda v: min(255, int(v*(1+.015*gold)+1)))
    B = B.point(lambda v: int(v*(1-.075*gold)))
    im = Image.merge("RGB", (R, G, B))
    im = im.point(lambda v: int(255*(v/255)**(1/bright)))
    im = ImageEnhance.Color(im).enhance(sat); im = ImageEnhance.Contrast(im).enhance(1.04)
    return im.filter(ImageFilter.UnsharpMask(1.0, 60, 2))

def crop(src, w, h, x=.5, y=.5, pre=None):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if pre: im = im.crop(pre)
    r = max(w/im.width, h/im.height); assert r <= 1.02, (src, im.size, w, h)
    im = im.resize((round(im.width*r), round(im.height*r)), Image.LANCZOS)
    l = int((im.width-w)*x); t = int((im.height-h)*y); return im.crop((l, t, l+w, t+h))

def hl(s):   # "line one|line two" -> white line + coral line
    a, _, b = s.partition("|")
    return html.escape(a) + (f"<br><span class='co'>{html.escape(b)}</span>" if b else "")

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{NAVY}}}
.s{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:Mont;color:#fff}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.gl{{position:absolute;inset:0;background:linear-gradient(90deg,rgba({NAVY_RGB},.93) 0,rgba({NAVY_RGB},.84) 30%,rgba({NAVY_RGB},.52) 50%,rgba({NAVY_RGB},.12) 66%,rgba({NAVY_RGB},0) 76%)}}
.gt{{position:absolute;left:0;right:0;top:0;height:170px;background:linear-gradient(180deg,rgba({NAVY_RGB},.38),rgba({NAVY_RGB},0))}}
.gb{{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,rgba({NAVY_RGB},0) 0,rgba({NAVY_RGB},.62) 55%,rgba({NAVY_RGB},.9) 100%)}}
.tag{{position:absolute;left:{L}px;top:46px;color:{NAVY};font-weight:700;font-size:38px;letter-spacing:.02em;padding:10px 22px 9px;border-radius:9px;z-index:3}}
.c{{position:absolute;left:{L}px;top:150px;width:690px;z-index:3}}
h1{{font-family:Anton;font-weight:400;font-size:92px;line-height:1.02;letter-spacing:.004em;text-transform:uppercase;text-shadow:0 3px 18px rgba(0,0,0,.35)}}
.co{{color:{CORAL}}}
p.b{{font-size:33px;line-height:1.3;font-weight:500;margin-top:24px;max-width:600px;text-shadow:0 2px 12px rgba(0,0,0,.4)}}
ul{{list-style:none;margin-top:34px}}
li{{display:flex;align-items:center;font-weight:600;font-size:32px;white-space:nowrap;line-height:1.2;margin-bottom:22px;text-shadow:0 2px 12px rgba(0,0,0,.45)}}
.ck{{flex:0 0 auto;width:52px;height:52px;margin-right:20px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.25))}}
.ft{{position:absolute;left:{L}px;right:{L}px;bottom:46px;display:flex;justify-content:space-between;align-items:flex-end;z-index:3;
 font-weight:600;font-size:23px;letter-spacing:.12em;text-shadow:0 1px 8px rgba(0,0,0,.5)}}
.ft .ln{{display:block;width:46px;height:3px;background:{CORAL};margin-bottom:14px}}
.ft .pg{{letter-spacing:.06em;font-size:25px}}
"""

def foot(n, total, left="BUYER &amp; SELLER TIPS"):
    return f"<div class='ft'><div><span class='ln'></span>{left}</div><div class='pg'>{n} / {total} →</div></div>"

def cover(photo, lead, script, sub_html, **k): return dict(kind="cover", photo=photo, lead=lead, script=script, sub=sub_html, **k)
def edu(photo, head, body, items, **k):         return dict(kind="edu", photo=photo, head=head, body=body, items=items, **k)
def stats(head, rows, takeaway, source, **k):  return dict(kind="stats", head=head, rows=rows, takeaway=takeaway, source=source, **k)
def cta(photo, contact, **k):                   return dict(kind="cta", photo=photo, contact=contact, **k)

def inner(sd, n, total, series, img):
    tagc = SAGE if series == "buyer" else CORAL
    tagtxt = sd.get("tag", "BUYER TIP" if series == "buyer" else "SELLER TIP")
    bub = sd.get("bubble", CORAL)
    ph = f"<div class='ph' style=\"background-image:url('file://{img}')\"></div>" if img else ""
    k = sd["kind"]; extra = sd.get("css", "")
    if k == "edu":
        items = "".join(f"<li>{check(bub)}<span>{html.escape(i)}</span></li>" for i in sd["items"])
        body = (f"<div class='tag' style='background:{tagc}'>{tagtxt}</div><div class='c'><h1>{hl(sd['head'])}</h1>"
                f"<p class='b'>{html.escape(sd['body'])}</p><ul>{items}</ul></div>")
        return ph + "<div class='gl'></div><div class='gt'></div><div class='gb'></div>" + body + foot(n, total), extra
    if k == "cover":
        body = (f"<div class='box'><div class='b1'>BUYER &amp; SELLER TIPS</div><div class='b2'>CHARLOTTE METRO • NC + SC</div></div>"
                f"<div class='c cv'><div class='lead'>{html.escape(sd['lead'])}</div><div class='scr'>{html.escape(sd['script'])}</div>"
                f"<div class='sub'>{sd['sub']}</div></div>"
                f"<div class='ft'><div><div class='dw'>DENISE WILSON</div><div class='dw2'>BROKER/REALTOR® | LIFESTYLE INTERNATIONAL REALTY</div></div>"
                f"<div class='pg'>{n} / {total} →</div></div>")
        extra += (f".box{{position:absolute;left:{L}px;top:50px;background:rgba({NAVY_RGB},.92);border:2px solid rgba(255,255,255,.18);padding:16px 24px 14px;z-index:3;border-radius:4px}}"
                  ".b1{font-family:Anton;font-size:46px;letter-spacing:.03em;line-height:1}.b2{font-weight:600;font-size:19px;letter-spacing:.2em;margin-top:8px;color:#dfe8e4}"
                  ".cv{top:226px;width:900px}.lead{font-family:Anton;font-weight:400;font-size:104px;white-space:nowrap;line-height:1;letter-spacing:.01em;text-shadow:0 3px 16px rgba(0,0,0,.4)}"
                  f".scr{{font-family:Script;color:{CORAL};font-size:176px;line-height:.95;margin:6px 0 0 -6px;text-shadow:0 2px 4px rgba(10,30,42,.75),0 0 22px rgba(14,48,66,.9),0 0 44px rgba(14,48,66,.6)}}"
                  ".sub{font-size:40px;font-weight:500;line-height:1.2;margin-top:26px;text-shadow:0 2px 12px rgba(0,0,0,.45)}"
                  f".sub b{{font-family:Anton;font-weight:400;font-size:66px;color:{SAGE};letter-spacing:.02em}}"
                  f".gl{{background:linear-gradient(90deg,rgba({NAVY_RGB},.80) 0,rgba({NAVY_RGB},.58) 36%,rgba({NAVY_RGB},.16) 60%,rgba({NAVY_RGB},0) 72%)}}"
                  ".dw{font-family:Anton;font-size:34px;letter-spacing:.06em;line-height:1.1}.dw2{font-weight:600;font-size:17px;letter-spacing:.14em;margin-top:6px}")
        return ph + "<div class='gl'></div><div class='gt'></div><div class='gb'></div>" + body, extra
    if k == "stats":
        rows = "".join(f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>" for z, v, y in sd["rows"])
        body = (f"<div class='tag' style='background:{tagc}'>{tagtxt}</div><div class='c st'><h1>{hl(sd['head'])}</h1><div class='rows'>{rows}</div>"
                f"<p class='b'>{html.escape(sd['takeaway'])}</p><p class='src'>{html.escape(sd['source'])}</p></div>")
        extra += (".st{width:964px}.rows{margin-top:36px}"
                  f".row{{display:flex;align-items:center;background:rgba(255,255,255,.06);border-left:7px solid {CORAL};border-radius:10px;padding:22px 30px;margin-bottom:16px}}"
                  ".row .z{flex:0 0 330px;font-weight:700;font-size:25px;letter-spacing:.1em;line-height:1.2;color:#dfe8e4}"
                  ".row .v{flex:1;font-family:Anton;font-size:76px;line-height:1}.row .y{font-weight:700;font-size:28px;color:" + CORAL + "}"
                  ".src{font-size:21px;line-height:1.4;margin-top:22px;color:#c9d6d1}"
                  f".s{{background:radial-gradient(120% 80% at 85% 10%,#174A63 0,{NAVY} 55%,#0A2533 100%)}}")
        return body + foot(n, total), extra
    # cta (slide 10): headshot on the right over a bright, warm, blurred living room
    c = sd["contact"]
    hs = f"<img class='hs' src='file://{sd.get('headshot', HEADSHOT)}'>"
    body = (f"<div class='c ct'><div class='lt'>LET'S TALK</div><div class='lt2'>BUYING OR SELLING?<br>I'M HERE TO HELP.</div></div>"
            f"<div class='card'><div class='nm'>{html.escape(c['name'])}</div><div class='ti'>{html.escape(c['title'])}</div>"
            f"<div class='fm'>{html.escape(c['firm'])}</div><div class='ph2'>{html.escape(c['phone'])}</div><div class='wb'>{html.escape(c['web'])}</div>"
            f"<div class='eq'>{EHO}<span>Equal Housing<br>Opportunity</span></div></div>")
    extra += (".hs{position:absolute;right:-60px;bottom:0;height:1000px;z-index:2;filter:drop-shadow(0 10px 30px rgba(0,0,0,.25))}"
              f".gl{{background:linear-gradient(90deg,rgba({NAVY_RGB},.92) 0,rgba({NAVY_RGB},.78) 36%,rgba({NAVY_RGB},.2) 55%,rgba({NAVY_RGB},0) 66%)}}"
              ".ct{top:70px;width:960px}.lt{font-weight:800;font-size:104px;line-height:1;letter-spacing:.01em;text-shadow:0 3px 16px rgba(0,0,0,.35)}"
              ".lt2{font-weight:500;font-size:44px;line-height:1.18;letter-spacing:.05em;margin-top:14px;text-shadow:0 2px 12px rgba(0,0,0,.4)}"
              f".card{{position:absolute;left:{L}px;top:560px;width:470px;z-index:3;text-shadow:0 2px 10px rgba(0,0,0,.45)}}"
              f".nm{{font-family:Script;color:{CORAL};font-size:92px;line-height:1;margin-left:-4px;word-spacing:.12em;white-space:nowrap}}"
              ".ti{font-weight:700;font-size:34px;margin-top:14px}.fm{font-size:27px;line-height:1.3;margin-top:8px}"
              ".ph2{font-size:32px;font-weight:600;margin-top:18px}.wb{font-size:28px;margin-top:8px}"
              ".eq{display:flex;align-items:center;margin-top:30px;font-size:21px;line-height:1.2;font-weight:600}.eho{width:62px;height:60px;margin-right:16px}")
    return ph + "<div class='gl'></div><div class='gb'></div>" + hs + body + foot(n, total), extra

def page(inner_html, extra):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{CSS}{extra}</style></head>"
            f"<body><div class='s'>{inner_html}</div></body></html>")

def render(hp, png):
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--screenshot={png}", "--allow-file-access-from-files", "--virtual-time-budget=4000",
                    f"file://{hp}"], check=True, capture_output=True)
    assert Image.open(png).size == (W, H), png

def build(SL, D, B, pdf_name, series="buyer"):
    total = len(SL); idir = os.path.join(B, "img"); os.makedirs(idir, exist_ok=True); pngs = []
    for n, sd in enumerate(SL, 1):
        img = None
        if sd.get("photo"):
            img = os.path.join(idir, f"{n:02d}.jpg"); x, y = sd.get("xy", (.5, .5))
            im = warm(crop(os.path.join(B, "src", sd["photo"]), W, H, x, y, sd.get("pre")), **sd.get("grade", {}))
            if sd.get("blur"): im = im.filter(ImageFilter.GaussianBlur(sd["blur"]))
            im.save(img, quality=92)
        hi, extra = inner(sd, n, total, series, img)
        hp = os.path.join(B, f"slide-{n:02d}.html"); open(hp, "w").write(page(hi, extra))
        png = os.path.join(D, f"slide-{n:02d}.png"); render(hp, png); pngs.append(png)
    with zipfile.ZipFile(os.path.join(D, "slides.zip"), "w") as z:
        for i, p in enumerate(pngs, 1): z.write(p, f"slide-{i:02d}.png")
    ims = [Image.open(p).convert("RGB") for p in pngs]
    ims[0].save(os.path.join(D, pdf_name), save_all=True, append_images=ims[1:], resolution=150)
    return pngs
