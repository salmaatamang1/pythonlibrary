import cv2 as cv

i=cv.imread("images/kitten.jpg")
img=cv.resize(i,(400,350),interpolation=cv.INTER_AREA)
cv.imshow("real img",img)

#averaging
avg=cv.blur(img,(3,3))
cv.imshow("Averaging smooting filter",avg)

#gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian blur smoothing filter",gauss)

#median bluring
med=cv.medianBlur(img,3)
cv.imshow("Median bluring",med)

#bilateral bluring
bilateral=cv.bilateralFilter(img,5,55,55)
cv.imshow("Bilateral bluring",bilateral)

cv.waitKey(0)