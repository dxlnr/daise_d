#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:28:46 2018

@author: MikkelGronning
"""
import matplotlib.pyplot as plt
import numpy as np
import h5py
import os
from sklearn.cluster import DBSCAN

"""

"""
def All_HDF5(directory):
    fileDirectory = os.listdir(directory)
    
    f = []
    count = 0
    for files in fileDirectory:
        
        # Make sure all file type  are .h5 files 
        if( files[-3:] == '.h5' ):
            f = np.append(f, directory + files)
            count = count + 1
    
    return(f)
###############################################################################
    

"""

"""
def loadHDF5_File(fileDirectory):
    with h5py.File(fileDirectory, 'r') as hdf:
        ls = list(hdf.keys())
        
        
        ## Get all data sets of the HDF5 File
        datasets = list() 
        for dataset in ls:
            data = np.array(hdf.get(dataset))
            datasets.append(data)
        
        return(ls, datasets)
###############################################################################


"""

"""
def createHDF5(name, keys, data):
    if len(keys) != len(data):
        print("keys have to match dataset")
        return -1
    with h5py.File(name, "w") as hdf:
        for i in range( len(keys) ):
             hdf.create_dataset(keys[i], data = data[i] )
    print(name, " created.")
###############################################################################


"""

"""
def plot24H_TimeSerie(data, name, col, y_label, numOfTics = 25):   

    Tics = np.array(('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'))
    
    if numOfTics == 5:
         Tics = np.array(('00', '06', '12', '18', '24'))
        
    
    
    plt.plot(data, col)
    plt.title( name )
    plt.xlabel( "Time" )
    plt.ylabel( y_label )
    plt.xticks(np.linspace(0, 24*60*60, num=numOfTics), Tics)
###############################################################################


"""

"""
def SideBySide(datasets, ls, group):
    plt.figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k') 
    plt.subplot(1, 3, 1)
    plotTimeSerie(datasets[ group[0] ], ls[ group[0] ], 'b', 'Voltage [V]', numOfTics = 5)
    
    plt.subplot(1, 3, 2)
    plotTimeSerie(datasets[ group[1] ], ls[ group[1] ], 'g', 'Current [A]', numOfTics = 5)
    
    plt.subplot(1, 3, 3)
    plotTimeSerie(datasets[ group[2] ], ls[ group[2] ], 'r' , 'Power [W]', numOfTics = 5)
    
###############################################################################


"""

"""        
def minuteAvg(HFD5File):
    [ls, datasets] = loadHDF5_File(HFD5File)
    
    for i in range(0, len(datasets)):
        
        dataset = datasets[i]
        
        tmp = np.empty([24*60])
        count = 0
        for j in range(0, 24*60*60, 60):
            tmp[count] = (np.mean(dataset[ (j) : (j+1) ]))
            count = count + 1
        datasetsMin.append(tmp)    
            
            
        return(datasetsMin)
###############################################################################
        

"""

"""
def KNNTimeSeries(X, k, MinToCompare, progress = False):   
    n = len(X)
    
    disInd = np.zeros((n, k))
    disMat = np.zeros((n, k))
    
    for i in range(n):
        # Print progress in percent
        if progress == True:
            if  i % np.floor(n/100) == 0:
                print("{0:.2f} %" .format(i/n * 100))
        
            if i == n-1:
                print("100.00 %")
        
        # Find the 900 values before index i 
        # if i < 900 when pick the valeus before
        if i < MinToCompare:
            xbVal = X[ 0 : i ]
            xbIndex = np.arange(0, i)
            xbIndex.astype(int)  # make sure index is int
            
            xb = np.column_stack((xbVal, xbIndex))
            
        else:
            xbVal = X[ (i-MinToCompare) : i ]
            xbIndex = np.arange(i-MinToCompare, i)
            xbIndex.astype(int) # make sure index is int
            
            xb = np.column_stack((xbVal, xbIndex))
        
        
        # Find the 900 values after index i 
        # if i + 900 < 900 when pick the valeus before
        if (i + 1 + MinToCompare) > n:
            xaVal = X[ (i+1) : n ]
            xaIndex = np.arange( (i+1) , n)
            xaIndex.astype(int) # make sure index is int
            
            xa = np.column_stack((xaVal, xaIndex))
            
        else:
            xaVal = X[ (i+1) : (i+1+MinToCompare) ]
            xaIndex = np.arange( (i+1),  (i+1+MinToCompare) )
            xaIndex.astype(int) # make sure index is int
            
            xa = np.column_stack((xaVal, xaIndex))
        
        # Combinde the observation before i with observations after:
        xD = np.concatenate((xb, xa), axis=0)
        point = np.array((X[i], i))
        
        # Find the eucldean distance to the index and and xD
        dis = np.column_stack((np.sum(( xD - point )**2, axis=1), xD[:,1]))
        closestIndex = dis[:,1][np.argsort(dis[:,0])[:k]]
        closestVal = dis[:,0 ][np.argsort(dis[:,0])[:k]]
        
        disInd[i,:] = closestIndex
        disMat[i,:] = closestVal

    return(disInd, disMat)
    



"""

"""
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
###############################################################################



"""

"""
def DBSACN_Clusters(data, MinToCompare):
    
    minSamples = int( np.floor(np.log(len(data))) )
    
    [disInd, disMat] = KNNTimeSeries(X=data, k=minSamples, MinToCompare=30, progress=False)
    
    disMatSorted = np.sort(disMat[:, minSamples-1 ])
    n = len(disMat[:,0])
    
    slope = ( disMatSorted[1:n] - disMatSorted[0:(n-1)]  )  * n
    
    # Using a threshold value of 0.01% so that the slope has a slope of 1% difference
    # is an optimal Eps value. 
    val = find_nearest(slope, 0.01)
    
    # Reshape data for input to DBSCAN 
    X = data.reshape(-1, 1)
    clustering = DBSCAN(eps = val, min_samples=minSamples, metric='euclidean').fit(X)
    
    Clusters = clustering.labels_
    
    print(val)
    print(minSamples)
    print(np.unique(clustering.labels_))
    
    return(Clusters)
###############################################################################










