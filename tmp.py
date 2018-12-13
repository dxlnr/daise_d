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

    

print(seconds[ findEventTime(32,1) ])

office1