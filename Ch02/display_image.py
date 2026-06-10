import numpy as np
import cv2

# 讀取影像檔案（-1 表示以原始格式讀取，包含透明度通道）
img = cv2.imread( "Lenna.bmp", -1 )
# 在視窗中顯示影像
cv2.imshow( "Example", img )
# 等待按鍵輸入（0 表示無限等待）
cv2.waitKey( 0 )
# 關閉所有開啟的視窗
cv2.destroyAllWindows( )
