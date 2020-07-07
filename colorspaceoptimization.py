# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:53:40 2018

@author: hp
"""

#%%loading the images
import numpy as np
from PIL import Image
import Fuzzyclustering
X = np.zeros((150*625,3))
for i in range(1,51):
    img = Image.open("D:\\smart space lab\\yogeshimgs\\fireimgpos\\firepos ("+str(i)+").jpg")
    crp_img = img.resize((25,25))
    imagearr = np.reshape(np.array(crp_img),(625,3))
    X[(i-1)*625:i*625,:] = imagearr
for i in range(1,63):
    img = Image.open("D:\\smart space lab\\yogeshimgs\\fireimgneg\\nonfireimg ("+str(i)+").jpg")
    crp_img = img.resize((25,25))
    imagearr = np.reshape(np.array(crp_img),(625,3))
    X[46875+(i-1)*625:46875+i*625,:] = imagearr

Y = np.zeros((93750,1))
Y[0:46875] =1
#%%Shuffling step 
perm = np.random.permutation(93750)
Xshuf = X[perm,:]
Yshuf= Y[perm]
#%%Perform fuzzy-cmeans
'''
import fcmn 
lbl,_ = fcmn.fuzzy_cmeans(Xshuf)'''
#%%Linear transformation
W = np.random.uniform(low = -1,high = 1,size=(3,3))
X1 = np.dot(Xshuf,W)
err,tem = Fuzzyclustering.cost_func(Xshuf,W,Yshuf)
#err = np.sum(np.reshape(lbl1,(6250,1))==Yshuf*1)
print(err)
print(tem)

#%%Optimization
W = np.random.uniform(low = -1,high =1, size=(100,3,3))    
localbest = np.array(W)
localbestcost = np.zeros(W.shape[0])
centres = np.zeros((W.shape[0],2,3))
for i in range(W.shape[0]):
    localbestcost[i],centres[i,:,:]= Fuzzyclustering.cost_func(Xshuf,W[i,:,:],Yshuf)
globalbest_cost = np.min(localbestcost)
globalbest = W[np.argmin(localbestcost),:,:]
centrebest = centres[np.argmin(localbestcost),:,:]
w = 1
c1=2
c2 =2
v = np.random.uniform(low=-1,high=1,size=W.shape)
#%%Perform iteratios
max_iter=20
for it in range(max_iter):
    print(it)
    for i in range(100):
        v[i,:,:] = w*v[i,:,:] + c1*np.random.uniform(low =0 , high =1,size=1)*(localbest[i,:,:]-W[i,:,:])+c2 * np.random.uniform(low =0 , high =1,size=1)*(globalbest-W[i,:,:])
        W[i,:,:]= W[i,:,:] + v[i,:,:]
        tempcost,tempcentre = Fuzzyclustering.cost_func(Xshuf,W[i,:,:],Yshuf)
        if(tempcost<localbestcost[i]):
                localbestcost[i] = tempcost
                localbest[i,:,:] = W[i,:,:]
               # print(x[i],localbest[i],localbest_cost[i])
                if(tempcost<globalbest_cost):
                    globalbest = W[i,:,:]
                    globalbest_cost = tempcost
                    centrebest = tempcentre
                    print(globalbest,globalbest_cost)





