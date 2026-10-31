import sys, numpy as np, onnxruntime as ort
from PIL import Image
so=ort.SessionOptions(); so.intra_op_num_threads=0
S=ort.InferenceSession('/workspace/models/RealESRGAN_x4plus.fp16.onnx', so)
def up(path, out, tile=192, pad=16, blend=.8):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(np.float32)/255.; H,W,_=a.shape
    o=np.zeros((H*4,W*4,3),np.float32)
    for y in range(0,H,tile):
        for x in range(0,W,tile):
            y0,x0=max(0,y-pad),max(0,x-pad); y1,x1=min(H,y+tile+pad),min(W,x+tile+pad)
            t=a[y0:y1,x0:x1].transpose(2,0,1)[None]
            r=S.run(None,{'input':t})[0][0].transpose(1,2,0)
            ty,tx=(y-y0)*4,(x-x0)*4; th,tw=min(tile,H-y)*4,min(tile,W-x)*4
            o[y*4:y*4+th, x*4:x*4+tw]=r[ty:ty+th, tx:tx+tw]
    sr=np.clip(o,0,1)
    lz=np.asarray(im.resize((W*4,H*4),Image.LANCZOS)).astype(np.float32)/255.
    res=sr*blend+lz*(1-blend)      # keep a little natural texture so it doesn't look painted
    Image.fromarray((res*255+.5).astype('uint8')).save(out, quality=97)
if __name__=='__main__':
    up(sys.argv[1], sys.argv[2])
