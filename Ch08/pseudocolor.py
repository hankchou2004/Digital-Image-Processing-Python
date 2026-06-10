import numpy as np
import cv2

# 偽彩色處理：將灰階影像映射到彩色色彩圖（colormap）
# 用於增強視覺辨識度（例如熱像儀影像、醫學影像）
print( "Pseudocolor Image Processing:")
print( "(0) Autumn" )
print( "(1) Bone" )
print( "(2) Jet" )
print( "(3) Winter" )
print( "(4) Rainbow" )
print( "(5) Ocean" )
print( "(6) Summer" )
print( "(7) Spring" )
print( "(8) Cool" )
print( "(9) HSV" )
print( "(10) Pink" )
print( "(11) Hot" )
print( "(12) Parula" )
print( "(13) Magma" )
print( "(14) Inferno" )
print( "(15) Plasma" )
print( "(16) Viridis" )
print( "(17) Cividis" )
print( "(18) Twilight" )
print( "(19) Twilight Shifted" )
# 輸入色彩圖編號（對應 OpenCV 的 COLORMAP_ 常數）
colormap = eval( input( "Enter your choice: " ) )
img1 = cv2.imread( "Gray_Level.bmp", -1 )
# 套用選擇的色彩圖到灰階影像
img2 = cv2.applyColorMap( img1, colormap )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Pseudocolor Image", img2 )
cv2.waitKey( 0 )
