import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Lenna.bmp", -1 )
# 套用高斯濾波（高斯模糊）
# 核心大小為 5x5，sigmaX=0 表示由核心大小自動計算標準差
# 高斯濾波的特點：對高斯雜訊有良好的去除效果，且保留較多邊緣細節
img2 = cv2.GaussianBlur( img1, ( 5, 5 ), 0 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Gaussian Filtering", img2 )
cv2.waitKey( 0 )
