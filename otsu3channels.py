# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:59:39 2019

@author: hp
"""


import numpy as np
from PIL import Image
import time
img = Image.open("sslabimg.jpg")
#img =Image.open("D:\\smart space lab\\testfolder\\test1.jpg")

X = np.array(img)
W = np.load("D:\\smart space lab\\w112.npy")
#W = np.load("D:\\smart space lab\\wglobalbest.npy")
#W = np.array([[3.3614,1.2995,0.7155],[-0.4734,-0.2932,0.5155],[-1.9117,-1.6223,-1.5836]])
t1 = time.process_time()
Xnew = np.dot(X,W)
t2 = time.process_time()
#%%
from skimage.filters import threshold_otsu
channel1 = Xnew[:,:,0]
channel2 = Xnew[:,:,1]
channel3 = Xnew[:,:,2]
#%%
t3 = time.process_time()
thresh1 = threshold_otsu(channel1)
thresh2 = threshold_otsu(channel2)
thresh3 = threshold_otsu(channel3)
t4 = time.process_time()
print(thresh1,thresh2,thresh3)
#%%
thresholdedch1 = channel1>= thresh1
thresholdedch2 = channel2>= thresh2
thresholdedch3 = channel3>= thresh3
#%%
binarr =  np.zeros((X.shape[0],X.shape[1]))
t5 = time.process_time()
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        if(channel1[i][j]>=-3000 and channel2[i][j] >=25000 and channel3[i][j]>= 35000): #-5000,20000,13000
            if(thresholdedch1[i][j] and thresholdedch2[i][j] and thresholdedch3[i][j]):
                binarr[i][j] = 255
t6 = time.process_time()
#%%
bin = np.array(img.convert('LA'))
bin[:,:,0] = 0
bin[:,:,0]= binarr
binaryimg = Image.fromarray(bin,mode='LA')
#%%
img.show()
binaryimg.show()