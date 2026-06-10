import numpy as np
import cv2

# 前向映射：將來源影像的每個像素映射到目標影像（放大 2 倍）
def forward_mapping( f ):
	nr, nc = f.shape[:2]
	# 建立 2 倍大的空白輸出影像（前向映射會在間隔處留下空洞）
	g = np.zeros( [nr*2, nc*2, 3], dtype = 'uint8' )
	# 將來源每個像素複製到輸出的偶數位置
	for x in range( nr ):
		for y in range( nc ):
			for k in range( 3 ):
				g[x*2, y*2, k] = f[x,y,k]
	return g

def main( ):
	img1 = cv2.imread( "Baboon.bmp", -1 )
	# 執行前向映射（輸出影像中每隔一個像素為黑色空洞）
	img2 = forward_mapping( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Forward Mapping", img2 )
	cv2.waitKey( 0 )

main( )
