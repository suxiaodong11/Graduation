# Graduation
盲道导航-深度学习

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


注：由于百度云盘不支持上传 __init__.py 空文件，特将 python\caffe\proto中的 __init__.py 去掉，目前不知道改文件的作用，在使用时自信创建补上。
