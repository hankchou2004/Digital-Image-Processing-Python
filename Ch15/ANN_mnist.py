from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# 載入 MNIST 手寫數字資料集（60000 張訓練、10000 張測試，28x28 灰階影像）
(train_images, train_labels), (test_images, test_labels) = mnist.load_data( )

# 建立人工神經網路（ANN）：全連接前饋式網路
network = Sequential( )
# 輸入層：784 個神經元（28x28 像素展平），隱藏層：512 個神經元，ReLU 激活函式
network.add( Dense( 512, activation = 'relu', input_shape = ( 784, ) ) )
# 輸出層：10 個神經元（對應 0~9 共 10 個數字類別），Softmax 輸出機率
network.add( Dense( 10, activation = 'softmax' ) )
# 編譯模型：使用 RMSprop 優化器，交叉熵損失函式
network.compile( optimizer = 'rmsprop', loss = 'categorical_crossentropy',
	             metrics = ['accuracy'] )
print( network.summary() )

# 資料前處理
# 將 28x28 影像展平為 784 維向量
train_images = train_images.reshape( ( 60000, 28 * 28 ) )
# 正規化像素值到 [0, 1]（原本為 0~255 整數）
train_images = train_images.astype( 'float32' ) / 255
test_images = test_images.reshape( ( 10000, 28 * 28 ) )
test_images = test_images.astype( 'float32' ) / 255
# 將標籤轉換為 One-Hot 編碼（例如 3 → [0,0,0,1,0,0,0,0,0,0]）
train_labels = to_categorical( train_labels )
test_labels = to_categorical( test_labels )

# 訓練階段：訓練 5 個 epoch，每批次 200 筆資料
network.fit( train_images, train_labels, epochs = 5, batch_size = 200 )

# 測試階段：評估模型在未見過測試資料上的準確率
test_loss, test_acc = network.evaluate( test_images, test_labels )
print( "Test Accuracy:", test_acc )
