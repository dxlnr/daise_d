#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:37:23 2018

@author: MikkelGronning
"""

from scipy.io import loadmat
import numpy as np
import my_functions as my_f
import pandas as pd

#%%

def timeStringToTuple(date):
    time_tuple = (int(date[0:4]), int(date[5:7]), int(date[8:10]))
    
    return(time_tuple)



def dateToint(date):
    start = '2016-10-01'
    startDate = timeStringToTuple(start)

    tmp = timeStringToTuple(date)
    
    MonthDiff = tmp[1] - startDate[1]
    DayDiff   = tmp[2] - startDate[2]
    
    # in case the date is okotober
    if MonthDiff == 0:
        diff = DayDiff
        # print("september")
    
    # in case the date is different from oktober.
    if MonthDiff != 0:
        
        # November
        if tmp[1] == 11:
            diff = tmp[2] + 31 - startDate[2]
            # print("november")
            
        # December
        if tmp[1] == 12:
            diff = tmp[2] + 31+30 - startDate[2]
            # print("December")

    return diff

def medalToOffie(mN):
    # mN: Meal number
    
    # Office 1:
    of1 = np.array((1, 2, 3, 7, 12))
    if mN in of1:
        return(1)
    
    # Office 2: 
    of2 = np.array((6, 10, 11, 13, 14))
    if mN in of2:
        return(2)
        
    # Office 3
    of3 = np.array((4, 5, 8, 9, 15))
    if mN in of3:
        return(3)
        
def timeStampToNum(timeStamp):
    time = pd.to_datetime(timeStamp-719529, unit='D').strftime('%H:%M:%S')
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:8])
    
    timeinsec = h*60*60+m*60+s
    return(timeinsec)

#%%
mat_contents = loadmat('eventList_10_11_12_2016_datenum.mat')
events = mat_contents['eventList']


evenMat = np.zeros((11722,3))
for i in range(11722):
    tmp = list(events[0,i])
    
    evenMat[i,0] = dateToint(tmp[2][0])
    evenMat[i,1] = timeStampToNum(float(list(tmp[0])[0]))
    evenMat[i,2] = medalToOffie(tmp[1][0][0])
    
#%%
    
SortEvenMat = evenMat[evenMat[:,0].argsort()]

#%%
SortedTrueEvents = np.empty((0,3), int) 


for i in np.unique(SortEvenMat[:,0]):
    
    tmp = SortEvenMat[ SortEvenMat[:,0] == i ]
    tmp2 = tmp[tmp[:,1].argsort()]

    SortedTrueEvents = np.append(SortedTrueEvents, tmp2, axis=0)  
    
    
#%%
NowSortedTrueEvents = np.empty((0,3), int) 
for i in range(31,62):
    
    tmp = SortedTrueEvents[SortedTrueEvents[:,0] == i]
    
    NowSortedTrueEvents = np.append(NowSortedTrueEvents, tmp, axis=0)  
#%%

tmp = [ NowSortedTrueEvents[:,0], NowSortedTrueEvents[:,1], NowSortedTrueEvents[:,2] ]
my_f.createHDF5("NovemberSortedTrueEvent.h5", ["Days", "Seconds", "Office"], tmp)