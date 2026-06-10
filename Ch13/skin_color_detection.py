import numpy as np
import cv2

# 皮膚顏色偵測：使用三種不同的色彩空間方法進行皮膚區域分割
def skin_color_detection( f, method ):
	g = f.copy()
	g.fill( 0 )   # 輸出影像初始化為全黑
	nr, nc = f.shape[:2]

	if method == 1:  # RGB 方法：基於 RGB 值的規則式判別
		for x in range( nr ):
			for y in range( nc ):
				B = int( f[x,y,0] )
				G = int( f[x,y,1] )
				R = int( f[x,y,2] )
				# 皮膚顏色條件：R>G>B，且最大值與最小值差異足夠大
				if R > 95 and G > 40 and B > 20 and \
					max(R,G,B) - min(R,G,B) > 15 and \
					abs( R- G ) > 15 and R > G and R > B:
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255

	elif method == 2:  # HSV 方法：基於色相和飽和度的判別（對光照變化較穩定）
		hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
		for x in range( nr ):
			for y in range( nc ):
				H = int( hsv[x,y,0] * 2 )  # 還原到 0~360 度
				S = float( hsv[x,y,1] / 255 )
				# 皮膚色相在紅色附近（0~50° 或 320~360°），飽和度適中
				if ( ( ( H > 0 and H < 50 ) or \
					   ( H > 320 and H < 360 ) ) and
					   ( S > 0.23 and S < 0.68 ) ):
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255

	else:  # YCrCb 方法：基於色差分量的判別（JPEG 標準常用）
		ycrcb = cv2.cvtColor( f, cv2.COLOR_BGR2YCrCb )
		for x in range( nr ):
			for y in range( nc ):
				Cr = int( ycrcb[x,y,1] )  # 紅色色差
				Cb = int( ycrcb[x,y,2] )  # 藍色色差
				# 皮膚的 Cr 和 Cb 值在特定範圍內
				if ( Cb >= 77 and Cb <= 127 and \
					 Cr >= 133 and Cr <= 173 ):
					g[x,y,0] = g[x,y,1] = g[x,y,2] = 255
	return g

def main( ):
	img1 = cv2.imread( "Thumb_Up.bmp", -1 )
	# 使用 RGB 方法偵測皮膚區域
	img2 = skin_color_detection( img1, 1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Skin Color Detection", img2 )
	cv2.waitKey( 0 )

main( )
