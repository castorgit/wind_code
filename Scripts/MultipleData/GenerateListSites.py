# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:39:47 2019

@author: Manero
"""
import numpy as np
import pandas as pd
import os

size = 2000
lsites = np.random.choice(range(126692), size, replace=False)
lsites = [f'{site // 500}-{site}' for site in lsites]
print(lsites)
df = pd.DataFrame(lsites)
print(os.getcwd())
#df.to_csv('./list_sites(JM).csv')