#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:00:07 2018

@author: MikkelGronning
"""

import numpy as np
from sklearn.cluster import DBSCAN
import my_functions as my_f
import matplotlib.pyplot as plt

#%%
HDF5_Files = np.sort(my_f.All_HDF5("preprocced_data/"))


for i in range(0,3):
    
    [ls, datasets] = my_f.loadHDF5_File(HDF5_Files[i])

    
    ## current_rms1
    ## current_rms2
    ## current_rms3
    clusters = []
    for j in range(3,6):
        
        print(ls[j])
        [disInd, disMat] = my_f.KNNTimeSeries(X=datasets[j], k=1, MinToCompare=30, progress=False)
        
        clusters.append(DBSACN_Clusters( disMat,  datasets[j] ))
        
    name = "clusters/" +  HDF5_Files[i][-13:]    
    my_f.createHDF5(name, ls[0:3], clusters)
    
