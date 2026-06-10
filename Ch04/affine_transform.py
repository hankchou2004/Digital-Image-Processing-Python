import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Poker.bmp", -1 )
nr, nc = img1.shape[:2]
# 定義仿射變換的來源三個控制點
pts1 = np.float32( [ [ 160, 165 ], [ 240, 390 ], [ 270, 125 ] ] )
# 定義仿射變換的目標三個控制點
pts2 = np.float32( [ [ 190, 140 ], [ 190, 375 ], [ 310, 140 ] ] )
# 根據三組對應點計算仿射變換矩陣（2x3）
T = cv2.getAffineTransform( pts1, pts2 )
# 套用仿射變換（輸出影像大小與原始相同）
img2 = cv2.warpAffine( img1, T, ( nc, nr ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Affine Transform", img2 )
cv2.waitKey( 0 )
# 儲存結果
cv2.imwrite( "O.bmp", img2 )
