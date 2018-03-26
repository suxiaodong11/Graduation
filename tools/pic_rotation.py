# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:29:08 2018

@author: Mr.Su
"""

import os
from PIL import Image  

    
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
      
        