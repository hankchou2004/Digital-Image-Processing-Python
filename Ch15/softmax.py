import numpy as np

# Softmax 函數：將任意實數向量轉換為機率分布（所有元素為正且總和為 1）
# 廣泛用於神經網路的多類別分類輸出層
z = np.array( [ 1, 2, 3, 4, 1, 2 ] )
# 計算每個元素的指數（exp 確保輸出為正數）
z_exp = np.exp( z )
# 計算指數值的總和（用於正規化）
sum = np.sum( z_exp )
# Softmax 輸出：每個元素 = exp(z_i) / Σexp(z_j)
# 數值較大的元素對應較高的機率（指數放大差異）
softmax = np.round( z_exp / sum, 3 )
print( softmax )
