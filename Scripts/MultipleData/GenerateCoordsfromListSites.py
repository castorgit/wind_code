# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:19:41 2019

@author: Manero
"""

import numpy as np
import pandas as pd

a = np.load("e:/data_turbines/Coords.npy")
df = pd.read_csv('e:/Wind/Scripts/MultipleData/list_sites(JM1).csv', index_col=0,header = 0)

coords = a[0]

l = []
for index, row in df.iterrows():
    i = int(row['site'].split('-')[1])
#    print(index, row['site'], a[i])
    l.append(a[i])
    
myarray = np.asarray(l)
np.save("e:/data_turbines/CoordsJM_list.npy",myarray)

# tio hazlo con un lambda como esto no me sale tu

#df['coordenadas'] = a[df.index]