# 基于caffe的盲道导航-深度学习

## 原理： 
利用大量盲道图像和GoogleNet网络结构对深度学习的Caffe神经网络进行训练，最终得到能识别盲道图像的model。盲道图像采取盲人第一视角拍摄，图像根据盲道所在图像中的位置分成left、right、middle、warning四类图片，最终系统会根据盲道在图像的位置给出修正偏差的语音提示，即对left或right类图片给出盲人向右或向左调整的反馈，对warning类图像给出注意反馈，对middle类图片则不给予反馈。最终利用model对盲道图像做出判断，在此基础上给出语音反馈，实行对盲人的指引。目前在windows在平台测试model预测效果。
  
## 系统设想图  
https://github.com/用户名/repository仓库名/raw/分支名master/图片文件夹名称/***.png or***.jpg

环境要求：
python2.7

model_settings文件包含： 
1、caffenet_train_iter_2000.caffemodel，即训练出来的用于预测的model
由于github文件大小要求，该model放在百度云盘：https://pan.baidu.com/s/1RA0aH-yxjM3czr7xY03gsA 
2、mean.npy 即是用于python环境下的均值文件 
3、word.txt 为分类标签对应的类型 
4、deploy.prototxt  用于预测时使用

python文件包含caffe的接口

show中的图片用于演示

voice中即为反馈的语音文件

