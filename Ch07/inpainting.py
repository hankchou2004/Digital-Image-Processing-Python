import numpy as np
import cv2

# 影像修復（Inpainting）：自動填補影像中被標記的損壞區域
def inpainting( f, method = 1 ):
	nr, nc = f.shape[:2]
	mask = np.zeros( [ nr, nc ], dtype = 'uint8' )  # 建立遮罩（標記需修復的區域）
	# 找出青色（0, 255, 255）像素作為損壞區域標記
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y,0] == 0 and f[x,y,1] == 255 and f[x,y,2] == 255:
				mask[x,y] = 255
	if method == 1:
		# NS 方法（Navier-Stokes）：基於流體力學的修復演算法
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_NS )
	else:
		# TELEA 方法：基於快速行進法的修復演算法（通常較快）
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_TELEA )
	return g

def main( ):
	img1 = cv2.imread( "Shizheng_N7_Mask.bmp", -1 )
	img2 = inpainting( img1, 1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Inpainting", img2 )
	cv2.waitKey( 0 )

main( )
