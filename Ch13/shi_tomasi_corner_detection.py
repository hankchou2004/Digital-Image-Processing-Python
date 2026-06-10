import numpy as np
import cv2

# Shi-Tomasi 角點偵測（改良版 Harris）：選取「品質最好的」角點
def shi_tomasi_corner_detection( f ):
	# 建立彩色輸出影像
	g = cv2.cvtColor( f, cv2.COLOR_GRAY2BGR )
	nr, nc = f.shape[:2]
	# goodFeaturesToTrack：偵測最多 20 個角點
	# qualityLevel=0.01（品質閾值），minDistance=10（角點間最小距離）
	corners = cv2.goodFeaturesToTrack( f, 20, 0.01, 10 )
	corners = np.int0( corners )
	# 在每個角點位置繪製藍色圓圈
	for corner in corners:
		x, y = corner.ravel()
		cv2.circle( g, (x,y), 5, [255,0,0], 2 )
	return g

def main( ):
	img1 = cv2.imread( "Blox.bmp", 0 )
	img2 = shi_tomasi_corner_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Shi-Tomasi Corners", img2 )
	cv2.waitKey( 0 )

main( )
