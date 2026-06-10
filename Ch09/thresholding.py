import cv2

# 讀取灰階影像
img1 = cv2.imread( "Bug.bmp", 0 )
# 使用 Otsu 自動閾值化進行二值化
# THRESH_BINARY_INV：前景（蟲體）為白色，背景為黑色
# THRESH_OTSU：自動計算最佳閾值（最大化類間變異數）
thresh, img2 = cv2.threshold( img1, 127, 255,
               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )
# 顯示 Otsu 自動計算的閾值
print( "Threshold =", thresh )
cv2.imshow( "Original Image",  img1 )
cv2.imshow( "Thresholding", img2 )
cv2.waitKey( 0 )
