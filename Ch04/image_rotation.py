import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Lenna.bmp", -1 )
nr2, nc2 = img1.shape[:2]
# 計算旋轉矩陣（2x3 仿射矩陣）
# 參數：旋轉中心（影像中心）、旋轉角度（逆時針30度）、縮放比例（1.0不縮放）
rotation_matrix = cv2.getRotationMatrix2D( ( nc2 / 2, nr2 / 2 ), 30, 1 )
# 套用仿射變換執行旋轉（輸出影像大小與原始相同）
img2 = cv2.warpAffine( img1, rotation_matrix, ( nc2, nr2 ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Rotation", img2 )
cv2.waitKey( 0 )
