#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:37:51 2018

@author: MikkelGronning
"""
import numpy as np
import my_functions as my_f
import matplotlib.pyplot as plt

[Clusters_LS, clusters] = my_f.loadHDF5_File("clusters/2016_11_02.h5")
[LS, data]              = my_f.loadHDF5_File("preprocced_data/2016_11_02.h5")


#%%


def computeLengths(cluster, i):
    
    tmp = np.where( cluster == i )[0]
    
    length = np.sum(cluster == i)
    
    u = tmp[0]
    v = tmp[len(tmp)-1]
    temporalLength = v - u + 1


    loc = length/temporalLength
    
    return(length, temporalLength, loc)
    

n = len(np.unique(clusters[0]))
for i in range(n-1):
    
    print(i, computeLengths(clusters[0], i))


#%%
        
np.where( clusters[0] == 1 )[0]