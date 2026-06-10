import numpy as np
import cv2

# 讀取原始影像
img = cv2.imread( "Brunch.bmp", -1 )
# 鉛筆素描效果（Pencil Sketch）：將照片轉換為手繪素描風格
# img1：灰階素描（只有亮度資訊，類似鉛筆速寫）
# img2：彩色素描（保留色彩資訊，類似彩色鉛筆畫）
img1, img2 = cv2.pencilSketch( img )
cv2.imshow( "Original Image", img )
cv2.imshow( "Pencil Sketch 1", img1 )
cv2.imshow( "Pencil Sketch 2", img2 )
cv2.waitKey( 0 )
