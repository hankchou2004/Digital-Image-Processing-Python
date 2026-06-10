import numpy as np
import cv2

# 形態學細化（Thinning）：使用 Hit-or-Miss 轉換和結構元素集合迭代細化物件
def thinning( f ):
	# 定義 8 個方向的結構元素（B1~B8），用於偵測邊緣方向
	# -1 表示不關心，0 表示背景，1 表示前景
	B1 = np.array( [ [ -1, -1, -1 ], [ 0, 1, 0 ], [ 1, 1, 1 ] ] )  # 南方邊緣
	B2 = np.array( [ [ 0, -1, -1 ], [ 1, 1, -1 ], [ 1, 1, 0 ] ] )  # 西南方
	B3 = np.array( [ [ 1, 0, -1 ], [ 1, 1, -1 ], [ 1, 0, -1 ] ] )  # 西方邊緣
	B4 = np.array( [ [ 1, 1, 0 ], [ 1, 1, -1 ], [ 0, -1, -1 ] ] )  # 西北方
	B5 = np.array( [ [ 1, 1, 1 ], [ 0, 1, 0 ], [ -1, -1, -1 ] ] )  # 北方邊緣
	B6 = np.array( [ [ 0, 1, 1 ], [ -1, 1, 1 ], [ -1, -1, 0 ] ] )  # 東北方
	B7 = np.array( [ [ -1, 0, 1 ], [ -1, 1, 1 ], [ -1, 0, 1 ] ] )  # 東方邊緣
	B8 = np.array( [ [ -1, -1, 0 ], [ -1, 1, 1 ], [ 0, 1, 1 ] ] )  # 東南方
	g  = f.copy( )
	g2 = f.copy( )
	change = True
	# 持續迭代直到影像不再改變（收斂）
	while change:
		# 對每個方向的結構元素執行 Hit-or-Miss 轉換並從影像中減去匹配點
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B1 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B2 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B3 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B4 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B5 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B6 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B7 )
		g = g - temp
		temp = cv2.morphologyEx( g, cv2.MORPH_HITMISS, B8 )
		g = g - temp
		# 判斷是否收斂（影像不再改變則停止）
		if np.array_equal( g, g2 ):
			change = False
		else:
			g2 = g.copy( )
			change = True
	return g

def main( ):
	img1 = cv2.imread( "ABC.bmp", -1 )
	img2 = thinning( img1 )
	cv2.imshow( "Original Image",  img1 )
	cv2.imshow( "Thinning", img2 )
	cv2.waitKey( 0 )

main( )
