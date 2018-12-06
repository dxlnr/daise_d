#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dez 05 17:03:27 2018

@author: DanielIllner
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def compute_temporal_length():
    return 0

def compute_temporal_locality():
    return 0


'''
    input: case 1,2,3 for the specific Event Model
'''
def event_model(case):

    if case == 1:
        return 0
    elif case == 2:
        return 0
    elif case == 3:
        return 0
    else:
        #Errorexception




def model_loss(case,X,u,v):

    return 0



'''
    forward_detection:
        (1) Receive new sample Xn+1 and append it to X
        (2) Update the clustering vector y and the clustering structure
        (3) Check Loss(Mi, X, u, v) <= lambda for all u,v until it is satisfied
'''
def forward_detection(lambda):
    X = []
    N = 0
    while True:
        #self.X.append()
        X.append(Xn[N])

        for i in range(0, 3):
            loss = model_loss(i)

        if loss <= lambda:
            break

        N = N + 1

    return 0

'''
    backward_reduction:
        (1) Delete oldest sample X1 from the segment
        (2) Update the clustering vector y and the clustering structure
        (3) Check Loss(Mi, X, u, v) <= lambda for all u,v until it is not satisfied
'''
def backward_reduction(X, lambda):

    N = 0
    while True:
        #self.X.append()
        X..pop(0)

        for i in range(0, 3):
            loss = model_loss(i)

        if loss >= lambda:
            break

    return X


def detection():


    while (True):

    return 0
