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
