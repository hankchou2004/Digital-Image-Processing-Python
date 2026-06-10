import numpy as np
import cv2

# 輸入影像檔名
filename = input( "Please enter filename: " )
# 讀取影像（-1 保留原始通道數）
img = cv2.imread( filename, -1 )
# 取得影像的列數（高度）與行數（寬度）
nr, nc = img.shape[:2]
print( "Number of Rows =", nr )
print( "Number of Columns =", nc )
# 判斷是灰階影像（2維）還是彩色影像（3維）
if img.ndim != 3:
	print( "Gray-Level Image" )
else:
	print( "Color Image" )
