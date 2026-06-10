import numpy as np
import cv2

# CMY 色彩模型：從 RGB 轉換為印刷用的青（Cyan）、洋紅（Magenta）、黃（Yellow）
# 轉換公式：CMY = 1 - RGB（以 0~255 表示則為 CMY = 255 - RGB）
def CMY_model( f, channel ):
	if channel == 1:	# 青色（Cyan）= 255 - Red（移除紅色成分）
		return 255 - f[:,:,2]
	elif channel == 2:	# 洋紅（Magenta）= 255 - Green（移除綠色成分）
		return 255 - f[:,:,1]
	else:				# 黃色（Yellow）= 255 - Blue（移除藍色成分）
		return 255 - f[:,:,0]

def main( ):
	img = cv2.imread( "Rose.bmp", -1 )
	# 分別擷取 C、M、Y 三個色版
	C = CMY_model( img, 1 )
	M = CMY_model( img, 2 )
	Y = CMY_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Cyan", C )
	cv2.imshow( "Magenta", M )
	cv2.imshow( "Yellow", Y )
	cv2.waitKey( 0 )

main( )
