import cv2

#copying one part of the image to another part of the same image

img_path  = "D:\\Manoj\\Arena\\OpenCv\\breeze\\assets\\logo.jpg"
img = cv2.imread(img_path,-1)

print(img.shape)
print(img.ndim)

removed = img[500:700,600:900]
img[100:300,650:950] = removed

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
