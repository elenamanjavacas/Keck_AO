#!/usr/bin/env python
# coding: utf-8

import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# Load a WFC configuration file and restore the AO system if possible
# Transcription IDL to Python 3 by Elena Manjavacas

def LOADCONFIG(configfn):
    
    failed = 0
    
    if len(configfn) != 1:
        print('Usage: LOADCONFIG, configfn')
    
    
    path2cfg='/kroot/rel/ao/qfix/data/ControlParms/ConfigFiles/'
    tmp = os.path.isfile(path2cfg+configfn)
    
    if tmp == False:
        print('Could not find a unique file ' + path2cfg+configfn)
        failed = 1
    
    
# load all the non-WFC parameters if they exist  

    idlfn = configfn.replace('.cft','.sav')
    
    tmp = os.path.isfile(path2cfg+idlfn)
    
    if tmp == True:
        print('Loading non-WFC parameters in '+path2cfg+idlfn)
        print('Restoring the WFS optics')
        
        status = caput('ao.obwnname',obwnname)
        status = caput('ao.obsdname',obsdname)
        
        if obpsxfs != caget('ao.obpsxfs'):
            status = caput('ao.obpsxfs',obpsxfs)
            print('No non-WFC parameters saved for this configuration')
    
# read wcoper so we can leave the system in its initial state  

    wcoper=caget('ao.wcoper')
    
    if statuswc != 0:
        print('Unable to read wcoper, returning')
 
    # SETWCOPER,0
                
    status = caput('ao.wcldcfgfn',configfn)  
    status = caput('ao.wcldcfg',1)

    print('Waiting until the WFC is configured before turning WFC on')
    time.sleep(3)
    
    wcldcfgd = caget('ao.wcldcfgd')
    counter = 0
    
    while wcldcfgd != 1:
        time.sleep(0.5)
        counter = counter + 1
        wcldcfgd = caget('ao.wcldcfgd')
        
        if counter == 100:
            print('Unable to load configuration file')
            print('Please try loading it again, setting the AO system manually or rebooting the WFC')
            print('Unable to load configuration file. Please try loading it again, setting the AO system manually or rebooting the WFC')
            
            failed = 1
            
    print('Configuration file '+configfn[0]+' loaded successfully')       
    
    if loadsavfile == 1:
        # continue to load the saved configuration
        # this keyword does not exist in the WFC
        status=caput('ao.wsfrrt',wsfrrt)
        
        # these file names are not saved by the WFC (only the values)     
        # note: we are not loading the files, just restoring the filenames   
        
        status=caput('ao.wscnorfn',wscnorfn)
        status=caput('ao.dmorfn',dmorfn)
        status=caput('ao.dmmrfn',dmmrfn)
        status=caput('ao.wsbkfn',wsbkfn)
        status=caput('ao.wsflfn',wsflfn)
  
     
        # restore the reconstructor angle so the reconstructor knows if it needs to trigger a new one     
        status=caput('ao.recanguse',recanguse)
        
    # Need to wait before setting wcoper back to 1. Otherwise, we will leave the wait in in case there is a future call to setwcoper
  
    print('WFC is configured.' )
    
    if wcoper == 1:
        #SETWCOPER,1
    

