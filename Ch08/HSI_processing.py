import numpy as np
import cv2

# RGB 轉 HSI 色彩空間
def RGB_to_HSI( R, G, B ):
	r = R / 255
	g = G / 255
	b = B / 255
	if R == G and G == B:
		H = -1.0
		S =  0.0
		I = ( r + g + b ) / 3
	else:
		x = ( 0.5 * ( ( r - g ) + ( r - b ) ) ) / \
		    np.sqrt( ( r - g ) ** 2 + ( r - b ) * ( g - b ) )
		if x < -1.0:  x = -1.0
		if x >  1.0:  x =  1.0
		theta = np.arccos( x ) * 180 / np.pi
		if B <= G:
			H = theta
		else:
			H = 360.0 - theta
		S = 1.0 - 3.0 / ( r + g + b ) * min( r, g, b )
		I = ( r + g + b ) / 3
	return H, S, I

# HSI 轉回 RGB 色彩空間
def HSI_to_RGB( H, S, I ):
	if H == -1.0:   # 無彩色
		r = I; g = I; b = I
	elif H >= 0 and H < 120:   # RG 扇區（0~120°）
		HH = H
		b = I * ( 1 - S )
		r = I * ( 1 + ( S * np.cos( HH * np.pi / 180 ) ) /
			np.cos( ( 60 - HH ) * np.pi / 180 ) )
		g = 3.0 * I - ( r + b )
	elif H >= 120 and H < 240:  # GB 扇區（120~240°）
		HH = H - 120.0
		r = I * ( 1 - S )
		g = I * ( 1 + ( S * np.cos( HH * np.pi / 180 ) ) /
			np.cos( ( 60 - HH ) * np.pi / 180 ) )
		b = 3 * I - ( r + g )
	else:                       # BR 扇區（240~360°）
		HH = H - 240
		g = I * ( 1 - S )
		b = I * ( 1 + ( S * np.cos( HH * np.pi / 180 ) ) /
			np.cos( ( 60 - HH ) * np.pi / 180 ) )
		r = 3 * I - ( g + b )
	rr = round( r * 255 )
	gg = round( g * 255 )
	bb = round( b * 255 )
	R = np.uint8( np.clip( rr, 0, 255 ) )
	G = np.uint8( np.clip( gg, 0, 255 ) )
	B = np.uint8( np.clip( bb, 0, 255 ) )
	return R, G, B

# 在 HSI 空間中調整影像的色相、飽和度、強度
def HSI_processing( f, angle = 0, saturation = 100, intensity = 100 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
			# 旋轉色相（angle 度）
			H = H + angle
			if H > 360:  H = H - 360
			# 縮放飽和度（百分比）
			S = S * saturation / 100
			# 縮放強度（百分比）
			I = I * intensity / 100
			R, G, B = HSI_to_RGB( H, S, I )
			g[x,y,0] = B
			g[x,y,1] = G
			g[x,y,2] = R
	return g

def main( ):
	img = cv2.imread( "Rainbow_Village.bmp", -1 )
	# 色相旋轉 180 度（顏色互補）
	img1 = HSI_processing( img, 180, 100, 100 )
	# 飽和度降至 50%（顏色變淡）
	img2 = HSI_processing( img, 0, 50, 100 )
	# 強度降至 50%（影像變暗）
	img3 = HSI_processing( img, 0, 100, 50 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Hue(Rotate 180 degrees)", img1 )
	cv2.imshow( "Saturation by 50%", img2 )
	cv2.imshow( "Intensity by 50%", img3 )
	cv2.waitKey( 0 )

main( )
