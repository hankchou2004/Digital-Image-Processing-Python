import numpy as np
import cv2

# 漩渦效果（Twirl Effect）：以極座標為基礎，對每個像素加上與半徑成正比的旋轉角度
def twirl_effect( f, K ):
	nr, nc = f.shape[:2]
	# 建立映射表
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	# 以影像中心為旋轉中心
	x0, y0 = nr // 2, nc // 2
	for x in range( nr ):
		for y in range( nc ):
			# 計算像素到中心的距離和角度
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			if y - y0 < 0:  theta = -theta
			# 旋轉量 r/K：距中心越遠的像素旋轉越多（K 越小，漩渦越強烈）
			phi = theta + r / K
			# 計算映射後的座標
			map_x[x,y] = np.clip( y0 + r * np.sin( phi ), 0, nc - 1 )
			map_y[x,y] = np.clip( x0 + r * np.cos( phi ), 0, nr - 1 )
	# 使用雙線性內插進行重映射
	g = cv2.remap( f, map_x, map_y, cv2.INTER_LINEAR )
	return g

def main( ):
	img1 = cv2.imread( "Car.bmp", -1 )
	# K=50：漩渦強度適中
	img2 = twirl_effect( img1, 50 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Twirl Effect", img2 )
	cv2.waitKey( 0 )

main( )
