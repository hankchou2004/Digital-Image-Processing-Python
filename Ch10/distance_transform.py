import numpy as np
import cv2

# 讀取二值化的幾何形狀影像（白色前景，黑色背景）
img1 = cv2.imread( "Shapes.bmp", 0 )
# 距離轉換：計算每個前景像素到最近背景像素的距離
# 使用 L1 距離（曼哈頓距離），遮罩大小為 3x3
dist = cv2.distanceTransform( img1, cv2.DIST_L1, 3 )
# 正規化距離值到 0~255 以便顯示（中心點距離最大，邊緣為 0）
cv2.normalize( dist, dist, 0, 255, cv2.NORM_MINMAX )
img2 = np.uint8( dist )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Distance Transform", img2 )
cv2.waitKey( 0 )
