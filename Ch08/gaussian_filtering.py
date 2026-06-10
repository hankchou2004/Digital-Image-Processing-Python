import numpy as np
import cv2

# 讀取彩色影像
img1 = cv2.imread( "Baboon.bmp", -1 )
# 對彩色影像套用高斯濾波（5x5 核心）
# OpenCV 的 GaussianBlur 會同時處理 BGR 三個通道
img2 = cv2.GaussianBlur( img1, ( 5, 5 ), 0 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Gaussian Filtering", img2 )
cv2.waitKey( 0 )
