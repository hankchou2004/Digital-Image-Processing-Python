import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Brunch.bmp", -1 )
# 邊緣保留濾波器（Edge-Preserving Filter）
# 平滑影像的同時保留邊緣，類似雙邊濾波但使用不同演算法
# 預設使用 RECURS_FILTER（遞迴式濾波，速度較快）
img2 = cv2.edgePreservingFilter( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Edge-Preserving Filter", img2 )
cv2.waitKey( 0 )
