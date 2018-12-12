#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:58:50 2018

@author: MikkelGronning
"""
import numpy as np
import my_functions as my_f
import matplotlib.pyplot as plt

[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_02.h5")



#%%



u = 33780
v = 34080
data = datasets[3][u:v]
n = len(data)
timeTic = ["09:23", "09:24", "09:25", "09:26 ", "09:27", "09:28"]
ticks = np.append(np.arange(u,v,60), v)



minSamples = int(np.floor(np.log(len(data))))
[disInd, disMat] = my_f.KNNTimeSeries(X=data, k=minSamples, MinToCompare=30, progress=False)

disMatSorted = np.sort(disMat[:,minSamples-1], axis=0) 



slope = ( disMatSorted[1:n] - disMatSorted[0:(n-1)]  )  * n
val = my_f.find_nearest(slope, 0.01)

x = np.where(slope==val)[0][0]


plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), data)
plt.xticks(ticks, timeTic)
plt.ylabel('Current [A]')
plt.xlabel('Time')


plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(disMatSorted)
plt.plot(x, disMatSorted[x],'r+')
plt.ylabel('K distances')
plt.xlabel('Object')

#%%
u = 33000
v = 33400
data = datasets[3][u:v]

tmp = my_f.DBSACN_Clusters(data, MinToCompare = 30)
 

plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k') 
plt.plot(np.arange(u,v), data)
plt.ylabel('Current [A]')
plt.xlabel('Time')

plt.figure(num=None, figsize=(6, 4), dpi=80, facecolor='w', edgecolor='k')
plt.plot(np.arange(u,v),tmp)
 

