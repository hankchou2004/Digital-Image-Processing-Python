import numpy as np
import cv2
from numpy.random import normal

def gaussian_noise( f, scale ):		# 高斯雜訊：加入均值為0、標準差為 scale 的高斯隨機值
	g = f.copy( )
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + normal( 0, scale )
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

# 計算峰值訊噪比（PSNR）：評估影像失真程度的客觀指標
def PSNR( f, g ):					# 數值越高表示影像品質越好（通常 >30dB 表示品質良好）
	nr, nc = f.shape[:2]
	MSE = 0.0
	# 計算均方誤差（MSE）
	for x in range( nr ):
		for y in range( nc ):
			MSE += ( float( f[x,y] ) - float( g[x,y] ) ) ** 2
	MSE /= ( nr * nc )
	# PSNR = 10 * log10(MAX^2 / MSE)，MAX=255 for 8-bit image
	PSNR = 10 * np.log10( ( 255 * 255 ) / MSE )
	return PSNR

def main( ):
	f = cv2.imread( "Brunch.bmp", 0 )
	# 加入標準差為 20 的高斯雜訊
	g = gaussian_noise( f, 20 )
	print( "PSNR =", PSNR( f, g ) )
	cv2.imshow( 'Original Image', f )
	cv2.imshow( 'Gaussian Noise', g )
	cv2.waitKey( 0 )

main( )
