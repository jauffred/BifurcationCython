# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:07:31 2020

@author: jauff
"""

from math import pi,sin

def Py_logistic(x,mu):
    
    xout= mu*x*(1.-x)
    
    return xout


def Py_sine_model(x,mu):
    
    xout= mu * sin(pi*x)
    
    return xout


def Py_quartic_model(x,mu):
    
    W= 3*x*(1.-x)
    
    xout= mu*W*(3.-3.*W+W*W)
    
    return xout


def Py_tent_model(x,mu):
    
    e=.45
    
    if x<=e:
        xout= mu*x/e
    else:
        if x<1.-e:
            xout= mu
        else:
            xout=mu*(1.-x)/e
            
    return xout


def Py_RunManager(model,mu_min,mu_max,nparm,niter,nout):
    
    burnout= niter - nout
    
    mu_array=[mu_min+i*(mu_max-mu_min)/nparm for i in range(nparm+1)]
    
    xarray=[]
    
    for mu in mu_array:
        
        xi=[]
        
        x0= .5
        
        for j in range(niter):
            
            x0= model(x0,mu)
            
            if j<burnout:
                continue
            
            xi+=[x0]
            
        xarray+=[xi]
        
    return xarray,mu_array


            
            
            
            
