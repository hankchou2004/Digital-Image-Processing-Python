import numpy as np
from numpy.fft import fft, ifft

# 定義一維離散訊號 x
x = np.array( [ 1, 2, 4, 3 ] )
# 執行快速傅立葉轉換（FFT）：將訊號從時域轉換到頻域
X = fft( x )
# 執行反快速傅立葉轉換（IFFT）：從頻域還原回時域
xx = ifft ( X )

print( "x =", x )
print( "X =", X )
# 反轉換後的結果應與原始訊號相同（可能有微小浮點數誤差）
print( "Inverse FFT of X =", xx )
