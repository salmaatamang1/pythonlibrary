import cv2 as cv
import numpy as np
img=cv.imread("images/nature.jpg")

resize=cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
cv.imshow("Resized image",resize)

b,g,r=cv.split(resize)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)
print(resize.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow("Merged images",merged)

cv.waitKey(0)
