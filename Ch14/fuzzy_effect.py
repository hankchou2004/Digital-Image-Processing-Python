import numpy as np
import cv2
from numpy.random import uniform

# 模糊效果（Fuzzy Effect）：將每個像素隨機偏移，產生類似毛玻璃的效果
def fuzzy_effect( f, W ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			# 在 [-W/2, W/2] 範圍內隨機偏移座標
			xp = int( x + W * uniform() - W // 2 )
			yp = int( y + W * uniform() - W // 2 )
			# 夾住偏移後的座標，確保不超出影像範圍
			xp = np.clip( xp, 0, nr - 1 )
			yp = np.clip( yp, 0, nc - 1 )
			# 從偏移位置取像素值（仿佛透過不平整的玻璃觀看）
			g[x,y] = f[xp,yp]
	return g

def main( ):
	img1 = cv2.imread( "Brunch.bmp", -1 )
	# W=3：偏移範圍 ±1.5 像素（效果較輕微）
	img2 = fuzzy_effect( img1, 3 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Fuzzy Effect", img2 )
	cv2.waitKey( 0 )

main( )
