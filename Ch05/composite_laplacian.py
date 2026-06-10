import numpy as np
import cv2

# 複合拉普拉斯銳化：使用「增強型拉普拉斯濾波器」直接強化邊緣
def composite_laplacian( f ):
	# 核心 = I + (-∇²)，其中中心值為5，周圍為-1（4-鄰域）
	# 等同於原影像加上拉普拉斯邊緣，達到銳化效果
	kernel = np.array( [ [0, -1, 0], [-1, 5, -1], [0, -1, 0] ] )
	# 套用濾波器（使用 float32 避免溢位）
	temp = cv2.filter2D( f, cv2.CV_32F, kernel )
	# 裁切到 0~255 範圍並轉回 uint8
	g = np.uint8( np.clip( temp, 0, 255 ) )
	return g

def main( ):
	img1 = cv2.imread( "Osaka.bmp", -1 )
	img2 = composite_laplacian( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Composite Laplacian", img2 )
	cv2.waitKey( 0 )

main( )
