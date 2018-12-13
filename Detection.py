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
                        eventBegining = WindowMat[1,i]
                    
                    # The end of event interval 
                    if i > j:
                        eventEnd = WindowMat[0,i]
        
        eventInterval = np.array((eventBegining, eventEnd))
    
        return(eventInterval)
###############################################################################
        
"""

"""       
def detection(data, windowsize, epsilon = 0.25, delta=0.01, MinToCompare = 30, progress = False):
    # This is the array where the events will be stored.
    eventArray = np.empty((0,2), int) 
    
    # Used to determine the amount of calculations in the while loop
    n = len(data)
    
    u = 0
    v = u + windowsize
    
    # The next two variables are used to print fo the progress of the
    # the detection algorithm 
    prog = n / windowsize # Number of times it will gå thorugh the loop
    count = 0
    
    while v < n:
        
        # Display the progress of algorithm
        if progress == True:
            count = count + 1
    
            if count == int(prog/100):
                print("{0:.2f} %".format(v/n * 100) )
                count = 0
        
        # Load the approriate data window from the data file
        if u == 0:
            dataWin = data[u:v]
        # Load in the previuos 5 values so there is a little data overlap.
        else:
            dataWin = data[(u-5):v]
        if v > n:
            dataWin = data[(u-5):n]
            
        # Pre cluster the data
        cluster = my_f.DBSACN_Clusters(dataWin, MinToCompare, delta)
        # Calucalte the lengths. I.e. Cardinality, Loc 
        WindowMat = lengths(cluster, u, v, False)
        
        # In case there is more than one cluster 
        if WindowMat.shape[1] > 1:
            checkMat = eventModel(WindowMat, epsilon) 
     
            if np.sum(checkMat) > 0:
                event = eventInterval(WindowMat, checkMat)
                eventArray = np.append(eventArray, np.array([event]), axis=0)
                
        # Update the the window size to stream in more Data 
        u = u + windowsize
        v = v + windowsize
    
    return(eventArray)
###############################################################################

#%%
#[ls, datasets] = my_f.loadHDF5_File("November.h5")

[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_03.h5")
#%%

office1 = detection(data = datasets[3], windowsize = 150, epsilon = 0.25, delta=0.01, MinToCompare = 30, progress = True)
office2 = detection(data = datasets[4], windowsize = 150, epsilon = 0.25, delta=0.01, MinToCompare = 30, progress = True)
office3 = detection(data = datasets[5], windowsize = 150, epsilon = 0.25, delta=0.01, MinToCompare = 30, progress = True)











    
            
            
