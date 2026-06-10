import numpy as np
import cv2

# 影像下採樣函式：以指定取樣率縮減影像大小
def image_downsampling( f, sampling_rate ):
	# 取得原始影像的列數與行數
	nr, nc = f.shape[:2]
	# 計算下採樣後的影像大小
	nr_s, nc_s = nr // sampling_rate, nc // sampling_rate
	# 建立空白的下採樣輸出影像（灰階）
	g = np.zeros( [ nr_s, nc_s ], dtype = 'uint8' )
	# 以取樣率為間隔，選取對應像素（最近鄰取樣）
	for x in range( nr_s ):
		for y in range( nc_s ):
			g[x,y] = f[x * sampling_rate, y * sampling_rate]
	return g

def main( ):
	# 讀取原始灰階影像
	img1 = cv2.imread( "Barbara.bmp", -1 )
	# 以 2 倍取樣率進行下採樣
	img2 = image_downsampling( img1, 2 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Downsampling by 2", img2 )
	cv2.waitKey( 0 )

main( )
