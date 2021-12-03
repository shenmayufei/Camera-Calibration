# Camera-Calibration
Camera Calibration toolbox using Python &amp; openCV
## Introduction
Cameras have been around in our lives for a while. When first appeared, they were very expensive. Fortunately, in the late 20th century, the pinhole camera was developed and sold at suitable prices such that everybody was able to afford it. However, as is the case with any trade off, this convenience comes at a price. This camera model is typically not good enough for accurate geometrical computations based on images; hence, significant distortions may result in images.

Camera calibration is the process of determining the relation between the camera’s natural units (pixels) and the real world units (for example, millimeters or inches). Technically, camera calibration estimates intrinsic (camera's internal characteristics such as focal length, skew, distortion) and extrinsic (its position and orientation in the world) parameters. Camera calibration is an important step towards getting a highly accurate representation of the real world in the captured images. It helps removing distortions as well.
There are several calibration tools available online, such as:
* [Bouguet Toolbox for Matlab](http://www.vision.caltech.edu/bouguetj/calib_doc/)
* [BoofCV: open source Java library](https://boofcv.org/index.php?title=Tutorial_Camera_Calibration)

Here, I create my own calibration toolbox from scratch using python and OpenCV. I follow Zhang’s description in his paper “A flexible new technique for camera calibration,” with allows calibration from multiple 2D plane images. My toolbox is characterized by its friendly user interface, its compatibility to work on any camera and any operation system, and automation such that instead of taking 2D points on captured images individually and manually, a corner detection algorithm automatically handles this task and saves much time and effort.

## Installation
1. Clone or download this repository.

2. Make sure python 3.x is installed on your PC. To check if and which version is installed, run the following command:
```
python -V
```
If this results an error, this means that python isn’t installed on your PC! please install it from [the original website](https://www.python.org/)

3. (optional) it is recommended that you create a python virtual environment and install the necessary libraries in it to prevent versions collisions:
```
python -m venv CV
```
where CV is the environment name. Once you’ve created a virtual environment, you may activate it.
```
CV\Scripts\activate.bat
```

4. Install required libraries from the provided file (**requirements.txt**):
```
pip install -r requirements.txt
```
Make sure you provide the correct path of **requirements.txt**

5. DONE :) Run the script:
```
python calibration_GUI.py
```

## DEMO
This is the main page of the graphical interface:

![image](https://user-images.githubusercontent.com/9033365/46244812-56756600-c3ed-11e8-9b62-6c9600c025e0.png)

Check the **Detect Corners** checkbox and click **START**. The webcam will start capturing frame and displaying them in the interface:

![image](https://user-images.githubusercontent.com/9033365/46244851-021eb600-c3ee-11e8-8752-054269ff1bbe.png)

If you are happy with the captured image, click **CONFIRM**. Otherwise, click **IGNORE** to take another image. Once you click **CONFIRM** or **IGNORE**, the webcam will continue capturing frames, displaying them, and trying to detect corners. The **Images taken** counter on the top right indicates how many images you have confirmed so far.

![image](https://user-images.githubusercontent.com/9033365/46244963-79a11500-c3ef-11e8-8784-69e840e553aa.png)

At least three images are required. The more, the better the parameters estimation. Once you confirm at least three images, you can click **DONE** on the bottom right. Once clicked:
* the intrinsic and extrinsic parameters will be calculated. Three files will be created: **intrinsic.txt**, **extrinsic.txt**, and **predicted VS actual.txt**
* The 2D points of the first confirmed image will be predicted using the following relation:

![image](https://user-images.githubusercontent.com/9033365/46245137-cede2600-c3f1-11e8-96d5-6e3895f60f1f.png)

* To check accuracy, the predicted 2D points will be displayed on the image in the graphical interface as white circles with a plus sign inside.

![image](https://user-images.githubusercontent.com/9033365/46245120-a1917800-c3f1-11e8-918a-38cdfc13fa97.png)


[Click here to see the demo as video.](https://drive.google.com/file/d/16kSAB0DtYn3Hs7U9yBGAok8P0g7BMp-G/view?usp=sharing)


# dependency
pip install opencv-python
pip install opencv-python-contrib

## [拍照说明](https://blog.csdn.net/j_shui/article/details/77262947)

相机标定是进行视觉测量和定位的基础工作之一，标定参数准确与否直接关系到整个系统的精度，为此根据自己项目中的经验及参考相关的商用视觉软件的做法将相机标定过程中标定图片的获取过程中需要注意的问题总结如下：

标定板拍摄的张数要能覆盖整个测量空间及整个测量视场，把相机图像分成四个象限（如图1所示），应保证拍摄的标定板图像均匀分布在四个象限中，且在每个象限中建议进行不同方向的两次倾斜，图2是一组推荐摆放方式图片。

标定图片的数量通常在15~25张之间，图像数量太少，容易导致标定参数不准确。

圆或者圆环特征的像素数尽量大于20，标定板的成像尺寸应大致占整幅画面的1/4

用辅助光源对标定板进行打光，保证标定板的亮度足够且均匀

标定板成像不能过爆，过爆会导致特征轮廓的提取的偏移，从而导致圆心提取不准确。

标定板特征成像不能出现明显的离焦距，出现离焦时可通过调整调整标定板的距离、光圈的大小和像距（对于定焦镜头，通常说的调焦就是指调整像距）。

标定过程，相机的光圈、焦距不能发生改变，改变需要重新标定。

![图1 图像的四象限位](https://img-blog.csdn.net/20170816182848063?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQval9zaHVp/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![图2 标定板合适摆放位置](https://img-blog.csdn.net/20170816182944722?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQval9zaHVp/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- https://github.com/opencv/opencv/blob/master/samples/cpp/tutorial_code/calib3d/camera_calibration/camera_calibration.cpp)

### 图片获取

```bash
# step01 安装vedio拍照
F:\xuanwu\tools\aiot-release-V20210331-202106041540.apk
adb connect id_Address
adb devices # checking the connecting
adb install F:\xuanwu\tools\aiot-release-V20210331-202106041540.apk

# step02 拍照
# step03 pull the images
E:\data\camera_calibration
```

## usage

```bash
# you need change image_dir /image fomat/棋盘对应的检测列（WIDTH）/棋盘对应检测的行（HEIGHT）/棋盘方块对应的大小（SQUARE_SIZE， 长或宽）。
# step01 
python calibrate_chessboard.py #get calibration_chessboard.yml

# step02 undist
python undist.py # load the camera calibration_chessboard.yml and distort
```



### calibration parameter and add code

```bash
# note SQUARE_SIZE 指的是正方向的大小。
data: [ 6.3679404207355321e+02, 0., 6.3701922316458365e+02, 0.,
       6.4220781758881571e+02, 3.1267232337362935e+02, 0., 0., 1. ]
D: !!opencv-matrix
   rows: 1
   cols: 5
   dt: d
   data: [ -3.6721049616656565e-01, 1.1686644036526267e-01,
       1.3678611194601928e-03, 1.3781249474976913e-03,
       -1.5966288380859801e-02 ]
```

新增代码:缩放原图到90%，在周边padding 到原图大小

```bash
Mat src, dst;
int top, bottom, left, right;
int borderType = BORDER_CONSTANT;
cv::Mat roi_dest;
cv::resize(roi, roi_dest, cv::Size(), 0.9 , 0.9 );

top = (int) (0.05*roi.rows); bottom = top;
left = (int) (0.05*roi.cols); right = left;

Scalar value(255,255,255);
copyMakeBorder( roi_dest, dst, top, bottom, left, right, borderType, value );
```



## reference

- [code referece](E:\gitlab\cpp\test\camera_calibrateion.cpp) and [opencv offical camera calibration](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html）

- [world coor and camera coor](https://www.cnblogs.com/mikewolf2002/p/5746667.html)
- [张正友相机标定Opencv实现以及标定流程&&标定结果评价&&图像矫正流程解析](https://blog.csdn.net/dcrmg/article/details/52939318)
- [https://medium.com/vacatronics/3-ways-to-calibrate-your-camera-using-opencv-and-python-395528a51615](https://medium.com/vacatronics/3-ways-to-calibrate-your-camera-using-opencv-and-python-395528a51615)
- [undistor](https://aishack.in/tutorials/calibrating-undistorting-opencv-oh-yeah/) and [c++ code](https://github.com/Thomio-Watanabe/undistort_images/blob/master/src/main.cpp)
## key word
摄像头标定 camera calibration





#   

