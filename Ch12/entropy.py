import numpy as np
import cv2

# 計算影像的資訊熵（Shannon Entropy）
# 熵反映影像灰階值的隨機程度，熵越高表示資訊量越豐富
def entropy( f ):
	nr, nc = f.shape[:2]
	# 建立機率密度函數（PDF）：統計每個灰階值出現的次數
	pdf = np.zeros( 256 )
	for x in range( nr ):
		for y in range( nc ):
			pdf[f[x,y]] += 1
	# 正規化為機率（除以總像素數）
	pdf /= ( nr * nc )
	# 計算 Shannon 熵：H = -Σ p(k) * log2(p(k))
	H = 0
	for k in range( 256 ):
		if pdf[k] != 0:
			H += ( -pdf[k] * np.log2( pdf[k] ) )
	return H

def main( ):
	img = cv2.imread( "Lenna.bmp", -1 )
	H = entropy( img )
	# 熵的單位為 bits/pixel，自然影像通常在 6~8 bits/pixel 之間
	print( "Entropy =", H )

main( )
