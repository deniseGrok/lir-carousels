# Concord NC spotlight (Nov 10 2026; built Nov 8) YouTube Short: 1080x1920 FULL-FRAME H.264, NO audio stream (Denise Oct 24 2026: no music).
# Frames: '9x16v' video slides rendered by build_slides.py into build/v916 (header "NEIGHBORHOOD SPOTLIGHT / Concord · NC" at y=262,
# key text clear of top 250 / bottom 420 / right 140 px). Slow centered push-in (1.000 -> 1.03), eased 0.6 s crossfades, ends holding on
# the contact slide. Never says "swipe". (Re-created verbatim Nov 6 after the build/ wipe.)
import numpy as np, subprocess, sys
from PIL import Image
D, V = sys.argv[1], sys.argv[2]
W, H, FPS = 1080, 1920, 30; PER = [4.6] * 9 + [7.0]; XF = 0.6; N = 10; ZMAX = 1.03
slides = [Image.open(f"{V}/slide-{i:02d}.png").convert("RGB") for i in range(1, 11)]
for s in slides: assert s.size == (W, H)
starts = []; t = 0
for i in range(N): starts.append(t); t += PER[i] - (XF if i < N - 1 else 0)
TOT = t; NF = int(round(TOT * FPS))
ease = lambda x: 0.5 - 0.5 * np.cos(np.pi * min(max(x, 0), 1))
def frame_for(i, tt):
    z = 1.0 + (ZMAX - 1.0) * ease(tt / PER[i]); cw, ch = W / z, H / z; x0, y0 = (W - cw) / 2, (H - ch) / 2
    return slides[i].transform((W, H), Image.EXTENT, (x0, y0, x0 + cw, y0 + ch), Image.BICUBIC)
p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
  "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", "-movflags", "+faststart", D + "/youtube-short.mp4"],
  stdin=subprocess.PIPE)
for n in range(NF):
    T = n / FPS; act = [i for i in range(N) if starts[i] <= T < starts[i] + PER[i]]
    if len(act) == 1: fr = frame_for(act[0], T - starts[act[0]])
    else:
        a, b = act[0], act[-1]; al = float(ease((T - starts[b]) / XF)); fr = Image.blend(frame_for(a, T - starts[a]), frame_for(b, T - starts[b]), al)
    p.stdin.write(fr.tobytes())
p.stdin.close(); assert p.wait() == 0
print("duration", round(TOT, 2))
