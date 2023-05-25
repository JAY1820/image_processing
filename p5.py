#image histogram

import cv2
import matplotlib.pyplot as plt

imgpath = "D:\Programing Language\Python\image processing\image1.jpg"
img1=cv2.imread(imgpath,1)

#find a frequency of each pixel value in grayscale image in range 0-255
#none is for mask -  which means the entire image will be used to calculate the histogram
#256 is for number of bins
#0-255 is for range
hist1=cv2.calcHist([img1],[0],None,[256],[0,255])
plt.plot(hist1)
plt.show()

#equalize histogram - it is used to improve contrast of image
img2=cv2.equalizeHist(img1)
hist2=cv2.calcHist([img2],[0],None,[256],[0,255])
plt.plot(hist2)
plt.show()
