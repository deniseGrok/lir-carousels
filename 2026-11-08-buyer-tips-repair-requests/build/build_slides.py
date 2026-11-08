"""Buyer Tips, Sun Nov 8 2026: Asking for repairs after the inspection. Signature Authority v2.
Phase 1 (copy + prompts) written ~4:40 AM ET. Phase 2: put generated images in build/src/gen-NN-raw.jpg, upscale to gen-NN.jpg
(TEMPLATES/tools/esrgan_upscale.py), then run this script. Slide 9 = stats (navy, no photo); gen-09 = slide 10 background."""
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import signature_authority as sa
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B = os.path.join(D, "build")
G = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)   # gentler grade for generated images
def E(n, head, body, items, **k):
    k.setdefault("crisp", G); k.setdefault("bright_all", True); k.setdefault("xy_1x1", (.6, .5)); k.setdefault("xy_9x16", (.8, .5))
    return sa.edu(f"gen-{n:02d}.jpg", head, body, items, bubble=sa.SAGE if n % 2 else sa.CORAL, **k)
SL = [
 sa.cover("gen-01.jpg", "ASKING FOR", "repairs", "Practical advice for<br><b>BUYERS</b>", crisp=G, bright_all=True, xy_1x1=(.6, .5), xy_9x16=(.8, .5)),
 E(2, "Start with|the full report",
   "Read every page with your agent. Get a repair pro's opinion on big items before you decide what to ask for.",
   ["Read the whole report", "Big systems first", "Get quotes on big items", "Know your must-haves"]),
 E(3, "The seller|can say no",
   "On NC Form 2-T, the home is sold in its current condition unless you both agree otherwise. The seller may negotiate repairs but isn't required to.",
   ["Sold as is unless agreed", "You can ask for anything", "Seller may agree or decline", "Then you choose next steps"]),
 E(4, "Ask early in|due diligence",
   "Form 2-T strongly advises making repair requests early enough to finish talks before the Due Diligence Period ends.",
   ["Inspect right away", "Send requests early", "Leave time to negotiate", "Extensions need seller OK"]),
 E(5, "Be specific|in writing",
   "In NC, a repair agreement must be in writing and signed by all parties; in SC, put it in writing too. Spell out what, how and who.",
   ["What gets repaired", "How it should be done", "Who does the work", "Receipts or reports"]),
 E(6, "Repair, credit|or price",
   "You can ask for a repair, a credit or a price change. Money instead of repairs needs the right signed amendment.",
   ["Seller makes the repair", "Credit toward closing costs", "A lower price", "Ask your lender first"]),
 E(7, "If you can't|agree",
   "In NC, you can go ahead without the repairs, or end the contract in writing before the Due Diligence Period ends and get your earnest money back.",
   ["Move forward as is", "Or end it in writing", "Before the deadline", "DD fee usually not refunded"]),
 E(8, "Verify the work|before closing",
   "Agreed repairs must be done in a good and workmanlike manner, and you have the right to verify them before settlement.",
   ["Re-inspect if you wish", "Check receipts and reports", "Confirm at the walk-through", "Speak up before you sign"]),
 sa.stats("Charlotte metro|October 2026",
   [("MEDIAN DAYS ON MARKET", "65", "+11.1% YoY"), ("ACTIVE LISTINGS", "11,547", "+13.2% YoY"),
    ("PENDING LISTINGS", "4,129", "−13.0% YoY"), ("PRICE-REDUCED SHARE", "27.1%", "+0.0 pts YoY")],
   "More homes and more time on the market can mean more room to talk through repairs. Every home and seller is different.",
   "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia NC-SC metro, October 2026 (released Nov 4, 2026)."),
 sa.cta("gen-09.jpg", dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
        phone="704-615-7347", web="denisewilson.lircarolinas.com"), blur=6, grade=dict(bright=1.12, sat=1.05)),
]
if __name__ == "__main__":
    import glob, zipfile
    from PIL import Image
    name = "2026-11-08-buyer-tips-repair-requests-DRAFT.pdf"
    # NO PDF (Denise). write_pdf=False so the shared renderer does not emit one.
    for fmt in ("4x5", "1x1", "9x16"):
        sa.build(SL, D, B, name, series="buyer", fmt=fmt, write_pdf=False)
    for p in glob.glob(os.path.join(D, "*.pdf")):
        os.remove(p); print("removed PDF", p)
    for zp in ("slides.zip", "slides-1x1.zip", "slides-9x16.zip"):
        path = os.path.join(D, zp)
        if not os.path.exists(path): continue
        mb = os.path.getsize(path) / 1e6
        print(zp, f"{mb:.1f} MB")
        if mb > 25:
            jz = path.replace(".zip", "-jpg.zip")
            folder = D if zp == "slides.zip" else os.path.join(D, zp.replace(".zip", ""))
            with zipfile.ZipFile(jz, "w") as z:
                for i in range(1, 11):
                    png = os.path.join(folder, f"slide-{i:02d}.png")
                    tmp = os.path.join(B, f"jpg-{i:02d}.jpg")
                    Image.open(png).convert("RGB").save(tmp, quality=92, subsampling=0)
                    z.write(tmp, f"slide-{i:02d}.jpg"); os.remove(tmp)
            print(os.path.basename(jz), f"{os.path.getsize(jz)/1e6:.1f} MB")
