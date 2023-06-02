#live video capture using webcam
import cv2


vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()
    #display the frame
    cv2.imshow('jay',frame)
    #the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()



   
