# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:21:01 2018

@author: Mr.Su
"""

import os
import cv2


rootdir = r'C:\\caffe\\caffe-master\\data\\road\\warnning'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
 
        document = os.path.join(currentPath)
        img = cv2.imread(document)
        img = cv2.resize(img, (256,256))
        newname=r"C:\\caffe\\caffe-master\\data\\road\\train\\train_warnning\\" + filename
        
        cv2.imwrite(newname,img)



