#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:26:02 2018

@author: MikkelGronning


This file get all the summary files from BLOND dataset.
"""



import requests

# Getting all the summary files from november 01-30
dates = ["%.2d" % i for i in range(1, 31)]
for date in dates:
    
    print("data/2016_11_" + date + ".h5")
    url = "http://138.246.224.34/s/m1375836/download?path=%2FBLOND%2FBLOND-50%2F2016-11-" + date + "%2Fclear&files=summary-2016-11-" + date +  "-clear.hdf5"
    filename = "data/2016_11_" + date + ".h5"
    
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

#%%

# Get the Summary PDFS
for date in dates:
    print("data/2016_11_" + date + ".pdf")
    url = "http://138.246.224.34/s/m1375836/download?path=%2FBLOND%2FBLOND-50%2F2016-11-" + date + "%2Fclear&files=summary-2016-11-"+ date + "-clear.pdf"
    filename = "summary_PDFs/2016_11_" + date + ".pdf"
    
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
