# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:41:44 2018

@author: Mr.Su
"""

import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import shutil


#扫面文件
def GetFileList(FindPath,FlagStr=[]):      
	import os
	FileList=[]
	FileNames=os.listdir(FindPath)
	if len(FileNames)>0:
		for fn in FileNames:
			if len(FlagStr)>0:
				if IsSubString(FlagStr,fn):
					fullfilename=os.path.join(FindPath,fn)
					FileList.append(fullfilename)
			else:
				fullfilename=os.path.join(FindPath,fn)
				FileList.append(fullfilename)

   
	if len(FileList)>0:
		FileList.sort()

	return FileList
def IsSubString(SubStrList,Str):      
	flag=True
	for substr in SubStrList:
		if not(substr in Str):
			flag=False

	return flag

txt=open('train.txt','w')
#制作标签数据，如果是男的，标签设置为０，如果是女的标签为１
imgfile=GetFileList('first_batch/train_female')
for img in imgfile:
	str=img+'\t'+'1'+'\n'
	txt.writelines(str)

imgfile=GetFileList('first_batch/train_male')
for img in imgfile:
	str=img+'\t'+'0'+'\n'
	txt.writelines(str)
