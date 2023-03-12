import cv2 as cv

# img=cv.imread('images/elephant.jpg')

# cv.imshow('Animal',img)
# cv.waitKey(0)

#reading videos
capture=cv.VideoCapture('videos/video1.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('nature',frame)
    if cv.waitKey(50)&0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()