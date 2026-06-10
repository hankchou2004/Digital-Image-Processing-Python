from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.utils import to_categorical

# 載入 CIFAR-10 資料集（60000 張 32x32 彩色影像，10 個類別）
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data( )

# 建立卷積神經網路（CNN）
network = Sequential( )
# 第一個卷積層：32 個 3x3 濾波器，ReLU 激活，same padding 保持尺寸
network.add( Conv2D( filters = 32, kernel_size = ( 3, 3 ),
	         input_shape = ( 32, 32, 3 ), activation = 'relu',
	         padding = 'same' ) )
# 第一個最大池化層：2x2 視窗，將特徵圖縮小為 16x16
network.add( MaxPooling2D( pool_size = ( 2, 2 ) ) )
# 第二個卷積層：64 個 3x3 濾波器，ReLU 激活
network.add( Conv2D( filters = 64, kernel_size = ( 3, 3 ),
	                 activation = 'relu', padding = 'same' ) )
# 第二個最大池化層：將特徵圖縮小為 8x8
network.add( MaxPooling2D( pool_size = ( 2, 2 ) ) )
# 展平層：將 8x8x64 的特徵圖展平為 4096 維向量
network.add( Flatten( ) )
# 全連接層：1024 個神經元，ReLU 激活
network.add( Dense( 1024, activation = 'relu' ) )
# 輸出層：10 個神經元（對應 10 個類別），Softmax 輸出機率
network.add( Dense( 10, activation = 'softmax' ) )
# 使用 Adam 優化器（自適應學習率，收斂較快）
network.compile( optimizer = 'adam', loss = 'categorical_crossentropy',
	             metrics = ['accuracy'] )
print( network.summary() )

# 資料前處理
# 正規化像素值到 [0, 1]
train_images = train_images.astype( 'float32' ) / 255
test_images = test_images.astype( 'float32' ) / 255
# 將標籤轉換為 One-Hot 編碼
train_labels = to_categorical( train_labels )
test_labels = to_categorical( test_labels )

# 訓練階段：訓練 10 個 epoch，每批次 200 筆資料
network.fit( train_images, train_labels, epochs = 10, batch_size = 200 )

# 測試階段：評估模型準確率
test_loss, test_acc = network.evaluate( test_images, test_labels )
print( "Test Accuracy:", test_acc )
