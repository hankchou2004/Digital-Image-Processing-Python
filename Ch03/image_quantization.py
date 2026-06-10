import numpy as np
import cv2

# 影像灰階量化：將連續灰階值縮減為有限個離散等級
def image_quantization( f, bits ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 量化等級數 = 2^bits（例如 bits=5 → 32 個等級）
	levels = 2 ** bits
	# 每個等級對應的原始灰階範圍寬度
	interval = 256 / levels
	# 輸出等級之間的間距（均勻分布在 0~255）
	gray_level_interval = 255 / ( levels - 1 )
	# 建立 256 個輸入灰階對應到量化輸出的查找表
	table = np.zeros( 256 )
	for k in range( 256 ):
		for l in range( levels ):
			if k >= l * interval and k < ( l + 1 ) * interval:
				table[k] = round( l * gray_level_interval )
	# 套用查找表到每個像素
	for x in range( nr ):
		for y in range( nc ):
			g[x,y] = np.uint8( table[f[x,y]] )
	return g

def main( ):
	img1 = cv2.imread( "Lenna.bmp", -1 )
	# 量化為 5-bit（32 個灰階等級），可觀察到明顯的偽輪廓效應
	img2 = image_quantization( img1, 5 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Quantization", img2 )
	cv2.waitKey( 0 )

main( )
