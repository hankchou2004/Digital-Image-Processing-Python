import numpy as np
import cv2

# 擷取 RGB 色彩模型的指定通道（以灰階影像顯示單一色版）
def RGB_model( f, channel ):
	if channel == 1:	# 紅色（Red）通道（OpenCV BGR 索引為 2）
		return f[:,:,2]
	elif channel == 2:	# 綠色（Green）通道（OpenCV BGR 索引為 1）
		return f[:,:,1]
	else:				# 藍色（Blue）通道（OpenCV BGR 索引為 0）
		return f[:,:,0]

def main( ):
	img = cv2.imread( "Rose.bmp", -1 )
	R = RGB_model( img, 1 )
	G = RGB_model( img, 2 )
	B = RGB_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Red", R )
	cv2.imshow( "Green", G )
	cv2.imshow( "Blue", B )
	cv2.waitKey( 0 )

main( )
