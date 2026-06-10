import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Osaka.bmp", -1 )
# Canny 邊緣偵測：多步驟邊緣偵測演算法
# 步驟：高斯平滑 → 計算梯度 → 非最大值抑制 → 雙閾值處理 → 邊緣追蹤
# 低閾值=50，高閾值=200（比例建議為 1:3 或 1:2）
img2 = cv2.Canny( img1, 50, 200 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Canny Edge Detection", img2 )
cv2.waitKey( 0 )
