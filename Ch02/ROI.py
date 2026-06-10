import numpy as np
import cv2

# 輸入影像檔名
filename = input( "Please enter filename: " )
# 輸入感興趣區域（ROI）的起始座標 (x, y)
ROI_x, ROI_y = eval( input( "Enter (x, y) for ROI: " ) )
# 輸入感興趣區域的大小（列數與行數）
ROI_nr, ROI_nc = eval( input( "Enter (rows, columns) for ROI: " ) )
# 讀取影像
img = cv2.imread( filename, -1 )
# 擷取感興趣區域（使用陣列切片）
ROI = img[ ROI_x : ROI_x + ROI_nr, ROI_y : ROI_y + ROI_nc ]
# 將擷取的 ROI 儲存為 BMP 檔案
cv2.imwrite( "ROI.bmp", ROI )
