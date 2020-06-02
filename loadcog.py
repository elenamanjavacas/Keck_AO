#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput


# In[5]:


# load a cog file into the WFC
# Marcos van Dam
# Elena Manjavacas

def loadcog(save_fn):
    print('File to be loaded is: '+save_fn)
    path='/kroot/rel/ao/qfix/data/ControlParms/CentOrigin/'
    tmp = os.path.isfile(path+save_fn)
    
    if tmp == False:
        print('Cog file '+save_fn+' does not exist')
    
    else:
        tmp = caput('ao.WSCNORFN', save_fn, wait=true)
        tmp = caput('ao.WSCNORFD', 1, save_fn)


# In[ ]:




