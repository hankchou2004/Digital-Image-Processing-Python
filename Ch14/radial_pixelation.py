import numpy as np
import cv2

# 徑向像素化（Radial Pixelation）：以極座標為基礎對影像進行區塊化，產生放射狀馬賽克效果
def radial_pixelation( f, delta_r, delta_theta ):
	nr, nc = f.shape[:2]
	# 建立映射表
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	# 以影像中心為極座標原點
	x0, y0 = nr // 2, nc // 2
	for x in range( nr ):
		for y in range( nc ):
			# 轉換為極座標（r：半徑，theta：角度）
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			# 對半徑和角度進行量化（四捨五入到最近的 delta_r 和 delta_theta）
			r = r - r % delta_r           # 半徑量化
			if y - y0 < 0:  theta = -theta
			theta = theta - theta % ( np.radians( delta_theta ) )  # 角度量化
			# 計算量化後的像素座標
			map_x[x,y] = np.clip( y0 + r * np.sin( theta ), 0, nc - 1 )
			map_y[x,y] = np.clip( x0 + r * np.cos( theta ), 0, nr - 1 )
	# 使用雙線性內插進行重映射
	g = cv2.remap( f, map_x, map_y, cv2.INTER_LINEAR )
	return g

def main( ):
	img1 = cv2.imread( "Peacock.bmp", -1 )
	# delta_r=5（半徑量化步階），delta_theta=5（角度量化步階，單位：度）
	img2 = radial_pixelation( img1, 5, 5 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Radial Pixelation", img2 )
	cv2.waitKey( 0 )

main( )
