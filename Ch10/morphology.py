import numpy as np
import cv2

# 讀取二值化影像（前景為白色）
img1 = cv2.imread( "Bug.bmp", -1 )
print( "Morphological Image Processing" )
print( "(1) Erosion" )
print( "(2) Dilation" )
print( "(3) Opening" )
print( "(4) Closing" )
choice = eval( input( "Please enter your choice: " ) )
# 輸入結構元素的大小（正方形）
size = eval( input( "Size of structuring element: " ) )
# 建立全為1的正方形結構元素（SE，Structuring Element）
kernel = np.ones( ( size, size ), np.uint8 )
if choice == 1:
	# 腐蝕（Erosion）：縮小前景物件，移除小突起和細線
	img2 = cv2.erode( img1, kernel, iterations = 1 )
elif choice == 2:
	# 膨脹（Dilation）：擴大前景物件，填補小孔洞
	img2 = cv2.dilate( img1, kernel, iterations = 1 )
elif choice == 3:
	# 開運算（Opening）= 先腐蝕再膨脹：去除小雜點，保持物件形狀
	img2 = cv2.morphologyEx( img1, cv2.MORPH_OPEN, kernel )
else:
	# 閉運算（Closing）= 先膨脹再腐蝕：填補物件內部小孔洞
	img2 = cv2.morphologyEx( img1, cv2.MORPH_CLOSE, kernel )
cv2.imshow( "Original Image",  img1 )
cv2.imshow( "Morphological Image Processing", img2 )
cv2.waitKey( 0 )
