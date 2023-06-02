#video resolution

import cv2

#read video
vid=cv2.VideoCapture('D:\\Programing Language\\Python\\image processing\\image\\video1.mp4')

if(vid.isOpened()==False):
    print('Error opening video file')
    exit(1)

while(vid.isOpened()):
    ret,frame=vid.read()
    if ret==True:
        cv2.imshow('jay',frame)
        #20 is in milliseconds, try to increase or decrease it
        key=cv2.waitKey(2000)
        if key==ord('q'):
            break
        else:
            break

    #release the video capture object
    vid.release()
    cv2.destroyAllWindows()

   