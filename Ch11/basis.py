import numpy as np
import cv2

# 計算並視覺化 DFT 基函數（實部或虛部）
def DFT_basis( n, method ):
	basis = np.zeros( [ n * n + n - 1, n * n + n - 1 ] )
	img = np.zeros( [ n * n + n - 1, n * n + n - 1 ], dtype = 'uint8' )
	for u in range( n ):
		for v in range( n ):
			for x in range( n ):
				for y in range( n ):
					if method == 1:
						# 實部基函數：cos(2π(ux+vy)/n)
						value = np.cos( 2 * np.pi * ( u * x + v * y ) / n )
					else:
						# 虛部基函數：-sin(2π(ux+vy)/n)
						value = -np.sin( 2 * np.pi * ( u * x + v * y ) / n )
					basis[ u * ( n + 1 ) + x, v * ( n + 1 ) + y ] = value
	cv2.normalize( basis, basis, 0, 255, cv2.NORM_MINMAX )
	img = np.uint8( basis )
	return img

# 計算並視覺化 DCT（離散餘弦轉換）基函數
def DCT_basis( n ):
	basis = np.zeros( [ n * n + n - 1, n * n + n - 1 ] )
	img = np.zeros( [ n * n + n - 1, n * n + n - 1 ], dtype = 'uint8' )
	for u in range( n ):
		for v in range( n ):
			for x in range( n ):
				for y in range( n ):
					# 計算正規化係數 alpha
					if u == 0:
						alpha_u = np.sqrt( 1.0 / n )
					else:
						alpha_u = np.sqrt( 2.0 / n )
					if v == 0:
						alpha_v = np.sqrt( 1.0 / n )
					else:
						alpha_v = np.sqrt( 2.0 / n )
					# DCT 基函數公式
					value = alpha_u * alpha_v * \
					    np.cos( ( ( 2 * x + 1 ) * u * np.pi ) / ( 2 * n ) ) * \
					    np.cos( ( ( 2 * y + 1 ) * v * np.pi ) / ( 2 * n ) )
					basis[ u * ( n + 1 ) + x, v * ( n + 1 ) + y ] = value
	cv2.normalize( basis, basis, 0, 255, cv2.NORM_MINMAX )
	img = np.uint8( basis )
	return img

# 輔助函式：取得整數 x 的第 i 個位元
def b_i( x, i ):
	j = 1
	return j & ( x >> i )

# 計算 WHT 中的位元排列索引
def p_i( x, i, m ):
	if i == 0:
		return b_i( x, m - 1 )
	else:
		return b_i( x, m - 1 ) + b_i( x, m - i - 1 )

# 計算並視覺化 WHT（Walsh-Hadamard 轉換）基函數
def WHT_basis( n ):
	basis = np.zeros( [ n * n + n - 1, n * n + n - 1 ] )
	img = np.zeros( [ n * n + n - 1, n * n + n - 1 ], dtype = 'uint8' )
	# m = log2(n)
	m = int( np.log( n ) / np.log( 2.0 ) )
	for u in range( n ):
		for v in range( n ):
			for x in range( n ):
				for y in range( n ):
					sum = 0
					for i in range( m ):
						sum += ( b_i( x, i ) * p_i( u, i, m ) + \
							     b_i( y, i ) * p_i( v, i, m ) )
					# WHT 基函數值為 +1 或 -1
					value = ( 1 / n ) * pow( -1.0, sum )
					if value > 0:
						img[ u * ( n + 1 ) + x, v * ( n + 1 ) + y ] = 255
					else:
						img[ u * ( n + 1 ) + x, v * ( n + 1 ) + y ] = 0
	return img

def main( ):
	print( "Matrix-based Transform Basis" )
	print( "(1) Discrete Fourier Transform (DFT) Real" )
	print( "(2) Discrete Fourier Transform (DFT) Imaginary" )
	print( "(3) Discrete Cosine Transform (DCT)")
	print( "(4) Walsh-Hadamard Transform (WHT)" )
	method = eval( input( "Please select your choice: " ) )
	n = eval( input( "Please select n: " ) )
	if method == 1:
		img = DFT_basis( n, 1 )
	if method == 2:
		img = DFT_basis( n, 2 )
	if method == 3:
		img = DCT_basis( n )
	if method == 4:
		img = WHT_basis( n )
	cv2.imshow( "Basis", img )
	cv2.waitKey( 0 )

main( )
