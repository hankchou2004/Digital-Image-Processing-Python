import numpy as np
import cv2
from numpy.fft import fft2, fftshift

# 計算並顯示影像的頻率振幅頻譜
def spectrum( f ):
	# 執行 2D FFT 轉換到頻域
	F = fft2( f )
	# 將零頻率移到中心（低頻在中間，高頻在四周）
	Fshift = fftshift( F )
	# 取對數頻譜（log 壓縮大動態範圍），+1 避免 log(0)
	mag = 20 * np.log( np.abs( Fshift ) + 1 )
	# 正規化到 0~255
	mag = mag / mag.max( ) * 255.0
	g = np.uint8( mag )
	return g

# 計算並顯示影像的相位頻譜
def phase_spectrum( f ):
	F = fft2( f )
	# 計算每個頻率分量的相位角（單位：度）
	phase = np.angle( F, deg = True )
	nr, nc = phase.shape[:2]
	# 將相位值從 [-180, 180] 映射到 [0, 255]
	for x in range( nr ):
		for y in range( nc ):
			if phase[x,y] < 0:
				phase[x,y] = phase[x,y] + 360
			phase[x,y] = int( phase[x,y] * 255 / 360 )
	g = np.uint8( np.clip( phase, 0, 255 ) )
	return g

def main( ):
	img = cv2.imread( "Lenna.bmp", -1 )
	# 計算振幅頻譜與相位頻譜
	magnitude = spectrum( img )
	phase = phase_spectrum( img )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Frequency Spectrum", magnitude )
	cv2.imshow( "Phase Specrum", phase )
	cv2.waitKey( 0 )

main( )
