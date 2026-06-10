import numpy as np
import cv2

# 計算並繪製物件輪廓的凸包（Convex Hull）
# 凸包：包含物件所有點的最小凸多邊形
def convex_hull( f ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 找到所有最外層輪廓
	contours, hierarchy = cv2.findContours( f,
	              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	hull = []
	# 計算每個輪廓對應的凸包
	for i in range( len( contours ) ):
		hull.append( cv2.convexHull( contours[i], False ) )
	# 將前景像素設為較暗的灰色
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	# 繪製輪廓（白色細線）
	cv2.drawContours( g, contours, -1, ( 255, 255, 255 ), 1, 8 )
	# 繪製凸包（白色粗線，覆蓋在輪廓上方）
	cv2.drawContours( g, hull, -1, ( 255, 255, 255 ), 2, 8 )
	return g

def main( ):
	img1 = cv2.imread( "Hand.bmp", 0 )
	img2 = convex_hull( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Convex Hull", img2 )
	cv2.waitKey( 0 )

main( )
