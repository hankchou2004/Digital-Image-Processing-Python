import numpy as np
import cv2

# 魚眼效果：使用極座標映射模擬廣角鏡頭的桶形失真
def fisheye_effect( f ):
	nr, nc = f.shape[:2]
	# 建立映射表（對每個輸出像素，記錄對應的輸入像素座標）
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	# 以影像中心為圓心
	x0, y0 = nr // 2, nc // 2
	# 最大半徑（對角線長的一半）
	R = np.sqrt( nr ** 2 + nc ** 2 ) / 2
	for x in range( nr ):
		for y in range( nc ):
			# 計算每個像素到中心的距離和角度
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			# 魚眼效果：用 r² 代替 r（使靠近邊緣的像素更往外推）
			r = ( r * r ) / R
			if y - y0 < 0:  theta = -theta
			# 計算映射座標
			map_x[x,y] = np.clip( y0 + r * np.sin( theta ), 0, nc - 1 )
			map_y[x,y] = np.clip( x0 + r * np.cos( theta ), 0, nr - 1 )
	# 使用三次內插進行重映射
	g = cv2.remap( f, map_x, map_y, cv2.INTER_CUBIC )
	return g

def main( ):
	img1 = cv2.imread( "Bug.bmp", -1 )
	img2 = fisheye_effect( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Fisheye Effect", img2 )
	cv2.waitKey( 0 )

main( )
