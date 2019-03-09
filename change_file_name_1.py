# -*- coding: utf-8 -*-
import os
from nt import chdir
datadir = r"G:\zunyi_data\gpp"
filename = os.listdir(datadir)
for temp in filename:
    
    num = temp.rfind('2016')#找到"mask_"的下标
    #new_name = temp[num+4:num+7]
    num2 = temp.rfind('_500m')
    new_name = temp[num+4:num+7] + temp[num2-6:num2]
    print(new_name)
    chdir(os.path.dirname(datadir))
    os.rename(datadir+os.sep+temp,datadir+os.sep+new_name+".tif")
#move file
'''output= r"G:\zunyi_data\gpp\ori\PsnNet"
if not os.path.exists(output):
    os.mkdir(output)
import shutil
filename = os.listdir('G:\zunyi_data\gpp')
for temp in filename:
    if temp.endswith('PsnNet.tif'):
        print(temp)
        shutil.move('G:\zunyi_data\gpp'+os.sep+temp,output+os.sep+temp)   '''

########################################
##更改文件所在文件夹
import os 
import sys
import shutil

path = r'I:\future_clim\tasmin'
os.chdir(path)
for i in os.listdir():
    if 'rcp45' in i:
        shutil.move(i, r'I:\future_clim\tasmin\4.5')
