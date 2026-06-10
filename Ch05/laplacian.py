import numpy as np
import cv2

# 拉普拉斯邊緣偵測：計算二階導數，用於偵測邊緣（包含正負值）
def laplacian( f ):
	# 計算拉普拉斯值並加 128，使結果平移到 0~255 可視範圍
	# （拉普拉斯輸出有正有負，128 為中性基準值）
	temp = cv2.Laplacian( f, cv2.CV_32F ) + 128
	g = np.uint8( np.clip( temp, 0, 255 ) )
	return g

def main( ):
	img1 = cv2.imread( "Osaka.bmp", -1 )
	img2 = laplacian( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Laplacian", img2 )
	cv2.waitKey( 0 )

main( )
