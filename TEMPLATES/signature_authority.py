"""Signature Authority renderer: Denise's "Buyer & Seller Tips — Signature Authority" design (template sheet received Oct 31 2026,
reference image TEMPLATES/signature-authority-template.png, spec TEMPLATES/SIGNATURE_AUTHORITY.md).

Usage (from a carousel's build/build_slides.py):
    import sys; sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
    import signature_authority as sa
    SL = [sa.cover(...), sa.stats(...), sa.edu(...), ..., sa.cta(...)]   # 10 slide dicts
    sa.build(SL, carousel_dir, build_dir, pdf_name, series="buyer")       # 4:5 + 1:1 (+ 9:16 if formats includes "9x16")

Outputs: slide-NN.png 1080x1350 (4:5, IG + LinkedIn) + PDF + slides.zip; slides-1x1/slide-NN.png 1080x1080 (Facebook) + slides-1x1.zip;
optional slides-9x16/slide-NN.png 1080x1920 (TikTok, only when Denise asks for it) + slides-9x16.zip.
Headline markup: [[words]] -> coral highlight. Photos: full-bleed, graded and cropped per format from build/src originals.
"""
import os, html, subprocess, zipfile
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
Image.MAX_IMAGE_PIXELS = None

NAVY, TEAL, CORAL, WHITE, CHAR = "#0E3042", "#9BB7AE", "#E38B6C", "#F5F3EE", "17,33,42"   # CHAR = #11212A as rgb
GF = "/usr/share/fonts/truetype/sand-box/google"
FONTS = (f"@font-face{{font-family:Bebas;src:url('file://{GF}/Bebas Neue/BebasNeue-Regular.ttf')}}"
         f"@font-face{{font-family:Mont;src:url('file://{GF}/Montserrat/Montserrat-VariableFont_wght.ttf');font-weight:100 900}}"
         f"@font-face{{font-family:Script;src:url('file://{GF}/Great Vibes/GreatVibes-Regular.ttf')}}")
CHECK = (f"<svg viewBox='0 0 24 24' class='ck'><circle cx='12' cy='12' r='12' fill='{CORAL}'/>"
         "<path d='M6.6 12.4l3.6 3.5 7.2-7.6' fill='none' stroke='#fff' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/></svg>")
EHO_ICON = ("<svg viewBox='0 0 40 40' class='eho'><path d='M20 3L2 17h5v20h26V17h5z' fill='none' stroke='currentColor' stroke-width='3'/>"
            "<rect x='12' y='19' width='16' height='3.6' fill='currentColor'/><rect x='12' y='26' width='16' height='3.6' fill='currentColor'/></svg>")
PHONE_ICON = (f"<svg viewBox='0 0 24 24' class='ic'><circle cx='12' cy='12' r='12' fill='{NAVY}'/><path d='M8.2 6.5l2 .1 1 2.6-1.3 1.1a8 8 0 0 0 3.8 3.8l1.1-1.3 2.6 1 .1 2a1.6 1.6 0 0 1-1.8 1.6A10.6 10.6 0 0 1 6.6 8.3a1.6 1.6 0 0 1 1.6-1.8z' fill='#fff'/></svg>")
WEB_ICON = (f"<svg viewBox='0 0 24 24' class='ic'><circle cx='12' cy='12' r='12' fill='{NAVY}'/><g fill='none' stroke='#fff' stroke-width='1.4'>"
            "<circle cx='12' cy='12' r='6'/><ellipse cx='12' cy='12' rx='2.6' ry='6'/><path d='M6 12h12'/></g></svg>")

# Per-format geometry. Safe margins ~120px (4:5); 9:16 keeps TikTok UI zones clear (top 150, bottom 250, right 120).
FMT = {
 "4x5":  dict(W=1080, H=1350, L=110, R=110, T=110, B=110, h1=118, body=34, li=33, tag=27, foot=25, cover=150, script=168, gap=1.0),
 "1x1":  dict(W=1080, H=1080, L=96,  R=96,  T=84,  B=84,  h1=98,  body=29, li=28, tag=24, foot=23, cover=124, script=138, gap=.72),
 "9x16": dict(W=1080, H=1920, L=100, R=140, T=170, B=262, h1=140, body=40, li=39, tag=30, foot=27, cover=168, script=190, gap=1.4),
}

def hl(s):
    s = html.escape(s, quote=False)
    return s.replace("[[", "<span class='hi'>").replace("]]", "</span>").replace("|", "<br>")

def grade(im, lift=1.0, sat=1.0):
    """Bright, warm, clean grade (never dark): mild autocontrast, slight warmth, +5% contrast, sharpen; optional gamma lift."""
    im = Image.blend(im, ImageOps.autocontrast(im, cutoff=0.3), 0.35)
    R, G, B = im.split(); R = R.point(lambda v: min(255, int(v*1.012+1))); B = B.point(lambda v: int(v*0.988)); im = Image.merge("RGB", (R, G, B))
    im = ImageEnhance.Contrast(im).enhance(1.05)
    if lift != 1.0: im = im.point(lambda v: int(255*(v/255)**(1/lift)))
    if sat != 1.0: im = ImageEnhance.Color(im).enhance(sat)
    return im.filter(ImageFilter.UnsharpMask(1.0, 70, 2))

def crop(src, W, H, x=.5, y=.5, pre=None):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if pre: im = im.crop(pre)
    r = max(W/im.width, H/im.height); assert r <= 1.02, (src, im.size, W, H)   # downscale only (<=2% tolerance)
    im = im.resize((round(im.width*r), round(im.height*r)), Image.LANCZOS)
    l = int((im.width-W)*x); t = int((im.height-H)*y); return im.crop((l, t, l+W, t+H))

CSS = """*{margin:0;padding:0;box-sizing:border-box}html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden;background:%(NAVY)s}
.s{position:relative;width:%(W)dpx;height:%(H)dpx;overflow:hidden;font-family:Mont;color:#fff}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.ov{position:absolute;inset:0;background:%(OV)s}
.fs{position:absolute;left:0;right:0;bottom:0;height:%(FS)dpx;background:linear-gradient(180deg,rgba(17,33,42,0) 0,rgba(17,33,42,.42) 50%%,rgba(17,33,42,.6) 100%%)}
.tag{position:absolute;left:%(L)dpx;top:%(T)dpx;background:%(TAGBG)s;color:%(NAVY)s;font-weight:600;letter-spacing:.14em;font-size:%(tag)dpx;
 padding:.5em 1.05em .46em;border-radius:6px;text-transform:uppercase}
.c{position:absolute;left:%(L)dpx;right:%(R)dpx;top:%(CT)dpx;z-index:1}
.c.scrim:before{content:'';position:absolute;z-index:-1;left:-%(L)dpx;right:-%(R)dpx;top:-%(SCT)dpx;bottom:-170px;background:linear-gradient(180deg,rgba(17,33,42,.66) 0,rgba(17,33,42,.60) calc(100%% - 230px),rgba(17,33,42,.26) calc(100%% - 110px),rgba(17,33,42,0) 100%%)}
.tag,.ft{z-index:2}
h1{font-family:Bebas;font-weight:400;font-size:%(h1)dpx;line-height:.94;letter-spacing:.012em;text-transform:uppercase;text-shadow:0 2px 18px rgba(0,0,0,.35)}
.hi{color:%(CORAL)s}
p.b{font-size:%(body)dpx;line-height:1.38;margin-top:%(g1)dpx;max-width:30em;text-shadow:0 1px 10px rgba(0,0,0,.45)}
ul{list-style:none;margin-top:%(g2)dpx}
li{display:flex;align-items:flex-start;font-weight:500;font-size:%(li)dpx;line-height:1.3;margin-bottom:%(g3)dpx;text-shadow:0 1px 10px rgba(0,0,0,.45)}
.ck{flex:0 0 auto;width:1.15em;height:1.15em;margin:.08em .62em 0 0}
.ft{position:absolute;left:%(L)dpx;right:%(R)dpx;bottom:%(B)dpx;display:flex;justify-content:space-between;align-items:center;
 font-weight:600;font-size:%(foot)dpx;letter-spacing:.16em;color:#fff;padding-top:18px;text-shadow:0 1px 3px rgba(17,33,42,.9),0 0 14px rgba(17,33,42,.85);border-top:2px solid rgba(155,183,174,.55)}
.ft .pg{letter-spacing:.06em}.ft .pg b{color:%(CORAL)s;font-weight:700;font-size:1.45em;line-height:0;vertical-align:-.06em;margin-left:.15em}
.src{font-size:%(src)dpx;line-height:1.35;opacity:.92;margin-top:%(g2)dpx}
"""

def page(fmt, inner, ov, extra="", tagbg=TEAL):
    f = dict(FMT[fmt]); W, H = f["W"], f["H"]
    f.update(NAVY=NAVY, CORAL=CORAL, OV=ov, TAGBG=tagbg, CT=f["T"]+int(f["tag"]*3.6), FS=f["B"]+150, SCT=f["T"]+int(f["tag"]*3.6), g1=int(26*f["gap"]), g2=int(34*f["gap"]),
             g3=int(20*f["gap"]), src=int(f["body"]*.72))
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{CSS % f}{extra}</style></head>"
            f"<body><div class='s'>{inner}</div></body></html>")

def overlay(fmt, kind):
    """Charcoal #11212A at 60-80% where text sits, lighter over the open photo so it stays bright; footer zone re-darkened."""
    c = CHAR
    if kind == "flat":   return f"rgba({c},.80)"
    if kind == "cover":  return (f"linear-gradient(90deg,rgba({c},.60) 0,rgba({c},.40) 48%,rgba({c},0) 80%),"
                                 f"linear-gradient(180deg,rgba({c},.06) 0,rgba({c},0) 60%,rgba({c},.40) 100%)")
    return f"rgba({c},.04)"   # edu / cta: light wash only; the charcoal scrim (60-66%) sits behind the text block (.c.scrim)

def bullets(items): return "<ul>" + "".join(f"<li>{CHECK}<span>{html.escape(i, quote=False)}</span></li>" for i in items) + "</ul>"
def footer(n, total, series): return (f"<div class='ft'><span>BUYER &amp; SELLER TIPS</span><span class='pg'>{n} / {total} <b>→</b></span></div>")

# ---- slide constructors (return dicts; rendered per format in build) ----
def cover(photo, lead, script, sub, kicker="", **k):   return dict(kind="cover", photo=photo, lead=lead, script=script, sub=sub, kicker=kicker, **k)
def edu(photo, head, body, items, **k):                 return dict(kind="edu", photo=photo, head=head, body=body, items=items, **k)
def stats(photo, head, rows, takeaway, source, **k):    return dict(kind="stats", photo=photo, head=head, rows=rows, takeaway=takeaway, source=source, **k)
def cta(photo, head, sub, body, contact, **k):          return dict(kind="cta", photo=photo, head=head, sub=sub, body=body, contact=contact, **k)

def inner(sd, fmt, n, total, series, imgurl):
    f = FMT[fmt]; tag = sd.get("tag", "BUYER TIP" if series == "buyer" else "SELLER TIP")
    tagbg = TEAL if series == "buyer" else CORAL
    ph = f"<div class='ph' style=\"background-image:url('{imgurl}')\"></div>"
    k = sd["kind"]; extra = ""
    if k == "cover":
        body = (f"<div class='lead'>{hl(sd['lead'])}</div><div class='scr'>{html.escape(sd['script'])}</div>"
                f"<div class='sub'>{sd['sub']}</div>" + (f"<div class='kick'>{html.escape(sd['kicker'])}</div>" if sd['kicker'] else ""))
        top = {"4x5": 330, "1x1": 240, "9x16": 470}[fmt]
        extra = (f".c{{top:{top}px}}.lead{{font-family:Bebas;font-size:{f['cover']}px;line-height:.9;letter-spacing:.01em;text-shadow:0 2px 18px rgba(0,0,0,.35)}}"
                 f".scr{{font-family:Script;color:{CORAL};font-size:{f['script']}px;line-height:1;margin:-.06em 0 0 .04em;text-shadow:0 2px 16px rgba(0,0,0,.35)}}"
                 f".sub{{font-size:{int(f['body']*1.12)}px;margin-top:{int(30*f['gap'])}px;line-height:1.3}}.sub b{{font-weight:800;color:{TEAL};letter-spacing:.06em}}"
                 f".kick{{display:inline-block;margin-top:{int(30*f['gap'])}px;font-weight:600;letter-spacing:.14em;font-size:{f['tag']}px;"
                 f"padding:.55em 1em;border:2px solid {CORAL};border-radius:6px}}")
        ov = overlay(fmt, "cover")
    elif k == "edu":
        body = f"<h1>{hl(sd['head'])}</h1><p class='b'>{html.escape(sd['body'], quote=False)}</p>{bullets(sd['items'])}"
        ov = overlay(fmt, "edu")
        if sd.get("h1"): extra = f"h1{{font-size:{int(f['h1']*sd['h1'])}px}}"
    elif k == "stats":
        rows = "".join(f"<div class='row'><span class='z'>{z}</span><span class='v'>{v}</span><span class='y'>{y}</span></div>" for z, v, y in sd["rows"])
        body = (f"<h1>{hl(sd['head'])}</h1><div class='rows'>{rows}</div><p class='b tk'>{html.escape(sd['takeaway'], quote=False)}</p>"
                f"<p class='src'>{html.escape(sd['source'], quote=False)}</p>")
        rp = {"4x5": (24, 66, 13), "1x1": (14, 50, 9), "9x16": (32, 74, 18)}[fmt]
        extra = (f".rows{{margin-top:{int(30*f['gap'])}px}}.row{{display:flex;align-items:center;background:rgba(14,48,66,.82);border-left:6px solid {TEAL};"
                 f"border-radius:8px;padding:{rp[0]}px 28px;margin-bottom:{rp[2]}px}}"
                 f".row .z{{flex:0 0 40%;font-weight:600;letter-spacing:.1em;font-size:{int(f['li']*.8)}px;line-height:1.2}}"
                 f".row .v{{flex:1;font-family:Bebas;font-size:{rp[1]}px;line-height:1}}.row .y{{font-weight:600;font-size:{int(f['li']*.86)}px;color:{CORAL}}}"
                 f".tk{{margin-top:{int(22*f['gap'])}px}}")
        ov = overlay(fmt, "flat")
    else:  # cta
        c = sd["contact"]
        card = (f"<div class='card'><div class='nm'>{html.escape(c['name'])}</div><div class='ti'>{html.escape(c['title'])}</div>"
                f"<div class='fm'>{html.escape(c['firm'])}</div>"
                f"<div class='ln'>{PHONE_ICON}<span>{html.escape(c['phone'])}</span></div>"
                f"<div class='ln'>{WEB_ICON}<span>{html.escape(c['web'])}</span></div>"
                f"<div class='eq'>{EHO_ICON}<span>Equal Housing Opportunity</span></div></div>")
        body = (f"<h1>{hl(sd['head'])}</h1><div class='sb'>{html.escape(sd['sub'])}</div>"
                f"<p class='b'>{html.escape(sd['body'], quote=False)}</p>{card}")
        g = f["gap"]
        extra = (f".sb{{margin-top:{int(14*g)}px;font-weight:600;letter-spacing:.14em;font-size:{f['tag']+2}px;color:{TEAL};text-transform:uppercase}}"
                 f".card{{margin-top:{int(30*g)}px;background:rgba(245,243,238,.96);color:{NAVY};border-radius:14px;padding:{int(30*g)}px 40px {int(28*g)}px;"
                 f"border-top:8px solid {CORAL};max-width:{ {'4x5':760,'1x1':720,'9x16':800}[fmt] }px;box-shadow:0 10px 40px rgba(0,0,0,.28)}}"
                 f".nm{{font-family:Script;color:{CORAL};font-size:{int(f['h1']*.66)}px;line-height:1.05;word-spacing:.22em}}"
                 f".ti{{font-weight:700;letter-spacing:.12em;font-size:{int(f['li']*.82)}px;margin-top:4px}}"
                 f".fm{{font-weight:500;font-size:{int(f['li']*.84)}px;margin:6px 0 {int(16*g)}px}}"
                 f".ln{{display:flex;align-items:center;font-weight:600;font-size:{int(f['li']*.92)}px;margin-top:{int(10*g)}px}}"
                 f".ic{{width:1.25em;height:1.25em;margin-right:.6em}}"
                 f".eq{{display:flex;align-items:center;font-weight:600;letter-spacing:.06em;font-size:{int(f['li']*.66)}px;margin-top:{int(18*g)}px;"
                 f"padding-top:{int(14*g)}px;border-top:1px solid rgba(14,48,66,.25)}}.eho{{width:1.9em;height:1.9em;margin-right:.6em}}")
        ov = overlay(fmt, "edu")
    html_inner = ph + f"<div class='ov'></div><div class='fs'></div><div class='tag'>{html.escape(tag)}</div><div class='c{" scrim" if k in ("edu","cta") else ""}'>{body}</div>" + footer(n, total, series)
    return html_inner, ov, extra, tagbg

def render(html_path, png, W, H):
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--screenshot={png}", "--allow-file-access-from-files", "--virtual-time-budget=4000",
                    f"file://{html_path}"], check=True, capture_output=True)
    assert Image.open(png).size == (W, H), png

def build(SL, D, B, pdf_name, series="buyer", formats=("4x5", "1x1")):
    total = len(SL); out = {}
    for fmt in formats:
        f = FMT[fmt]; W, H = f["W"], f["H"]
        hdir = B if fmt == "4x5" else (B if fmt == "1x1" else os.path.join(B, "9x16"))
        idir = os.path.join(B, "img") if fmt == "4x5" else os.path.join(B, "img", fmt)
        odir = D if fmt == "4x5" else os.path.join(D, "slides-" + fmt)
        for d in (hdir, idir, odir): os.makedirs(d, exist_ok=True)
        pngs = []
        for n, sd in enumerate(SL, 1):
            img = os.path.join(idir, f"{n:02d}.jpg")
            fx, fy = sd.get("focus", {}).get(fmt, sd.get("xy", (.5, .5)))
            grade(crop(os.path.join(B, "src", sd["photo"]), W, H, fx, fy, sd.get("pre")), sd.get("lift", 1.0), sd.get("sat", 1.0)).save(img, quality=92)
            hi, ov, extra, tagbg = inner(sd, fmt, n, total, series, "file://" + img)
            h = page(fmt, hi, ov, extra + sd.get("css", {}).get(fmt, ""), tagbg)
            hp = os.path.join(hdir, f"slide-{n:02d}" + ("-1x1" if fmt == "1x1" else "") + ".html"); open(hp, "w").write(h)
            png = os.path.join(odir, f"slide-{n:02d}.png"); render(hp, png, W, H); pngs.append(png)
        zname = {"4x5": "slides.zip", "1x1": "slides-1x1.zip", "9x16": "slides-9x16.zip"}[fmt]
        suf = {"4x5": "", "1x1": "-1x1", "9x16": "-9x16"}[fmt]
        with zipfile.ZipFile(os.path.join(D, zname), "w") as z:
            for i, p in enumerate(pngs, 1): z.write(p, f"slide-{i:02d}{suf}.png")
        out[fmt] = pngs
    ims = [Image.open(p).convert("RGB") for p in out["4x5"]]
    ims[0].save(os.path.join(D, pdf_name), save_all=True, append_images=ims[1:], resolution=150)
    return out
