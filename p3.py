# We can read image using imread() function and display using imshow() function
#we also display shape , size , dimension of image
import cv2

imgpath = "D:\Programing Language\Python\image processing\image1.jpg"
img=cv2.imread(imgpath,1)

print(type(img))
print('image data type',img.dtype)
print('image shape',img.shape)
print('image dimension',img.ndim)
print('image size',img.size)

# nr,nc,ch are the variables store dimension of image
(nr,nc,ch)=img.shape

print('no of rows',nr)
print('no of columns',nc)
print('no of channels',ch)

output = "D:\Programing Language\Python\image processing\image2.jpg.jpg"
cv2.imshow('jay', img)
cv2.imwrite(output, img)
cv2.waitKey(0)
cv2.destroyAllWindows()