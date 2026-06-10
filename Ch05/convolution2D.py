import numpy as np
from scipy.signal import convolve2d

# 定義 3x3 的二維輸入影像 x（全為 1 的矩陣）
x = np.array( [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ] )
# 定義 3x3 的卷積核心 h
h = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
# 執行二維卷積（'same'：輸出大小與輸入 x 相同）
y = convolve2d( x, h, 'same' )
print( "x =" )
print( x )
print( "h =" )
print( h )
print( "Convolution y =" )
print( y )
