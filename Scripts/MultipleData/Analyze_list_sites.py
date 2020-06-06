# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:48:53 2019

@author: Manero
"""

import numpy as np
import pandas as pd
import sys


df = pd.read_csv('e:/Wind/Scripts/MultipleData/list_sites(JM1).csv', index_col=0,names = ['i','site'])


df[['k','num']] = df.site.str.split("-",expand=True)


#df = df.apply(lambda x : x.str.split('-').expand= true)

print(df['num'].count())
df = pd.DataFrame(df)
df['num'] = pd.to_numeric(df['num'])

print(df['num'].std())