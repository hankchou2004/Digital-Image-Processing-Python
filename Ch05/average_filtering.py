import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Lenna.bmp", -1 )
# 套用平均濾波（均值模糊），核心大小為 5x5
# 每個像素值取周圍 5x5 範圍的平均值，達到模糊雜訊的效果
img2 = cv2.blur( img1, ( 5, 5 ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Average Filtering", img2 )
cv2.waitKey( 0 )
