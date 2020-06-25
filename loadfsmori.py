#!/usr/bin/env python
# coding: utf-8

import numpy as np
import os.path
import matplotlib.pyplot as plt
from epics import caget, caput
import time


# load the FSM origin
# Elena Manjavacas IDL to Python transcription


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


