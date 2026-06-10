import numpy as np
import cv2
import pywt

# 使用離散小波轉換（DWT）進行邊緣偵測
def DWT_edge_detection( f, wavelet ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 執行單層 2D DWT，分解為四個子頻帶
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs
	# LL：低頻（近似分量），LH：水平邊緣，HL：垂直邊緣，HH：對角邊緣
	# 將低頻分量（LL）清零，只保留高頻邊緣資訊
	LL.fill( 0 )
	coeffs = LL, (LH, HL, HH)
	# 執行反 DWT 重建（僅含高頻邊緣成分）
	output = pywt.idwt2( coeffs, wavelet )
	gradients = np.uint8( np.clip( abs( output ), 0, 255 ) )
	# 用 Otsu 閾值化得到二值邊緣圖
	thresh, g = cv2.threshold( gradients, 127, 255, cv2.THRESH_OTSU )
	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	# 使用 db8（Daubechies 8-tap）小波進行邊緣偵測
	img2 = DWT_edge_detection( img1, 'db8' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Edge Detection using DWT", img2 )
	cv2.waitKey( 0 )

main( )
