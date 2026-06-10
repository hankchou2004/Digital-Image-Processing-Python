import numpy as np

# 定義複數 z = 3 + 4j（實部=3，虛部=4）
z = 3 + 4j
# 計算複數的模（magnitude）= sqrt(實部² + 虛部²) = sqrt(9+16) = 5
magnitude = abs( z )
# 計算複數的相位角（phase angle）= arctan(虛部/實部)，單位轉換為度
theta = np.degrees( np.angle( z ) )
print( "z =", z )
print( "Magnitude =", magnitude )
print( "Phase Angle =", theta )
