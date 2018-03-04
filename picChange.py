# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:12:27 2018

@author: Mr.Su
"""

import os
import time

import cv2

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

alter('C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\MZhang-master\\picture\\stop','C:\\Users\\Yaodong Su\\Desktop\\GraduationThesis\\MZhang-master\\picture\\stop2')
