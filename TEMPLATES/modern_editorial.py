"""Community Spotlight — Modern Charlotte Editorial renderer (Denise Wilson's design, in use from Nov 1 2026).
Design reference: TEMPLATES/community-spotlight-modern-editorial/reference-sheet.png + example-01..08.png. Docs: TEMPLATES/MODERN_EDITORIAL.md.
Applies ONLY to the Neighborhood / Community Spotlight carousel (replaces fullbleed_teal there from Nov 1 2026).
Formats: '4x5' 1080x1350 (IG), '1x1' 1080x1080 (FB Page), '9x16' 1080x1920 (TikTok; text clear of ~150 px top / 350 px bottom / 140 px right),
'9x16v' 1080x1920 video frames for the YouTube Short (key text clear of 250 px top / 420 px bottom / 140 px right, header in the safe zone).

Usage from a day's build script:
    import sys; sys.path.insert(0, '/workspace/repos/lir-carousels/TEMPLATES'); import modern_editorial as me
    me.upscale(raw, up)                                   # Real-ESRGAN x4 (TEMPLATES/tools/esrgan_upscale.py) once per image
    me.prep_photo(up, out_png, fmt, x=.5, y=.5, **grade)  # cover-crop at the focal point, Lanczos to full res, bright crisp grade (lossless PNG)
    me.render(slide, out_png, fmt, n, total=10, photo_png=..., html_dir=...)
slide keys: kind ('cover'|'info'|'stats'|'cta'), pill, h1 ('[o]..[/o]' = terracotta highlight words, '|' = line break), bullets (list of 3),
  cover: discover, name, tagline, intro;  stats: kicker, cards [(label, value)x4], source;  cta: body;
  optional per-format overrides: h1_<fmt>, css_<fmt>, g0 (gradient start, fraction of height), minTop (text block may not rise above this fraction).
Rendering: photo graded at final size (lossless), text/gradient layer rendered at 2x on a transparent page via headless Chrome (CDP),
Lanczos-downscaled and alpha-composited over the photo, so type stays razor sharp. A JS fitter shrinks the headline to <= its max lines and
then the body until the text block clears minTop, so long copy never collides with the pill.
"""
import os, sys, json, time, base64, html as H, subprocess
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
sys.path.insert(0, "/workspace/tools"); import cdp

TEAL, TERRA, IVORY, CHAR, GOLD = "#183C46", "#C66C4E", "#F5F0E8", "#293338", "#D9A84E"
TEAL_RGB = "24,60,70"
SIZES = {"4x5": (1080, 1350), "1x1": (1080, 1080), "9x16": (1080, 1920), "9x16v": (1080, 1920)}
ESRGAN = "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py"
HEADSHOT = "/workspace/repos/lir-carousels/TEMPLATES/denise-wilson-headshot-cutout-hires.png"
FONT_DIR = "/usr/share/fonts/truetype/sand-box/google"
FONTS = (f"@font-face{{font-family:PF;src:url('file://{FONT_DIR}/Playfair Display/PlayfairDisplay-Italic-VariableFont_wght.ttf');font-style:italic;font-weight:400 900}}"
         f"@font-face{{font-family:PF;src:url('file://{FONT_DIR}/Playfair Display/PlayfairDisplay-VariableFont_wght.ttf');font-style:normal;font-weight:400 900}}"
         f"@font-face{{font-family:MS;src:url('file://{FONT_DIR}/Montserrat/Montserrat-VariableFont_wght.ttf');font-style:normal;font-weight:100 900}}")

# Per-format layout (px). m=side margin, top=pill top, r=right clearance for text, fb=footer-bar bottom offset, fh=footer-bar height,
# h1 headline, li body, lbl label, pill, stat value, ft footer text, g0 gradient start (fraction of height), minTop text block limit.
L = {
 "4x5":  dict(m=46, top=40, r=60,  fb=0,   fh=96, h1=100, li=29, pill=28, lbl=26, val=84, ft=25, g0=.40, minTop=.42, name=156, disc=74, tag=46, intro=30, gap=16),
 "1x1":  dict(m=42, top=34, r=56,  fb=0,   fh=86, h1=88,  li=27, pill=26, lbl=24, val=76, ft=23, g0=.30, minTop=.33, name=134, disc=62, tag=40, intro=27, gap=12),
 "9x16": dict(m=56, top=166,r=150, fb=350, fh=96, h1=110, li=33, pill=30, lbl=27, val=88, ft=25, g0=.36, minTop=.40, name=164, disc=80, tag=48, intro=32, gap=18),
 "9x16v":dict(m=56, top=380,r=150, fb=420, fh=96, h1=108, li=32, pill=30, lbl=27, val=88, ft=25, g0=.34, minTop=.42, name=164, disc=80, tag=48, intro=32, gap=18),
}

# ---------------------------------------------------------------- photos
def upscale(raw, out):
    """4x Real-ESRGAN (fp16 ONNX) once; skipped when out already exists."""
    if not os.path.exists(out): subprocess.run([sys.executable, ESRGAN, raw, out], check=True)
    return out

def crisp(im, expo=1.06, shadows=.16, clarity=20, vib=1.14, warmth=.7, sharp=80, contrast=1.04):
    """Bright, crystal-clear golden-hour grade (same pipeline as signature_authority.crisp, gentler defaults for generated images)."""
    im = ImageOps.autocontrast(im, cutoff=(0.4, 0.2))
    a = np.asarray(im).astype(np.float32) / 255.
    a = a ** (1 / expo)
    lum = a.mean(axis=2, keepdims=True)
    a = a + shadows * a * (1 - a) * (1 - lum) ** 2 * 2.2
    a[..., 0] *= 1 + .035 * warmth; a[..., 1] *= 1 + .010 * warmth; a[..., 2] *= 1 - .045 * warmth
    mx, mn = a.max(axis=2, keepdims=True), a.min(axis=2, keepdims=True); sat = mx - mn; g = a.mean(axis=2, keepdims=True)
    a = g + (a - g) * (1 + (vib - 1) * (1 - sat) * 1.6)
    im = Image.fromarray((np.clip(a, 0, 1) * 255 + .5).astype("uint8"))
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = im.filter(ImageFilter.UnsharpMask(40, clarity, 0))
    return im.filter(ImageFilter.UnsharpMask(1.0, sharp, 3))

def prep_photo(src, out, fmt, x=.5, y=.5, **grade):
    W, Hh = SIZES[fmt]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    r = max(W / im.width, Hh / im.height)
    im = im.resize((max(W, round(im.width * r)), max(Hh, round(im.height * r))), Image.LANCZOS)
    l = int((im.width - W) * x); t = int((im.height - Hh) * y); im = im.crop((l, t, l + W, t + Hh))
    crisp(im, **grade).save(out); return r

# ---------------------------------------------------------------- markup
def _h(s):
    s = H.escape(s).replace("|", "<br>").replace("[o]", '<span class="o">').replace("[/o]", "</span>")
    return s.replace("&#x27;", "’").replace("'", "’")

SWOOSH = ('<svg class="sw" viewBox="0 0 600 30" preserveAspectRatio="none"><defs><linearGradient id="g" x1="0" x2="1">'
          f'<stop offset="0" stop-color="{GOLD}"/><stop offset=".55" stop-color="#E9A35C"/><stop offset="1" stop-color="{TERRA}" stop-opacity=".9"/></linearGradient></defs>'
          '<path d="M2 22 C 160 6, 380 2, 598 12 C 380 8, 170 13, 2 26 Z" fill="url(#g)"/></svg>')
PIN = ('<svg class="pin" viewBox="0 0 40 52"><path d="M20 1C9.5 1 1 9.4 1 19.8 1 33.5 20 51 20 51s19-17.5 19-31.2C39 9.4 30.5 1 20 1z" fill="#C66C4E"/>'
       f'<circle cx="20" cy="19.5" r="7.2" fill="{IVORY}"/></svg>')
EHO = ("<svg viewBox='0 0 48 46' class='eho'><path d='M24 2L1 20h6v24h34V20h6z' fill='none' stroke='#F5F0E8' stroke-width='3.4' stroke-linejoin='round'/>"
       "<rect x='14' y='22' width='20' height='4.4' fill='#F5F0E8'/><rect x='14' y='31' width='20' height='4.4' fill='#F5F0E8'/></svg>")

def css(fmt, sl):
    W, Hh = SIZES[fmt]; l = L[fmt]; g0 = sl.get("g0", l["g0"]); fb, fh = l["fb"], l["fh"]
    textbot = fb + fh + (30 if fmt == "1x1" else 40)
    if sl["kind"] == "cover": textbot = fb + (44 if fmt == "1x1" else 56)
    return f"""{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:{W}px;height:{Hh}px;overflow:hidden;background:transparent}}
.s{{position:relative;width:{W}px;height:{Hh}px;overflow:hidden;color:{IVORY};font-family:MS}}
.gr{{position:absolute;left:0;right:0;bottom:0;top:{int(Hh*g0)}px;background:linear-gradient(180deg,rgba({TEAL_RGB},0) 0%,rgba({TEAL_RGB},.50) 16%,
 rgba({TEAL_RGB},.80) 34%,rgba({TEAL_RGB},.92) 58%,rgba({TEAL_RGB},.96) 100%)}}
.gt{{position:absolute;left:0;right:0;top:0;height:{l['top']+150}px;background:linear-gradient(180deg,rgba({TEAL_RGB},.20),rgba({TEAL_RGB},0))}}
.pill{{position:absolute;z-index:5;left:{l['m']-6}px;top:{l['top']}px;background:rgba({TEAL_RGB},.95);border:2px solid {GOLD};border-radius:16px;
 padding:{int(l['pill']*.42)}px {int(l['pill']*.85)}px {int(l['pill']*.38)}px;font-weight:800;font-size:{l['pill']}px;letter-spacing:1.6px;line-height:1.1;
 box-shadow:0 6px 18px rgba(0,0,0,.30)}}
.tx{{position:absolute;z-index:4;left:{l['m']}px;right:{l['r']}px;bottom:{textbot}px}}
h1{{font-family:PF;font-style:italic;font-weight:900;font-size:{l['h1']}px;line-height:1.0;letter-spacing:-.5px;text-transform:uppercase;
 filter:drop-shadow(0 3px 10px rgba(0,0,0,.45))}}
.o{{background:linear-gradient(180deg,#F3A06A 0%,#E08452 45%,{TERRA} 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.sw{{display:block;width:62%;height:{int(l['h1']*.26)}px;margin-top:{int(l['gap']*.5)}px;filter:drop-shadow(0 1px 3px rgba(0,0,0,.3))}}
ul{{list-style:none;margin-top:{l['gap']+6}px}}
li{{display:flex;align-items:flex-start;font-weight:500;font-size:{l['li']}px;line-height:1.3;margin-bottom:{int(l['gap']*.8)}px;text-shadow:0 1px 6px rgba(0,0,0,.35)}}
li:before{{content:"";flex:0 0 auto;width:{int(l['li']*.52)}px;height:{int(l['li']*.52)}px;background:#D97A52;border-radius:2px;margin:{int(l['li']*.38)}px {int(l['li']*.7)}px 0 0;
 box-shadow:0 1px 4px rgba(0,0,0,.3)}}
.ft{{position:absolute;z-index:6;left:0;right:0;bottom:{fb}px;height:{fh}px;background:{TEAL};border-top:2px solid rgba(217,168,78,.55)}}
.ft .l{{position:absolute;left:{l['m']}px;top:0;bottom:0;display:flex;align-items:center;font-weight:800;font-size:{l['ft']}px;letter-spacing:2.4px}}
.ft .p{{position:absolute;right:0;top:0;bottom:0;width:{int(W*.38)}px;background:linear-gradient(90deg,#B95F42,{TERRA} 40%,#CF7652);
 clip-path:polygon({int(fh*.62)}px 0,100% 0,100% 100%,0 100%)}}
.ft .st{{position:absolute;top:0;bottom:0;width:{int(fh*.12)}px;transform:skewX(-32deg);right:{int(W*.38)+8}px}}
.ft .st.a{{background:#E9A35C}}.ft .st.b{{right:{int(W*.38)+30}px;background:{TERRA};opacity:.85}}
.ft .n{{position:absolute;right:{max(l['r'], l['m'])}px;top:0;bottom:0;display:flex;align-items:center;font-weight:800;font-size:{int(l['ft']*1.18)}px;letter-spacing:1.2px}}
"""

def foot(n, total):
    return (f'<div class="ft"><div class="l">NEIGHBORHOOD SPOTLIGHT</div><div class="st b"></div><div class="st a"></div><div class="p"></div>'
            f'<div class="n">{n} / {total}</div></div>')

def inner(sl, fmt, n, total):
    l = L[fmt]; k = sl["kind"]; W, Hh = SIZES[fmt]
    h1 = sl.get(f"h1_{fmt}", sl.get("h1", ""))
    bullets = "".join(f"<li><span>{H.escape(b)}</span></li>" for b in sl.get("bullets", []))
    pill = f'<div class="pill">{H.escape(sl["pill"])}</div>' if sl.get("pill") else ""
    extra = ""
    if k == "info":
        body = f'{pill}<div class="tx" data-lines="{sl.get("lines_"+fmt, sl.get("lines", 2))}"><h1>{_h(h1)}</h1>{SWOOSH}<ul>{bullets}</ul></div>{foot(n, total)}'
    elif k == "cover":
        body = (f'<div class="pill cv">{PIN}<div><div class="c1">COMMUNITY SPOTLIGHT</div><div class="c2">CHARLOTTE METRO • NC + SC</div></div></div>'
                f'<div class="tx" data-lines="1" data-fit="nm"><div class="ds">{H.escape(sl["discover"])}</div><div class="nm">{H.escape(sl["name"])}</div>{SWOOSH}'
                f'<div class="tg"><span class="o">{H.escape(sl["tagline"])}</span></div><div class="in">{H.escape(sl["intro"])}</div>'
                f'<div class="dw">DENISE WILSON</div><div class="dw2">Broker/REALTOR® | LIFESTYLE INTERNATIONAL REALTY</div></div>'
                f'<div class="pg">{n} / {total} →</div>')
        extra = (f".pill.cv{{display:flex;align-items:center;gap:{int(l['pill']*.55)}px;padding:{int(l['pill']*.45)}px {int(l['pill']*.8)}px}}"
                 f".pin{{width:{int(l['pill']*1.35)}px;height:{int(l['pill']*1.75)}px;filter:drop-shadow(0 2px 4px rgba(0,0,0,.3))}}"
                 f".c1{{font-size:{int(l['pill']*1.12)}px;font-weight:800;letter-spacing:1.4px}}.c2{{font-size:{int(l['pill']*.66)}px;font-weight:600;letter-spacing:3px;margin-top:6px;color:#EDE3D3}}"
                 f".ds{{font-family:PF;font-style:italic;font-weight:600;font-size:{l['disc']}px;line-height:1;filter:drop-shadow(0 3px 10px rgba(0,0,0,.45))}}"
                 f".nm{{font-family:PF;font-weight:800;font-size:{l['name']}px;line-height:1.02;white-space:nowrap;letter-spacing:-1px;filter:drop-shadow(0 4px 14px rgba(0,0,0,.45))}}"
                 f".tx .sw{{width:58%;margin-top:{int(l['gap']*.6)}px}}"
                 f".tg{{font-family:PF;font-style:italic;font-weight:700;font-size:{l['tag']}px;line-height:1.15;margin-top:{l['gap']}px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.45))}}"
                 f".in{{font-weight:500;font-size:{l['intro']}px;line-height:1.32;margin-top:{l['gap']}px;max-width:860px;text-shadow:0 1px 6px rgba(0,0,0,.4)}}"
                 f".dw{{font-weight:800;font-size:{int(l['intro']*1.12)}px;letter-spacing:2.4px;margin-top:{int(l['gap']*2)}px}}"
                 f".dw2{{font-weight:600;font-size:{int(l['intro']*.68)}px;letter-spacing:1.6px;margin-top:6px;color:#EDE3D3}}"
                 f".pg{{position:absolute;z-index:5;right:{l['r']}px;bottom:{l['fb'] + (44 if fmt=='1x1' else 56)}px;font-weight:700;font-size:{l['ft']+2}px;letter-spacing:1.5px}}")
    elif k == "stats":
        cards = "".join(f'<div class="cd"><div class="lb">{H.escape(a)}</div><div class="vl">{H.escape(b)}</div></div>' for a, b in sl["cards"])
        body = (f'{pill}<div class="tx" data-lines="{sl.get("lines_"+fmt, 1)}"><div class="kk">{H.escape(sl["kicker"])}</div><h1>{_h(h1)}</h1>{SWOOSH}'
                f'<div class="grid">{cards}</div><div class="src">{H.escape(sl["source"])}</div></div>{foot(n, total)}')
        extra = (f".kk{{font-weight:800;font-size:{int(l['lbl']*1.12)}px;letter-spacing:1.8px;margin-bottom:{int(l['gap']*.6)}px;text-shadow:0 2px 8px rgba(0,0,0,.45)}}"
                 f".grid{{display:grid;grid-template-columns:1fr 1fr;gap:{int(l['gap']*1.3)}px;margin-top:{l['gap']+6}px}}"
                 f".cd{{background:rgba({TEAL_RGB},.74);border:1.5px solid rgba(245,240,232,.30);border-radius:18px;padding:{int(l['lbl']*.85)}px {int(l['lbl']*1.05)}px;box-shadow:0 6px 18px rgba(0,0,0,.22)}}"
                 f".lb{{font-weight:800;font-size:{l['lbl']}px;letter-spacing:1.2px;line-height:1.12;text-transform:uppercase;min-height:{int(l['lbl']*2.24)}px}}"
                 f".vl{{font-weight:800;font-size:{l['val']}px;line-height:1.05;margin-top:{int(l['gap']*.5)}px;letter-spacing:-.5px}}"
                 f".src{{font-weight:500;font-size:{int(l['li']*.8)}px;line-height:1.35;margin-top:{l['gap']}px;color:#EFE8DC;text-shadow:0 1px 6px rgba(0,0,0,.4)}}")
    elif k == "cta":
        hs_h = {"4x5": 660, "1x1": 560, "9x16": 860, "9x16v": 820}[fmt]
        body = (f'{pill}<img class="hs" src="file://{HEADSHOT}">'
                f'<div class="tx" data-lines="2"><h1>{_h(h1)}</h1>{SWOOSH}<div class="bd">{H.escape(sl.get("body_" + fmt, sl["body"]))}</div>'
                f'<div class="card"><div class="c1">Denise Wilson | Broker/REALTOR®</div><div>Lifestyle International Realty — Carolinas</div>'
                f'<div>denisewilson.lircarolinas.com</div><div>704-615-7347</div><div class="eq">{EHO}Equal Housing Opportunity</div></div></div>{foot(n, total)}')
        cw = {"4x5": 650, "1x1": 640, "9x16": 700, "9x16v": 700}[fmt]
        extra = (f".hs{{position:absolute;z-index:5;right:{-40 if fmt!='9x16v' else -60}px;bottom:{l['fb']+l['fh']}px;height:{hs_h}px;filter:drop-shadow(0 8px 24px rgba(0,0,0,.35))}}"
                 f".tx{{z-index:4}}.bd{{font-weight:500;font-size:{l['li']}px;line-height:1.32;margin-top:{l['gap']}px;max-width:{cw+40}px;text-shadow:0 1px 6px rgba(0,0,0,.45)}}"
                 f".card{{margin-top:{l['gap']+8}px;width:{cw}px;background:rgba(16,44,52,.90);border-left:9px solid {GOLD};border-radius:16px;"
                 f"padding:{int(l['li']*.8)}px {int(l['li']*.95)}px;font-weight:500;font-size:{l['li']-3}px;line-height:1.42;white-space:nowrap;overflow:hidden;box-shadow:0 8px 22px rgba(0,0,0,.32)}}"
                 f".card .c1{{font-weight:700;font-size:{l['li']+3}px;margin-bottom:4px}}"
                 f".eq{{display:flex;align-items:center;margin-top:{int(l['li']*1.1)}px;font-weight:600;font-size:{l['li']-5}px}}"
                 f".eho{{width:{int(l['li']*1.25)}px;height:{int(l['li']*1.2)}px;margin-right:12px}}")
        if fmt.startswith("9x16"):   # tall frames: headshot top-right with a soft fade at its base, text stack full width below it
            top, hh = (215, 600) if fmt == "9x16" else (295, 530)
            extra += (f".hs{{top:{top}px;bottom:auto;right:-10px;height:{hh}px;-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent 100%);"
                      f"mask-image:linear-gradient(180deg,#000 70%,transparent 100%)}}.bd{{max-width:none}}")
    else:
        raise ValueError(k)
    if fmt == "9x16v" and k != "cover":   # Short header inside the safe zone (below the 250 px top band); the cover has its own pill
        body += ('<div class="vh"><div class="v1">COMMUNITY SPOTLIGHT</div>'
                 f'<div class="v2">{H.escape(sl.get("place", ""))}</div></div>')
        extra += (f".vh{{position:absolute;z-index:6;left:{l['m']-6}px;top:262px;padding:12px 22px;border-left:6px solid {TERRA};background:rgba({TEAL_RGB},.80);border-radius:0 12px 12px 0}}"
                  ".v1{font-weight:800;font-size:26px;letter-spacing:2.4px}.v2{font-family:PF;font-style:italic;font-weight:700;font-size:32px;margin-top:2px}")
    return body, extra

FIT_JS = """
(()=>{const tx=document.querySelector('.tx'); if(!tx) return true;
 const Hh=document.body.clientHeight, minTop=%MINTOP%*Hh;
 const lines=+tx.dataset.lines||2;
 const nm=tx.querySelector('.nm'); if(nm){let f=parseFloat(getComputedStyle(nm).fontSize); while(nm.scrollWidth>tx.clientWidth+1 && f>60){f-=2; nm.style.fontSize=f+'px';}}
 const h=tx.querySelector('h1');
 if(h){let f=parseFloat(getComputedStyle(h).fontSize);
   while(h.getBoundingClientRect().height>lines*f*1.0*1.08 && f>48){f-=2;h.style.fontSize=f+'px';}}
 const body=[...tx.querySelectorAll('li,.bd,.in,.card,.card .c1,.eq,.src')];
 let guard=0; while(tx.getBoundingClientRect().top<minTop && guard<14){guard++;
   body.forEach(e=>{const f=parseFloat(getComputedStyle(e).fontSize); e.style.fontSize=(f-1)+'px';});
   if(h && guard%3==0){const f=parseFloat(getComputedStyle(h).fontSize); h.style.fontSize=(f-3)+'px';}}
 const card=tx.querySelector('.card'), hs=document.querySelector('.hs');
 if(card){const hr=hs?hs.getBoundingClientRect():null, cr=card.getBoundingClientRect(); const lim=(hr && hr.bottom-hr.height*.2>cr.top)? hr.left+hr.width*.18 : 1e9; let g=0;
   const over=()=>{const kids=[...card.children]; return kids.some(k=>k.scrollWidth>card.clientWidth-parseFloat(getComputedStyle(card).paddingLeft)*2+1 || k.getBoundingClientRect().left+k.scrollWidth>lim);};
   while(over() && g<20){g++; [card,...card.querySelectorAll('.c1,.eq')].forEach(e=>{const f=parseFloat(getComputedStyle(e).fontSize); e.style.fontSize=(f-1)+'px';});}}
 const r=tx.getBoundingClientRect(); window.__fit={top:r.top,bottom:r.bottom,right:r.right,guard:guard,h1:h?parseFloat(h.style.fontSize||getComputedStyle(h).fontSize):0};
 return true;})()
"""

def page(sl, fmt, n, total):
    body, extra = inner(sl, fmt, n, total)
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css(fmt, sl)}{extra}{sl.get("css_" + fmt, "")}</style></head>'
            f'<body><div class="s"><div class="gt"></div><div class="gr"></div>{body}</div></body></html>')

def shot2x(hp, out, w, h, mintop):
    """Transparent 2x screenshot of the text/gradient layer; returns the fitter's measurements."""
    t = cdp.Tab(); t.call("Page.enable")
    t.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=2, mobile=False)
    t.call("Emulation.setDefaultBackgroundColorOverride", color={"r": 0, "g": 0, "b": 0, "a": 0})
    t.call("Page.navigate", url="file://" + os.path.abspath(hp))
    for _ in range(100):
        if t.ev("document.readyState") == "complete": break
        time.sleep(.1)
    t.ev("document.fonts.ready.then(()=>Promise.all([...document.images].map(i=>i.decode().catch(()=>0))))")
    t.ev(FIT_JS.replace("%MINTOP%", str(mintop)))
    m = t.ev("JSON.stringify(window.__fit||{})"); time.sleep(.2)
    d = t.call("Page.captureScreenshot", format="png", clip={"x": 0, "y": 0, "width": w, "height": h, "scale": 1}, captureBeyondViewport=False)
    open(out, "wb").write(base64.b64decode(d["data"])); t.close()
    return json.loads(m or "{}")

def render(sl, out_png, fmt, n, total=10, photo_png=None, html_dir=None):
    W, Hh = SIZES[fmt]; l = L[fmt]
    hd = html_dir or os.path.dirname(out_png); os.makedirs(hd, exist_ok=True)
    hp = os.path.join(hd, f"{fmt}-slide-{n:02d}.html"); open(hp, "w").write(page(sl, fmt, n, total))
    lay = out_png + ".layer.png"
    fit = shot2x(hp, lay, W, Hh, sl.get("minTop_" + fmt, sl.get("minTop", l["minTop"])))
    L2 = Image.open(lay).convert("RGBA")
    if L2.size != (W, Hh): L2 = L2.convert("RGBa").resize((W, Hh), Image.LANCZOS).convert("RGBA")
    os.remove(lay)
    base = Image.open(photo_png).convert("RGBA") if photo_png else Image.new("RGBA", (W, Hh), TEAL)
    assert base.size == (W, Hh), (photo_png, base.size)
    base.alpha_composite(L2); base.convert("RGB").save(out_png)
    return fit
