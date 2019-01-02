import cv2
import numpy as np
from functools import reduce
from PIL import Image
import subprocess

def merge_bbox(box1, box2):
    x1,y1,w1,h1 = box1
    x2,y2,w2,h2 = box2
    newx,newy,neww,newh = 0,0,0,0

    newx,newy = min(x1,x2), min(y1,y2)

    c1,d1 = x1+w1,y1+h1
    c2,d2 = x2+w2,y2+h2
    newc,newd = max(c1,c2), max(d1,d2)

    neww,newh = (newc-newx),(newd-newy)

    return newx,newy,neww,newh

def trans2white(src, dst):
    ## Convert transparent background into white
    image = Image.open(src).convert("RGBA")
    pixel_data = image.load()
    if image.mode == "RGBA":
        # If the image has an alpha channel, convert it to white
        # Otherwise we'll get weird pixels
        for y in range(image.size[1]): # For each row ...
            for x in range(image.size[0]): # Iterate through each column ...
                # Check if it's opaque
                if pixel_data[x, y][3] < 255:
                    # Replace the pixel data with the colour white
                    pixel_data[x, y] = (255, 255, 255, 255)
    image.convert('RGB').save(dst)

PAD = 3

def crop_to_contents(src, dst):
    img = cv2.imread(src)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, \
                                       type=cv2.THRESH_BINARY_INV)

    # cv2.imshow('img', img)
    # cv2.imshow('gra', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Find bboxes for all contours
    image, contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                       cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    bboxes = [cv2.boundingRect(cont) for cont in contours]
    areas = [w*h for _,_,w,h in bboxes]

    # Sort bboxes by area
    conts = list(zip(bboxes, areas))
    top_areas = sorted(conts, key=lambda x: x[1])
    top_bboxes = [box for box,area in top_areas]

    # Create one big bbox
    merged = reduce(merge_bbox, top_bboxes)
    # print(top_areas)
    # print(merged, merged[2]*merged[3])
    # print(img.shape, img.shape[0]*img.shape[1])

    # # Show bbox on image
    # for (x,y,w,h) in top_bboxes:
    #     cv2.rectangle(img,(x-PAD,y-PAD),(x+w+PAD,y+h+PAD),(200,0,0),2)

    # cv2.imshow('rois', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    x,y,w,h = merged
    startx,starty = max(x-PAD,0),max(y-PAD,0)
    x,y,w,h = startx,starty,w+PAD,h+PAD
    roi=img[y:y+h,x:x+w]

    cv2.imwrite(dst, roi)

def sprite2ansi(src, dst):
    result = subprocess.run("python img2txt-gh-pages\img2txt.py {} --ansi --maxLen=30 --targetAspect=0.5 --bgcolor=#FFFFFF".format(src), stdout=subprocess.PIPE)
    with open(dst, 'wb') as f:
        f.write(result.stdout)

