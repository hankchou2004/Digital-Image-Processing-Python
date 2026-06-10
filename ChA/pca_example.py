import numpy as np
from sklearn.decomposition import PCA

# 定義二維資料點（4 個樣本，每個樣本有 2 個特徵）
x = np.array( [ [ 1, 1 ], [ 2, 4 ], [ 4, 2 ], [ 5, 5 ] ] )
# 計算各特徵的平均向量（用於中心化）
mean_vec = np.mean( x, axis = 0 )
# 手動計算共變異數矩陣（反映特徵間的線性相關程度）
cov_mat = ( x - mean_vec ).T.dot( x - mean_vec ) / x.shape[0]
# 計算共變異數矩陣的特徵值與特徵向量
# 特徵值代表各主成分的變異量，特徵向量代表主成分方向
eig_vals, eig_vecs = np.linalg.eig( cov_mat )
# 使用 sklearn 的 PCA 執行主成分分析（保留 2 個主成分）
pca = PCA( 2 )
pca.fit( x )
# 將原始資料投影到主成分空間（降維後的新座標）
y = pca.transform( x )
print( "Mean Vector:\n", mean_vec )
print( "Covariance Matrix:\n", cov_mat )
print( "Eigenvalues\n", eig_vals )
print( "Eigenvectors\n", eig_vecs )
print( "Transform:\n", y )
