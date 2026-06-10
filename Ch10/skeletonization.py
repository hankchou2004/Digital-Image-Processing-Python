import numpy as np
import cv2

# Zhang-Suen 骨架化演算法：迭代移除邊緣像素，保留物件的拓樸骨架
def skeletonization( f ):
	nr, nc = f.shape[:2]
	temp = f.copy( )
	g = f.copy( )
	change = True
	step = 1
	while change:
		change = False
		if step == 1:
			# 第一步：檢查並標記可刪除像素（滿足特定鄰域條件）
			for x in range( 1, nr ):
				for y in range( 1, nc ):
					p = [ False ] * 10
					if temp[x,y] != 0:
						# 建立 3x3 鄰域的 8 個鄰居狀態（p2~p9，順時針排列）
						if temp[x-1,y]   != 0:  p[2] = True
						if temp[x-1,y+1] != 0:  p[3] = True
						if temp[x,y+1]   != 0:  p[4] = True
						if temp[x+1,y+1] != 0:  p[5] = True
						if temp[x+1,y]   != 0:  p[6] = True
						if temp[x+1,y-1] != 0:  p[7] = True
						if temp[x,y-1]   != 0:  p[8] = True
						if temp[x-1,y-1] != 0:  p[9] = True
						# N(p)：鄰居中前景像素的數量
						N = 0
						for k in range( 2, 10 ):
							if p[k] == True:
								N += 1
						# T(p)：順時針方向 0→1 的轉換次數（連通性）
						T = 0
						for k in range( 2, 9 ):
							if p[k] == False and p[k + 1] == True:
								T += 1
						if p[9] == False and p[2] == True:
							T += 1
						# 符合四個條件才刪除（第一步特定條件）
						if ( ( N >= 2 and N <= 6 ) and ( T == 1 ) and
							 ( ( p[2] and p[4] and p[6] ) == False ) and
							 ( ( p[4] and p[6] and p[8] ) == False ) ):
							g[x,y] = 0
							change = True
		if step == 2:
			# 第二步：使用不同條件再次標記可刪除像素
			for x in range( 1, nr ):
				for y in range( 1, nc ):
					p = [ False ] * 10
					if temp[x,y] != 0:
						if temp[x-1,y]   != 0:  p[2] = True
						if temp[x-1,y+1] != 0:  p[3] = True
						if temp[x,y+1]   != 0:  p[4] = True
						if temp[x+1,y+1] != 0:  p[5] = True
						if temp[x+1,y]   != 0:  p[6] = True
						if temp[x+1,y-1] != 0:  p[7] = True
						if temp[x,y-1]   != 0:  p[8] = True
						if temp[x-1,y-1] != 0:  p[9] = True
						N = 0
						for k in range( 2, 10 ):
							if p[k] == True:
								N += 1
						T = 0
						for k in range( 2, 9 ):
							if p[k] == False and p[k + 1] == True:
								T += 1
						if p[9] == False and p[2] == True:
							T += 1
						# 符合四個條件才刪除（第二步特定條件）
						if ( ( N >= 2 and N <= 6 ) and ( T == 1 ) and
							 ( ( p[2] and p[4] and p[8] ) == False ) and
							 ( ( p[2] and p[6] and p[8] ) == False ) ):
							g[x,y] = 0
							change = True
		temp = g.copy( )
		# 交替執行第一步和第二步，直到影像不再改變
		if step == 1:  step = 2
		else:          step = 1
	return g

def main( ):
	img1 = cv2.imread( "ABC.bmp", -1 )
	img2 = skeletonization( img1 )
	cv2.imshow( "Original Image",  img1 )
	cv2.imshow( "Skeletonization", img2 )
	cv2.waitKey( 0 )

main( )
