import cv2

img_path  = "D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\img.png"

img = cv2.imread(img_path,-1)

#image representation
print(img)
print(type(img))
print(img.shape)

tag = img[10:110,150:250]
img[50:150,100:200] = tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
