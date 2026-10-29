# Removes the visible house number (porch fascia) and the round blue address sign from the Davis House photo (no visible house numbers rule).
import cv2,numpy as np
im=cv2.imread('src/alg-davis-house.jpg')
m=np.zeros(im.shape[:2],np.uint8)
g=cv2.cvtColor(im[1360:1415,2830:2895],cv2.COLOR_BGR2GRAY); m[1360:1415,2830:2895]=(g<120).astype(np.uint8)*255
m=cv2.dilate(m,np.ones((7,7),np.uint8))
h=cv2.cvtColor(im,cv2.COLOR_BGR2HSV); sub=h[1525:1625,590:700]
blue=((sub[...,0]>95)&(sub[...,0]<135)&(sub[...,1]>60)).astype(np.uint8)*255
cnts,_=cv2.findContours(cv2.dilate(blue,np.ones((9,9),np.uint8)),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE); c=max(cnts,key=cv2.contourArea)
z=np.zeros_like(blue); cv2.drawContours(z,[cv2.convexHull(c)],-1,255,-1); z=cv2.dilate(z,np.ones((9,9),np.uint8)); m[1525:1625,590:700]|=z
out=cv2.inpaint(im,m,11,cv2.INPAINT_TELEA)
# brick texture: copy the same brick rows from just right of the sign into the sign area (rows align horizontally)
zz=np.zeros(im.shape[:2],bool); zz[1525:1625,590:700]=z>0
for dx in (96,):
    ys,xs=np.nonzero(zz); out[ys,xs]=im[ys+dx,xs]
soft=cv2.GaussianBlur(zz.astype(np.float32),(0,0),2)[...,None]; out=(out*1.0).astype(np.uint8); cv2.imwrite('src/alg-davis-house-clean.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,97])
cv2.imwrite('/tmp/n1c.png',out[1300:1480,2700:3050]);cv2.imwrite('/tmp/n2c.png',out[1480:1660,500:780])
