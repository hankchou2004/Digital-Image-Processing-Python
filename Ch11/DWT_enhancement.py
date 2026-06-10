import numpy as np
import cv2
import pywt

# 使用離散小波轉換（DWT）選擇性保留特定頻帶以增強影像
def DWT_enhancement( f, method, wavelet ):
	nr, nc = f.shape[:2]
	# 執行單層 2D DWT
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs
	if method == 1:  # 只保留 LL（低頻近似）：模糊化效果
		LH.fill( 0 )
		HL.fill( 0 )
		HH.fill( 0 )
	elif method == 2: # 只保留 LH（水平細節）：水平邊緣
		LL.fill( 0 )
		HL.fill( 0 )
		HH.fill( 0 )
	elif method == 3: # 只保留 HL（垂直細節）：垂直邊緣
		LL.fill( 0 )
		LH.fill( 0 )
		HH.fill( 0 )
	elif method == 4: # 只保留 HH（對角細節）：對角邊緣
		LL.fill( 0 )
		LH.fill( 0 )
		HL.fill( 0 )
	coeffs = LL, (LH, HL, HH)
	# 執行反 DWT 重建
	output = pywt.idwt2( coeffs, wavelet )
	g = f.copy( )
	if method == 1:
		# LL 保留原始強度範圍
		g = np.uint8( np.clip( output, 0, 255 ) )
	else:
		# 其他頻帶正規化到 0~255 以便視覺化
		temp = np.zeros( [ nr, nc ] )
		cv2.normalize( output, temp, 0, 255, cv2.NORM_MINMAX )
		g = np.uint8( temp )
	return g

def main( ):
	print( "Image Enhancement using DWT:" )
	print( "(1) LL only" )
	print( "(2) LH only" )
	print( "(3) HL only" )
	print( "(4) HH only" )
	method = eval( input( "Please enter your choice: " ) )
	img1 = cv2.imread( "House.bmp", -1 )
	# 使用 db1（Haar 小波）進行頻帶分解
	img2 = DWT_enhancement( img1, method, 'db1' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Image Enhancement using DWT", img2 )
	cv2.waitKey( 0 )

main( )
