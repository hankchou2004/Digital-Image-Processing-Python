import numpy as np
import pywt

# 定義一維測試訊號
f = np.array( [ 14, 8, 6, 4, 3, 5, 9, 7 ] )

# Haar 小波（db1）：最簡單的小波，濾波器為 [1,1]/√2 和 [1,-1]/√2
print( "Haar Wavelet" )
# cA：近似係數（低頻），cD：細節係數（高頻）
cA, cD = pywt.dwt( f, 'db1' )
print( "DWT Coefficients: ", cA, cD )
# 反 DWT 重建原始訊號
fp = pywt.idwt( cA, cD, 'db1' )
print( "Reconstruction: ", fp )

# Daubechies 小波（4-Tap，db2）：4個濾波器係數，更平滑的近似
print( "Daubechies Wavelet (4-Tap)" )
cA, cD = pywt.dwt( f, 'db2' )
print( "DWT Coefficients: ", cA, cD )
fp = pywt.idwt( cA, cD, 'db2' )
print( "Reconstruction: ", fp )

# Daubechies 小波（8-Tap，db4）：8個濾波器係數，更長的支撐
print( "Daubechies Wavelet (8-Tap)" )
cA, cD = pywt.dwt( f, 'db4' )
print( "DWT Coefficients: ", cA, cD )
fp = pywt.idwt( cA, cD, 'db4' )
print( "Reconstruction: ", fp )
