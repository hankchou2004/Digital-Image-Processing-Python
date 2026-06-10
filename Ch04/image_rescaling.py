import numpy as np
import cv2

# 讀取灰階影像
img = cv2.imread( "Baboon.bmp", 0 )
nr1, nc1 = img.shape[:2]
# 將影像縮小為原來的 1/4
nr2, nc2 = nr1 // 4, nc1 // 4
# 最近鄰內插法縮小，再放大回原尺寸（可見明顯馬賽克）
img1 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_NEAREST )
img1 = cv2.resize( img1, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
# 雙線性內插法縮小，再放大回原尺寸（較平滑）
img2 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_LINEAR )
img2 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
# 雙三次內插法縮小，再放大回原尺寸（更平滑）
img3 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_CUBIC )
img3 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )
cv2.imshow( "Original Image", img )
cv2.imshow( "Nearest Neighbor", img1 )
cv2.imshow( "Bilinear", img2 )
cv2.imshow( "Bicubic", img3 )
cv2.waitKey( 0 )
