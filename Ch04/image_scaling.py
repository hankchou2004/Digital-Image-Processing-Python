import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Lenna.bmp", -1 )
nr, nc = img1.shape[:2]
# 輸入縮放比例（例如 0.5 表示縮小一半，2.0 表示放大兩倍）
scale = eval( input( "Please enter scale: " ) )
# 計算縮放後的新尺寸
nr2 = int( nr * scale )
nc2 = int( nc * scale )
# 使用雙線性內插進行影像縮放
img2 = cv2.resize( img1, ( nr2, nc2 ), interpolation = cv2.INTER_LINEAR )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Scaling", img2 )
cv2.waitKey( 0 )
