import cv2 as cv

img=cv.imread('images/sunflower1.jpg')
cv.imshow("Original",img)

#converting image from BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#converting image from BGR TO LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#conveting image bgr to luv
luv=cv.cvtColor(img,cv.COLOR_BGR2LUV)
cv.imshow('luv',luv)

hls=cv.cvtColor(img,cv.COLOR_BGR2HLS)
cv.imshow('HLS',hls)


#now we will convert image from HSV to BGR
hsvtobgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsvtobgr",hsvtobgr)
cv.waitKey(0)


#note we cannot directly convert imag from hsv to lab or any 
# thing else except bgr .To convert from hsv to
#  lab convert hsv to bgr and then to lab