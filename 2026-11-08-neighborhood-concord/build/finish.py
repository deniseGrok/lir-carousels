"""Finish step for Concord NC spotlight (Sun Nov 8 2026).
  python3 build/finish.py check
  python3 build/finish.py
"""
import os, sys, csv, glob, hashlib, subprocess, datetime
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES"); import photo_registry as pr
from PIL import Image
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); NAME = os.path.basename(D)
REGS = ["/workspace/repos/lir-carousels/TEMPLATES/photo-registry.csv", "/workspace/lir-ai-team/content-research/carousels/TEMPLATES/photo-registry.csv"]
NOTE = "Concord NC Community Spotlight Nov 8 2026; Modern Charlotte Editorial; ORIGINAL image generated Nov 8 2026 with GenerateImage (no stock, no credit needed); DRAFT awaiting Denise approval"

def raws(): return sorted(glob.glob(os.path.join(B, "src", "gen-??-raw.*")))

def check():
    rows = pr.load()
    if not rows:
        alt = "/workspace/repos/lir-carousels/TEMPLATES/photo-registry.csv"
        rows = list(csv.DictReader(open(alt, newline="")))
    bad = 0
    for p in raws():
        hits = pr.check(p, rows); print(os.path.basename(p), "OK (no match)" if not hits else f"{len(hits)} possible match(es)")
        for s, r, why in hits[:5]: print("   ", s, r["carousel"], r["slide"], r["file"], why); bad += 1
    return bad

def register():
    today = datetime.date.today().isoformat(); new = []
    for p in raws():
        n = int(os.path.basename(p)[4:6]); sid = f"gen-2026-11-08-concord-{n:02d}"
        files = [(os.path.relpath(p, D), "src_original"), (f"build/src/gen-{n:02d}.jpg", "photo"),
                 (f"slide-{n:02d}.png", "slide_render"), (f"slides-1x1/slide-{n:02d}.png", "slide_render"), (f"slides-9x16/slide-{n:02d}.png", "slide_render")]
        for rel, kind in files:
            fp = os.path.join(D, rel)
            if not os.path.exists(fp): continue
            h = pr.hashes(Image.open(fp), kind)
            if not h: continue
            new.append(dict(carousel=NAME, slide=n, kind=kind, provider="generated:GenerateImage", source_id=sid, source_url="", photographer="",
                            file=f"{NAME}/{rel}", sha1=hashlib.sha1(open(fp, "rb").read()).hexdigest(), added=today, notes=NOTE, **h))
    for reg in REGS:
        if not os.path.exists(reg):
            print("skip missing", reg); continue
        have = {(r["carousel"], r["sha1"]) for r in csv.DictReader(open(reg, newline=""))}
        add = [r for r in new if (r["carousel"], r["sha1"]) not in have]
        with open(reg, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=pr.COLS, lineterminator="\r\n"); [w.writerow(r) for r in add]
        print(reg, "+", len(add), "rows")
    return len(new)

if __name__ == "__main__":
    if sys.argv[1:2] == ["check"]: sys.exit(1 if check() else 0)
    print("registered", register(), "rows per registry copy")
    subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/compliance_check.py", D])
    for f in ["slides.zip", "slides-1x1.zip", "slides-9x16.zip", "slides-jpg.zip", "slides-1x1-jpg.zip", "slides-9x16-jpg.zip", f"{NAME}-DRAFT.pdf", "youtube-short.mp4"]:
        p = os.path.join(D, f)
        if os.path.exists(p): print(f, f"{os.path.getsize(p)/1e6:.1f} MB")
    mp4 = os.path.join(D, "youtube-short.mp4")
    if os.path.exists(mp4):
        print(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height", "-of", "json", mp4],
                             capture_output=True, text=True).stdout)
