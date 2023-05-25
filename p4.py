# gray image conversion into negative image using opencv and matplotlib library

import cv2
import matplotlib.pyplot as plt

imgpath = "D:\Programing Language\Python\image processing\image1.jpg"

img1=cv2.imread(imgpath,1)
img2=abs(255-img1)

titles=['original image','negative image']
images=[img1,img2]
for k in range(2):
    #sublpot(nrows,ncols,index)
    plt.subplot(1,2,k+1)
    #cmap is color map
    plt.imshow(images[k],cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()    

#using a power law transformation
#im1c=cv2.pow(im,0.5)
#im=img1/255.0
#im1c*cv2.pow(im,0.5)


