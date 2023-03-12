import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)

#to print a certain images
# blank[200:300,200:250]=0,225,0
# cv.imshow('blank',blank)
#to drawvrectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,225),thickness=-1)
cv.imshow('rectangle',blank)

# to draw cirlce
cv.circle(blank,(blank.shape[1]//4,blank.shape[0]//4),50,(0,225,0),thickness=-1)
cv.imshow('cirlce',blank)


#to draw line
cv.line(blank,(0,255),(0,400),(225,8.50,0),thickness=9)
cv.imshow('line',blank)

#to write text in image
cv.putText(blank,'Bangladesh Flag',(25,300),cv.FONT_HERSHEY_COMPLEX,1,(200,25,125),thickness=2)
cv.imshow('Bangladeshflag',blank)
cv.waitKey(0)