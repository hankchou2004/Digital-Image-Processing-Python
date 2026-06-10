import numpy as np
import cv2

# SIFT（Scale-Invariant Feature Transform）特徵偵測
# 特點：具有尺度不變性與旋轉不變性，適合影像匹配與物件辨識
# 注意：SIFT 在舊版 OpenCV 需要 cv2.xfeatures2d 模組（有專利限制）
def SIFT_feature_detection( f ):
	# 建立彩色輸出影像
	g = cv2.cvtColor( f, cv2.COLOR_GRAY2BGR )
	# 建立 SIFT 特徵偵測器（需要 opencv-contrib-python）
	sift = cv2.xfeatures2d.SIFT_create()
	# 偵測關鍵點（在多個尺度空間中搜尋 DoG 極值點）
	kp = sift.detect( f, None )
	# 繪製關鍵點（包含方向和大小資訊）
	g = cv2.drawKeypoints( f, kp, g )
	return g

def main( ):
	img1 = cv2.imread( "Blox.bmp", 0 )
	img2 = SIFT_feature_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "SIFT Features", img2 )
	cv2.waitKey( 0 )

main( )
