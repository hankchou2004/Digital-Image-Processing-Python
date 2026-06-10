import numpy as np
import cv2
import scipy.special as special
import matplotlib.pyplot as plt

# 產生 0~255 的輸入灰階值（對應 0~1 的正規化值）
x = np.linspace( 0, 1, 256 )
x1 = x * 255
# 計算不同參數下的 Beta 函數輸出（a=b=0.5：S 形，增強對比）
y1 = special.betainc( 0.5, 0.5, x ) * 255
# 線性映射（a=b=1，即恆等函數）
y2 = x1
# a=b=2.0：反 S 形，壓縮高低灰階
y3 = special.betainc( 2.0, 2.0, x ) * 255

# 繪製三條 Beta 函數曲線
plt.plot( x1, y1, '--', label = 'a = 0.5, b = 0.5' )
plt.plot( x1, y2, '-',  label = 'a = 1.0, b = 1.0' )
plt.plot( x1, y3, '--', label = 'a = 2.0, b = 2.0' )
plt.xlabel( 'Input Intensity' )
plt.ylabel( 'Output Intensity' )
plt.legend( loc = 'lower right' )

plt.show( )
