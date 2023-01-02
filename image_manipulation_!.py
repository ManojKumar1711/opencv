import random

import cv2

img_path  = "D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\img.png"

img = cv2.imread(img_path,-1)

#image representation
print(img)
print(type(img))
print(img.shape)

# the standard coloring sequence is RGB whereas in opencv we'll have the representation as BGR
# the color range : 0 - 255

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [176, 43, 123]

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()