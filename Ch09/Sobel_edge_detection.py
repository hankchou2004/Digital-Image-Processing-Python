import numpy as np
import cv2

# Sobel 邊緣偵測：計算影像梯度並以 Otsu 閾值二值化
def Sobel_edge_detection( f ):
	# 計算 x 方向的 Sobel 梯度（偵測垂直邊緣）
	grad_x = cv2.Sobel( f, cv2.CV_32F, 1, 0, ksize = 3 )
	# 計算 y 方向的 Sobel 梯度（偵測水平邊緣）
	grad_y = cv2.Sobel( f, cv2.CV_32F, 0, 1, ksize = 3 )
	# 合成總梯度大小（絕對值相加近似 L1 範數）
	magnitude = abs( grad_x ) + abs( grad_y )
	g = np.uint8( np.clip( magnitude, 0, 255 ) )
	# 使用 Otsu 自動閾值化進行二值化（THRESH_BINARY + THRESH_OTSU）
	ret,g = cv2.threshold( g, 127, 255,
		    cv2.THRESH_BINARY + cv2.THRESH_OTSU )
	return g

def main( ):
	img1 = cv2.imread( "Osaka.bmp", -1 )
	img2 = Sobel_edge_detection( img1 )
	cv2.imshow( "Original Image",  img1 )
	cv2.imshow( "Sobel Edge Detection", img2 )
	cv2.waitKey( 0 )

main( )
