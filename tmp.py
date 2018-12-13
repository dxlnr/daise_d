#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:15:26 2018

@author: MikkelGronning
"""
import numpy as np

import my_functions as my_f
import matplotlib.pyplot as plt

[ls, datasets] = my_f.loadHDF5_File("NovemberSortedTrueEvent.h5")

days = datasets[0]
seconds = datasets[2]
offices = datasets[1]


### 31: November 1
### 32: November 2
### ...
### 61: November 30

#%%

def findEventTime(day, office):
    a = days == day
    b = offices == office
    
    n = len(a)
    EventTime = np.zeros((n), dtype=bool)
    
    for i in range(n):
        EventTime[i] = a[i] and b[i]
    
    return EventTime

    
#%%
def calculateResults(trueEvent, result):
    numOfevent = len(trueEvent)
    NumOfDeteted = len(result)
    
    gap = 10
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    
    for event in trueEvent:
        
        for j in range(result.shape[0]):
            
            if result[j,0]-gap <= event <= result[j,1]+gap:
                tp = tp + 1
        
        
    fp = nDet - fp          
    fn = nTrue - tp
    
    precision = round(tp/(tp+fp),3)
    return(numOfevent, NumOfDeteted, tp, fp, fn, precision)

trueEvent = seconds[ findEventTime(44,2) ]

#%%

trueEvent = seconds[findEventTime(32, 1)]

calculateResults(trueEvent, office1)
