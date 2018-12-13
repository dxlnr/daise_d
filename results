#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:37:23 2018

@author: MikkelGronning
"""

from scipy.io import loadmat
import numpy as np
import pandas as pd

#%%
mat_contents = sio.loadmat('eventList_10_11_12_2016_datenum.mat')

events = mat_contents['eventList']

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
    
#%% 

datetest = list(events[0,663])[2][0]
print(datetest)
dateToint(datetest)

#%%
evenMat = np.zeros((11722,3))
for i in range(11722):
    tmp = list(events[0,i])
    
    evenMat[i,0] = tmp[0][0]
    evenMat[i,1] = medalToOffie(tmp[1][0][0])
    evenMat[i,2] = dateToint(tmp[2][0])
    
#%% 
events_df = pd.DataFrame( loadmat('eventList_10_11_12_2016_datenum.mat') )
#%%
events_df.TimeStamp = events_df.TimeStamp.apply(lambda datenums: pd.to_datetime(datenums-719529, unit='D'))


#%%
import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd

mat = loadmat('eventList_10_11_12_2016_datenum.mat')  # load mat-file
mdata = mat['eventList']  # variable in mat file
mdtype = mdata.dtype  # dtypes of structures are "unsized objects"
# * SciPy reads in structures as structured NumPy arrays of dtype object
# * The size of the array is the size of the structure array, not the number
#   elements in any particular field. The shape defaults to 2-dimensional.
# * For convenience make a dictionary of the data using the names from dtypes
# * Since the structure has only one element, but is 2-D, index it at [0, 0]
ndata = {n: mdata[n][0, 0] for n in mdtype.names}
# Reconstruct the columns of the data table from just the time series
# Use the number of intervals to test if a field is a column or metadata
columns = [n for n, v in ndata.items() if v.size == ndata['MedalNr']]

# now make a data frame, setting the time stamps as the index
df = pd.DataFrame(np.concatenate([ndata[c] for c in columns], axis=1),
                  index=[datetime(*ts) for ts in ndata['MedalNr']],
                  columns=columns)























