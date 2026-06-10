import numpy as np
import cv2

# 反銳化遮罩（Unsharp Masking）：增強影像邊緣細節
def unsharp_masking( f, k = 1.0 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 對影像進行高斯模糊，取得低頻（平滑）成分
	f_avg = cv2.GaussianBlur( f, ( 15, 15 ), 0 )
	# 計算遮罩 = 原影像 - 模糊影像（即高頻邊緣成分）
	# 輸出 = 原影像 + k * 遮罩（k 控制銳化強度）
	for x in range( nr ):
		for y in range( nc ):
			g_mask = int( f[x,y] ) - int( f_avg[x,y] )
			g[x,y] = np.uint8( np.clip( f[x,y] + k * g_mask, 0, 255 ) )
	return g

def main( ):
	img1 = cv2.imread( "Osaka.bmp", -1 )
	# k=10.0 表示強力銳化（邊緣顯著增強）
	img2 = unsharp_masking( img1, 10.0 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Unsharp Masking", img2 )
	cv2.waitKey( 0 )

main( )
