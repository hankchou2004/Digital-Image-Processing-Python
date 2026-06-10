import numpy as np
import cv2

# JPEG 影像壓縮：使用 DCT、量化、閾值化模擬 JPEG 壓縮流程
def jpeg_compression( f, percentage = 25 ):
	# JPEG 標準量化表（用於正規化 DCT 係數）
	normalize = np.array( [ [ 16, 11, 10, 16,  24,  40,  51,  61 ],
							[ 12, 12, 14, 19,  26,  58,  60,  55 ],
							[ 14, 13, 16, 24,  40,  57,  69,  56 ],
							[ 14, 17, 22, 29,  51,  87,  80,  62 ],
							[ 18, 22, 37, 56,  68, 109, 103,  77 ],
							[ 24, 35, 55, 64,  81, 104, 113,  92 ],
							[ 49, 64, 78, 87, 103, 121, 120, 101 ],
							[ 72, 92, 95, 98, 112, 100, 103,  99 ] ] )
	# Zig-zag 掃描順序（從低頻到高頻的索引）
	table = np.array( [ [  0,  1,  5,  6, 14, 15, 27, 28 ],
					    [  2,  4,  7, 13, 16, 26, 29, 42 ],
					    [  3,  8, 12, 17, 25, 30, 41, 43 ],
					    [  9, 11, 18, 24, 31, 40, 44, 53 ],
					    [ 10, 19, 23, 32, 39, 45, 52, 54 ],
					    [ 20, 22, 33, 38, 46, 51, 55, 60 ],
					    [ 21, 34, 37, 47, 50, 56, 59, 61 ],
					    [ 35, 36, 48, 49, 57, 58, 62, 63 ] ] )
	g = f.copy( )
	nr, nc = f.shape[:2]
	n = 8
	coeffs = np.zeros( [ 8, 8 ] )
	# 以 8x8 區塊為單位處理整張影像
	for x in range( 0, nr, n ):
		for y in range( 0, nc, n ):
			# 擷取 8x8 像素區塊
			for k in range( n ):
				for l in range( n ):
					if x + k < nr and y + l < nc:
						coeffs[k,l] = int( f[x+k,y+l] )
					else:
						coeffs[k,l] = 0
			# JPEG 壓縮步驟
			coeffs = coeffs - 128          # 減去 128，使值域中心化
			coeffs = cv2.dct( np.float32( coeffs ) )   # 正向 DCT
			coeffs = np.round( coeffs )
			coeffs = np.round( coeffs / normalize )	   # 量化（除以量化表）
			# 閾值化：根據 percentage 決定保留多少低頻係數
			thresh = n * n * percentage / 100
			for k in range( n ):
				for l in range( n ):
					# zig-zag 順序超過閾值的高頻係數設為 0
					if table[k,l] > thresh - 1:
						coeffs[k,l] = 0
			# JPEG 解壓縮步驟
			coeffs = coeffs * normalize    # 反量化（乘以量化表）
			coeffs = cv2.idct( np.float32( coeffs ) )  # 反向 DCT
			coeffs = np.round( coeffs )
			coeffs = coeffs + 128          # 加回 128 還原像素值
			# 寫回重建的像素值
			for k in range( n ):
				for l in range( n ):
					if x + k < nr and y + l < nc:
						value = np.clip( coeffs[k,l], 0, 255 )
						g[x+k,y+l] = np.uint8( value )
					else:
						g[x,y] = 0
	return g

def main( ):
	img1 = cv2.imread( "House.bmp", -1 )
	# 保留 30% 的 DCT 係數（70% 的高頻係數被捨棄）
	img2 = jpeg_compression( img1, 30 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Compressed Image", img2 )
	cv2.waitKey( 0 )

main( )
