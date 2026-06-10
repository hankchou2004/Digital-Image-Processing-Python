import numpy as np
import cv2

# 運動模糊效果：模擬相機在快門開啟期間發生相對移動的模糊效果
def motion_blur( f, length, angle ):
	nr, nc = f.shape[:2]
	# 建立運動模糊濾波器（沿指定角度方向的線型濾波核心）
	filter = np.zeros( [ length, length ] )
	x0, y0 = length // 2, length // 2
	# 計算運動方向的端點位移
	x_len  = round( x0 * np.cos( np.radians( angle ) ) )
	y_len  = round( y0 * np.sin( np.radians( angle ) ) )
	x1, y1 = int( x0 - x_len ), int( y0 - y_len )
	x2, y2 = int( x0 + x_len ), int( y0 + y_len )
	# 在濾波器上繪製一條線段（表示運動軌跡）
	cv2.line( filter, ( y1, x1 ), ( y2, x2 ), ( 1, 1, 1 ) )
	# 正規化濾波器（使所有非零元素的和為 1）
	filter /= np.sum( filter )
	# 套用線型濾波器
	g = cv2.filter2D( f, -1, filter )
	return g

def main( ):
	img1 = cv2.imread( "Traffic_Lanes.bmp", -1 )
	# 水平方向（0 度）、長度 20 像素的運動模糊
	img2 = motion_blur( img1, 20, 0 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Motion Blur", img2 )
	cv2.waitKey( 0 )

main( )
