import numpy as np
import cv2

# JPEG 標準量化表（亮度通道）：低頻係數（左上角）量化步階小，高頻係數（右下角）步階大
normalize = np.array( [ [ 16, 11, 10, 16,  24,  40,  51,  61 ],
						[ 12, 12, 14, 19,  26,  58,  60,  55 ],
						[ 14, 13, 16, 24,  40,  57,  69,  56 ],
						[ 14, 17, 22, 29,  51,  87,  80,  62 ],
						[ 18, 22, 37, 56,  68, 109, 103,  77 ],
						[ 24, 35, 55, 64,  81, 104, 113,  92 ],
						[ 49, 64, 78, 87, 103, 121, 120, 101 ],
						[ 72, 92, 95, 98, 112, 100, 103,  99 ] ] )

img = cv2.imread( "Lenna.bmp", -1 )
# 擷取一個 8x8 的代表性像素區塊
block  = img[260:268,260:268]
print( "Original Block" )
print( block )

# JPEG 正向轉換過程
coeffs = np.array( [8, 8], dtype = 'int' )
# 步驟1：減去 128（使值域從 [0,255] 移至 [-128,127]）
coeffs = block.astype('int' ) - 128
print( "Minus 128" )
print( coeffs )

# 步驟2：正向 DCT（離散餘弦轉換）
coeffs = np.round( cv2.dct( np.float32( coeffs ) ) )
print( "Forward DCT" )
print( coeffs )

# 步驟3：量化（除以量化表，高頻係數大量消失）
coeffs = np.round( coeffs / normalize )
print( "Normalization" )
print( coeffs )

print( "-" * 60 )

# JPEG 反向轉換過程（解壓縮）
# 步驟4：反量化（乘回量化表，高頻係數已永久遺失）
coeffs = coeffs * normalize
print( "Denormalization" )
print( coeffs )

# 步驟5：反向 DCT
coeffs = np.round( cv2.idct( coeffs ) )
print( "Inverse DCT" )
print( coeffs )

# 步驟6：加回 128 還原像素值
coeffs = np.round( coeffs + 128 )
print( "Plus 128 (Reconstruction)" )
print( coeffs )
