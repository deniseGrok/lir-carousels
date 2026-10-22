"""Compliance scan for a carousel folder (see TEMPLATES/COMPLIANCE.md). Usage: python3 compliance_check.py <folder>
Checks captions/.md/youtube files + build/*.html slide text: banned Fair Housing / guarantee / urgency words, firm name,
phone, EHO, closing question per caption section, and 'swipe' in video/9:16 assets. Prints PASS/FAIL lines; exit 1 on FAIL."""
import os, re, sys, glob, html
FIRM = "Lifestyle International Realty — Carolinas"; PHONE = "704-615-7347"; EHO = "Equal Housing Opportunity"
BANNED = [r"perfect for", r"ideal for", r"great for (famil|couple|single|retire|empty|young)", r"family[- ]friendly", r"kid[- ]friendly",
  r"\bsafe\b", r"\bsafety\b", r"low[- ]crime", r"\bcrime\b", r"\bexclusive\b", r"\bintegrated\b", r"\bdiverse\b", r"\bethnic", r"christian",
  r"\bchurch", r"\btemple\b", r"\bmosque\b", r"handicap", r"wheelchair", r"able-bodied", r"bachelor", r"man cave", r"mother-in-law",
  r"\bmaster\b", r"school", r"guarantee", r"\bwill sell\b", r"act now", r"last chance", r"never be this low", r"\bbest agent\b", r"#1\b", r"\bswipe\b"]
def text(p):
    t = open(p, errors="ignore").read()
    if p.endswith(".html"): t = html.unescape(re.sub(r"<style.*?</style>|<[^>]+>", " ", t, flags=re.S))
    return t
def main(d):
    fails = 0
    def rep(ok, msg):
        nonlocal fails; fails += (not ok); print(("PASS " if ok else "FAIL ") + msg)
    caps = [p for p in glob.glob(os.path.join(d, "*.md")) if re.search(r"caption", os.path.basename(p))]
    for p in caps:
        secs = re.split(r"\n## ", open(p).read())[1:]
        for s in secs:
            name, body = s.split("\n", 1); b = body.strip()
            if name.lower().startswith(("notes", "compliance", "file")): continue
            rep(FIRM in b, f"{os.path.basename(p)} [{name}] firm name")
            rep(PHONE in b, f"{os.path.basename(p)} [{name}] phone")
            rep(EHO in b, f"{os.path.basename(p)} [{name}] Equal Housing Opportunity")
            last = [l for l in b.splitlines() if l.strip() and not l.lower().startswith("tags:")]
            rep(bool(last) and last[-1].rstrip().endswith("?"), f"{os.path.basename(p)} [{name}] ends with a question")
            if "instagram" in name.lower(): rep("@" not in b.replace("®", ""), f"[{name}] no email")
    files = caps + glob.glob(os.path.join(d, "build", "*.html")) + glob.glob(os.path.join(d, "build", "9x16", "*.html"))
    for p in files:
        t = text(p); base = os.path.relpath(p, d)
        if base.endswith(".html") and "-video" not in base and "9x16" not in base:
            pats = [x for x in BANNED if x != r"\bswipe\b"]
        else: pats = BANNED
        for pat in pats:
            for m in re.finditer(pat, t, re.I):
                ctx = t[max(0, m.start()-40):m.end()+40].replace("\n", " ")
                rep(False, f"{base}: banned/flag '{m.group(0)}' … {ctx} …  (fix, or confirm it is a neutral rule citation and whitelist in the .md)")
    s10 = [p for p in glob.glob(os.path.join(d, "build", "**", "*10*.html"), recursive=True)]
    for p in s10:
        t = text(p); rep(all(x in t for x in (FIRM, PHONE, EHO, "Denise Wilson", "denisewilson.lircarolinas.com")), f"{os.path.relpath(p, d)} contact block complete")
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} fail lines)"); return 1 if fails else 0
if __name__ == "__main__": sys.exit(main(sys.argv[1]))
