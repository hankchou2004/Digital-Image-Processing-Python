import numpy as np
import cv2

# 使用 Haar 特徵級聯分類器進行人臉偵測
def face_detection( f ):
	g = f.copy( )
	# 轉為灰階（分類器需要灰階影像）
	gray = cv2.cvtColor( f, cv2.COLOR_BGR2GRAY )
	# 載入預訓練的正臉 Haar 級聯分類器（XML 格式）
	face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml' )
	# 偵測人臉：scaleFactor=1.1（影像縮放比例），minNeighbors=5（有效偵測最少鄰居數）
	faces = face_cascade.detectMultiScale( gray, 1.1, 5 )
	# 在每個偵測到的臉部區域繪製藍色邊界框
	for ( x, y, w, h ) in faces:
		g = cv2.rectangle( g, ( x, y ), ( x + w, y + h ), ( 255, 0, 0 ), 2 )
	return g

def main( ):
	img1 = cv2.imread( "Akiyo.bmp", -1 )
	img2 = face_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Face Detection", img2 )
	cv2.waitKey( 0 )

main( )
