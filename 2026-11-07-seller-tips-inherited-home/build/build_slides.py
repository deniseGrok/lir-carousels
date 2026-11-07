# Seller tips Sat Nov 7 2026: "Inherited a home? Selling it, step by step" (selling an inherited home). Signature Authority. NO PDF.
# Mirrors 2026-11-05-seller-tips-credits-vs-price-cut (stats on slide 2) and 2026-11-06-buyer-tips-hoa-docs.
# Builds 4:5 (IG), 1:1 slides-1x1/ (FB), 9:16 slides-9x16/ (TikTok). Any PDF sa.build writes is deleted.
# IMAGES: save the generated originals as build/img/01.png 03.png 04.png 05.png 06.png 07.png 08.png 09.png 10.png
#   (slide 2 is the navy stats slide, no photo). `ingest` copies each one to build/src/gen-NN-raw.png (only when it is not a
#   1080x1350 graded render and its bytes changed), then upscales 4x with Real-ESRGAN to build/src/gen-NN.jpg (skipped if the
#   original is already >= 2160 px wide). sa.build then reads build/src/gen-NN.jpg and writes the graded 4:5 photo back to
#   build/img/NN.png (the raw stays safe in build/src/).
# Usage: python3 build_slides.py ingest            -> copy + upscale only
#        python3 build_slides.py ingest 4x5 1x1 9x16  -> copy + upscale, then render (default: all three sizes)
#        python3 build_slides.py 4x5               -> render only
# Facts/sources: ../2026-11-07-seller-tips-inherited-home.md (sources A–L).
import sys, os, subprocess, glob, shutil, filecmp
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
from PIL import Image
N = "2026-11-07-seller-tips-inherited-home"; B = os.path.dirname(os.path.abspath(__file__)); D = os.environ.get("OUT_DIR") or os.path.dirname(B)
PHOTOS = (1, 3, 4, 5, 6, 7, 8, 9, 10)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)
F = {k: dict(xy_1x1=(.5, .5), xy_9x16=(.72, .5)) for k in PHOTOS}
P = dict(xy=(.5, .5), crisp=GEN, bright_all=True)
NV = "14,48,66"
def band(a0, a1, a2, a3, stop):
    return (f".gl{{background:linear-gradient(90deg,rgba({NV},{a0}) 0,rgba({NV},{a1}) 30%,rgba({NV},{a2}) 46%,"
            f"rgba({NV},{a3}) 58%,rgba({NV},0) {stop}%)!important}}")
TALL = (f".gl{{background:radial-gradient(ellipse 92% 36% at 36% 37%,rgba({NV},.84) 0,rgba({NV},.62) 55%,rgba({NV},0) 100%),"
        f"linear-gradient(90deg,rgba({NV},.7) 0,rgba({NV},.52) 40%,rgba({NV},.22) 64%,rgba({NV},0) 78%)!important}}")
STRONG, MILD = band(.9, .84, .66, .32, 70), band(.86, .78, .52, .2, 66)
X = {k: dict(css_4x5=STRONG, css_1x1=STRONG, css_9x16=TALL) for k in (3, 4, 5, 6, 7, 8, 9)}
for k in (3, 6, 8, 9): F[k]['xy_9x16'] = (.95, .5)   # checked Nov 7: 3/6/8/9 crops keep the subject
# Slide 6: the bright roof gutter ran through the body text ("cover after 60 days vacant in a row"), so a deeper, wider band.
DEEP = band(.93, .9, .8, .55, 80)
TALL6 = (f".gl{{background:radial-gradient(ellipse 96% 40% at 38% 37%,rgba({NV},.9) 0,rgba({NV},.74) 58%,rgba({NV},0) 100%),"
         f"linear-gradient(90deg,rgba({NV},.78) 0,rgba({NV},.62) 45%,rgba({NV},.32) 70%,rgba({NV},0) 86%)!important}}")
X[6] = dict(css_4x5=DEEP, css_1x1=DEEP, css_9x16=TALL6)
SL = [
 sa.cover("gen-01.jpg", "INHERITED A", "home?", "Practical advice for<br><b>SELLERS.</b>", **P, **F[1], **X.get(1, {})),
 sa.stats("Charlotte metro|October 2026",
          [("MEDIAN<br>LIST PRICE", "$419,900", "−4.1% YoY"), ("MEDIAN DAYS<br>ON MARKET", "65", "+11.1% YoY"),
           ("PENDING<br>LISTINGS", "4,129", "−13.0% YoY"), ("PRICE-REDUCED<br>SHARE", "27.1%", "+0.0 pts YoY")],
          "Homes are taking longer to sell. Plan the estate's carrying costs into your timeline.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, October 2026"),
 sa.edu("gen-03.jpg", "Confirm who|can sign.",
        "NC: title passes to heirs or devisees at death (G.S. 28A-15-2); an executor sells under the will or a clerk proceeding (G.S. 28A-15-1). SC: will authority or court process (S.C. Code 62-3-711).",
        ["Executor or the heirs?", "Will's power of sale?", "NC: heirs' spouses on deed", "Ask the estate attorney"], **P, **F[3], **X.get(3, {})),
 sa.edu("gen-04.jpg", "Gather the|paperwork.",
        "You may need proof of your right to the home, such as the will, the death certificate, or a letter from the executor (CFPB).",
        ["Death certificate", "Will + executor letters", "Recorded deed", "Mortgage + tax bills"], **P, **F[4], **X.get(4, {})),
 sa.edu("gen-05.jpg", "Tell the|servicer.",
        "Send a written notice. Under the CFPB servicing rule, the servicer must describe the documents it needs to confirm you as a successor in interest.",
        ["Write to the servicer", "Name, address, loan no.", "Ask what proof it needs", "Ask how to keep paying"], **P, **F[5], **X.get(5, {})),
 sa.edu("gen-06.jpg", "Protect the|empty house.",
        "Tell the insurer about the death and any vacancy. One standard form limits vandalism and glass cover after 60 days vacant in a row (AAIS HO 0003 01 06).",
        ["Tell the insurer early", "Ask about vacancy limits", "Heat on, or water off", "Check on it often"], **P, **F[6], **X.get(6, {})),
 sa.edu("gen-07.jpg", "Disclosures|still matter.",
        "NC and SC exempt a fiduciary's sale during estate administration (G.S. 47E-2(a)(3); S.C. Code 27-50-30(3)). Heirs selling are not exempt, and brokers still disclose material facts.",
        ["Fiduciary sale: exempt", "Heirs selling: disclose", "Known facts still count", "Confirm with your attorney"], **P, **F[7], **X.get(7, {})),
 sa.edu("gen-08.jpg", "Know your|tax basis.",
        "Basis is generally fair market value at the date of death (IRS Pub. 551, Dec 2025). Inherited property counts as held over 1 year (IRS Pub. 544, 2025).",
        ["Date-of-death value", "Keep the appraisal", "Long-term holding rule", "Talk with a CPA"], **P, **F[8], **X.get(8, {})),
 sa.edu("gen-09.jpg", "Agree first,|then list.",
        "I recommend every owner agree in writing on price, repairs, and who covers carrying costs, then price from recent solds.",
        ["Every owner on board", "Agree on price + repairs", "Split carrying costs", "Price from recent solds"], **P, **F[9], **X.get(9, {})),
 sa.cta("gen-10.jpg", CONTACT, xy=(.5, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
def ingest():
    os.makedirs(os.path.join(B, "src"), exist_ok=True)
    for n in PHOTOS:
        src = os.path.join(B, "img", f"{n:02d}.png"); raw = os.path.join(B, "src", f"gen-{n:02d}-raw.png"); out = os.path.join(B, "src", f"gen-{n:02d}.jpg")
        if os.path.exists(src):
            w, h = Image.open(src).size
            if (w, h) != (1080, 1350) and not (os.path.exists(raw) and filecmp.cmp(src, raw, shallow=False)):
                shutil.copy2(src, raw); print("ingested", n, (w, h))
        if not os.path.exists(raw): print("MISSING image for slide", n, "->", src); continue
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(raw): continue
        if Image.open(raw).width >= 2160: Image.open(raw).convert("RGB").save(out, quality=97); print("copied (no upscale)", n)
        else: subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py", raw, out], check=True); print("upscaled", n)
if __name__ == "__main__":
    a = sys.argv[1:]
    if "ingest" in a:
        ingest(); a = [x for x in a if x != "ingest"]
        if not a: sys.exit(0)
    miss = [n for n in PHOTOS if not os.path.exists(os.path.join(B, "src", f"gen-{n:02d}.jpg"))]
    if miss: sys.exit(f"missing build/src/gen-NN.jpg for slides {miss}: save build/img/NN.png and run `ingest` first")
    for fmt in (a or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="seller", fmt=fmt)))
    for p in glob.glob(os.path.join(D, "*.pdf")): os.remove(p); print("removed PDF (no-PDF rule)", p)
