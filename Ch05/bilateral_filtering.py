import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Jenny.bmp", -1 )
# 雙邊濾波：同時考慮空間距離與像素強度差異
# 參數：核心直徑=11，空間 sigma=50（空間權重），灰階 sigma=50（強度權重）
# 特點：保留邊緣的同時平滑非邊緣區域（邊緣保留濾波）
img2 = cv2.bilateralFilter( img1, 11, 50, 50 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Bilateral Filtering", img2 )
cv2.waitKey( 0 )
