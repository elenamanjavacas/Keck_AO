#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# In[6]:


# load a background file into the WFC
# Elena Manjavacas based on Marcos van Dam IDL scripts

def loadcog(filename):
    
    tmp = caput('ao.wsbkfn', filename)
    tmp = caput('ao.wsbkfd', 1)
    
    waittime=1.
    max_iterations=10
    iterations=0
    
    time.sleep(waittime)
    
    bkgndlderr = caput('ao.wsbkfder')
    
    while bkgndlderr != 'Load Done':
        iterations = iterations + 1
        time.sleep(waittime)
        bkgndlderr = caput('ao.wsbkfder')
        
        if iterations == max_iterations:
            print('Your reached the max number of iterations')
        else:
            print('bkgndlderr')
            return bkgndlderr
        

