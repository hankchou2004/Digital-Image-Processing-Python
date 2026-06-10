import numpy as np
import cv2
from numpy.fft import fft2, ifft2

# 高斯低通濾波器（用於模擬影像退化）
def gaussian_lowpass( f, cutoff ):
	nr, nc = f.shape[:2]

	fp = np.zeros( [ nr, nc ] )				# 前處理：頻譜中心化
	for x in range( nr ):
		for y in range( nc ):
			fp[x,y] = pow( -1, x + y ) * f[x,y]

	F = fft2( fp )							# 離散傅立葉轉換
	G = F.copy( )

	for u in range( nr ):
		for v in range( nc ):
			dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
			                ( v - nc / 2 ) * ( v - nc / 2 ) )
			H = np.exp( -( dist * dist ) / ( 2 * cutoff * cutoff ) )
			G[u,v] *= H

	gp = ifft2( G )							# 反離散傅立葉轉換

	gp2 = np.zeros( [ nr, nc ] )			# 後處理
	for x in range( nr ):
		for y in range( nc ):
			gp2[x,y] = round( pow( -1, x + y ) * np.real( gp[x,y] ), 0 )
	g = np.uint8( np.clip( gp2, 0, 255 ) )

	return g

# 逆濾波（Inverse Filtering）：嘗試從退化影像恢復原始影像
def inverse_filtering( f, cutoff, radius ):
	nr, nc = f.shape[:2]

	fp = np.zeros( [ nr, nc ] )				# 前處理：頻譜中心化
	for x in range( nr ):
		for y in range( nc ):
			fp[x,y] = pow( -1, x + y ) * f[x,y]

	F = fft2( fp )							# 離散傅立葉轉換
	G = F.copy( )

	for u in range( nr ):					# 逆濾波：在 radius 範圍內除以退化函數
		for v in range( nc ):
			dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
			                ( v - nc / 2 ) * ( v - nc / 2 ) )
			H = np.exp( -( dist * dist ) / ( 2 * cutoff * cutoff ) )
			if dist <= radius:
				# 在截止半徑內執行逆濾波（距離外設為0避免高頻雜訊放大）
				G[u,v] /= H
			else:
				G[u,v] = 0

	gp = ifft2( G )							# 反離散傅立葉轉換

	gp2 = np.zeros( [ nr, nc ] )			# 後處理
	for x in range( nr ):
		for y in range( nc ):
			gp2[x,y] = round( pow( -1, x + y ) * np.real( gp[x,y] ), 0 )
	g = np.uint8( np.clip( gp2, 0, 255 ) )

	return g

def main( ):
	img1 = cv2.imread( "Brunch.bmp", 0 )
	# 先以截止頻率 50 模擬低通退化
	img2 = gaussian_lowpass( img1, 50 )
	# 再以逆濾波嘗試恢復（限制在 radius=100 內執行以避免雜訊放大）
	img3 = inverse_filtering( img2, 50, 100 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Lowpass Image", img2 )
	cv2.imshow( "Inverse Filtering", img3 )
	cv2.waitKey( 0 )

main( )
