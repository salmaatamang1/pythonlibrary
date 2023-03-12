import cv2 as cv
import numpy as np

img=cv.imread("images/nature.jpg")

resize=cv.resize(img,(300,300),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized original",resize)

blank=np.zeros(resize.shape[:2],dtype='uint8')

b,g,r=cv.split(resize)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

cv.waitKey(0)


