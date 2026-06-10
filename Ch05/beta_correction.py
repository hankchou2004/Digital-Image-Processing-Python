import numpy as np
import cv2
import scipy.special as special

# Beta 函數校正：利用不完全 Beta 函數建立灰階映射表
def beta_correction( f, a = 2.0, b = 2.0 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 建立 0~1 的等差數列作為輸入
	x = np.linspace( 0, 1, 256 )
	# 計算不完全 Beta 函數值並映射到 0~255 範圍
	table = np.round( special.betainc( a, b, x ) * 255, 0 )
	if f.ndim != 3:
		# 灰階影像：直接套用映射表
		for x in range( nr ):
			for y in range( nc ):
				g[x,y] = table[f[x,y]]
	else:
		# 彩色影像：對每個色彩通道套用映射表
		for x in range( nr ):
			for y in range( nc ):
				for k in range( 3 ):
					g[x,y,k] = table[f[x,y,k]]
	return g

def main( ):
	img = cv2.imread( "Building.bmp", 0 )
	# a=b=0.5：S 形曲線，增強對比（低灰階更暗，高灰階更亮）
	img1 = beta_correction( img, a = 0.5, b = 0.5 )
	# a=b=2.0：反 S 形曲線，壓縮對比（中間灰階增強）
	img2 = beta_correction( img, a = 2.0, b = 2.0 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Beta Correction (a = b = 0.5)", img1 )
	cv2.imshow( "Beta Correction (a = b = 2.0)", img2 )
	cv2.waitKey( 0 )

main( )
