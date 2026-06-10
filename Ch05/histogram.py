import numpy as np
import cv2
import matplotlib.pyplot as plt

# 繪製影像直方圖（統計各灰階值的像素數量分布）
def histogram( f ):
	if f.ndim != 3:
		# 灰階影像：計算單一通道的直方圖
		hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
		plt.plot( hist )
	else:
		# 彩色影像：分別計算 B、G、R 三個通道的直方圖
		color = ( 'b', 'g', 'r' )
		for i, col in enumerate( color ):
			hist = cv2.calcHist( f, [i], None, [256], [0,256] )
			plt.plot( hist, color = col )
	plt.xlim( [0,256] )
	plt.xlabel( "Intensity" )
	plt.ylabel( "#Intensities" )
	plt.show( )

def main( ):
	# 讀取低對比度影像（直方圖應集中在中間灰階範圍）
	img = cv2.imread( "Indoor_Low_Contrast.bmp", -1 )
	cv2.imshow( "Original Image", img )
	histogram( img )

main( )
