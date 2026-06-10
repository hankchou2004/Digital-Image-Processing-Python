import numpy as np
import cv2

# 讀取過度曝光的影像（直方圖集中於高灰階端）
img1 = cv2.imread( "Indoor_Over_Exposure.bmp", -1 )
# 直方圖均衡化：重新分配像素強度，使直方圖均勻分布
# 可有效改善過亮、過暗或對比度不足的影像
img2 = cv2.equalizeHist( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Histogram Equalization", img2 )
cv2.waitKey( 0 )
