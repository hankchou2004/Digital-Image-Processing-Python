import numpy as np
import cv2

# 讀取原始影像（含有需要校正的透視畫面）
img1 = cv2.imread( "Gallery.bmp", -1 )
nr, nc = img1.shape[:2]
# 定義來源影像中的四個角點（畫框的四個角落，帶透視變形）
pts1 = np.float32( [ [ 795, 350 ], [ 795, 690 ], [ 1090, 720 ], [ 1090, 250 ] ] )
# 定義目標影像中對應的四個角點（正矩形）
pts2 = np.float32( [ [ 0, 0 ], [ 0, 500 ], [ 650, 500 ], [ 650, 0 ] ] )
# 計算透視變換矩陣（3x3 單應性矩陣）
T = cv2.getPerspectiveTransform( pts1, pts2 )
# 套用透視變換，輸出校正後的影像
img2 = cv2.warpPerspective( img1, T, ( 650, 500 ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Perspective Transform", img2 )
cv2.waitKey( 0 )
