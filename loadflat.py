#!/usr/bin/env python
# coding: utf-8

# In[1]:


#; load a flat file
#PRO LOADFLAT,filename,flatlderr=flatlderr
#  COMPILE_OPT idl2

#  tmp=MODIFY('ao.wsflfn',filename,status=status,error=error)
#  tmp=MODIFY('ao.wsflfd',1,status=status,error=error) 
  
#  waittime=1.
#  max_iterations=10
#  iterations=0
#  WAIT,waittime
#  flatlderr=SHOW('ao.wsflfder',error=error,status=status)
  
#  WHILE flatlderr NE 'Load Done' DO BEGIN
#     iterations=iterations+1
#     WAIT,waittime
#     flatlderr=SHOW('ao.wsflfder',error=error,status=status)
#     if iterations EQ max_iterations THEN RETURN
#  ENDWHILE
  
#END


# In[4]:


import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# In[6]:


# load a flat file
# Elena Manjavacas based on Marcos van Dam IDL scripts

def loadcog(filename):
    
    tmp = caput('ao.wsbkfn', filename)
    tmp = caput('ao.wsbkfd', 1)
    
    waittime=1.
    max_iterations=10
    iterations=0
    
    time.sleep(waittime)
    
    flatlderr = caput('ao.wsflfder')
    
    while flatlderr != 'Load Done':
        iterations = iterations + 1
        time.sleep(waittime)
        flatlderr = caput('ao.wsflfder')
        
        if iterations == max_iterations:
            print('Your reached the max number of iterations')
        else:
            print('flatlderr')
            return flatlderr


# In[ ]:




