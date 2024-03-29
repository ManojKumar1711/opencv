import numpy as np
import cv2

imgpath = 'D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\chessboard.png'
img = cv2.imread(imgpath)
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

#print(corners)

for corner in corners:
    x, y = corner.ravel()
    #print(x,y)
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = corners[i][0]
        corner2 = corners[j][0]
        #color = tuple(map(lambda x:int(x),np.random.randint(0,255,size=4)))
        cv2.line(img, corner1, corner2, (47, 56, 134), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
