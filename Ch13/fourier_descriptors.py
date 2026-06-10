import numpy as np
import cv2
from numpy.fft import fft, ifft

# 傅立葉描述子（Fourier Descriptor）：利用 FFT 對輪廓進行頻域表示與近似
def fourier_descriptor( f, thresh ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 找到輪廓點
	contours, hierarchy = cv2.findContours( f,
	              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	# 將所有輪廓點合併並轉為一維陣列
	contour = np.vstack( contours ).squeeze( )
	N = len( contour )
	print( N )
	# 將輪廓點表示為複數形式（實部=列座標，虛部=行座標）
	s_arr = np.zeros( N, dtype = 'complex' )
	for n in range( N ):
		s_arr[n] = complex( contour[n][1], contour[n][0] )
	# 對輪廓複數序列執行 FFT
	S_arr = fft( s_arr )
	# 根據閾值百分比決定保留多少低頻描述子係數
	thresh /= 100
	thresh = int( round( N / 2 * thresh ) )
	# 將高頻係數（thresh~N-thresh）設為 0（低通濾波）
	for k in range( thresh, N - thresh ):
		S_arr[k] = 0
	# 反 FFT 得到近似輪廓
	s_arr = ifft( S_arr )
	# 以灰色顯示原始物件
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	# 繪製近似後的輪廓點（白色）
	for n in range( N ):
		x = int( round( s_arr[n].real ) )
		y = int( round( s_arr[n].imag ) )
		g[x,y] = 255
	return g

def main( ):
	thresh = eval( input( "Please enter threshold(%):"))
	img1 = cv2.imread( "Bug.bmp", 0 )
	img2 = fourier_descriptor( img1, thresh )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Fourier Descriptor", img2 )
	cv2.waitKey( 0 )

main( )
