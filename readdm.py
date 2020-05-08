# function to read dm origin files
# Marcos van Dam
# Elena Manjavacas, April 2020

import numpy as np
import os.path
from astropy.io import ascii


def readdm(filename):
    dmorigin = np.zeros(349)
    cddm = '/kroot/rel/ao/qfix/data/ControlParms/MirrorOrigin/'
    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print(tmp)
    if tmp == False:
        tmp0 = cddm+filename
        tmp = os.path.isfile(tmp0)
        print('File found in path '+cddm+'? =' ,tmp)
        
        if tmp == False:
            print('File '+filename+' not found, returning')
            return dmorigin
        else:
            fname = tmp0
            dmorigin =  np.fromfile(fname, dtype='f', offset=0)
            print(dmorigin)
            np.savetxt(fname, dmorigin)
            print('File written in path '+cddm)
            return dmorigin
    else: 
        fname = tmp0
        dmorigin =  np.fromfile(fname, dtype='f', offset=1)
        np.savetxt('new'+fname, dmorigin)
        print('File written')
        return dmorigin
