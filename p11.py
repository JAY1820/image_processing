#image resizing
import cv2
import numpy as np

imgpath = "D:\Programing Language\Python\image processing\image7.jpg"
img = cv2.imread(imgpath, 0)

# nr, nc, ch are the variables store dimension of image
(nr, nc, ch) = img.shape
cv2.imshow('jay', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

a = []
samplerate = 8
x = int(img.shape[0] / samplerate)
y = int(img.shape[1] / samplerate)
for i in range(0, img.shape[0], x):
    for j in range(0, img.shape[1], y):
        a.append(img[i][j])
b = np.reshape(a, (x, y))
bsize = b.shape
print(bsize)
cv2.imshow('jay', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
imgRsz = cv2.resize(b, (img.shape[0], img.shape[1]))
cv2.imshow('jay', imgRsz)
cv2.waitKey(0)
cv2.destroyAllWindows()
a.clear()

