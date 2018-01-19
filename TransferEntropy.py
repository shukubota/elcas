# -*- coding: utf-8 -*-

import numpy as np

def TransferEntropy(x,y,r,tau):
    '''
        Transfer Entropy from y to x with resolution r and time-delay tau
        MI(x(t+tau);y(t)|x(t))
    '''
    
    # the number of bins
    binsx = 1+int((max(x)-min(x))/(r))
    binsy = 1+int((max(y)-min(y))/(r))
    
    # histgrams
    # p(x(t))
    px = np.histogram(x,bins=binsx)
    # p(x(t),y(t))
    pxy = np.histogram2d(x,y,bins=(binsx,binsy))
    # p(x(t),x(t+tau))
    pxx = np.histogram2d(x[:(-tau)],x[tau:],bins=(binsx,binsx))
    # p(x(t),x(t+tau),y(t))
    pxxy = np.histogramdd(np.c_[x[:(-tau)],x[tau:],y[:(-tau)]],bins=(binsx,binsx,binsy))
    
    # estimation of p.d.f.
    # p(x(t))
    px = px[0]/np.sum(px[0])
    # p(x(t),y(t))
    pxy = pxy[0]/np.sum(pxy[0])
    # p(x(t),x(t+tau))
    pxx = pxx[0]/np.sum(pxx[0])
    # p(x(t),x(t+tau),y(t))
    pxxy = pxxy[0]/np.sum(pxxy[0])
    
    # joint entropy
    Hx = -np.dot(px[px!=0],np.log2(px[px!=0]))
    Hxx =-np.dot(pxx[pxx!=0],np.log2(pxx[pxx!=0])) 
    Hxy = -np.dot(pxy[pxy!=0],np.log2(pxy[pxy!=0]))
    Hxxy = -np.dot(pxxy[pxxy!=0],np.log2(pxxy[pxxy!=0]))
    
    return (Hxx-Hx+Hxy-Hxxy)

