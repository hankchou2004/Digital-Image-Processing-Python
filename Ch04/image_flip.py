import numpy as np
import cv2

# 讀取原始影像
img = cv2.imread( "Baboon.bmp", -1 )
# 垂直翻轉（flipCode=0：沿 x 軸翻轉，即上下翻轉）
img1 = cv2.flip( img, 0 )
# 水平翻轉（flipCode=1：沿 y 軸翻轉，即左右翻轉）
img2 = cv2.flip( img, 1 )
cv2.imshow( "Original Image", img )
cv2.imshow( "Flip Vertically", img1 )
cv2.imshow( "Flip Horizontally", img2 )
cv2.waitKey( 0 )
