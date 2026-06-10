import numpy as np
import cv2

# 讀取含有鹽與胡椒雜訊的灰階影像
img1 = cv2.imread( "Lenna_Salt_Pepper.bmp", 0 )
# 中值濾波：以鄰域像素的中位數取代中心像素
# 核心大小為 3x3，對鹽與胡椒雜訊（脈衝雜訊）有極佳的去除效果
img2 = cv2.medianBlur( img1, 3 )

cv2.imshow( "Original Image", img1 )
cv2.imshow( "Median Filtering", img2 )
cv2.waitKey( 0 )

# 儲存濾波結果
cv2.imwrite( "output.bmp", img2 )
