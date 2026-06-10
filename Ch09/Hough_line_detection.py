import numpy as np
import cv2
import math

# 讀取含有車道線的影像
img1 = cv2.imread( "Traffic_Lanes.bmp", -1 )
img2 = img1.copy( )
# 轉為灰階以進行邊緣偵測
gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY )
# 先用 Canny 偵測邊緣
edges = cv2.Canny( gray, 50, 200 )
# Hough 直線偵測：在極座標空間中搜尋直線
# 參數：邊緣影像、距離解析度=1、角度解析度=1度、累積閾值=120
lines = cv2.HoughLines( edges, 1, math.pi/180.0, 120 )
# 將偵測到的直線繪製在影像上
if lines is not None:
	a,b,c = lines.shape
	for i in range( a ):
		# 取得直線的極座標參數（rho：距離，theta：角度）
		rho = lines[i][0][0]
		theta = lines[i][0][1]
		a = math.cos( theta )
		b = math.sin( theta )
		x0, y0 = a*rho, b*rho
		# 計算直線的兩個端點（延伸至影像邊界外）
		pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
		pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
		# 繪製藍色直線
		cv2.line( img2, pt1, pt2, ( 255, 0, 0 ), 1, cv2.LINE_AA )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Canny Edge Detection", edges )
cv2.imshow( "Hough Line Detection", img2 )
cv2.waitKey( 0 )
