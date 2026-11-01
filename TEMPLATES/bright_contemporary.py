"""New Construction — Bright Contemporary renderer (Denise Wilson, approved design Oct 31 2026).
Design reference: TEMPLATES/new-construction-bright-contemporary/reference-sheet.png + example-01..10.png. Docs: TEMPLATES/BRIGHT_CONTEMPORARY.md.
Applies ONLY to the New Construction carousel. Three native layouts: '4x5' 1080x1350 (IG), '1x1' 1080x1080 (FB), '9x16' 1080x1920 (TikTok,
text kept clear of ~150 px top / 350 px bottom / 140 px right).
Usage from a day's build script:
    import sys; sys.path.insert(0, '/workspace/repos/lir-carousels/TEMPLATES'); import bright_contemporary as bc
    bc.prep_photo(src, out_jpg, fmt, fx=.5, fy=.5)          # cover-crop + bright grade (+ ESRGAN when the source is small)
    bc.render(slide_dict, photo_jpg, out_png, fmt, n, total=10)
slide_dict keys: kind ('cover'|'deal'|'tip'|'cta'), credit, pill, h1 (use [y]..[/y] for golden-yellow words), sub, bullets (list), note.
"""
import os, sys, html as H, subprocess
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
sys.path.insert(0, "/workspace/tools"); import cdp
NAVY, TEAL, YEL, WHITE, CHAR, CORAL = "#0B2E3A", "#0E7C8A", "#FFD200", "#FFFFFF", "#1B2A30", "#F0503C"
SIZES = {"4x5": (1080, 1350), "1x1": (1080, 1080), "9x16": (1080, 1920)}
# per-format layout: top/side/right/bottom paddings, font sizes, where the gradient starts (fraction of height)
L = {
 "4x5": dict(top=34, side=40, right=40, bot=34, tag=30, cr=22, pill=29, h1=104, h1c=92, sub=31, li=26, chk=34, note=20, ft=26, g0=.36, gap=12),
 "1x1": dict(top=26, side=34, right=34, bot=26, tag=27, cr=20, pill=25, h1=86, h1c=74, sub=27, li=23, chk=30, note=18, ft=23, g0=.30, gap=8),
 "9x16":dict(top=160, side=48, right=150, bot=360, tag=32, cr=23, pill=30, h1=108, h1c=92, sub=32, li=28, chk=36, note=21, ft=27, g0=.36, gap=14),
}
ESRGAN = "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py"

PH = {"4x5": .80, "1x1": .92, "9x16": .62}   # photo zone height (fraction of frame); below it the slide is navy under the text gradient

def prep_photo(src, out, fmt, fx=.5, fy=.5, esrgan_over=1.5, grade=1.0, ph=None):
    """Cover-crop a builder photo natively into the upper photo zone of the frame and grade it bright, saturated and crisp (no halos).
    The photo zone (PH) keeps landscape builder photos from being over-zoomed; its bottom edge fades into Deep Navy under the text.
    Never alters the home itself."""
    W, Hfull = SIZES[fmt]; ph = ph or PH[fmt]; Hh = int(Hfull * ph)
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    r = max(W / im.width, Hh / im.height)
    if r > esrgan_over:   # small source: 4x Real-ESRGAN first, then downscale (crisper than Lanczos upscaling)
        tmp = out + ".x4.jpg"
        if not os.path.exists(tmp): subprocess.run([sys.executable, ESRGAN, src, tmp], check=True)
        im = Image.open(tmp).convert("RGB"); r = max(W / im.width, Hh / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l = int((im.width - W) * fx); t = int((im.height - Hh) * fy); im = im.crop((l, t, l + W, t + Hh))
    im = Image.blend(im, ImageOps.autocontrast(im, cutoff=0.4), 0.5)
    im = ImageEnhance.Brightness(im).enhance(1 + .04 * grade)
    im = ImageEnhance.Contrast(im).enhance(1 + .07 * grade)
    im = ImageEnhance.Color(im).enhance(1 + .20 * grade)
    im = im.filter(ImageFilter.UnsharpMask(1.1, 70 if r < 1.2 else 95, 3))   # small radius = sharp without halos
    if Hh < Hfull:
        canvas = Image.new("RGB", (W, Hfull), NAVY); canvas.paste(im, (0, 0))
        fade = min(160, Hh // 5); navy = Image.new("RGB", (W, fade), NAVY)
        mask = Image.linear_gradient("L").resize((W, fade))
        canvas.paste(Image.composite(navy, im.crop((0, Hh - fade, W, Hh)), mask), (0, Hh - fade)); im = canvas
    im.save(out, quality=95); return r

CHECK = ('<svg viewBox="0 0 40 40" width="{s}" height="{s}"><circle cx="20" cy="20" r="19" fill="#FFD200"/>'
         '<path d="M11 20.5l6 6 12-13" fill="none" stroke="#0B2E3A" stroke-width="4.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def _h1(s):
    s = H.escape(s).replace("|", "<br>").replace("[y]", '<span class="y">').replace("[/y]", "</span>")
    return s

def _stripes(W, Hh, fmt):
    # decorative diagonal coral/orange, yellow and teal accents in the top-left and bottom-right corners (as in Denise's examples)
    k = 1.0 if fmt != "1x1" else .85
    tl = (f'<div class="st" style="left:-120px;top:-10px;width:{int(300*k)}px;height:54px;background:linear-gradient(90deg,#F0503C,#FF8A2A);transform:rotate(-50deg)"></div>'
          f'<div class="st" style="left:-130px;top:62px;width:{int(260*k)}px;height:24px;background:linear-gradient(90deg,#FFB21E,#FFD200);transform:rotate(-50deg)"></div>')
    br = ""
    specs = [(TEAL, 46, 0, "#1FB5C4"), ("#F0503C", 40, 56, "#FF8A2A"), ("#FFB21E", 34, 104, "#FFD200"), ("#2BC3D0", 18, 150, "#0E7C8A")]
    for c1, h, off, c2 in specs:
        br += (f'<div class="st" style="right:{-250+off}px;bottom:{int(40*k)+off}px;width:{int(500*k)}px;height:{h}px;'
               f'background:linear-gradient(90deg,{c1},{c2});transform:rotate(-52deg);opacity:.95"></div>')
    return tl + br

def html(sl, photo, fmt, n, total=10):
    W, Hh = SIZES[fmt]; l = L[fmt]
    g0 = sl.get("g0", l["g0"])
    h1size = l["h1c"] if sl.get("long") else l["h1"]
    if sl.get("h1size"): h1size = int(sl["h1size"] * (l["h1"] / 104))
    if sl.get(f"h1size_{fmt}"): h1size = sl[f"h1size_{fmt}"]      # per-format overrides
    h1txt = sl.get(f"h1_{fmt}", sl["h1"])
    bullets = "".join(f'<li><span class="ck">{CHECK.format(s=l["chk"])}</span><span>{H.escape(b)}</span></li>' for b in sl.get("bullets", []))
    pill_cls = {"cover": "pill py", "tip": "pill pc", "deal": "pill pc", "compare": "pill pc", "cta": ""}[sl["kind"]]
    pill = f'<div class="{pill_cls}">{_h1(sl["pill"])}</div>' if sl.get("pill") else ""
    sub = f'<div class="sub">{H.escape(sl["sub"])}</div>' if sl.get("sub") else ""
    body = f'<div class="body">{H.escape(sl["body"])}</div>' if sl.get("body") else ""
    note = f'<div class="note">{H.escape(sl["note"])}</div>' if sl.get("note") else ""
    card = ""
    if sl["kind"] == "cta":
        card = ('<div class="card"><b>Denise Wilson | Broker/REALTOR®</b><br>Lifestyle International Realty — Carolinas<br>'
                'denisewilson.lircarolinas.com<br>704-615-7347<br><br>Equal Housing Opportunity</div>')
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{Hh}px;overflow:hidden;background:{NAVY}}}
.s{{position:relative;width:{W}px;height:{Hh}px;overflow:hidden;color:#fff;font-family:'Montserrat','Inter',sans-serif}}
.ph{{position:absolute;inset:0;background:url('{photo}') center/cover no-repeat}}
.gr{{position:absolute;left:0;right:0;bottom:0;top:{int(Hh*g0)}px;background:linear-gradient(180deg,rgba(11,46,58,0) 0%,rgba(11,46,58,.62) 20%,rgba(11,46,58,.90) 42%,rgba(11,46,58,.97) 70%,rgba(11,46,58,.99) 100%)}}
.st{{position:absolute;transform-origin:center;z-index:2;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
.tag{{position:absolute;z-index:4;top:{l['top']}px;left:{l['side']-6}px;background:{NAVY};border-radius:14px;padding:{int(l['tag']*.45)}px {int(l['tag']*.8)}px {int(l['tag']*.4)}px;
 font-weight:800;font-size:{l['tag']}px;line-height:1.12;letter-spacing:1.2px;box-shadow:0 6px 18px rgba(0,0,0,.28);border-bottom:{max(5,l['tag']//5)}px solid {YEL}}}
.cr{{position:absolute;z-index:4;top:{l['top']+10}px;right:{l['right']-6}px;background:rgba(11,46,58,.92);border-radius:10px;padding:{int(l['cr']*.45)}px {int(l['cr']*.75)}px;font-weight:700;font-size:{l['cr']}px;box-shadow:0 4px 12px rgba(0,0,0,.25)}}
.tx{{position:absolute;z-index:3;left:{l['side']}px;right:{l['right']+ (95 if fmt!='9x16' else 0)}px;bottom:{l['bot']+l['ft']+ (30 if fmt=='1x1' else 40)}px}}
.pill{{display:inline-block;font-weight:800;font-size:{l['pill']}px;letter-spacing:.8px;text-transform:uppercase;border-radius:10px;padding:{int(l['pill']*.28)}px {int(l['pill']*.6)}px;margin-bottom:{l['gap']}px;box-shadow:0 4px 14px rgba(0,0,0,.3)}}
.pc{{background:linear-gradient(90deg,#E8412F,#F25C3A);color:#fff}}
.pc .y{{color:{YEL}}}
.py{{background:{YEL};color:{NAVY};font-family:'Anton';font-weight:400;font-size:{int(l['pill']*1.45)}px;letter-spacing:.5px;padding:{int(l['pill']*.12)}px {int(l['pill']*.55)}px}}
.py .y{{color:{NAVY}}}
h1{{font-family:'Anton';font-weight:400;font-size:{h1size}px;line-height:1.0;text-transform:uppercase;letter-spacing:.3px;text-shadow:0 4px 16px rgba(0,0,0,.45)}}
h1 .y{{color:{YEL}}}
.sub{{font-weight:800;font-size:{l['sub']}px;margin-top:{l['gap']}px;text-shadow:0 2px 8px rgba(0,0,0,.4)}}
.body{{font-weight:600;font-size:{l['li']}px;line-height:1.32;margin-top:{l['gap']}px;color:#F2F6F7}}
ul{{list-style:none;margin-top:{l['gap']+4}px}}
li{{display:flex;align-items:flex-start;gap:{int(l['li']*.65)}px;font-weight:600;font-size:{l['li']}px;line-height:1.28;margin-bottom:{int(l['gap']*.9)}px}}
li .ck{{flex:0 0 auto;margin-top:{-int(l['chk']*.06)}px}}
.note{{font-weight:500;font-size:{l['note']}px;line-height:1.32;margin-top:{l['gap']}px;color:#E6EEF0}}
.card{{margin-top:{l['gap']+8}px;background:rgba(11,46,58,.96);border-left:12px solid {YEL};border-radius:16px;padding:{int(l['li']*.9)}px {int(l['li']*1.1)}px;font-weight:600;font-size:{l['li']+1}px;line-height:1.38;box-shadow:0 6px 18px rgba(0,0,0,.3)}}
.card b{{font-weight:800;font-size:{l['li']+5}px}}
.ft{{position:absolute;z-index:4;left:{l['side']}px;right:{l['right']+ (60 if fmt!='9x16' else 0)}px;bottom:{l['bot']}px;display:flex;justify-content:space-between;font-weight:800;font-size:{l['ft']}px;letter-spacing:1.4px;text-shadow:0 2px 8px rgba(0,0,0,.45)}}
"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="s">
<div class="ph"></div><div class="gr"></div>{_stripes(W,Hh,fmt)}
<div class="tag">NEW BUILD DEALS<br>NC + SC</div>
<div class="cr">Photo: {H.escape(sl['credit'])}</div>
<div class="tx">{pill}<h1>{_h1(h1txt)}</h1>{sub}{body}<ul>{bullets}</ul>{note}{card}</div>
<div class="ft"><span>NEW CONSTRUCTION</span><span>{n} / {total}</span></div>
</div></body></html>"""

def render(sl, photo, out_png, fmt, n, total=10, html_dir=None):
    W, Hh = SIZES[fmt]
    hp = os.path.join(html_dir or os.path.dirname(out_png), f"{fmt}-slide-{n:02d}.html")
    open(hp, "w").write(html(sl, os.path.abspath(photo), fmt, n, total))
    cdp.shot(hp, out_png, W, Hh)
    return out_png
