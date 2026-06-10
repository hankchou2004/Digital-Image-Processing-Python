import numpy as np

# 定義一維輸入訊號 x 與濾波器 h
x = np.array( [ 1, 2, 4, 3, 2, 1, 1 ] )
h = np.array( [ 1, 2, 3, 1, 1 ] )
# 完整卷積（'full'）：輸出長度 = len(x) + len(h) - 1
y = np.convolve( x, h, 'full' )
# 相同長度卷積（'same'）：輸出長度與 x 相同，以 x 的中心對齊
y1 = np.convolve( x, h, 'same' )
print( "x =", x )
print( "h =", h )
print( "Full Convolution y =", y )
print( "Convolution y =", y1 )
