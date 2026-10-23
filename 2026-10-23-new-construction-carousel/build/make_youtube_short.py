# Oct 23 2026 new construction carousel YouTube Short / Reel: 1080x1920 FULL-FRAME from the native 9:16 slides (slides-9x16/slide-NN.png).
# No blur fill, letterbox or pillarbox: each frame is the 9:16 slide itself with a gentle centered push-in (1.000 -> 1.025, so
# the tag stays below ~250px and text stays above the bottom 420px), eased crossfades, generated soft ambient music. No "swipe".
import numpy as np, subprocess, wave, os, sys
from PIL import Image
D=sys.argv[1]; B=os.path.dirname(os.path.abspath(__file__))
W,H,FPS=1080,1920,30; PER=[4.5]*9+[6.8]; XF=0.6; N=10; ZMAX=1.025
slides=[Image.open(f"{D}/slides-9x16/slide-{i:02d}.png").convert("RGB") for i in range(1,11)]
for s in slides: assert s.size==(W,H)
starts=[]; t=0
for i in range(N): starts.append(t); t+=PER[i]-(XF if i<N-1 else 0)
TOT=t; NF=int(round(TOT*FPS))
ease=lambda x:0.5-0.5*np.cos(np.pi*min(max(x,0),1))
def frame_for(i,tt):
    z=1.0+(ZMAX-1.0)*ease(tt/PER[i]); cw,ch=W/z,H/z; x0,y0=(W-cw)/2,(H-ch)/2
    return slides[i].transform((W,H),Image.EXTENT,(x0,y0,x0+cw,y0+ch),Image.BICUBIC)
out=B+"/yt_video_noaudio.mp4"
p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
  "-c:v","libx264","-preset","slow","-crf","18","-pix_fmt","yuv420p","-r",str(FPS),out],stdin=subprocess.PIPE)
for n in range(NF):
    T=n/FPS; act=[i for i in range(N) if starts[i]<=T<starts[i]+PER[i]]
    if len(act)==1: fr=frame_for(act[0],T-starts[act[0]])
    else:
        a,b=act[0],act[-1]; al=float(ease((T-starts[b])/XF)); fr=Image.blend(frame_for(a,T-starts[a]),frame_for(b,T-starts[b]),al)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
sr=48000; L=int((TOT+0.5)*sr); tt=np.arange(L)/sr; audio=np.zeros(L)
hz=lambda m:440*2**((m-69)/12)
chords=[[50,57,62,66,69],[47,54,62,66,71],[43,50,59,62,67],[45,52,61,64,69]]
seg=TOT/(len(chords)*2)
for k in range(len(chords)*2):
    c=chords[k%4]; s0=int(k*seg*sr); s1=min(L,int((k+1)*seg*sr+1.5*sr)); n=s1-s0; x=np.arange(n)/sr
    env=np.minimum(1,x/1.6)*np.minimum(1,(n/sr-x)/1.5)
    for j,m in enumerate(c):
        f=hz(m); audio[s0:s1]+=env*(np.sin(2*np.pi*f*x+j)+0.18*np.sin(4*np.pi*f*x))*(0.9 if j else 1.1)*(1+0.08*np.sin(2*np.pi*0.2*x+j))
for k in range(int(TOT/2.3)):
    m=[78,81,76,74,73,69][k%6]; s0=int((1.2+k*2.3)*sr); n=int(2.2*sr)
    if s0+n>L: break
    x=np.arange(n)/sr; audio[s0:s0+n]+=0.35*np.exp(-x*1.6)*np.sin(2*np.pi*hz(m)*x)
audio=np.convolve(audio,np.ones(24)/24,mode="same")
audio*=np.minimum(1,np.minimum(tt/2.0,(TOT+0.5-tt)/3.0)); audio=audio/np.max(np.abs(audio))*0.22
st=np.stack([audio,np.roll(audio,240)],1)
with wave.open(B+"/yt_music.wav","w") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",out,"-i",B+"/yt_music.wav","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",D+"/youtube-short.mp4"],check=True)
print("duration",TOT)
