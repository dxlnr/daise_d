#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:36:18 2018

@author: MikkelGronning
"""

import h5py
import os
import numpy as np
import matplotlib.pyplot as plt


 
# This function find the minute averarge of HDF5 File

def MinAvg(files):
    apparent_power1 = np.array(())
    apparent_power2 = np.array(())
    apparent_power3 = np.array(())
    current_rms1 = np.array(())
    current_rms2 = np.array(())
    current_rms3 = np.array(())
    mains_frequency = np.array(())
    power_factor1 = np.array(())
    power_factor2 = np.array(())
    power_factor3 = np.array(())
    real_power1 = np.array(())
    real_power2 = np.array(())
    real_power3 = np.array(())
    voltage_rms1 = np.array(())
    voltage_rms2 = np.array(())
    voltage_rms3 = np.array(())
    
    
    for i in range(0,30):
        print( round(((i+1)/30)*100, 2), "% completed")
        print(files[i])
        tmp = minuteAvg(files[i])
        
        apparent_power1 = np.append(apparent_power1, tmp[0])
        apparent_power2 = np.append(apparent_power1, tmp[1])
        apparent_power3 = np.append(apparent_power1, tmp[2])
        current_rms1    = np.append(apparent_power1, tmp[3])
        current_rms2    = np.append(apparent_power1, tmp[4])
        current_rms3    = np.append(apparent_power1, tmp[5])
        mains_frequency = np.append(apparent_power1, tmp[6])
        power_factor1   = np.append(apparent_power1, tmp[7])
        power_factor2   = np.append(apparent_power1, tmp[8])
        power_factor3   = np.append(apparent_power1, tmp[9])
        real_power1     = np.append(apparent_power1, tmp[10])
        real_power2     = np.append(apparent_power1, tmp[11])
        real_power3     = np.append(apparent_power1, tmp[12])
        voltage_rms1    = np.append(apparent_power1, tmp[13])
        voltage_rms2    = np.append(apparent_power1, tmp[14])
        voltage_rms3    = np.append(apparent_power1, tmp[15])
        
    with h5py.File("november_AVG.h5", "w") as hdf:
        hdf.create_dataset('apparent_power1', data = apparent_power1)
        hdf.create_dataset('apparent_power2', data = apparent_power2)
        hdf.create_dataset('apparent_power3', data = apparent_power3)
        hdf.create_dataset('current_rms1', data = current_rms1)
        hdf.create_dataset('current_rms2', data = current_rms2)
        hdf.create_dataset('current_rms3', data = current_rms3)
        hdf.create_dataset('mains_frequency', data = mains_frequency)
        hdf.create_dataset('power_factor1', data = power_factor1)
        hdf.create_dataset('power_factor2', data = power_factor2)
        hdf.create_dataset('power_factor3', data = power_factor3)
        hdf.create_dataset('real_power1', data = real_power1)
        hdf.create_dataset('real_power2', data = real_power2)
        hdf.create_dataset('real_power3', data = real_power3)
        hdf.create_dataset('voltage_rms1', data = voltage_rms1)
        hdf.create_dataset('voltage_rms2', data = voltage_rms2)
        hdf.create_dataset('voltage_rms3', data = voltage_rms3)
        
    print("Minute Average of month succesufully made")

#%%

def writeHDF(name, distination, keys, data):
    #%%
    if type(name) != str:
        "HDF5 File name must be a string"
    
    #%%
    if type(thislist) == list:
        print("hej")


    
    
    
    

    
    
    
    
    
    
    
