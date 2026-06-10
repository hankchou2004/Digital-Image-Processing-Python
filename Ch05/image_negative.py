import numpy as np
import cv2

# 影像反相（負片效果）：將每個像素值從 f 轉換為 255-f
def image_negative( f ):
	# 利用 NumPy 向量化運算：g = 255 - f（高效率）
	g = 255 - f
	return g

def main( ):
	img1 = cv2.imread( "Lenna.bmp", -1 )
	# 執行影像反相（亮的地方變暗，暗的地方變亮）
	img2 = image_negative( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Image Negative", img2 )
	cv2.waitKey( 0 )

main( )
