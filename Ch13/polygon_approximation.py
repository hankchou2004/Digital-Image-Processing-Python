import numpy as np
import cv2

# 使用 Douglas-Peucker 演算法對輪廓進行多邊形近似
def polygon_approximation( f, epislon ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 找到最外層輪廓
	contours, hierarchy = cv2.findContours( f,
	              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	# 多邊形近似：epsilon 越大，近似誤差越大，頂點越少
	approx = cv2.approxPolyDP( contours[0], epislon, True )
	# 以灰色顯示原始物件
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	# 繪製近似多邊形（白色）
	cv2.drawContours( g, [approx], -1, ( 255, 255, 255 ) )
	return g

def main( ):
	# epsilon 越大，近似的多邊形頂點越少（形狀越簡化）
	epislon = eval( input( "Please enter epislon:" ) )
	img1 = cv2.imread( "Bug.bmp", 0 )
	img2 = polygon_approximation( img1, epislon )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Polygon Approximation", img2 )
	cv2.waitKey( 0 )

main( )
