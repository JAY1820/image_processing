# color image processing
#spliting into rgb

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pylab

imgpath = "D:\Programing Language\Python\image processing\image\image7.jpg"

img1=cv2.imread(imgpath,1)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.title('color image')
#the xticks() and yticks() function takes a list object as argument. 
# The elements of this list is the value of the ticks.
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('original color',img1)
cv2.waitKey(0)
#spliting into rgb
b,g,r=cv2.split(img1)
rgb_img=cv2.merge([r,g,b])
cv2.imshow('color image',rgb_img)
cv2.waitKey(0)
cv2.imshow('blue component',b)
cv2.waitKey(0)
cv2.imshow('green component',g)
cv2.waitKey(0)
cv2.imshow('red component',r)
cv2.waitKey(0)
cv2.destroyAllWindows()


