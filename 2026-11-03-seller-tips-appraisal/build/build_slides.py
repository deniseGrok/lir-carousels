# Seller tips Tue Nov 3 2026: "Prep for the appraisal" (seller side of the buyer's appraisal). 10 slides.
# Signature Authority v2 (approved Oct 31 2026): TEMPLATES/signature_authority.py, spec TEMPLATES/SIGNATURE_AUTHORITY.md.
# Mirrors 2026-11-01-seller-tips-what-stays (15e0020) and 2026-11-02-buyer-tips-homeowners-insurance.
# Builds 4:5 (IG), 1:1 slides-1x1/ (FB), 9:16 slides-9x16/ (TikTok). NO PDF: any PDF sa.build writes is deleted right after.
# Images: custom-generated (GenerateImage) raw -> build/src/gen-NN-raw.jpg; upscale 4x: python3 build_slides.py upscale
# Usage: python3 build_slides.py [upscale] [4x5 1x1 9x16]  (default: all three sizes)
# Facts and sources: ../2026-11-03-seller-tips-appraisal.md (sources A-C).
import sys, os, subprocess, glob
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-11-03-seller-tips-appraisal"; B = os.path.dirname(os.path.abspath(__file__)); D = os.environ.get("OUT_DIR") or os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)
F = {k: dict(xy_1x1=(.5, .5), xy_9x16=(.72, .5)) for k in (1, 3, 4, 5, 6, 7, 8, 9)}
P = dict(xy=(.5, .5), crisp=GEN, bright_all=True)
NV = "14,48,66"
def band(a0, a1, a2, a3, stop):
    return (f".gl{{background:linear-gradient(90deg,rgba({NV},{a0}) 0,rgba({NV},{a1}) 30%,rgba({NV},{a2}) 46%,"
            f"rgba({NV},{a3}) 58%,rgba({NV},0) {stop}%)!important}}")
TALL = (f".gl{{background:radial-gradient(ellipse 92% 36% at 36% 37%,rgba({NV},.84) 0,rgba({NV},.62) 55%,rgba({NV},0) 100%),"
        f"linear-gradient(90deg,rgba({NV},.7) 0,rgba({NV},.52) 40%,rgba({NV},.22) 64%,rgba({NV},0) 78%)!important}}")
STRONG, MILD = band(.9, .84, .66, .32, 70), band(.86, .78, .52, .2, 66)
# readability boosts (set Nov 3 after full-size inspection): pale sunlit walls (3/4/5/7/8) and bright foliage/props behind text (6/9)
X = {k: dict(css_4x5=STRONG, css_1x1=STRONG, css_9x16=TALL) for k in (3, 4, 5, 6, 7, 8, 9)}
for k in (3, 6, 9): F[k]['xy_9x16'] = (.95, .5)   # keep the right-side subject clear of the 9:16 text block
SL = [
 sa.cover("gen-01.jpg", "PREP FOR THE", "appraisal", "Practical advice for<br><b>SELLERS.</b>", **P, **F[1], **X.get(1, {})),
 sa.stats("Charlotte metro|September 2026",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("ACTIVE<br>LISTINGS", "11,182", "+10.3% YoY"),
           ("MEDIAN DAYS<br>ON MARKET", "64", "+10.3% YoY"), ("PRICE-REDUCED<br>SHARE", "26.2%", "+0.7 pts YoY")],
          "More homes to compare and more price cuts. Plan ahead for the appraisal.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026"),
 sa.edu("gen-03.jpg", "It's the|buyer's appraisal.", "On NC's standard offer form, an appraisal is a buyer due diligence item, and the buyer pays for it.",
        ["Hired by buyer or lender", "Paid by the buyer", "Listed in due diligence", "In SC, read your contract"], **P, **F[3], **X.get(3, {})),
 sa.edu("gen-04.jpg", "No appraisal|contingency.", "NC's standard form has no appraisal contingency. Buyers can end the deal for any reason during due diligence.",
        ["Know your DD end date", "Buyer can end it during DD", "After DD, EMD may be at risk", "Ask about the lender timeline"], **P, **F[4], **X.get(4, {})),
 sa.edu("gen-05.jpg", "List your|upgrades.", "Federal rules allow sharing added property facts with an appraiser. A clear list helps.",
        ["Roof, HVAC, water heater", "Kitchen and bath updates", "Dates and permits, if any", "Keep receipts handy"], **P, **F[5], **X.get(5, {})),
 sa.edu("gen-06.jpg", "Make access|easy.", "NC's standard form asks sellers to give reasonable access, with utilities on at the seller's cost.",
        ["Keep utilities on", "Clear attic and crawl access", "Unlock gates and sheds", "Plan for pets that day"], **P, **F[6], **X.get(6, {})),
 sa.edu("gen-07.jpg", "Finish the|small fixes.", "I recommend wrapping up open repairs before the visit, so the home shows as it really is.",
        ["Patch, paint, replace bulbs", "Fix drips and loose handles", "Tidy, not staged", "Keep a list of finished work"], **P, **F[7], **X.get(7, {})),
 sa.edu("gen-08.jpg", "Facts, not|pressure.", "Federal rules bar anyone in the deal from pushing an appraiser toward a value. Sharing facts is allowed.",
        ["Never name a target value", "Your agent can share comps", "Ask for errors to be fixed", "The value is their call"], **P, **F[8], **X.get(8, {})),
 sa.edu("gen-09.jpg", "If it comes|in low.", "A low appraisal starts a conversation. Any change to the contract must be in writing and signed.",
        ["Check the facts first", "Buyer can flag errors", "Talk price, cash or terms", "Get changes in writing"], **P, **F[9], **X.get(9, {})),
 sa.cta("gen-10.jpg", CONTACT, xy=(.5, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
def upscale():
    for n in (1, 3, 4, 5, 6, 7, 8, 9, 10):
        raw, out = os.path.join(B, "src", f"gen-{n:02d}-raw.jpg"), os.path.join(B, "src", f"gen-{n:02d}.jpg")
        if os.path.exists(raw) and (not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw)):
            subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py", raw, out], check=True); print("upscaled", n)
if __name__ == "__main__":
    a = sys.argv[1:]
    if "upscale" in a: upscale(); a = [x for x in a if x != "upscale"]
    for fmt in (a or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="seller", fmt=fmt)))
    for p in glob.glob(os.path.join(D, "*.pdf")): os.remove(p); print("removed PDF (no-PDF rule)", p)
