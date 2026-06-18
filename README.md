# Digital Image Processing Python
# 數位影像處理 Python 範例程式

數位影像處理課程各章節 Python 範例程式，涵蓋空間域/頻域濾波、色彩模型、形態學、小波、影像壓縮、特徵擷取及深度學習等主題。

Python example code for a Digital Image Processing course, covering spatial/frequency filtering, color models, morphology, wavelets, compression, feature extraction, and deep learning.

---

## 注意事項 / Notes

> ⚠️ **路徑限制 / Path Restriction**
>
> OpenCV 在 Windows 上**不支援路徑含有中文或特殊字元**。請確認專案資料夾與所有上層目錄的名稱均為**英文**，否則 `cv2.imread()` 將無法讀取圖片並回傳錯誤。
>
> OpenCV on Windows **does not support non-ASCII characters in file paths**. Please ensure the project folder and all parent directories use **English names only**, otherwise `cv2.imread()` will fail to load images.
>
> ✅ 正確：`C:\Users\John\Desktop\DIP\Ch02\`
> ❌ 錯誤：`C:\Users\使用者\桌面\影像處理\Ch02\`

> ⚠️ **工作目錄限制 / Working Directory Restriction**
>
> 各章節腳本使用**相對路徑**讀取圖片（如 `cv2.imread("Lenna.bmp")`），OpenCV 會從**執行指令時的工作目錄**尋找檔案，而非腳本所在的資料夾。請先 `cd` 進入對應章節資料夾後再執行，否則會出現 `can't open/read file` 錯誤。
>
> Each chapter's script uses a **relative path** (e.g. `cv2.imread("Lenna.bmp")`). OpenCV resolves it from the **current working directory**, not the script's folder. Always `cd` into the chapter folder first, or the file will not be found.
>
> ✅ 正確執行方式：`cd Ch02` → `python display_image.py`
> ❌ 錯誤執行方式：在上層目錄執行 `python Ch02/display_image.py`

---

## 目錄 / Table of Contents

| 章節 | 主題 |
|:----:|------|
| [Ch02](#ch02---影像讀取與基本操作--image-io--basic-operations) | 影像讀取與基本操作 / Image I/O & Basic Operations |
| [Ch03](#ch03---影像採樣與量化--image-sampling--quantization) | 影像採樣與量化 / Image Sampling & Quantization |
| [Ch04](#ch04---幾何變換--geometric-transformations) | 幾何變換 / Geometric Transformations |
| [Ch05](#ch05---空間域影像處理--spatial-domain-processing) | 空間域影像處理 / Spatial Domain Processing |
| [Ch06](#ch06---頻域影像處理--frequency-domain-processing) | 頻域影像處理 / Frequency Domain Processing |
| [Ch07](#ch07---影像復原--image-restoration) | 影像復原 / Image Restoration |
| [Ch08](#ch08---彩色影像處理--color-image-processing) | 彩色影像處理 / Color Image Processing |
| [Ch09](#ch09---影像分割--image-segmentation) | 影像分割 / Image Segmentation |
| [Ch10](#ch10---形態學影像處理--morphological-image-processing) | 形態學影像處理 / Morphological Image Processing |
| [Ch11](#ch11---小波轉換--wavelet-transform) | 小波轉換 / Wavelet Transform |
| [Ch12](#ch12---影像壓縮--image-compression) | 影像壓縮 / Image Compression |
| [Ch13](#ch13---影像特徵擷取--image-feature-extraction) | 影像特徵擷取 / Image Feature Extraction |
| [Ch14](#ch14---特效與影像合成--special-effects--synthesis) | 特效與影像合成 / Special Effects & Synthesis |
| [Ch15](#ch15---深度學習影像辨識--deep-learning-for-image-recognition) | 深度學習影像辨識 / Deep Learning for Image Recognition |
| [ChA](#cha---數學基礎--mathematical-foundations) | 數學基礎 / Mathematical Foundations |

---

## Ch02 - 影像讀取與基本操作 / Image I/O & Basic Operations

| 檔案 | 說明 |
|------|------|
| [display_image.py](Ch02/display_image.py) | 讀取並顯示影像 / Read and display image |
| [image_info.py](Ch02/image_info.py) | 取得影像尺寸與通道資訊 / Get image dimensions and channel info |
| [opencv_drawing.py](Ch02/opencv_drawing.py) | 繪製幾何圖形（線、矩形、圓、橢圓、多邊形）/ Draw geometric shapes |
| [opencv_puttext.py](Ch02/opencv_puttext.py) | 在影像上加入文字（所有字型樣式）/ Put text with all font styles |
| [pixel_info.py](Ch02/pixel_info.py) | 滑鼠點擊顯示 BGR 像素值 / Show BGR pixel info on mouse click |
| [puttext.py](Ch02/puttext.py) | 在黑色畫布繪製文字並儲存 / Draw text on black canvas and save |
| [ROI.py](Ch02/ROI.py) | 以陣列切片擷取感興趣區域 / Extract Region of Interest via array slicing |

---

## Ch03 - 影像採樣與量化 / Image Sampling & Quantization

| 檔案 | 說明 |
|------|------|
| [image_downsampling.py](Ch03/image_downsampling.py) | 最近鄰居法影像降採樣 / Image downsampling by nearest-neighbor |
| [image_formation_model.py](Ch03/image_formation_model.py) | 高斯光照影像形成模型 / Image formation model with Gaussian illumination |
| [image_quantization.py](Ch03/image_quantization.py) | 灰階位元深度量化（偽輪廓示範）/ Grayscale quantization with false contour |

---

## Ch04 - 幾何變換 / Geometric Transformations

| 檔案 | 說明 |
|------|------|
| [affine_transform.py](Ch04/affine_transform.py) | 仿射變換 / Affine transformation with `getAffineTransform` |
| [forward_mapping.py](Ch04/forward_mapping.py) | 前向映射（孔洞問題示範）/ Forward mapping demonstrating hole artifacts |
| [image_flip.py](Ch04/image_flip.py) | 影像垂直/水平翻轉 / Image flip (vertical and horizontal) |
| [image_rescaling.py](Ch04/image_rescaling.py) | 內插方法比較（最近鄰/雙線性/雙三次）/ Interpolation methods comparison |
| [image_rotation.py](Ch04/image_rotation.py) | 影像旋轉 / Image rotation with `getRotationMatrix2D` |
| [image_scaling.py](Ch04/image_scaling.py) | 使用者自訂縮放比例 / Image scaling with user-defined factor |
| [perspective_transform.py](Ch04/perspective_transform.py) | 透視變換 / Perspective transform with `warpPerspective` |

---

## Ch05 - 空間域影像處理 / Spatial Domain Processing

| 檔案 | 說明 |
|------|------|
| [average_filtering.py](Ch05/average_filtering.py) | 平均（盒）濾波 / Average (box) filtering for noise removal |
| [beta_correction.py](Ch05/beta_correction.py) | Beta 校正（色調映射）/ Beta correction for tone mapping |
| [beta_function.py](Ch05/beta_function.py) | 不完全 Beta 函數曲線 / Incomplete Beta function curve visualization |
| [bilateral_filtering.py](Ch05/bilateral_filtering.py) | 雙邊濾波（保留邊緣）/ Bilateral filtering preserving edges |
| [composite_laplacian.py](Ch05/composite_laplacian.py) | 複合拉普拉斯銳化 / Composite Laplacian sharpening filter |
| [convolution.py](Ch05/convolution.py) | 一維卷積（full/same 模式）/ 1D convolution with numpy |
| [convolution2D.py](Ch05/convolution2D.py) | 二維卷積 / 2D convolution with `scipy.signal` |
| [gamma_correction.py](Ch05/gamma_correction.py) | Gamma 校正（冪次律）/ Power-law gamma correction |
| [gamma_function.py](Ch05/gamma_function.py) | Gamma 函數曲線視覺化 / Gamma function curve visualization |
| [gaussian_filtering.py](Ch05/gaussian_filtering.py) | 高斯濾波 / Gaussian filtering for smoothing |
| [histogram.py](Ch05/histogram.py) | 灰階直方圖視覺化 / Grayscale histogram visualization |
| [histogram_equalization.py](Ch05/histogram_equalization.py) | 直方圖均衡化 / Histogram equalization for contrast enhancement |
| [image_gradient.py](Ch05/image_gradient.py) | Sobel 影像梯度 / Sobel gradient in x/y/combined directions |
| [image_negative.py](Ch05/image_negative.py) | 影像反相 / Image negative by intensity inversion |
| [laplacian.py](Ch05/laplacian.py) | 拉普拉斯邊緣偵測 / Laplacian edge detection with 128 offset |
| [median_filtering.py](Ch05/median_filtering.py) | 中值濾波（去除椒鹽雜訊）/ Median filtering for salt-and-pepper noise |
| [unsharp_masking.py](Ch05/unsharp_masking.py) | 反銳化遮罩 / Unsharp masking for image sharpening |

---

## Ch06 - 頻域影像處理 / Frequency Domain Processing

| 檔案 | 說明 |
|------|------|
| [FFT_example.py](Ch06/FFT_example.py) | 一維 FFT/IFFT 示範 / 1D FFT and IFFT demonstration |
| [frequency_filtering.py](Ch06/frequency_filtering.py) | 理想/高斯/Butterworth 低通高通濾波 / Ideal, Gaussian, Butterworth LP/HP filtering |
| [spectrum.py](Ch06/spectrum.py) | 幅度頻譜與相位頻譜視覺化 / Magnitude and phase spectrum visualization |

---

## Ch07 - 影像復原 / Image Restoration

| 檔案 | 說明 |
|------|------|
| [band_filtering.py](Ch07/band_filtering.py) | 帶通與帶阻濾波 / Band-pass and band-reject filtering |
| [image_noise.py](Ch07/image_noise.py) | 各類雜訊模型（均勻/高斯/指數/Rayleigh/椒鹽）/ Noise models |
| [inpainting.py](Ch07/inpainting.py) | 影像修復（NS 與 Telea 方法）/ Image inpainting with NS and Telea |
| [inverse_filtering.py](Ch07/inverse_filtering.py) | 頻域逆濾波 / Frequency domain inverse filtering |
| [noise_analysis.py](Ch07/noise_analysis.py) | ROI 雜訊分析（直方圖與標準差）/ ROI noise analysis |
| [periodic_noise.py](Ch07/periodic_noise.py) | 頻域週期性雜訊注入 / Periodic noise injection in frequency domain |
| [PSNR_example.py](Ch07/PSNR_example.py) | PSNR 計算 / Peak Signal-to-Noise Ratio calculation |
| [wiener_filtering.py](Ch07/wiener_filtering.py) | 維納濾波 / Wiener filter for image restoration |

---

## Ch08 - 彩色影像處理 / Color Image Processing

| 檔案 | 說明 |
|------|------|
| [CMY_model.py](Ch08/CMY_model.py) | CMY 色彩模型 / CMY color model (CMY = 255 − RGB) |
| [gaussian_filtering.py](Ch08/gaussian_filtering.py) | 彩色影像高斯濾波 / Gaussian filtering on color image |
| [HSI_model.py](Ch08/HSI_model.py) | RGB ↔ HSI 手動轉換 / Manual RGB-to-HSI conversion |
| [HSI_processing.py](Ch08/HSI_processing.py) | HSI 色調旋轉/飽和度/亮度調整 / HSI hue, saturation, intensity adjustment |
| [HSV_color_segmentation.py](Ch08/HSV_color_segmentation.py) | HSV 色彩範圍分割 / Color segmentation using HSV range mask |
| [HSV_histogram_equalization.py](Ch08/HSV_histogram_equalization.py) | HSV V 通道直方圖均衡化 / Equalize V channel in HSV space |
| [HSV_model.py](Ch08/HSV_model.py) | HSV 色彩模型通道擷取 / HSV color model channel extraction |
| [pseudocolor.py](Ch08/pseudocolor.py) | 偽彩色（20 種色彩映射）/ Pseudocolor with 20 OpenCV colormaps |
| [RGB_gamma_correction.py](Ch08/RGB_gamma_correction.py) | RGB 各通道 Gamma 校正 / Per-channel gamma correction |
| [RGB_histogram_equalization.py](Ch08/RGB_histogram_equalization.py) | RGB 各通道直方圖均衡化 / Per-channel histogram equalization |
| [RGB_model.py](Ch08/RGB_model.py) | RGB 色彩模型通道分割 / RGB color model channel splitting |
| [YCrCb_model.py](Ch08/YCrCb_model.py) | YCrCb 色彩模型轉換 / YCrCb color model conversion |

---

## Ch09 - 影像分割 / Image Segmentation

| 檔案 | 說明 |
|------|------|
| [adaptive_thresholding.py](Ch09/adaptive_thresholding.py) | 自適應閾值化（均值/高斯）/ Adaptive thresholding with mean and Gaussian |
| [Canny_edge_detection.py](Ch09/Canny_edge_detection.py) | Canny 邊緣偵測（雙閾值遲滯）/ Canny edge detection with hysteresis |
| [Hough_circle_detection.py](Ch09/Hough_circle_detection.py) | Hough 圓形偵測 / Hough circle detection with `HOUGH_GRADIENT` |
| [Hough_line_detection.py](Ch09/Hough_line_detection.py) | Hough 直線偵測（極座標）/ Hough line detection in polar coordinates |
| [Sobel_edge_detection.py](Ch09/Sobel_edge_detection.py) | Sobel 邊緣偵測 + Otsu 閾值 / Sobel edge detection with Otsu threshold |
| [thresholding.py](Ch09/thresholding.py) | Otsu 二值化 / Binary thresholding with Otsu method |

---

## Ch10 - 形態學影像處理 / Morphological Image Processing

| 檔案 | 說明 |
|------|------|
| [distance_transform.py](Ch10/distance_transform.py) | L1 距離轉換 / Distance transform with L1 norm |
| [hole_filling.py](Ch10/hole_filling.py) | 連通成分孔洞填補 / Hole filling using connected components |
| [morphology.py](Ch10/morphology.py) | 腐蝕/膨脹/開運算/閉運算 / Erode, dilate, open, close |
| [skeletonization.py](Ch10/skeletonization.py) | Zhang-Suen 骨架化演算法 / Skeletonization via Zhang-Suen algorithm |
| [thinning.py](Ch10/thinning.py) | 形態學細化（Hit-or-Miss）/ Morphological thinning with hit-or-miss transform |

---

## Ch11 - 小波轉換 / Wavelet Transform

| 檔案 | 說明 |
|------|------|
| [basis.py](Ch11/basis.py) | DFT/DCT/WHT 基底函數 / DFT, DCT, and WHT basis functions |
| [DWT_edge_detection.py](Ch11/DWT_edge_detection.py) | 小波子帶清零邊緣偵測 / Edge detection via DWT subband zeroing |
| [DWT_enhancement.py](Ch11/DWT_enhancement.py) | 小波子帶選擇影像增強 / Image enhancement via DWT subband selection |
| [DWT_example.py](Ch11/DWT_example.py) | 一維 DWT 示範（db1/db2/db4）/ 1D DWT with db1, db2, db4 wavelets |
| [DWT_image.py](Ch11/DWT_image.py) | 二維 DWT 四象限視覺化 / 2D DWT four-quadrant visualization |
| [wavelet.py](Ch11/wavelet.py) | 小波濾波器組莖葉圖 / Wavelet filter bank stem plot visualization |

---

## Ch12 - 影像壓縮 / Image Compression

| 檔案 | 說明 |
|------|------|
| [entropy.py](Ch12/entropy.py) | Shannon 資訊熵計算 / Shannon entropy calculation for images |
| [JPEG_compression.py](Ch12/JPEG_compression.py) | JPEG 壓縮（DCT + 量化 + 反量化）/ JPEG compression with DCT and quantization |
| [JPEG_example.py](Ch12/JPEG_example.py) | 8×8 區塊 JPEG 逐步示範 / Step-by-step JPEG forward and inverse transform |

---

## Ch13 - 影像特徵擷取 / Image Feature Extraction

| 檔案 | 說明 |
|------|------|
| [CC_labeling.py](Ch13/CC_labeling.py) | 連通成分標記與視覺化 / Connected component labeling and visualization |
| [convex_hull.py](Ch13/convex_hull.py) | 凸包偵測 / Convex hull detection with contour drawing |
| [convexity_defects.py](Ch13/convexity_defects.py) | 凸性缺陷偵測 / Convexity defects detection |
| [face_detection.py](Ch13/face_detection.py) | Haar 級聯人臉偵測 / Face detection with Haar cascade classifier |
| [find_contours.py](Ch13/find_contours.py) | 外部輪廓尋找 / Find external contours with `CHAIN_APPROX_NONE` |
| [fourier_descriptors.py](Ch13/fourier_descriptors.py) | 傅立葉形狀描述子 / Fourier descriptors for shape representation |
| [harris_corner_detection.py](Ch13/harris_corner_detection.py) | Harris 角點偵測 / Harris corner detection with relative threshold |
| [ORB_feature_detection.py](Ch13/ORB_feature_detection.py) | ORB 關鍵點偵測與描述 / ORB keypoint detection and description |
| [ORB_feature_matching.py](Ch13/ORB_feature_matching.py) | ORB 特徵匹配（BFMatcher）/ ORB feature matching with BFMatcher |
| [polygon_approximation.py](Ch13/polygon_approximation.py) | Douglas-Peucker 多邊形近似 / Polygon approximation |
| [shape_features.py](Ch13/shape_features.py) | 形狀特徵（面積/質心/緊密度）/ Shape features: area, centroid, compactness |
| [shi_tomasi_corner_detection.py](Ch13/shi_tomasi_corner_detection.py) | Shi-Tomasi 角點偵測 / Shi-Tomasi good features to track |
| [SIFT_feature_detection.py](Ch13/SIFT_feature_detection.py) | SIFT 尺度不變特徵偵測 / SIFT scale-invariant feature detection |
| [skin_color_detection.py](Ch13/skin_color_detection.py) | RGB/HSV/YCrCb 三種皮膚偵測法 / Skin color detection in RGB, HSV, YCrCb |
| [SURF_feature_detection.py](Ch13/SURF_feature_detection.py) | SURF 加速穩健特徵偵測 / SURF speeded-up robust feature detection |

---

## Ch14 - 特效與影像合成 / Special Effects & Synthesis

| 檔案 | 說明 |
|------|------|
| [detail_enhancement.py](Ch14/detail_enhancement.py) | 細節增強 / Detail enhancement with OpenCV |
| [edge_preserving_filter.py](Ch14/edge_preserving_filter.py) | 邊緣保留濾波比較 / Edge-preserving filter comparison |
| [fisheye_effect.py](Ch14/fisheye_effect.py) | 魚眼鏡頭效果（徑向失真）/ Fisheye lens effect with radial distortion |
| [fuzzy_effect.py](Ch14/fuzzy_effect.py) | 隨機像素偏移模糊效果 / Fuzzy blur with random pixel displacement |
| [motion_blur.py](Ch14/motion_blur.py) | 方向性運動模糊 / Directional motion blur filter |
| [pencil_sketch.py](Ch14/pencil_sketch.py) | 鉛筆素描效果 / Pencil sketch effect |
| [radial_blur.py](Ch14/radial_blur.py) | 徑向弧形平均模糊 / Radial blur by circular arc averaging |
| [radial_pixelation.py](Ch14/radial_pixelation.py) | 徑向像素化（量化極座標）/ Radial pixelation by quantizing polar coordinates |
| [ripple_effect.py](Ch14/ripple_effect.py) | 正弦波位移波紋效果 / Ripple effect with sine wave displacement |
| [stylization.py](Ch14/stylization.py) | 風格化效果 / Stylization effect with OpenCV |
| [twirl_effect.py](Ch14/twirl_effect.py) | 漩渦旋轉效果 / Twirl effect with angular rotation by radius |

---

## Ch15 - 深度學習影像辨識 / Deep Learning for Image Recognition

| 檔案 | 說明 |
|------|------|
| [softmax.py](Ch15/softmax.py) | Softmax 函數實作 / Softmax activation function implementation |
| [ANN_mnist.py](Ch15/ANN_mnist.py) | 全連接神經網路 MNIST 手寫數字辨識 / ANN on MNIST handwritten digits |
| [CNN_cifar10.py](Ch15/CNN_cifar10.py) | 卷積神經網路 CIFAR-10 影像分類 / CNN on CIFAR-10 image classification |
| [GoogLeNet.py](Ch15/GoogLeNet.py) | GoogLeNet 影像辨識（OpenCV DNN）/ GoogLeNet via OpenCV DNN module |
| [VGG16.py](Ch15/VGG16.py) | VGG16 ImageNet 影像辨識（Keras）/ VGG16 ImageNet recognition via Keras |

---

## ChA - 數學基礎 / Mathematical Foundations

| 檔案 | 說明 |
|------|------|
| [complex_number.py](ChA/complex_number.py) | 複數模與相位角 / Complex number magnitude and phase angle |
| [gaussian_function.py](ChA/gaussian_function.py) | 高斯函數及一/二階導數（LoG）/ Gaussian function and its derivatives |
| [gaussian_function2D.py](ChA/gaussian_function2D.py) | 二維高斯函數 3D 曲面圖 / 2D Gaussian function with 3D surface plot |
| [pca_example.py](ChA/pca_example.py) | 主成分分析（手動 + sklearn）/ PCA with manual covariance and sklearn |

---

## 環境需求 / Requirements

```
opencv-python
numpy
scipy
matplotlib
scikit-learn
PyWavelets
tensorflow / keras
```

---

## 聯絡方式 / Contact

對本專題的實作內容、演算法原理或程式碼有任何疑問，或有其他問題與建議，歡迎直接聯絡，將盡力協助解答。

If you have questions about the implementation, algorithms, or code in this project, or any other suggestions, feel free to reach out.

- 📧 [hankchou10655006@gmail.com](mailto:hankchou10655006@gmail.com)
- 📧 [412410077@o365.tku.edu.tw](mailto:412410077@o365.tku.edu.tw)
