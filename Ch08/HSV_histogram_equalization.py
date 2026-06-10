import numpy as np
import cv2

# 在 HSV 色彩空間中進行直方圖均衡化（只對亮度通道 V 處理）
def HSV_histogram_equalization( f ):
	# 轉換到 HSV 色彩空間（H：色相, S：飽和度, V：明度）
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	# 只對 V（明度）通道進行直方圖均衡化，避免色偏問題
	hsv[:,:,2] = cv2.equalizeHist( hsv[:,:,2] )
	# 轉換回 BGR 色彩空間
	g = cv2.cvtColor( hsv, cv2.COLOR_HSV2BGR )
	return g

def main( ):
	img1 = cv2.imread( "Rose.bmp", -1 )
	img2 = HSV_histogram_equalization( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Histogram Equalization(HSV)", img2 )
	cv2.waitKey( 0 )

main( )
