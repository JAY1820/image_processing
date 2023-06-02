#live video capture using webcam and save it
import cv2
vid=cv2.VideoCapture(0)

#we need to set the resolution of the video,so convert float to integer
frame_width=int(vid.get(3))
frame_height=int(vid.get(4))
size=(frame_width,frame_height)

# result=cv2.VideoWriter('myvideo.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,size)
result2=cv2.VideoWriter('myvideo2.mp4',cv2.VideoWriter_fourcc(*'mp4v'),30,size)

while(True):
    ret,frame=vid.read()
    if ret==True:
        #write the frame into the file 'myvideo.avi'
        # result.write(frame)
        result2.write(frame)
        # cv2.imshow('jay',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()



   
