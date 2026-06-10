import numpy as np
import cv2
from cv2 import dnn

# 讀取 ImageNet 類別清單（synset_words.txt）
# 每行格式為「nXXXXXXXX 類別名稱」，只取名稱部分
def get_class_list( ):
    with open( "synset_words.txt", "rt" ) as f:
        return [ x[x.find(" ") + 1:] for x in f ]

def main( ):
	# 讀取測試影像
	img = cv2.imread( "Space_Shuttle.bmp", -1 )
	# 將影像轉換為 DNN 輸入的 blob 格式
	# 參數：影像、縮放因子=1（不縮放）、目標尺寸=(224,224)（GoogLeNet 輸入大小）
	blob = dnn.blobFromImage( img, 1, ( 224, 224 ), False )
	# 載入預訓練的 GoogLeNet（Caffe 格式）
	# prototxt：網路架構定義檔，caffemodel：預訓練權重檔
	network = dnn.readNetFromCaffe( "bvlc_googlenet.prototxt",
		      "bvlc_googlenet.caffemodel" )
	# 設定輸入並執行前向推論
	network.setInput( blob )
	prob = network.forward( )   # 輸出：1000 個 ImageNet 類別的機率
	# 取得類別名稱清單並顯示最高機率的預測結果
	classes = get_class_list( )
	print( "Best match:", classes[ prob.argmax( ) ] )
	cv2.imshow( "Input",  img )
	cv2.waitKey( )

main( )
