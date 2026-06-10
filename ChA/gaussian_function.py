import numpy as np
import matplotlib.pyplot as plt

# 標準差（控制高斯函數的寬度，sigma 越大曲線越寬）
sigma = 1

# 高斯函數：g(x) = exp(-x²/(2σ²))，鐘形曲線，常用於模糊和加權運算
x = np.linspace( -3 * sigma, 3 * sigma, 100 )
g = np.exp( -( x * x ) / ( 2 * sigma * sigma ) )
# 高斯函數的一階導函數：g'(x) = -(x/σ²) * g(x)，用於邊緣偵測（零交叉點為邊緣）
gx = -( x / ( sigma * sigma ) ) * g
# 高斯函數的二階導數：g''(x) = ((x²-σ²)/σ⁴) * g(x)，即 LoG（高斯拉普拉斯），用於精確邊緣定位
gxx = ( ( x * x - sigma * sigma ) / pow( sigma, 4 ) ) * g

# 繪製高斯函數
plt.figure( 1 )
plt.plot( x, g )
plt.xlabel( "x" )
plt.ylabel( "g(x)" )
# 繪製一階導函數（奇函數，零交叉點即為高斯函數的峰值）
plt.figure( 2 )
plt.plot( x, gx )
plt.xlabel( "x" )
plt.ylabel( "g'(x)" )
# 繪製二階導函數（Mexican hat 形狀，零交叉點對應邊緣位置）
plt.figure( 3 )
plt.plot( x, gxx )
plt.xlabel( "x" )
plt.ylabel( "g''(x)" )
plt.show( )
