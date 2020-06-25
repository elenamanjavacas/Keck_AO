#!/usr/bin/env python
# coding: utf-8

# In[1]:


#@kidl
#; load the FSM origin
#pro loadfsmori
#  message, /info, ' Reading /kroot/rel/ao/qfix/data/fsm_origin.dat'
#  fxpos0 = 0.0
#  fypos0 = 0.0
#  pxpos0 = 0.0
#  pypos0 = 0.0
#  openr,lun,'/kroot/rel/ao/qfix/data/fsm_origin.dat',/get_lun
#  readf,lun,fxpos0,fypos0,pxpos0,pypos0
#  free_lun,lun
#  message, /info, ' Setting FSM origins for pupil and field'
#  temp=modify('ao.obfmximo',fxpos0/1000.)
#  temp=modify('ao.obfmyimo',fypos0/1000.)
#  temp=modify('ao.obfmxpuo',pxpos0)
#  temp=modify('ao.obfmypuo',pypos0)
#  fmt='$(f8.4)'
#  print, 'Current values: '
#  print, 'Field x: '+string(show("ao.obfmximo")*1000,format=fmt)
#  print, 'Field y: '+string(show("ao.obfmyimo")*1000,format=fmt)
#  print, 'Pupil x: '+string(show("ao.obfmxpuo"),format=fmt)
#  print, 'Pupil y: '+string(show("ao.obfmypuo"),format=fmt)
#  message, /info, '.. done'
  
#; trigger an FSM move
#  status=modify('ao.obfmgoim',1,error=error,/notrace)
#end


# In[2]:


import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# In[3]:


# load the FSM origin
# Elena Manjavacas IDL to Python transcription


# In[1]:


def loadfsmori(filename):
    print('Reading /kroot/rel/ao/qfix/data/fsm_origin.dat')
    fxpos0 = 0.0
    fypos0 = 0.0
    pxpos0 = 0.0
    pypos0 = 0.0

   
    pos0 = np.fromfile('/kroot/rel/ao/qfix/data/fsm_origin.dat', dtype='f', offset=1)
    fxpos0 = pos0[:,0]
    fypos0 = pos0[:,1]
    pxpos0 = pos0[:,2]
    pypos0 = pos0[:,3]
    
    print(' Setting FSM origins for pupil and field')
    
    temp=caput('ao.obfmximo',fxpos0/1000.)
    temp=caput('ao.obfmyimo',fypos0/1000.)
    temp=caput('ao.obfmxpuo',pxpos0)
    temp=caput('ao.obfmypuo',pypos0)
    
    print( 'Current values: ')
    print, 'Field x: '+caget("ao.obfmximo")*1000
    print, 'Field y: '+caget("ao.obfmyimo")*1000
    print, 'Pupil x: '+caget("ao.obfmxpuo")
    print, 'Pupil y: '+caget("ao.obfmypuo")
    
    print('.. done')
    
    
#   trigger an FSM move
    status=caput('ao.obfmgoim',1)  


# In[ ]:




