#calculate video duration and frame per second
import datetime
import cv2

vid=cv2.VideoCapture('D:\\Programing Language\\Python\\image processing\\image\\video1.mp4')

frames=vid.get(cv2.CAP_PROP_FRAME_COUNT)
fps=vid.get(cv2.CAP_PROP_FPS)

#calculate video duration
seconds=round(frames/fps)
video_time=str(datetime.timedelta(seconds=seconds))
print('Total frames:',frames)
print(f"Frames per second: {seconds}")
print(f"video time: {video_time}")

#release the video capture object
vid.release()
cv2.destroyAllWindows()
