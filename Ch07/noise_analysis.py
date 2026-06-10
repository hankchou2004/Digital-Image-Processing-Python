import numpy as np
import cv2
import matplotlib.pyplot as plt

# 繪製直方圖以分析雜訊的統計分布
def histogram( f ):
	if f.ndim != 3:
		hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
		plt.plot( hist )
	else:
		color = ( 'b', 'g', 'r' )
		for i, col in enumerate( color ):
			hist = cv2.calcHist( f, [i], None, [256], [0,256] )
			plt.plot( hist, color = col )
	plt.xlim( [0,256] )
	plt.xlabel( "Intensity" )
	plt.ylabel( "#Intensities" )
	plt.show( )

# 讀取含有雜訊的影像
f = cv2.imread( "Noisy_Pattern.bmp", 0 )
# 擷取均勻區域（ROI）以分析純雜訊的統計特性
ROI = f[55:95, 55:95]
# 顯示該均勻區域的直方圖（可從形狀判斷雜訊類型）
histogram( ROI )
# 計算並顯示雜訊的標準差（反映雜訊強度）
print( "Sigma =", np.std( ROI ) )
