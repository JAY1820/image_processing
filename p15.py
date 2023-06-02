
#check video properties
import cv2

#read video
vid=cv2.VideoCapture('D:\\Programing Language\\Python\\image processing\\image\\video1.mp4')

if(vid.isOpened()==False):
    print('Error opening video file')
    exit(1)
    
#showing video resolution
print('Frame width:',vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame height:',vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame rate:',vid.get(cv2.CAP_PROP_FPS))
print('Frame count:',vid.get(cv2.CAP_PROP_FRAME_COUNT))