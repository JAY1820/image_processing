# Write a program to read an image and save the image in a different format.

import cv2
img = cv2.imread("D:\Programing Language\Python\image processing\image1.jpg",0)
output = "D:\Programing Language\Python\image processing\image2.jpg.jpg"
cv2.imshow('jay', img)
cv2.imwrite(output, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
