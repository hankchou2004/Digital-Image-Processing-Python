import numpy as np
import cv2

# 影像形成模型：使用高斯照度函數模擬光源照射效果
def image_formation_model( f, x0, y0, sigma ):
	# 複製原始影像作為輸出
	g = f.copy( )
	nr, nc = f.shape[:2]
	# 建立照度圖（高斯分布）
	illumination = np.zeros( [ nr, nc ], dtype = 'float32' )
	# 計算每個像素的照度值（以 (x0, y0) 為光源中心的高斯函數）
	for x in range( nr ):
		for y in range( nc ):
			illumination[x,y] = np.exp( -( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 ) /
								( 2 * sigma * sigma ) )
	# 將照度乘以原始影像各像素值
	for x in range( nr ):
		for y in range( nc ):
			for k in range( 3 ):
				val = round( illumination[x,y] * f[x,y,k] )
				g[x,y,k] = np.uint8( val )
	return g

def main( ):
	img = cv2.imread( "Monet.bmp", -1 )
	nr, nc = img.shape[:2]
	# 設定光源中心為影像正中央
	x0 = nr // 2
	y0 = nc // 2
	# sigma 控制高斯照度的擴散範圍
	sigma = 400
	img2 = image_formation_model( img, x0, y0, sigma )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Image Formation Model", img2 )
	cv2.waitKey( 0 )

main( )
