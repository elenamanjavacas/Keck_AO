#!/usr/bin/env python
# coding: utf-8

import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time

# load a reconstructor into the WFC
# tries to load the reconstructor for 10s and returns if it fails
# Marcos van Dam
# Translation from IDL to Python 3 Elena Manjavacas

def loadmr(save_fn):
    
    waittime=1.
    max_iterations=10
    iterations=0
    
# check that the file exists

    path='/kroot/rel/ao/qfix/data/ControlParms/Recon/'
    
    tmp0 = save_fm
    tmp = os.path.isfile(path+tmp0)
    print(tmp)
    
    if tmp == False:
        print('File '+save_fn+' does not exist')
    
    status=caput('ao.DMMRFN',save_fn)
    time.sleep(0.2)
    dmmrfn=caget('ao.dmmrfn')
    
    while dmmrfn[0] !=  save_fn:
        print('reloading')
        status=caput('ao.DMMRFN',save_fn)
        time.sleep(0.2)
        dmmrfn=caget('ao.dmmrfn')
        
    tmp = caput('ao.DMMRFD',1)
    print('Loading reconstructor')
    
    time.sleep(waittime)
    errormsg=caget('ao.DMMRFDER') 
    

    while errormsg != 'Load Done':
        iterations=iterations+1
        if errormsg == 'MGAOS param write failed':
            tmp=caput('ao.DMMRFD',1)
        
        time.sleep(waittime)
        errormsg=caget('ao.DMMRFDER')
        
        if iterations == max_iterations:
            print('Reconstructor file load failed')
            
    print('Reconstructor file load successful')
        
