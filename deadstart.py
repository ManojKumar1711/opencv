import cv2

img_path = "D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\stark.jpg"
img = cv2.imread(img_path,0)
img = cv2.resize(img,(0,0),fx=2,fy=2)
img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imwrite('new_jpg.jpg',img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 

