import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Brunch.bmp", -1 )
# 細節增強（Detail Enhancement）：強化影像中的紋理和細節
# 使用 OpenCV 的非真實感渲染模組（ximgproc）
# 效果：保留邊緣的同時增強細節，常用於攝影後製
img2 = cv2.detailEnhance( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Detail Enhance", img2 )
cv2.waitKey( 0 )
# 儲存結果
cv2.imwrite( "B.bmp", img2 )
