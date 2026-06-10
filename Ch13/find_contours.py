import numpy as np
import cv2

# 讀取二值化的幾何形狀影像
img1 = cv2.imread( "Shapes.bmp", 0 )
# 轉為彩色以便用顏色繪製輪廓
img2 = cv2.cvtColor( img1, cv2.COLOR_GRAY2BGR )
# 找到輪廓：RETR_EXTERNAL 只找最外層輪廓，CHAIN_APPROX_NONE 保留所有輪廓點
contours, hierarchy = cv2.findContours( img1, cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_NONE )
# 在彩色影像上繪製藍色輪廓（-1 表示繪製所有輪廓，thickness=2）
cv2.drawContours( img2, contours, -1, ( 255, 0, 0 ), thickness = 2 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Contours", img2 )
cv2.waitKey( 0 )
