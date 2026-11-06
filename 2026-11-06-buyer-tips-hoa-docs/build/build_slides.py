# Buyer tips Fri Nov 6 2026: "Read the HOA / condo docs before you buy". Signature Authority. NO PDF.
# Mirrors 2026-11-05-seller-tips-credits-vs-price-cut and 2026-11-04-buyer-tips-read-the-disclosures.
# Builds 4:5 (IG), 1:1 slides-1x1/ (FB), 9:16 slides-9x16/ (TikTok). Any PDF sa.build writes is deleted.
# Images: GenerateImage raws in build/src/gen-NN-raw.jpg (no gen-09 — slide 9 is navy stats). Upscale: python3 build_slides.py upscale
# Usage: python3 build_slides.py [upscale] [4x5 1x1 9x16]
# Facts/sources: ../2026-11-06-buyer-tips-hoa-docs.md (sources A–J).
# NOTE (Nov 6 ~6:30 AM ET): build/ (src images + HTML) was wiped by a disk cleanup after the slides were rendered; this script was
# re-created verbatim from the run log. Final PNGs/zips in the folder are the delivered renders.
import sys, os, subprocess, glob
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-11-06-buyer-tips-hoa-docs"; B = os.path.dirname(os.path.abspath(__file__)); D = os.environ.get("OUT_DIR") or os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)
F = {k: dict(xy_1x1=(.5, .5), xy_9x16=(.72, .5)) for k in (1, 2, 3, 4, 5, 6, 7, 8, 10)}
P = dict(xy=(.5, .5), crisp=GEN, bright_all=True)
NV = "14,48,66"
def band(a0, a1, a2, a3, stop):
    return (f".gl{{background:linear-gradient(90deg,rgba({NV},{a0}) 0,rgba({NV},{a1}) 30%,rgba({NV},{a2}) 46%,"
            f"rgba({NV},{a3}) 58%,rgba({NV},0) {stop}%)!important}}")
TALL = (f".gl{{background:radial-gradient(ellipse 92% 36% at 36% 37%,rgba({NV},.84) 0,rgba({NV},.62) 55%,rgba({NV},0) 100%),"
        f"linear-gradient(90deg,rgba({NV},.7) 0,rgba({NV},.52) 40%,rgba({NV},.22) 64%,rgba({NV},0) 78%)!important}}")
STRONG, MILD = band(.9, .84, .66, .32, 70), band(.86, .78, .52, .2, 66)
X = {k: dict(css_4x5=STRONG, css_1x1=STRONG, css_9x16=TALL) for k in (2, 3, 4, 5, 6, 7, 8)}
for k in (2, 3, 6, 8): F[k]['xy_9x16'] = (.95, .5)
SL = [
 sa.cover("gen-01.jpg", "READ THE HOA", "docs", "Practical advice for<br><b>BUYERS.</b>", **P, **F[1], **X.get(1, {})),
 sa.edu("gen-02.jpg", "Ask for the|full packet.",
        "Form 2A12-T authorizes release of covenants, bylaws, rules, budget, financials, architectural guidelines, parking rules, and association insurance. Confirm during Due Diligence.",
        ["Covenants and bylaws", "Budget and financials", "Rules and guidelines", "Association insurance"], **P, **F[2], **X.get(2, {})),
 sa.edu("gen-03.jpg", "Know the dues|and coverage.",
        "Match assessments to what they pay for, and factor the dues into affordability before you offer.",
        ["Ask what dues cover", "Insurance and amenities", "Roads and maintenance", "Factor into affordability"], **P, **F[3], **X.get(3, {})),
 sa.edu("gen-04.jpg", "Reserves and|special assessments.",
        "Thin reserves can mean special assessments. Ask what is in reserve and what is already approved.",
        ["Ask what's in reserve", "Check recent dues raises", "Approved assessments?", "Read budget financials"], **P, **F[4], **X.get(4, {})),
 sa.edu("gen-05.jpg", "Rental, pet,|and use rules.",
        "Read the covenants for rentals, pets, parking, exterior changes, businesses, and RVs or boats.",
        ["Rental rules in writing", "Pet and parking limits", "Exterior change rules", "Business and RV rules"], **P, **F[5], **X.get(5, {})),
 sa.edu("gen-06.jpg", "HOA insurance|+ transfer fees.",
        "Ask what the association policy covers, the deductible, and what you still insure. Get every transfer fee in writing.",
        ["Association policy cover", "Deductible amount", "What you still insure", "Transfer fees in writing"], **P, **F[6], **X.get(6, {})),
 sa.edu("gen-07.jpg", "Minutes, lawsuits,|violations.",
        "Request recent minutes. Ask if the property is in violation. Read disclosed judgments and lawsuits.",
        ["Request recent minutes", "Ask about violations", "Check judgments listed", "Read pending lawsuits"], **P, **F[7], **X.get(7, {})),
 sa.edu("gen-08.jpg", "Finish inside|Due Diligence.",
        "NC new condos: public offering statement plus a 7-day cancel right (G.S. 47C-4-108). Many resales get a fee statement (47C-4-109). Finish document review before Form 2-T Due Diligence ends.",
        ["New condo POS + cancel", "Resale fee statement", "Review before DD ends", "Confirm during diligence"], **P, **F[8], **X.get(8, {})),
 sa.stats("Charlotte metro|October 2026",
          [("MEDIAN<br>LIST PRICE", "$419,900", "−4.1% YoY"), ("ACTIVE<br>LISTINGS", "11,547", "+13.2% YoY"),
           ("MEDIAN DAYS<br>ON MARKET", "65", "+11.1% YoY"), ("PRICE-REDUCED<br>SHARE", "27.1%", "+0.0 pts YoY")],
          "More inventory means room to be selective. Finish your HOA document review carefully.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, October 2026"),
 sa.cta("gen-10.jpg", CONTACT, xy=(.5, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
def upscale():
    for n in (1, 2, 3, 4, 5, 6, 7, 8, 10):
        raw, out = os.path.join(B, "src", f"gen-{n:02d}-raw.jpg"), os.path.join(B, "src", f"gen-{n:02d}.jpg")
        if os.path.exists(raw) and (not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw)):
            subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py", raw, out], check=True); print("upscaled", n)
if __name__ == "__main__":
    a = sys.argv[1:]
    if "upscale" in a: upscale(); a = [x for x in a if x != "upscale"]
    for fmt in (a or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="buyer", fmt=fmt)))
    for p in glob.glob(os.path.join(D, "*.pdf")): os.remove(p); print("removed PDF (no-PDF rule)", p)
