# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:43:04 2018

@author: hp
"""

import numpy as np
def cost_func(x):
    x1 = x
    if np.size(x1==1):
        return (x1-15)**2
    return np.power(x-5,2)
x = np.random.uniform(low = -1000,high = 1000,size=(1000,1))
localbest = x[:]
localbest_cost = cost_func(x)
#%%
#cost = cost_func(x)
globalbest_cost = np.min(cost_func(x))
globalbest = x[np.argmin(cost_func(x))]
#localbest = np.minimum(cost,cost_func(x))
max_iter = 1000
w = 1
c1 =2
c2 =2
v = np.random.randn(1000,1)
#%%
for it in range(max_iter):
    for i in range(1000):
        v[i] = w*v[i]+ c1 * np.random.uniform(low =0 , high =1,size=1)*(localbest[i]-x[i])+c2 * np.random.uniform(low =0 , high =1,size=1)*(globalbest-x[i])
        x[i] = x[i]+v[i]
        temp_cost = cost_func(x[i])[0]
        if(temp_cost<localbest_cost[i]):
            localbest_cost[i] = temp_cost
            localbest[i] = x[i]
           # print(x[i],localbest[i],localbest_cost[i])
            if(temp_cost<globalbest_cost):
                globalbest = x[i]
                globalbest_cost = temp_cost
                print(x[i],globalbest,globalbest_cost)
        if(globalbest_cost<0.01):
            break
            