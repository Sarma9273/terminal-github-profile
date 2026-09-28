#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import argparse

def largest_component(binary):
    count, labels, stats, _ = cv2.connectedComponentsWithStats(binary, 8)
    if count <= 1: return binary
    largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    return np.where(labels == largest, 255, 0).astype(np.uint8)

def build_subject_mask(image):
    rgb = np.array(image.convert("RGB"))
    h, w = rgb.shape[:2]
    seg_w = min(520, w)
    seg_h = max(1, round(h * seg_w / w))
    small = cv2.resize(rgb, (seg_w, seg_h), interpolation=cv2.INTER_AREA)
    bgr = cv2.cvtColor(small, cv2.COLOR_RGB2BGR)
    mask = np.full((seg_h, seg_w), cv2.GC_PR_BGD, dtype=np.uint8)
    border = max(5, int(seg_w * .018))
    mask[:border,:] = cv2.GC_BGD; mask[-border:,:] = cv2.GC_BGD
    mask[:,:border] = cv2.GC_BGD; mask[:,-border:] = cv2.GC_BGD
    cx = seg_w // 2
    cv2.ellipse(mask,(cx,int(seg_h*.36)),(int(seg_w*.23),int(seg_h*.26)),0,0,360,cv2.GC_PR_FGD,-1)
    torso=np.array([[int(seg_w*.12),int(seg_h*.58)],[int(seg_w*.88),int(seg_h*.58)],
                    [int(seg_w*.98),int(seg_h*.98)],[int(seg_w*.02),int(seg_h*.98)]],dtype=np.int32)
    cv2.fillConvexPoly(mask,torso,cv2.GC_PR_FGD)
    cv2.ellipse(mask,(cx,int(seg_h*.39)),(int(seg_w*.12),int(seg_h*.15)),0,0,360,cv2.GC_FGD,-1)
    cv2.rectangle(mask,(int(seg_w*.30),int(seg_h*.68)),(int(seg_w*.70),int(seg_h*.94)),cv2.GC_FGD,-1)
    bg=np.zeros((1,65),np.float64); fg=np.zeros((1,65),np.float64)
    cv2.grabCut(bgr,mask,None,bg,fg,5,cv2.GC_INIT_WITH_MASK)
    binary=np.where((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD),255,0).astype(np.uint8)
    binary=largest_component(binary)
    binary=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8),iterations=2)
    binary=cv2.morphologyEx(binary,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=1)
    binary=cv2.GaussianBlur(binary,(5,5),0)
    return Image.fromarray(binary).resize((w,h),Image.Resampling.LANCZOS)

def cover_crop_box(w,h,ratio):
    src=w/h
    if src>ratio:
        cw=int(h*ratio); left=(w-cw)//2
        return left,0,left+cw,h
    ch=int(w/ratio); top=(h-ch)//2
    return 0,top,w,top+ch

def generate(image_path,output_path):
    image=Image.open(image_path).convert("RGBA")
    mask=build_subject_mask(image)
    W,H=760,980; TOP,BOTTOM,SPACING=58,42,8
    DURATION,REVEAL_END,HOLD_END=8.5,5.7,7.6
    draw_h=H-TOP-BOTTOM
    crop=cover_crop_box(image.width,image.height,W/draw_h)
    gray=image.convert("L").crop(crop); subject=mask.crop(crop)
    cols,rows=W//SPACING,draw_h//SPACING
    gray_small=ImageEnhance.Contrast(gray.resize((cols,rows),Image.Resampling.LANCZOS)).enhance(1.20)
    mask_small=subject.resize((cols,rows),Image.Resampling.LANCZOS)
    circles=[]; total=max(1,rows*cols-1)
    for y in range(rows):
        for x in range(cols):
            if mask_small.getpixel((x,y))<125: continue
            lum=gray_small.getpixel((x,y))/255
            radius=.72+(lum**.90)*2.25; opacity=.42+lum*.58
            cx=x*SPACING+SPACING/2; cy=TOP+y*SPACING+SPACING/2
            raster=(y*cols+x)/total
            appear=.65+raster*(REVEAL_END-.65); appear2=min(appear+.08,HOLD_END)
            kt=f"0;{appear/DURATION:.6f};{appear2/DURATION:.6f};{HOLD_END/DURATION:.6f};1"
            circles.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius:.2f}" fill="#78ff9c" fill-opacity="{opacity:.3f}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt}" dur="{DURATION}s" repeatCount="indefinite"/><animate attributeName="r" values="{radius:.2f};{radius:.2f};{radius*1.75:.2f};{radius:.2f};{radius:.2f}" keyTimes="{kt}" dur="{DURATION}s" repeatCount="indefinite"/></circle>')
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="#000"/>{"" .join(circles)}</svg>'
    output_path.write_text(svg,encoding="utf-8")
    print(f"Generated {output_path} ({len(circles):,} dots)")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("image",type=Path); p.add_argument("-o","--output",type=Path,default=Path("portrait.svg"))
    a=p.parse_args()
    if not a.image.exists(): raise SystemExit(f"Input image not found: {a.image}")
    generate(a.image,a.output)
