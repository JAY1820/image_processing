# We will use this file to check if OpenCV is installed or not.
try:
    import cv2
    print("OpenCV (cv2) is installed.")
    print("OpenCV version:", cv2.__version__)
except ImportError:
    print("OpenCV (cv2) is not installed.")
