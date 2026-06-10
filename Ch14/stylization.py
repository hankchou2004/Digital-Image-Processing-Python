import numpy as np
import cv2

# 讀取原始影像
img1 = cv2.imread( "Brunch.bmp", -1 )
# 風格化效果（Stylization）：將照片轉換為類似油畫或插畫的風格
# 使用邊緣保留濾波與細節增強，使影像看起來像手繪或卡通效果
img2 = cv2.stylization( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Stylization", img2 )
cv2.waitKey( 0 )
