import numpy as np
import cv2

# 對彩色影像的指定 RGB 通道個別套用 Gamma 校正
def RGB_gamma_correction( f, channel, gamma ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 計算正規化常數
	c = 255.0 / ( 255.0 ** gamma )
	# 建立 256 個灰階值的查找表
	table = np.zeros( 256 )
	for i in range( 256 ):
		table[i] = round( i ** gamma * c, 0 )
	# 根據選擇的通道決定陣列索引（OpenCV 儲存順序為 BGR）
	if channel == 1:    k = 2   # 紅色（Red）通道
	elif channel == 2:  k = 1   # 綠色（Green）通道
	else:    		    k = 0   # 藍色（Blue）通道
	# 只對指定通道套用 Gamma 校正
	for x in range( nr ):
		for y in range( nc ):
			g[x,y,k] = table[f[x,y,k]]
	return g

def main( ):
	img  = cv2.imread( "Rose.bmp", -1 )
	gamma = eval( input( "Please enter gamma: " ) )
	# 對三個通道分別套用相同 gamma 值
	img1 = RGB_gamma_correction( img, 1, gamma )
	img2 = RGB_gamma_correction( img, 2, gamma )
	img3 = RGB_gamma_correction( img, 3, gamma )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Gamma Correction(R)", img1 )
	cv2.imshow( "Gamma Correction(G)", img2 )
	cv2.imshow( "Gamma Correction(B)", img3 )
	cv2.waitKey( 0 )

main( )
