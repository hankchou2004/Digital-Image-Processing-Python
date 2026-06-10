import numpy as np
import cv2

# 讀取模板影像（要尋找的目標物件）
img1 = cv2.imread( "DSP.bmp", 0 )
# 讀取場景影像（目標物件可能出現在其中的影像）
img2 = cv2.imread( "DSP_Scene.bmp", 0 )
# 建立 ORB 特徵偵測器
orb = cv2.ORB_create()
# 同時偵測並計算兩張影像的 ORB 關鍵點與描述子
kp1, des1 = orb.detectAndCompute( img1, None )
kp2, des2 = orb.detectAndCompute( img2, None )
# 使用暴力比對器（BFMatcher）進行特徵匹配
# NORM_HAMMING：適用於二進位描述子（如 BRIEF/ORB），crossCheck=True 進行雙向驗證
bf = cv2.BFMatcher( cv2.NORM_HAMMING, crossCheck = True )
# 比對兩組描述子（回傳按距離排序的最佳匹配）
matches = bf.match( des1,des2 )
# 繪製匹配結果（flags=2 只繪製匹配的關鍵點）
img3 = cv2.drawMatches( img1, kp1, img2, kp2, matches, None, flags = 2 )
cv2.imshow( "Feature Matching", img3 )
cv2.waitKey( 0 )
