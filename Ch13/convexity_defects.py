import cv2
import numpy as np

# 計算並繪製輪廓的凸性缺陷（Convexity Defects）
# 凸性缺陷：物件輪廓與其凸包之間的凹陷區域
def convexity_defects( f ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 找到最外層輪廓
	contours, hierarchy = cv2.findContours( f,
	              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	cnt = contours[0]
	# 計算凸包（returnPoints=False 表示回傳點的索引）
	hull = cv2.convexHull( cnt,returnPoints = False)
	# 計算凸性缺陷（每個缺陷包含起點、終點、最遠點、深度）
	defects = cv2.convexityDefects( cnt, hull )
	# 將前景像素設為較暗的灰色以便視覺化
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	# 繪製每個凸性缺陷（連接起點到終點，並標示最遠點）
	for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple( cnt[s][0] )
		end = tuple( cnt[e][0] )
		far = tuple( cnt[f][0] )   # 缺陷中距離凸包最遠的點
		cv2.line( g, start, end, ( 255,255,255 ), 1 )
		cv2.circle( g, far, 5, ( 255,255,255 ), -1 )
	return g

def main( ):
	img1 = cv2.imread( "Hand.bmp", -1 )
	img2 = convexity_defects( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Convex Defects", img2 )
	cv2.waitKey( 0 )

main( )
