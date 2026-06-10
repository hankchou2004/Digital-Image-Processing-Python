import numpy as np
import cv2

# 定義數位影像(全黑)，尺寸為 400x500，3 個色彩通道
img = np.zeros( [ 400, 500, 3 ], dtype = 'uint8' )
# 置入文字到影像中，示範各種 OpenCV 字體樣式
text = "Hello OpenCV"
# FONT_HERSHEY_SIMPLEX：標準無襯線字體
fontFace = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText( img, text, ( 10, 50 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_PLAIN：較小的無襯線字體
fontFace = cv2.FONT_HERSHEY_PLAIN
cv2.putText( img, text, ( 10, 90 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_DUPLEX：雙線無襯線字體
fontFace = cv2.FONT_HERSHEY_DUPLEX
cv2.putText( img, text, ( 10, 130 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_COMPLEX：複雜無襯線字體
fontFace = cv2.FONT_HERSHEY_COMPLEX
cv2.putText( img, text, ( 10, 170 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_TRIPLEX：三線無襯線字體
fontFace = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText( img, text, ( 10, 210 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_COMPLEX_SMALL：小型複雜字體
fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText( img, text, ( 10, 250 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_SCRIPT_SIMPLEX：手寫風格字體
fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText( img, text, ( 10, 290 ), fontFace, 1.0, ( 255, 255, 255 ) )
# FONT_HERSHEY_SCRIPT_COMPLEX：複雜手寫字體
fontFace = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText( img, text, ( 10, 330 ), fontFace, 1.0, ( 255, 255, 255 ) )
# 顯示數位影像
cv2.imshow( "Example", img )
cv2.waitKey( 0 )
