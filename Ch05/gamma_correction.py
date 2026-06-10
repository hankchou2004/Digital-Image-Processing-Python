import numpy as np
import cv2

# Gamma 校正：對影像強度套用冪次函數 g = c * f^gamma
def gamma_correction( f, gamma = 2.0 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 計算正規化常數 c，使輸入 255 對應輸出 255
	c = 255.0 / ( 255.0 ** gamma )
	# 預先建立 256 個灰階值的映射查找表（加速計算）
	table = np.zeros( 256 )
	for i in range( 256 ):
		table[i] = round( i ** gamma * c, 0 )
	if f.ndim != 3:
		# 灰階影像：套用查找表
		for x in range( nr ):
			for y in range( nc ):
				g[x,y] = table[f[x,y]]
	else:
		# 彩色影像：對每個色彩通道套用查找表
		for x in range( nr ):
			for y in range( nc ):
				for k in range( 3 ):
					g[x,y,k] = table[f[x,y,k]]
	return g

def main( ):
	img = cv2.imread( "Museum.bmp", 0 )
	# gamma < 1：影像變亮（適合過暗的影像）
	img1 = gamma_correction( img, 0.1 )
	img2 = gamma_correction( img, 0.2 )
	img3 = gamma_correction( img, 0.5 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Gamma = 0.1", img1 )
	cv2.imshow( "Gamma = 0.2", img2 )
	cv2.imshow( "Gamma = 0.5", img3 )
	cv2.waitKey( 0 )

main( )
