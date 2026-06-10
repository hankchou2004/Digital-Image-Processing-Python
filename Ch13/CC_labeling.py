import numpy as np
import cv2

# 讀取二值化影像（含多個分離的連通區域）
img1 = cv2.imread( "ABC.bmp", -1 )
# 連通成分標記（Connected Component Labeling）
# 返回：n = 連通成分數量（含背景），labels = 每個像素的成分標籤陣列
n, labels = cv2.connectedComponents( img1 )
print( "Number of Connected Components =", n )
# 正規化標籤值到 0~255 以便顯示（不同標籤顯示為不同灰階值）
cv2.normalize( labels, labels, 0, 255, cv2.NORM_MINMAX )
img2 = np.uint8( labels )
cv2.imshow( "Original Image",  img1 )
cv2.imshow( "Connected Component Labeling", img2 )
cv2.waitKey( 0 )
