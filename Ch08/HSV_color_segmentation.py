import numpy as np
import cv2

# 基於 HSV 色彩空間的顏色分割：保留特定顏色範圍的像素，其餘設為黑色
def HSV_color_segmentation( f, H1, H2, S1, S2, V1, V2 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 將影像轉換到 HSV 色彩空間
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	for x in range( nr ):
		for y in range( nc ):
			# OpenCV 的 H 值範圍是 0~180，乘以 2 還原為 0~360
			H = hsv[x,y,0] * 2
			# S、V 值正規化為 0~100
			S = hsv[x,y,1] / 255 * 100
			V = hsv[x,y,2] / 255 * 100
			# 不在指定 HSV 範圍內的像素設為黑色
			if not ( H >= H1 and H <= H2 and S >= S1 and S <= S2
				     and V >= V1 and V <= V2 ):
				g[x,y,0] = g[x,y,1] = g[x,y,2] = 0
	return g

def main( ):
	img1 = cv2.imread( "Flower.bmp", -1 )
	# 分割黃綠色花朵（色相 30~70°，飽和度與明度各 30~100%）
	img2 = HSV_color_segmentation( img1, 30, 70, 30, 100, 30, 100 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "HSV Color Segmentation", img2 )
	cv2.waitKey( 0 )

main( )
