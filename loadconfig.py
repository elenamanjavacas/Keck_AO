#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# In[2]:


#; Load a WFC configuration file and restore the AO system if possible
#;

#PRO LOADCONFIG, configfn, failed=failed
#  failed=0
  
#  IF N_ELEMENTS(configfn) NE 1 THEN BEGIN
#     MESSAGE,/INFO,'Usage: LOADCONFIG, configfn'
#     RETURN
#  ENDIF
  
#  path2cfg='/kroot/rel/ao/qfix/data/ControlParms/ConfigFiles/'
#  tmp=FINDFILE(path2cfg+configfn, count=count)
  
#  IF count NE 1 THEN BEGIN
#     MESSAGE,/INFO,'Could not find a unique file '+path2cfg+configfn
#     failed=1
#     RETURN
#  ENDIF
  
#                                ; load all the non-WFC parameters if they exist
#  configfnbase=STRSPLIT(configfn,'.cfg',/extract,/regex)
#  idlfn=configfnbase+'.sav'
#  tmp=FINDFILE(path2cfg+idlfn,count=loadsavfile)
#  IF loadsavfile EQ 1 THEN BEGIN
#     MESSAGE,/INFO,'Loading non-WFC parameters in '+path2cfg+idlfn
#     RESTORE,path2cfg+idlfn
#     MESSAGE,/INFO,'Restoring the WFS optics'
#     status=MODIFY('ao.obwnname',obwnname,/notrace)
#     status=MODIFY('ao.obsdname',obsdname,/notrace)     
#     IF obpsxfs NE SHOW('ao.obpsxfs',/notrace) THEN BEGIN        
#        status=MODIFY('ao.obpsxfs',obpsxfs,/notrace)
#        WFSCONFIG
#     ENDIF     
#  ENDIF ELSE MESSAGE,/INFO,'No non-WFC parameters saved for this configuration'
  
#; read wcoper so we can leave the system in its initial state  
#  wcoper=SHOW('ao.wcoper',error=errorwc, status=statuswc,/notrace)
  
#  IF statuswc NE 0 THEN BEGIN
#     MESSAGE,/INFO,'Unable to read wcoper, returning'
#     RETURN
#  ENDIF
    
#  SETWCOPER,0  
#  status=MODIFY('ao.wcldcfgfn',configfn,error=error,/notrace)
#  status=MODIFY('ao.wcldcfg',1,error=error,/notrace)
  
#  MESSAGE,/INFO,'Waiting until the WFC is configured before turning WFC on'
#  WAIT,3
  
#  wcldcfgd=SHOW('ao.wcldcfgd',error=error,status=status,/notrace,/nowait) 
#  counter=0
  
#  WHILE wcldcfgd NE 1 DO BEGIN
#     WAIT,0.5
#     counter=counter+1
#     wcldcfgd=SHOW('ao.wcldcfgd',error=error,status=status,/notrace,/nowait) 
     
#     IF counter EQ 100 THEN BEGIN
#        MESSAGE,/INFO,'Unable to load configuration file'
#        MESSAGE,/INFO,'Please try loading it again, setting the AO system manually or rebooting the WFC'
#        tmp=DIALOG_MESSAGE('Unable to load configuration file. Please try loading it again, setting the AO system manually or rebooting the WFC',/error)
#        failed=1
#        RETURN
#     ENDIF
#  ENDWHILE
  
#  MESSAGE,/INFO,'Configuration file '+configfn[0]+' loaded successfully'
  
#  IF loadsavfile EQ 1 THEN BEGIN
#; continue to load the saved configuration
     
#; this keyword does not exist in the WFC     
#     status=MODIFY('ao.wsfrrt',wsfrrt,/notrace)
#; these file names are not saved by the WFC (only the values)     
#; note: we are not loading the files, just restoring the filenames     
#     status=MODIFY('ao.wscnorfn',wscnorfn,/notrace)
#     status=MODIFY('ao.dmorfn',dmorfn,/notrace)
#     status=MODIFY('ao.dmmrfn',dmmrfn,/notrace)
#     status=MODIFY('ao.wsbkfn',wsbkfn,/notrace)
#     status=MODIFY('ao.wsflfn',wsflfn,/notrace)
     
#; restore the reconstructor angle so the reconstructor knows if it needs to trigger a new one     
#     status=MODIFY('ao.recanguse',recanguse,/notrace)
#  ENDIF
  
#; Need to wait before setting wcoper back to 1. Otherwise, we will leave the wait in in case there is a future call to setwcoper
  
#  MESSAGE,/INFO,'WFC is configured.'  
#  IF wcoper EQ 1 THEN SETWCOPER,1
#END
  
  


# In[9]:


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
    

