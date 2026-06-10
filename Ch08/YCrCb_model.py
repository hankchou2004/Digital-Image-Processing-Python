import numpy as np
import cv2

# 擷取 YCrCb 色彩模型的指定分量
# YCrCb 廣泛用於視訊壓縮標準（JPEG、MPEG）
# Y：亮度（Luma），Cr：紅色色差，Cb：藍色色差
def YCrCb_model( f, channel ):
	# 使用 OpenCV 轉換到 YCrCb 色彩空間
	ycrcb = cv2.cvtColor( f, cv2.COLOR_BGR2YCrCb )
	if channel == 1:	# Y：亮度分量（人眼最敏感）
		return ycrcb[:,:,0]
	elif channel == 2:	# Cr：紅色色差（偏紅程度）
		return ycrcb[:,:,1]
	else:				# Cb：藍色色差（偏藍程度）
		return ycrcb[:,:,2]

def main( ):
	img = cv2.imread( "Rose.bmp", -1 )
	Y  = YCrCb_model( img, 1 )
	Cr = YCrCb_model( img, 2 )
	Cb = YCrCb_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Y", Y )
	cv2.imshow( "Cr", Cr )
	cv2.imshow( "Cb", Cb )
	cv2.waitKey( 0 )

main( )
