# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:40:42 2020

@author: jauff
"""

import sys
import matplotlib.pyplot as plt
from time import perf_counter
from BifurcationPy import Py_logistic,Py_sine_model,Py_quartic_model,Py_tent_model,Py_RunManager
from BifurcationCy import Cy_logistic,Cy_sine_model,Cy_quartic_model,Cy_tent_model,Cy_RunManager

##################
# Default Values
##################

mu_points_d=      1000
n_iterations_d=   10000
n_xpoints_d=      100

py_models=[Py_logistic,Py_sine_model,Py_quartic_model,Py_tent_model]
cy_models=[Cy_logistic,Cy_sine_model,Cy_quartic_model,Cy_tent_model]
model_names=['Logistic','Sine','Quartic','Tent']

mu_param=[(2.5,4.),(.3,1.),(0.8,64./63.),(0.46,1.)]


if __name__=='__main__':
    
    try:
        mu_points=      int(sys.argv[1])
        n_iterations=   int(sys.argv[2])
        n_xpoints=      int(sys.argv[3])
        
        if mu_points<=0 or n_iterations<=0 or n_xpoints<=0:
            raise ValueError
        
    except (ValueError,IndexError):
        print('Usage python BifurcationTest.py (#points in x axis) (#iterations) (#points y axis)')
        print('\nUsing default values.')
        
        mu_points=      mu_points_d
        n_iterations=   n_iterations_d
        n_xpoints=      n_xpoints_d
    
    
    ################
    # Python
    ################
    
    py_mu_out= []
    py_xa_out= []
    py_tcount= []
    
    for i,model in enumerate(py_models):
        
        t0= perf_counter()
        
        x,mu= Py_RunManager(model,mu_param[i][0],mu_param[i][1],mu_points,n_iterations,n_xpoints)
        
        t1= perf_counter()
        
        py_tcount+=[t1-t0]
        
        py_xa_out+=[x]
        py_mu_out+=[mu]
     
        
    ################
    # Cython
    ################
        
    cy_mu_out= []
    cy_xa_out= []
    cy_tcount= []
    
    for i,modelc in enumerate(cy_models):
        
        t2= perf_counter()
        
        x,mu= Cy_RunManager(modelc,mu_param[i][0],mu_param[i][1],mu_points,n_iterations,n_xpoints)
        
        t3= perf_counter()
        
        cy_tcount+=[t3-t2]
        
        cy_xa_out+=[x]
        cy_mu_out+=[mu]
        
    ####################
    # Report
    ####################
        

    avg_sav=0.
    
    for h,mname in enumerate(model_names):
        
        sout=   mname+'\t\tPyhon Time %.2f'%py_tcount[h]+'s'
        sout+=  '\t\tCython Time %.2f'%cy_tcount[h]+'s'
        
        saving= 100.*(1.-cy_tcount[h]/py_tcount[h])
        avg_sav+= saving
        
        sout+= '\tSaving %.2f'%saving+'%'
        
        print(sout)
        
    avg_sav/=4.
        
    print('Average savings %.2f'%avg_sav+'%')
            
    #############################
    # Figure
    ############################
    
    fig=plt.figure(1)
        
    iplt= 421
    
    for k,mname in enumerate(model_names):
        
        plt.subplot(iplt+2*k)
        
        plt.title('Python '+mname)
        
        for j in range(mu_points):
            
            muv= [py_mu_out[k][j] for i in range(n_xpoints)]
            
            plt.scatter(muv,py_xa_out[k][j],marker=".",c='k',s=(72./fig.dpi)**2)
            
        plt.subplot(iplt+2*k+1)
        
        plt.title('Cython '+mname)
        
        for j in range(mu_points):
            
            muc= [cy_mu_out[k][j] for i in range(n_xpoints)]
            
            plt.scatter(muc,cy_xa_out[k][j],marker=".",c='k',s=(72./fig.dpi)**2)
   
    plt.show()
        
        
        
        
        
        
    
        
    
    
    