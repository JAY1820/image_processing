
# #scalled image
# matrix_scale=np.float32([[0.5,0,0],[0,0.5,0]])
# scalled_img=cv2.warpAffine(img1,matrix_scale,(img1.shape[1],img1.shape[0]))
# cv2.imshow('scalled image',scalled_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #rotated image
# rows,cols,ch=img1.shape
# matrix_roate=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# rotated_img=cv2.warpAffine(img1,matrix_roate,(cols,rows))
# cv2.imshow('rotated image',rotated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


