# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:14:21 2019

@author: Manero
"""

import h5py

file_name = 'e:/Wind/Scripts/MultipleData/configsjm/model156929069441-11-5794-12'

f = h5py.File(file_name)
for key in f.keys():
    print(key) #Names of the groups in HDF5 file.
group = f[key]

#Checkout what keys are inside that group.
for key in group.keys():
    print(key)
    
    
def read_hdf5(path):

    weights = {}

    keys = []
    with h5py.File(path, 'r') as f: # open file
        f.visit(keys.append) # append all keys to list
        for key in keys:
            if ':' in key: # contains data if ':' in key
                print(f[key].name)
                weights[f[key].name] = f[key].value
    return weights

read_hdf5(file_name)