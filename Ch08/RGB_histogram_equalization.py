import numpy as np
import cv2

# 對 RGB 彩色影像的每個通道分別進行直方圖均衡化
def RGB_histogram_equalization( f ):
	g = f.copy( )
	# 對 B、G、R 三個通道（索引 0、1、2）各自均衡化
	for k in range( 3 ):
		g[:,:,k] = cv2.equalizeHist( f[:,:,k] )
	return g

def main( ):
	img1 = cv2.imread( "Rose.bmp", -1 )
	img2 = RGB_histogram_equalization( img1 )
	cv2.imshow( "Original Image", img1 )
	# 注意：各通道獨立均衡化可能造成色偏，建議使用 HSV 方法
	cv2.imshow( "Histogram Equalization(RGB)", img2 )
	cv2.waitKey( 0 )

main( )
