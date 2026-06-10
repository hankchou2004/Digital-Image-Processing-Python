import numpy as np
import cv2

# 將 RGB 轉換為 HSI（色相、飽和度、強度）色彩空間
def RGB_to_HSI( R, G, B ):
	# 將 0~255 正規化為 0~1
	r = R / 255
	g = G / 255
	b = B / 255
	if R == G and G == B:  # 無彩色（灰階）像素
		H = -1.0           # 無色相（以 -1 表示未定義）
		S =  0.0           # 飽和度為 0
		I = ( r + g + b ) / 3
	else:
		# 計算色相角的餘弦值
		x = ( 0.5 * ( ( r - g ) + ( r - b ) ) ) / \
		    np.sqrt( ( r - g ) ** 2 + ( r - b ) * ( g - b ) )
		# 夾住浮點誤差
		if x < -1.0:  x = -1.0
		if x >  1.0:  x =  1.0
		theta = np.arccos( x ) * 180 / np.pi  # 轉換為角度（0~180）
		# 根據藍色與綠色大小決定色相在 0~360 的位置
		if B <= G:
			H = theta
		else:
			H = 360.0 - theta
		S = 1.0 - 3.0 / ( r + g + b ) * min( r, g, b )
		I = ( r + g + b ) / 3
	return H, S, I

# 擷取 HSI 色彩模型的指定分量並以灰階影像顯示
def HSI_model( f, channel ):
	nr, nc = f.shape[:2]
	g = np.zeros( [nr, nc], dtype = 'uint8' )
	if channel == 1:		# 色相（Hue）：映射到 0~255
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				if H == -1:
					k = 0
				else:
					k = round( H * 255 / 360 )
				g[x,y] = np.uint8( k )
	elif channel == 2:		# 飽和度（Saturation）：映射到 0~255
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				k = round( S * 255 )
				g[x,y] = np.uint8( k )
	else:					# 強度（Intensity）：映射到 0~255
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				k = round( I * 255 )
				g[x,y] = np.uint8( k )
	return g

def main( ):
	img = cv2.imread( "Rose.bmp", -1 )
	H = HSI_model( img, 1 )
	S = HSI_model( img, 2 )
	I = HSI_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Hue", H )
	cv2.imshow( "Saturation", S )
	cv2.imshow( "Intensity", I )
	cv2.waitKey( 0 )

main( )
