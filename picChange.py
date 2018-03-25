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

#变换图片大小
def alter(path,object):
    result = []
    s = os.listdir(path)
    count = 1
    for i in s:
        document = os.path.join(path,i)
        img = cv2.imread(document)
        img = cv2.resize(img, (200,200))
        listStr = [str(int(time.time())), str(count)]
        fileName = ''.join(listStr)
        cv2.imwrite(object+os.sep+'%s.jpg' % fileName, img)
        count = count + 1

#alter('C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\MZhang-master\\picture\\stop','C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\MZhang-master\\picture\\stop2')


    

'''      
#水平翻转图片函数        
rootdir = r'C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\自拍素材\图片\\right'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
 
        im = Image.open(currentPath)
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        newname=r"C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\自拍素材\图片\\right2"+'\\'+filename
        out.save(newname)    
'''        
        

#偏移图片
rootdir = r'C:\\caffe\\caffe-master\\data\\road\\left\\left'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    counter = 1
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        img = cv2.imread(currentPath)
        
       
        count = 5
        while count <= 50 :             
            mouth = img[0:img.shape[0], 0:img.shape[1] - count] #
        
            string = 'left-right-' + str(count)
            filename = string + '-' + str(counter) + '.jpg'
            newname=r"C:\\caffe\\caffe-master\\data\\road\\\left\\left-right-5-50\\" + filename
            cv2.imwrite(newname,mouth)
            print('width:' + str(mouth.shape[1]) + ' ' + 'hight:' + str(mouth.shape[0]) + filename + ' done')
            count = count + 5
            
        counter = counter + 1;
  
