# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:12:27 2018

@author: Mr.Su
"""

import os
import cv2
import time
import argparse
import numpy as np
from PIL import Image  
import matplotlib.pyplot as plt





#左右偏移图片
rootdir = r'C:\\caffe\\caffe-master\\data\\road\\warnning\\warnning'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    counter = 1
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        img = cv2.imread(currentPath)
        
''' 
        #图片重命名       
        string = 'warnning-0'
        filename = string + '-' + str(counter) + '.jpg'
        newname=r"C:\\caffe\\caffe-master\\data\\road\\warnning\\warnning-0-0\\" + filename
        cv2.imwrite(newname,img)
        print(' done')
        counter = counter + 1;
'''         
       
        count = 5
        while count <= 50 :             
            mouth = img[0:img.shape[0], count:img.shape[1]] #，坐标形式（Y,X），左上角（0,count），右下角坐标（img.shape[0]，img.shape[1]）
        
            string = 'right-left-' + str(count)
            filename = string + '-' + str(counter) + '.jpg'
            newname=r"C:\\caffe\\caffe-master\\data\\road\\right\\right-left-5-50\\" + filename
            cv2.imwrite(newname,mouth)
            print('width:' + str(mouth.shape[1]) + ' ' + 'hight: ' + str(mouth.shape[0]) + filename + ' done')
            count = count + 5
            
        counter = counter + 1;

      
       