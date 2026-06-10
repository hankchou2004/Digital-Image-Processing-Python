import pywt
import matplotlib.pyplot as plt

# 視覺化各種小波的低通濾波器係數（縮放函數）
# Haar 小波（db1）：最簡單，2個係數 [1/√2, 1/√2]，具有箱型函數的形狀
plt.figure( 1 )
wavelet = pywt.Wavelet( 'db1' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

# Daubechies 小波（4-Tap，db2）：4個係數，比 Haar 更平滑的近似
plt.figure( 2 )
wavelet = pywt.Wavelet( 'db2' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

# Daubechies 小波（8-Tap，db4）：8個係數，更長的支撐，更好的頻率局部化
plt.figure( 3 )
wavelet = pywt.Wavelet( 'db4' )
plt.stem( wavelet.filter_bank[0], use_line_collection = True )

plt.show( )
