# YouTube Short (1080x1920, H.264/AAC) from the 10 approved slides: Ken Burns on the slide card (scale only, never cropped),
# slow drift on a blurred teal-tinted photo background, crossfades, generated soft ambient music. No SWIPE (uses slide-NN-video.png).
import numpy as np, subprocess, wave, os
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
D="/workspace/lir-ai-team/content-research/carousels/2026-10-19-neighborhood-eastover"; B=D+"/build"
W,H,FPS=1080,1920,30; PER=[4.6]*9+[7.0]; XF=0.7; N=10
TEAL=(15,76,92); GOLD=(242,183,5)
font="/usr/share/fonts/truetype/sand-box/google/Montserrat/Montserrat-VariableFont_wght.ttf"
def F(sz,w="Bold"):
    f=ImageFont.truetype(font,sz); f.set_variation_by_name(w); return f
slides=[Image.open(f"{D}/slide-{i:02d}-video.png").convert("RGB") for i in range(1,11)]
bgs=[]
for i in range(1,11):
    p=Image.open(f"{B}/img/{i:02d}.jpg").convert("RGB")  # 1080x1350
    s=max(W*1.18/p.width,H*1.18/p.height); p=p.resize((int(p.width*s),int(p.height*s)),Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    p=Image.blend(p,Image.new("RGB",p.size,(9,46,56)),0.55); bgs.append(p)
# header/footer overlay (top band only; bottom is left clear for YouTube UI)
ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
t1="NEIGHBORHOOD SPOTLIGHT"; f1=F(34,"Bold"); w1=d.textlength(t1,font=f1); d.text(((W-w1)/2,62),t1,font=f1,fill=GOLD+(255,))
t2="Eastover · Charlotte NC"; f2=F(44,"SemiBold"); w2=d.textlength(t2,font=f2); d.text(((W-w2)/2,108),t2,font=f2,fill=(255,255,255,255))
d.rectangle(((W-120)//2,172,(W+120)//2,176),fill=GOLD+(255,))
starts=[]; t=0
for i in range(N): starts.append(t); t+=PER[i]-(XF if i<N-1 else 0)
TOT=t; NF=int(round(TOT*FPS))
ease=lambda x:0.5-0.5*np.cos(np.pi*min(max(x,0),1))
shadow=Image.new("L",(W,H),0)
def frame_for(i,tt):
    u=ease(tt/PER[i])
    bg=bgs[i]; z=1.0+0.08*u; bw,bh=W*1.0/z*1.0,H/z  # crop window in bg coords (bg is 1.18x cover)
    sx=bg.width/(W*1.18); cw,ch=bw*1.18*sx/1.18, bh*1.18*sx/1.18
    cw,ch=bg.width/1.18/z*1.0, bg.height/1.18/z
    dx=(bg.width-cw)*(0.35+0.3*(u if i%2==0 else 1-u)); dy=(bg.height-ch)*0.5
    fr=bg.transform((W,H),Image.EXTENT,(dx,dy,dx+cw,dy+ch),Image.BICUBIC)
    sc=0.925+0.055*(u if i%2==0 else 1-u)  # alternate in/out so crossfading cards match in size; card 0.925 -> 0.98 of full width: always fully visible
    cw2,ch2=1080*sc,1350*sc; cx,cy=W/2,225+1350*0.98/2  # card sits high, clear of YouTube's bottom title overlay
    x0,y0=cx-cw2/2,cy-ch2/2
    # inverse affine for subpixel-smooth scaling
    card=slides[i].transform((W,H),Image.AFFINE,(1/sc,0,-x0/sc,0,1/sc,-y0/sc),Image.BICUBIC)
    m=Image.new("L",(W,H),0); ImageDraw.Draw(m).rectangle((x0,y0,x0+cw2-1,y0+ch2-1),fill=255)
    sh=Image.new("L",(W,H),0); ImageDraw.Draw(sh).rectangle((x0+6,y0+14,x0+cw2+6,y0+ch2+14),fill=150); sh=sh.filter(ImageFilter.GaussianBlur(18))
    fr=Image.composite(Image.new("RGB",(W,H),(0,0,0)),fr,sh)
    fr=Image.composite(card,fr,m)
    fr.paste(ov,(0,0),ov); return fr
out=D+"/build/yt_video_noaudio.mp4"
p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
  "-c:v","libx264","-preset","slow","-crf","16","-pix_fmt","yuv420p","-r",str(FPS),out],stdin=subprocess.PIPE)
for n in range(NF):
    T=n/FPS; act=[i for i in range(N) if starts[i]<=T<starts[i]+PER[i]]
    if len(act)==1: fr=frame_for(act[0],T-starts[act[0]])
    else:
        a,b=act[0],act[-1]; al=(T-starts[b])/XF; al=float(ease(al))
        fr=Image.blend(frame_for(a,T-starts[a]),frame_for(b,T-starts[b]),al)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
# generated soft ambient pad: Cmaj9 - Am9 - Fmaj9 - Gsus, slow attack, gentle lowpassed sines, very low level
sr=48000; L=int((TOT+0.5)*sr); tt=np.arange(L)/sr; audio=np.zeros(L)
hz=lambda m:440*2**((m-69)/12)
chords=[[48,55,64,67,74],[45,52,60,67,71],[41,48,57,64,67],[43,50,60,62,67]]
seg=TOT/ (len(chords)*2)
for k in range(len(chords)*2):
    c=chords[k%4]; s0=int(k*seg*sr); s1=min(L,int((k+1)*seg*sr+1.5*sr)); n=s1-s0; x=np.arange(n)/sr
    env=np.minimum(1,x/1.6)*np.minimum(1,(n/sr-x)/1.5)
    for j,m in enumerate(c):
        f=hz(m); audio[s0:s1]+=env*(np.sin(2*np.pi*f*x+j)+0.18*np.sin(4*np.pi*f*x))*(0.9 if j else 1.1)*(1+0.08*np.sin(2*np.pi*0.2*x+j))
# soft sparkle notes
for k in range(int(TOT/2.3)):
    m=[76,79,74,72,71,67][k%6]; s0=int((1.2+k*2.3)*sr); n=int(2.2*sr)
    if s0+n>L: break
    x=np.arange(n)/sr; audio[s0:s0+n]+=0.35*np.exp(-x*1.6)*np.sin(2*np.pi*hz(m)*x)
kern=np.ones(24)/24; audio=np.convolve(audio,kern,mode="same")
fade=np.minimum(1,np.minimum(tt/2.0,(TOT+0.5-tt)/3.0)); audio*=fade
audio=audio/np.max(np.abs(audio))*0.22
st=np.stack([audio,np.roll(audio,240)],1)
with wave.open(B+"/yt_music.wav","w") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",out,"-i",B+"/yt_music.wav","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",D+"/youtube-short.mp4"],check=True)
print("duration",TOT)
