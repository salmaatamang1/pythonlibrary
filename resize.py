import cv2 as cv

def frame_resize(frame,scale=1.75):#function defination for resizing
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return(cv.resize(frame,dimension,interpolation=cv.INTER_AREA))

capture=cv.VideoCapture('videos/video1.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=frame_resize(frame)#function call
    cv.imshow('old video',frame)
    cv.imshow('new video',frame_resized)
    if cv.waitKey(20)&0xff==ord('d'):
        break

capture.release()
cv.displayAllWindows()