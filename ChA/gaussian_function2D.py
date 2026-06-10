import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# 標準差（控制二維高斯函數的擴散範圍）
sigma = 1

# 二維高斯函數：g(x,y) = exp(-(x²+y²)/(2σ²))
# 具有旋轉對稱性，常用於影像模糊（高斯濾波核心）
X = np.linspace( -3 * sigma, 3 * sigma, 100 )
Y = np.linspace( -3 * sigma, 3 * sigma, 100 )
# 建立 x-y 平面的網格座標
x, y = np.meshgrid( X, Y )
# 計算每個網格點的高斯函數值
z = np.exp( -( x * x + y * y ) / ( 2 * sigma * sigma ) )

# 以 3D 曲面圖視覺化二維高斯函數（coolwarm 色彩圖）
fig = plt.figure( )
ax = plt.axes( projection = "3d" )
ax.plot_surface( x, y, z, cmap = cm.coolwarm, linewidth = 0,
	             antialiased = False )
plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.show( )
