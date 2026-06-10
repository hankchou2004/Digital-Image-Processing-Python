import numpy as np
import cv2

# 使用 Sobel 運算子計算影像梯度（邊緣強度）
def Sobel_gradient( f, direction = 1 ):
	# Sobel x 方向核心：偵測水平邊緣（垂直方向的亮度變化）
	sobel_x = np.array( [ [-1,-2,-1], [ 0, 0, 0], [ 1, 2, 1] ] )
	# Sobel y 方向核心：偵測垂直邊緣（水平方向的亮度變化）
	sobel_y = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
	if direction == 1:
		# 僅計算 x 方向梯度
		grad_x = cv2.filter2D( f, cv2.CV_32F, sobel_x )
		gx = abs( grad_x )
		g = np.uint8( np.clip( gx, 0, 255 ) )
	elif direction == 2:
		# 僅計算 y 方向梯度
		grad_y = cv2.filter2D( f, cv2.CV_32F, sobel_y )
		gy = abs( grad_y )
		g = np.uint8( np.clip( gy, 0, 255 ) )
	else:
		# 計算總梯度大小（x 和 y 梯度絕對值之和）
		grad_x = cv2.filter2D( f, cv2.CV_32F, sobel_x )
		grad_y = cv2.filter2D( f, cv2.CV_32F, sobel_y )
		magnitude = abs( grad_x ) + abs( grad_y )
		g = np.uint8( np.clip( magnitude, 0, 255 ) )
	return g

def main( ):
	img = cv2.imread( "Osaka.bmp", -1 )
	# 分別計算 x 方向、y 方向及總梯度
	gx  = Sobel_gradient( img, 1 )
	gy  = Sobel_gradient( img, 2 )
	g   = Sobel_gradient( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Gradient in x", gx )
	cv2.imshow( "Gradient in y", gy )
	cv2.imshow( "Gradient", g )
	cv2.waitKey( 0 )

main( )
