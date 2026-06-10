import numpy as np
import cv2

# 讀取灰階影像（含有不均勻照明的文字影像）
img = cv2.imread( "Script.bmp", 0 )
# 全域閾值化：以單一閾值 128 二值化整張影像（不均勻照明效果差）
thresh, img1 = cv2.threshold( img, 128, 255, cv2.THRESH_BINARY )
# 自適應閾值化（平均法）：以 11x11 鄰域的平均值為局部閾值
# 可有效處理不均勻照明，適合掃描文件等場景
img2 = cv2.adaptiveThreshold( img, 255,
	   cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0 )
# 自適應閾值化（高斯法）：以 11x11 鄰域的高斯加權平均值為局部閾值
# 比平均法更平滑，對雜訊較不敏感
img3 = cv2.adaptiveThreshold( img, 255,
	   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0 )
cv2.imshow( "Original Image",  img )
cv2.imshow( "Global Thresholding", img1 )
cv2.imshow( "Adaptive Thresholding(Mean)", img2 )
cv2.imshow( "Adaptive Thresholding(Gaussian)", img3 )
cv2.waitKey( 0 )
