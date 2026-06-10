import numpy as np
import cv2

# 波紋效果（Ripple Effect）：利用正弦函數扭曲影像座標，模擬水面波紋
def ripple_effect( f, method, amplitude, period ):
	nr, nc = f.shape[:2]
	# 建立映射表（記錄每個輸出像素對應的輸入座標）
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	x0, y0 = nr // 2, nc // 2
	for x in range( nr ):
		for y in range( nc ):
			if method == 1:		# x 方向波紋（上下波動）
				xx = np.clip( x + amplitude * np.sin( x / period ), 0, nr - 1 )
				map_x[x,y] = y
				map_y[x,y] = xx
			elif method == 2:	# y 方向波紋（左右波動）
				yy = np.clip( y + amplitude * np.sin( y / period ), 0, nc - 1 )
				map_x[x,y] = yy
				map_y[x,y] = x
			elif method == 3:	# x 和 y 雙方向波紋（斜向波動）
				xx = np.clip( x + amplitude * np.sin( x / period ), 0, nr - 1 )
				yy = np.clip( y + amplitude * np.sin( y / period ), 0, nc - 1 )
				map_x[x,y] = yy
				map_y[x,y] = xx
			else:				# 徑向波紋（以中心向外擴散的圓形波紋）
				r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
				if r == 0:  theta = 0
				else:		theta = np.arccos( ( x - x0 ) / r )
				# 對徑向距離套用正弦波動
				r = r + amplitude * np.sin( r / period )
				if y - y0 < 0:  theta = -theta
				map_x[x,y] = np.clip( y0 + r * np.sin( theta ), 0, nc - 1 )
				map_y[x,y] = np.clip( x0 + r * np.cos( theta ), 0, nr - 1 )
	# 使用雙線性內插進行重映射
	g = cv2.remap( f, map_x, map_y, cv2.INTER_LINEAR )
	return g

def main( ):
	img1 = cv2.imread( "Snow_Mountain.bmp", -1 )
	# x 方向波紋，振幅=5，週期=2
	img2 = ripple_effect( img1, 1, 5, 2 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Ripple Effect", img2 )
	cv2.waitKey( 0 )

main( )
