# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:55:59 2020

@author: jauff
"""

from libc.math cimport pi,sin
from libc.stdlib cimport malloc, free


cdef class ModelBase:  
    pass
     

cdef double logistic(double x, double mu) nogil:
    
    cdef double xout
    
    xout= mu*x*(1.-x)
    
    return xout


cdef class C_logistic(ModelBase):
    
    def __call__(self, double x, double mu):
        
        return logistic(x,mu)
    
Cy_logistic= C_logistic()


cdef double sine_model(double x,double mu) nogil:
       
    cdef double xout
    
    xout= mu * sin(pi*x)
    
    return xout


cdef class C_sine_model(ModelBase):
    
    def __call__(self,double x, double mu):
        return sine_model(x,mu)
    
Cy_sine_model= C_sine_model()


cdef double quartic_model(double x,double mu) nogil:
    
    cdef double W, xout
    
    W= 3*x*(1.-x)
    
    xout= mu*W*(3.-3.*W+W*W)
    
    return xout

cdef class C_quartic_model(ModelBase):
    
    def __call__(self,double x, double mu):
        return quartic_model(x,mu)
    
Cy_quartic_model= C_quartic_model()


cdef double tent_model(double x,double mu) nogil:

    cdef:
        
        double e=.45
        double xout
    
    if x<=e:
        xout= mu*x/e
    else:
        if x<1.-e:
            xout= mu
        else:
            xout=mu*(1.-x)/e
            
    return xout

cdef class C_tent_model(ModelBase):
    
    def __call__(self,double x, double mu):
        return tent_model(x,mu)
        
Cy_tent_model= C_tent_model()


def Cy_RunManager(ModelBase model,double mu_min,double mu_max,int nparm,int niter,int nout):
    
    cdef:
        list x_array,mu_array
        int i,j,k,jp
        int burnout
        double* mu= <double*>malloc((nparm+1)*sizeof(double))
        double* xi= <double*>malloc(nout*sizeof(double))
        double x0
        
    if not mu or not xi:
        raise MemoryError()
        
    burnout= niter - nout
    
    try:
        
        x_array=[]
        
        for i in range(nparm+1):
            mu[i]= mu_min+((<double>i)*(mu_max-mu_min))/nparm
        
        for i in range(nparm+1):
    
            x0= .5
            jp= 0
            
            for j in range(niter):
                
                x0= model(x0,mu[i])
                
                if j<burnout:
                    continue
    
                xi[jp]= x0
                jp+=1
                
            x_array+=[[xi[k] for k in range(nout)]]
            
        mu_array=[mu[i] for i in range(nparm+1)]
            
        return x_array,mu_array
    
    finally:
        
        free(mu)
        free(xi)
        
        
    