#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:32:33 2018

@author: MikkelGronning
"""
import numpy as np
import my_functions as my_f
import matplotlib.pyplot as plt

[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_02.h5")


#%%



u = 33800
v = 34100

cluster = DBSACN_Clusters(datasets[3][u:v])

plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), datasets[3][u:v])



plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), cluster)



#%%

def lengths(cluster, u, v, diagnostics = False):

    numOfcluster = np.max(np.unique(cluster)) + 1
    lengthMatrix = np.zeros((5, numOfcluster))
    for j in range(0, numOfcluster):
        tmp = np.where( cluster == j )[0]
         
        uWin = tmp[0]
        vWin = tmp[len(tmp)-1]
        
        length = np.sum( cluster == j )
        temporalLength = vWin - uWin + 1
        loc = length/temporalLength
        
        lengthMatrix[0,j] = u + uWin # start of cluster j
        lengthMatrix[1,j] = u + vWin # end of cluster j
        lengthMatrix[2,j] = length
        lengthMatrix[3,j] = temporalLength 
        lengthMatrix[4,j] = length/temporalLength
        
        if diagnostics == True:
            print(j, length, temporalLength, loc)
        
    return(lengthMatrix)

def timeOverlap(WindowMat):

    # number of clusters 
    numOfCluster = WindowMat.shape[1]
    
    startEnd = WindowMat[0:(numOfCluster-1), :]
    
    checkMat = np.zeros((numOfCluster, numOfCluster))
    compareVec = np.arange((numOfCluster))
    
    for i in range(numOfCluster):
    
        for j in range(numOfCluster):
            
            if i < j:
                val = startEnd[1,i]
                compareval = startEnd[0, compareVec[j]]
                
                if val < compareval:
                    checkMat[i,j] = 1
                
            if i == j:
                checkMat[i,j] = 0
                
                
            if i > j:
                val = startEnd[0,i]
                compareval = startEnd[1, compareVec[j]]
                
                if val > compareval:
                    checkMat[i,j] = 1
    
    return(checkMat)   
    
#%%

def HighTempporalLocality(checkMat, lengthMatrix, epsilon = 0.25):
    
    loc = lengthMatrix[4,:]
    
    for i in range(len(loc)):
        if( loc[i] <= 1-epsilon ):
            checkMat[:,i] = 0
            checkMat[i,:] = 0
            
    return checkMat
    
test = lengths(cluster, u, v, False)

checkMat = timeOverlap(test)       
Overlap = HighTempporalLocality(checkMat, test)


    





           
#%%

print(test[0,0])
print(test[1,0])
print(test[0,1])
print(test[1,1])


if i < j:   
            val = compareVec[ x[j] ]  
            
            if Compare > val:
                checkMat[i,j] = 0
            
            if Compare < val:
                checkMat[i,j] = 1
                
        # Diagnonal element are always True
        if i == j:
            checkMat[i,j] = 1
        
        if i > j:
            val = compareVec[ x[j] ]  
            
            if Compare < val:
                checkMat[i,j] = 0
                
            if Compare > val:
                checkMat[i,j] = 1



