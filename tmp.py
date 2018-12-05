#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:15:26 2018

@author: MikkelGronning
"""

import my_functions as my_f
import matplotlib.pyplot as plt

[Clusters_LS, clusters] = my_f.loadHDF5_File("clusters/2016_11_07.h5")
[ls, datasets] = my_f.loadHDF5_File("preprocced_data/2016_11_07.h5")

#%%
plt.figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k') 
plt.subplot(1, 3, 1)
my_f.plot24H_TimeSerie(clusters[ 0 ], Clusters_LS[ 0 ], 'b', 'Current [A]', numOfTics = 5)

plt.subplot(1, 3, 2)
my_f.plot24H_TimeSerie(clusters[ 1 ], Clusters_LS[ 1 ], 'g', 'Current [A]', numOfTics = 5)

plt.subplot(1, 3, 3)
my_f.plot24H_TimeSerie(clusters[ 2 ], Clusters_LS[ 2 ], 'r' , 'Current [A]', numOfTics = 5)

plt.figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(1, 3, 1)
my_f.plot24H_TimeSerie(datasets[ 3 ], Clusters_LS[ 0 ], 'b', 'Current [A]', numOfTics = 5)

plt.subplot(1, 3, 2)
my_f.plot24H_TimeSerie(datasets[ 4 ], Clusters_LS[ 1 ], 'g', 'Current [A]', numOfTics = 5)

plt.subplot(1, 3, 3)
my_f.plot24H_TimeSerie(datasets[ 5 ], Clusters_LS[ 2 ], 'r' , 'Current [A]', numOfTics = 5)


#%%

plt.figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k') 

a = 0
b = 5000
plt.plot(np.arange(a,b), clusters[ 0 ][a:b])

#%%
print( np.unique(clusters[ 2 ]) )