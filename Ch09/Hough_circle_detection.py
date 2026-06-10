import numpy as np
import cv2
import math

# 讀取含有圓形物件的影像
img1 = cv2.imread( "Cans.bmp", -1 )
img2 = img1.copy( )
# 轉為灰階以進行 Hough 轉換
gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY )
# Hough 圓形偵測（梯度法）
# 參數：灰階影像、方法、dp(解析度反比)、minDist(圓心最小距離)
# param1（高閾值）=200，param2（累積器閾值）=50
# minRadius=120，maxRadius=200 限制偵測範圍
circles = cv2.HoughCircles( gray, cv2.HOUGH_GRADIENT, 1, 150, 200, 50,
                            minRadius = 120, maxRadius = 200 )
circles = np.uint16( np.around( circles ) )
# 在影像上繪製偵測到的圓形
for i in circles[0,:]:
	# 繪製圓形邊界（綠色）
	cv2.circle( img2, ( i[0], i[1] ), i[2], ( 0, 255, 0 ), 2 )
	# 繪製圓心（紅色點）
	cv2.circle( img2, ( i[0], i[1] ), 2, ( 0, 0, 255 ), 3 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Circle Detection", img2 )
cv2.waitKey( 0 )
