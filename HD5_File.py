#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:22:43 2018

@author: MikkelGronning
"""

import h5py
import numpy as np
#
# Create a new file using default properties.
#

def getHd5file(file):
    
    with h5py.File(file, 'r') as hdf:
        ls = list(hdf.keys())
        # print('List of dataset in this file: \n', ls)
        
        # data = hdf.get("ls")
        # dataset1 = np.array(data)
        # print('Shape of dataset1: \n', dataset1.shape)
        
        datasets = list() 
        for dataset in ls:
            data = hdf.get(dataset)
            
            datasets.append(np.array(data))
        

        
        return(ls, datasets)
    
file = '/Users/MikkelGronning/Dropbox/DTU/5_Semester_TUM/DAISE/data/2016_11_30.h5'
[ls, data] = getHd5file(file)


#%%

dates = ["%.2d" % i for i in range(1, 31)]

for i in range(1,31):
    print(i)
    file = '/Users/MikkelGronning/Dropbox/DTU/5_Semester_TUM/DAISE/data/2016_11_' + dates[i-1] + '.h5'
    
    [ls, data] = getHd5file(file)
    
    for j in range(0, 16):
        print(ls[j])
        print(data[j].shape)
