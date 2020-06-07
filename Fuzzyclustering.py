# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 19:05:13 2018

@author: hp
"""

import numpy as np
import skfuzzy as fuzz
def fuzzyclustering(X):
    cnt,u,_,_,_,_,_ = fuzz.cmeans(X,2,2,0.5,100,seed=1)
    return cnt,u
def cost_func(X,W,Y):
    Xnew = np.dot(X,W)
    cnt,u = fuzzyclustering(Xnew.T)
    err = min(np.sum((np.reshape(np.argmax(u,axis =0),(93750,1))!=Y)*1),93750-np.sum((np.reshape(np.argmax(u,axis =0),(93750,1))!=Y)*1))
    return err,cnt