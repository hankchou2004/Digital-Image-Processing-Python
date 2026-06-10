import numpy as np
import cv2

# SURF（Speeded-Up Robust Features）特徵偵測
# 特點：比 SIFT 更快（使用積分影像和 Hessian 矩陣行列式），同樣具有尺度不變性
# 注意：SURF 有專利限制，需要 opencv-contrib-python 並在非商業場合使用
def SURF_feature_detection( f ):
	# 建立彩色輸出影像
	g = cv2.cvtColor( f, cv2.COLOR_GRAY2BGR )
	# 建立 SURF 特徵偵測器（需要 opencv-contrib-python）
	surf = cv2.xfeatures2d. SURF_create()
	# 偵測關鍵點（在多個尺度的 Hessian 響應空間中搜尋極值）
	kp = surf.detect( f, None )
	# 繪製關鍵點（flags=4 表示繪製含方向與尺度的豐富關鍵點）
	g = cv2.drawKeypoints( f, kp, g, flags = 4 )
	return g

def main( ):
	img1 = cv2.imread( "Blox.bmp", 0 )
	img2 = SURF_feature_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( " SURF Features", img2 )
	cv2.waitKey( 0 )

main( )
