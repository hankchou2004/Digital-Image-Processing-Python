import numpy as np
import cv2

# 擷取 HSV 色彩模型的指定分量
def HSV_model( f, channel ):
	# 使用 OpenCV 內建函式轉換到 HSV 色彩空間
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	if channel == 1:	# 色相（Hue）：H 值範圍 0~180（OpenCV 慣例）
		return hsv[:,:,0]
	elif channel == 2:	# 飽和度（Saturation）：S 值範圍 0~255
		return hsv[:,:,1]
	else:				# 明度（Value）：V 值範圍 0~255
		return hsv[:,:,2]

def main( ):
	img = cv2.imread( "Rose.bmp", -1 )
	H = HSV_model( img, 1 )
	S = HSV_model( img, 2 )
	V = HSV_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Hue", H )
	cv2.imshow( "Saturation", S )
	cv2.imshow( "Value", V )
	cv2.waitKey( 0 )

main( )
