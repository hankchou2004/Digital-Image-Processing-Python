import numpy as np
import cv2

global img

# 滑鼠事件回呼函式：點擊影像時顯示座標與像素值
def onMouse( event, x, y, flags, param ):
	# 注意：OpenCV 影像索引為 (列, 行)，因此 x 與 y 需要對調
	x, y = y, x
	if img.ndim != 3:
		# 灰階影像：顯示灰階值
		print( "(x,y) = (%d, %d)" % (x, y), end = "  " )
		print( "Gray-Level = %3d" % img[x, y] )
	else:
		# 彩色影像：顯示 RGB 值（OpenCV 儲存順序為 BGR）
		print( "(x,y) = (%d, %d)" % (x, y), end = "  " )
		print( "(R, G, B) = (%3d, %3d, %3d)" %
			   ( img[x, y, 2], img[x, y, 1], img[x, y, 0] ) )

# 輸入檔名並讀取影像
filename = input( "Please enter filename: " )
img = cv2.imread( filename, -1 )
# 建立視窗並設定滑鼠事件回呼
cv2.namedWindow( filename )
cv2.setMouseCallback( filename, onMouse )
cv2.imshow( filename, img )
cv2.waitKey( 0 )
