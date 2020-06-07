# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:59:39 2019

@author: hp
"""


import numpy as np
#from PIL import Image
import cv2
from skimage.filters import threshold_otsu


count=0
def compute(img):
    #img =Image.open("D:\\smart space lab\\testfolder\\test1.jpg")
    global count
    file = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    X = np.array(file)
    W = np.load("w112.npy")
    #W = np.load("D:\\smart space lab\\wglobalbest.npy")
    #W = np.array([[3.3614,1.2995,0.7155],[-0.4734,-0.2932,0.5155],[-1.9117,-1.6223,-1.5836]])
    Xnew = np.dot(X,W)
    #%%

    channel1 = Xnew[:,:,0]
    channel2 = Xnew[:,:,1]
    channel3 = Xnew[:,:,2]
    #%%
    thresh1 = threshold_otsu(channel1)
    thresh2 = threshold_otsu(channel2)
    thresh3 = threshold_otsu(channel3)
    #%%
    thresholdedch1 = channel1>= thresh1
    thresholdedch2 = channel2>= thresh2
    thresholdedch3 = channel3>= thresh3
    #%%
    binarr =  np.zeros((X.shape[0],X.shape[1]))
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if(thresh1>=-5000 and thresh2 >=20000 and thresh3>= 13000):
                if(thresholdedch1[i][j] and thresholdedch2[i][j] and thresholdedch3[i][j]):
                    binarr[i][j] = 255

    #%%
    cv2.imwrite('D:\\machinelearning projects\\fuzzy svm\\Fire Dataset\\videos\\SSlabbin\\pic'+str(count)+".jpg",binarr)
    count=count+1

def extractFrames(pathIn):

    cap = cv2.VideoCapture(pathIn)
    count =0
    while (cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            compute(frame)

        else:
            break
        if ret== False:
            break
        print(count)
        cv2.imwrite('D:\\machinelearning projects\\fuzzy svm\\Fire Dataset\\videos\\SSlaborg\\pic'+str(count)+".jpg",frame)
        count+=1
       
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    extractFrames("D:\\machinelearning projects\\fuzzy svm\\Fire Dataset\\videos\\SSlab\\v1.mp4")
