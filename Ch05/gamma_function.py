import numpy as np
import matplotlib.pyplot as plt

# 定義多個 gamma 值，涵蓋小於1（變亮）到大於1（變暗）的範圍
gamma1 = 0.1
gamma2 = 0.2
gamma3 = 0.5
gamma4 = 1.0   # 線性映射（無校正）
gamma5 = 2.0
gamma6 = 5.0
gamma7 = 10.0

# 計算對應的正規化常數，使輸入255對應輸出255
c1 = 255.0 / ( 255.0 ** gamma1 )
c2 = 255.0 / ( 255.0 ** gamma2 )
c3 = 255.0 / ( 255.0 ** gamma3 )
c4 = 255.0 / ( 255.0 ** gamma4 )
c5 = 255.0 / ( 255.0 ** gamma5 )
c6 = 255.0 / ( 255.0 ** gamma6 )
c7 = 255.0 / ( 255.0 ** gamma7 )

# 產生 0~255 的輸入強度值
x  = np.linspace( 0, 255, 100 )

# 計算各 gamma 值對應的輸出強度
y1 = x ** gamma1 * c1
y2 = x ** gamma2 * c2
y3 = x ** gamma3 * c3
y4 = x ** gamma4 * c4
y5 = x ** gamma5 * c5
y6 = x ** gamma6 * c6
y7 = x ** gamma7 * c7

# 繪製所有 gamma 曲線（gamma<1 的曲線位於對角線上方，表示變亮效果）
plt.plot( x, y1, x, y2, x, y3, x, y4, x, y5, x, y6, x, y7 )
plt.xlabel( "Input Intensity" )
plt.ylabel( "Output Intensity" )
plt.xlim( [0,255] )
plt.ylim( [0,255] )
plt.show( )
