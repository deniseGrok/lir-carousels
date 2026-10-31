# Buyer tips Oct 31 2026: "Know what you're really buying" (title, survey, easements, HOA covenants). 10 slides.
# Signature Authority v2 (Oct 31 2026, Denise's example slides): TEMPLATES/signature_authority.py, spec TEMPLATES/SIGNATURE_AUTHORITY.md.
# DESIGN-APPROVAL ROUND: 4:5 1080x1350 only (slide-NN.png, PDF, slides.zip). No 1:1 / 9:16 until Denise approves the design.
# Facts and sources unchanged (see ../2026-10-31-buyer-tips-title-and-survey.md, sources A-G); bullets tightened to short lines.
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-10-31-buyer-tips-title-and-survey"; B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
SL = [
 sa.cover("p7340487.jpg", "KNOW WHAT YOU'RE", "really buying", "Practical advice for<br><b>BUYERS.</b>", xy=(.5, .55), grade=dict(bright=1.06, gold=.9, sat=1.1)),
 sa.stats("Charlotte metro|September 2026",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("PRICE PER<br>SQ FT", "$217", "−1.4% YoY"),
           ("NEW<br>LISTINGS", "3,742", "−7.5% YoY"), ("PENDING<br>LISTINGS", "4,681", "−5.9% YoY")],
          "Whatever the price, check the title and boundaries before you close.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026"),
 sa.edu("p12955837.jpg", "Title means|ownership.",
        "At closing, the deed shows the seller transferred ownership, or \"title,\" to you.",
        ["Old claims can surface later", "Like unpaid taxes or contractors", "Title search: public records",
         "Title insurance can cover them"], xy=(.85, .5)),
 sa.edu("p1358900.jpg", "Lender's policy|vs. owner's.", "Two policies, two jobs. An owner's policy can help protect your investment.",
        ["Lender's: usually required", "Protects the lender's loan", "Not your equity",
         "Owner's policy is optional"], xy=(.62, .5), grade=dict(gold=1.4, bright=1.08)),
 sa.edu("p7888648.jpg", "You can shop|for title.", "Title services can usually be shopped. Start with your Loan Estimate.",
        ["Check section C, page 2", "Ask for the provider list", "Compare more than one",
         "Bundling usually costs less"], xy=(.55, .5)),
 sa.edu("photo-1720670797121-109f3f21136e.jpg", "Know where|the lines are.", "A survey shows what you're buying on the ground, not just on paper.",
        ["Boundaries and property lines", "Easements and setbacks", "A due diligence item in NC",
         "Order it early"], xy=(.5, .62), grade=dict(gold=.6)),
 sa.edu("p5002323.jpg", "Read the|land questions.", "NC's disclosure (REC 4.22) asks about issues on or around the property.",
        ["Easements, shared driveways", "Encroachments, private roads", "Liens that could affect title",
         "SC's form covers covenants too"], xy=(.7, .5), grade=dict(gold=1.3)),
 sa.edu("p4792507.jpg", "Read the|HOA rules.", "Covenants and HOA documents can set mandatory rules for the home and lot.",
        ["Restrictive covenants", "Bylaws and rules", "Ask about document fees", "Review during due diligence"], xy=(.6, .5)),
 sa.edu("p36845626.jpg", "Ask questions|before you sign.", "Your closing attorney can explain what the title search found.",
        ["Review the title results", "Ask what exceptions mean", "Compare survey to your tour",
         "Bring questions early"], xy=(.5, .5), grade=dict(bright=1.14)),
 sa.cta("photo-1722247482035-73d55ee3d258.jpg", CONTACT, xy=(.55, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
if __name__ == "__main__":
    print(len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="buyer")))
