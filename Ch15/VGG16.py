import numpy as np
import cv2
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions

# 載入預訓練的 VGG16 模型（使用 ImageNet 資料集訓練的權重）
# include_top=True：包含最後的全連接分類層（輸出 1000 個 ImageNet 類別）
model = VGG16( weights = "imagenet", include_top = True )
# 顯示 VGG16 的網路結構摘要（13 個卷積層 + 3 個全連接層）
print( model.summary() )

# 讀取並前處理測試影像
img = cv2.imread( "Dog.jpg", -1 )
# VGG16 的固定輸入尺寸為 224x224
img = cv2.resize( img, ( 224, 224 ), interpolation = cv2.INTER_LINEAR )
# 轉換為 Keras 所需的陣列格式
x = image.img_to_array( img )
# 增加批次維度（從 (224,224,3) 變為 (1,224,224,3)）
x = np.expand_dims( x, axis = 0 )
# VGG16 的輸入正規化（減去 ImageNet 各通道的平均值）
x = preprocess_input( x )
# 執行前向推論
features = model.predict( x )
# 解碼並顯示最可能的前 3 個預測結果（類別名稱和機率）
print( "Predicted:", decode_predictions( features, top = 3 )[0] )
