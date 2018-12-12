#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:32:33 2018

@author: MikkelGronning
"""
import numpy as np
import my_functions as my_f
import matplotlib.pyplot as plt



"""

"""
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
        lengthMatrix[2,j] = length   # the cardinality
        lengthMatrix[3,j] = temporalLength 
        lengthMatrix[4,j] = length/temporalLength
        
        if diagnostics == True:
            print(j, length, temporalLength, loc)
        
    return(lengthMatrix)
###############################################################################
    
"""
Function Description:
    Check a seqeunce of samples X if model conditions are furfilled. If they
    are it returns a matrix N x N (where N represents the number of clusters)
    The value of the matrix are booleans and state if condindations are valid
    between two clusters. 
        If No = 0
        If yes = 1
"""
def eventModel(WindowMat, epsilon=0.25):

    # number of clusters 
    numOfCluster = WindowMat.shape[1]
    
    # Get the start and the end of clusters.
    # I.e. the the first two row of window matrix.
    startEnd = WindowMat[0:2, :]
    
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
        
        
        checkMat = HighTempporalLocality(checkMat, WindowMat, epsilon)
    return(checkMat)   
###############################################################################

def HighTempporalLocality(checkMat, lengthMatrix, epsilon = 0.25):
    
    loc = lengthMatrix[4,:]
    
    for i in range(len(loc)):
        if( loc[i] <= 1-epsilon ):
            checkMat[:,i] = 0
            checkMat[i,:] = 0
            
    return checkMat
###############################################################################

"""

"""
def eventInterval(WindowMat, checkMat):
    
    if np.sum(checkMat) == 0:
        print("The CheckMat dosen't contain to clusters which lives up to the model")
        return -1
    
    
    if np.sum(checkMat) != 0:
        # The dimension of the checkMat used to loop trhough the values:
        l = checkMat.shape[0]
        
        # Rows of the checkMat matrix
        for i in range(l):
            
            # Colums of CheckMat Matrix
            for j in range(l):
                if(checkMat[i,j]==1):
                    
                    # The start of event interval 
                    if i < j:
                        print("small value")
                        print(i,j)
                        eventBegining = WindowMat[1,i]
                    
                    # The end of event interval 
                    if i > j:
                        eventEnd = WindowMat[0,i]
        
        eventInterval = np.array((eventBegining, eventEnd))
    
        return(eventInterval)
###############################################################################
#%%

[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_02.h5")
u = 33800
v = 34100


data = datasets[3][u:v]
cluster = my_f.DBSACN_Clusters(data, 30, 0.01)

plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), data)



plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), cluster)


WindowMat = lengths(cluster, u, v, False)

if WindowMat.shape[1] > 1:
    checkMat = eventModel(WindowMat) 
     
    if np.sum(checkMat) > 0:
        print("event detected")
        event = eventInterval(WindowMat, checkMat)
    
    if np.sum(checkMat) == 0:
        print("no event")
        v = v + 30

#%%
[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_02.h5")

data = datasets[3]
n = len(data)

windowsize = 150

u = 0
v = windowsize
while v < n:
    
    u = u + windowsize
    v = v + windowsize
    
    if u == 0:
        dataWin = data[u:v]
        
    else:
        dataWin = data[(u-5):v]
    
    if v > n:
        dataWin = data[(u-5):n]

    
    cluster = my_f.DBSACN_Clusters(dataWin, 30, 0.01)


