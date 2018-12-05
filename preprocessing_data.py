#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:50:30 2018

@author: MikkelGronning
"""

import h5py
import numpy as np
import my_functions as my_f


def preprocess(HDF5_File):
    [ls, datasets] = my_f.loadHDF5_File( HDF5_File )
            
    correctDim = 24*60*60
    for i in range( len(datasets) ):
            
        # check if there are obervation 24*60*60 = 86400
        if(datasets[i].shape[0] != correctDim):
            numOfMissingValues = correctDim - datasets[i].shape[0]
            
            # Handle the missing data by creating a vector with same length 
            # as the missing data where the value is the mean of next 15 minutes
            mean15min = np.mean(datasets[i][0:15*60])
            
            ArtificalVal = np.full((numOfMissingValues), mean15min)
            
            # Concantenate the ArtificalVal onto the datasets
            datasets[i] = np.concatenate((ArtificalVal, datasets[i]), axis=0)
    return(ls, datasets)




#%% 
"""
Get all the HDF5 summary data file and preprocess them to make sure they all
have 24*60*60 = 86400 measurement. 
"""

f = np.sort(my_f.All_HDF5("data/"))

for i in range(len(f)):
    [ls, datasets] = preprocess( f[i] )
    print(datasets[1].shape)
    filename = "preprocced_data/" + f[i][-13:]
    my_f.createHDF5(filename, ls, datasets)


#%%
    
preproccedFiles = np.sort( my_f.All_HDF5("preprocced_data/") )


[ls, datasets] = my_f.loadHDF5_File( preproccedFiles[0] )
datasetList = []
for keys in ls:
    datasetList.append( np.array(()) )

    
for i in range( len(preproccedFiles) ):
    # Load file number i
    [ls, datasets] = my_f.loadHDF5_File( preproccedFiles[i] )
    for j in range( len( datasets) ):
        

        datasetList[j] = np.append( datasetList[j],  datasets[j] )
        
    print( round(((i+1)/len(preproccedFiles))*100, 2), "% completed")

my_f.createHDF5("November.h5", ls, datasetList)






    
    