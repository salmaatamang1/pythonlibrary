import cv2 as cv
img=cv.imread("images/sunflower1.jpg")
cv.imshow("real",img)

#converting to gray color
gray=cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
cv.imshow('Gray',gray)


#bluring images
blur=cv.GaussianBlur(img,(7,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#canning of an image
canny=cv.Canny(img,175,125)
cv.imshow('canny',canny)

#cropping of an image
cropped=img[250:650,300:500]
cv.imshow("Cropping",cropped)

#resizing of an image
resize=cv.resize(img,(250,250),interpolation=cv.INTER_AREA)
cv.imshow("resized",resize)
cv.waitKey(0)