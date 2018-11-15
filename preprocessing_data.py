#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:50:30 2018

@author: MikkelGronning
"""

import h5py
import numpy as np
import os

   
#%% GET ALL DATA FILES
fileDirectory = os.listdir("data/")

f = []

count = 0
for files in fileDirectory:
    
    # Make sure all file type  are .h5 files 
    if( files[-3:] == '.h5' ):
        f = np.append(f, 'data/' + files)
        count = count + 1
  


#%%
with h5py.File(f[1], 'r') as hdf:
    ls = list(hdf.keys())
    
    
    ## Get all data sets of the HDF5 File
    datasets = list() 
    for dataset in ls:
        print(dataset)
        data = np.array(hdf.get(dataset))
        
        datasets.append(data)
        
    
    
    shape = datasets[0].shape
    for i in range(len(datasets)):
        
        ## check if all data sets in the list datasets have the same dimension
        if(datasets[i].shape != shape):
            print("Error: The dataset in data set list don't have the same shape.")
            # return(0)
    
        # check if there are obervation 24*60*60 = 86400
        if(datasets[i].shape[0] != 86400):
            numOfMissingValues = 86400 - datasets[i].shape[0]
            
            # Handle the missing data by creating a vector with same length 
            # as the missing data where the value is the mean of next 15 minutes
            mean15min = np.mean(datasets[i][0:15*60])
            
            ArtificalVal = np.full((numOfMissingValues), mean15min)
            
            # Concantenate the ArtificalVal onto the datasets
            datasets[i] = np.concatenate((ArtificalVal, datasets[i]), axis=0)