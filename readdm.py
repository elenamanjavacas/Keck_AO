import os.path
import numpy as np

# function to read dm origin files
# Marcos van Dam
# Elena Manjavacas April 2020


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
        else:
            fname = tmp0
            dmorigin = np.loadtxt(fname)
            np.savetxt(fname, dmorigin)
            print(dmorigin)
            print('File written in path '+cddm)
            
    else: 
        fname = tmp0
        dmorigin = np.loadtxt(fname)
        np.savetxt(fname, dmorigin)
        print(dmorigin)
        print('File written')
