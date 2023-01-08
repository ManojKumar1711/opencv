import cv2
import numpy as np

imgpath1 = 'D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\soccer_match.png'
imgpath2 = 'D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\shoe.png'

img = cv2.resize(cv2.imread(imgpath1,0),(0,0),fx=0.5,fy=0.5)
template = cv2.resize(cv2.imread(imgpath2,0),(0,0),fx=0.5,fy=0.5)

h,w = template.shape
#print(img)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
    #print(min_loc,max_loc)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:#these both are based on minimum values and minimum locations
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0]+w,location[1]+h)


    cv2.rectangle(img,location,bottom_right,255,5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
