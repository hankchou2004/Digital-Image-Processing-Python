import numpy as np
import cv2

# 孔洞填補：填滿二值影像中前景物件內部的黑色孔洞
def hole_filling( f ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 對影像取補（前景變背景）
	negative = 255 - f
	# 找出補影像中的連通成分（每個孔洞和背景各是一個連通成分）
	n, labels = cv2.connectedComponents( negative )
	# label=0 是最外圍背景，label>1 的是孔洞（被前景包圍的區域）
	for x in range( nr ):
		for y in range( nc ):
			if labels[x,y] > 1:
				g[x,y] = 255   # 填滿孔洞
	return g

def main( ):
	img1 = cv2.imread( "ABC.bmp", -1 )
	img2 = hole_filling( img1 )
	cv2.imshow( "Original Image",  img1 )
	cv2.imshow( "Hole Filling", img2 )
	cv2.waitKey( 0 )

main( )
