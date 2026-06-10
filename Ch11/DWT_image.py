import numpy as np
import cv2
import pywt

# 執行 2D DWT 並將四個子頻帶拼接成一張顯示影像
def DWT_image( f, wavelet ):
	nr, nc = f.shape[:2]
	# 執行單層 2D DWT，分解為四個子頻帶
	coeffs = pywt.dwt2( f, wavelet )
	LL, (LH, HL, HH) = coeffs
	# 每個子頻帶的大小約為原影像的一半
	nr1, nc1 = LL.shape[:2]
	# 建立 2 倍大的輸出影像（拼接四個子頻帶）
	g = np.zeros( [nr1 * 2, nc1 * 2], dtype = 'uint8' )

	# 左上角：LL（低低頻，近似影像）— 正規化後顯示
	LL_normalized = np.zeros( [nr1, nc1] )
	cv2.normalize( LL, LL_normalized, 0, 255, cv2.NORM_MINMAX )
	g[0:nr1,0:nc1] = np.uint8( LL_normalized[:,:] )

	# 右上角：LH（低高頻，水平細節）— 加 128 平移以便顯示正負值
	g[0:nr1,nc1:2*nc1] = np.uint8( np.clip( LH + 128, 0, 255 ) )
	# 左下角：HL（高低頻，垂直細節）
	g[nr1:2*nr1,0:nc1] = np.uint8( np.clip( HL + 128, 0, 255 ) )
	# 右下角：HH（高高頻，對角細節）
	g[nr1:2*nr1,nc1:nc1*2] = np.uint8( np.clip( HH + 128, 0, 255 ) )

	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	# 使用 db4（Daubechies 8-tap）小波進行分解
	img2 = DWT_image( img1, 'db4' )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Discrete Wavelet Transform", img2 )
	cv2.waitKey( 0 )

main( )
