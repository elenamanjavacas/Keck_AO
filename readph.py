# function to read the WYKO interferometer
# Marcos van Dam
# November 2005
# Elena Manjavacas, April 2020

import numpy as np
import os.path

def readph(filename):
    cdph = '/kroot/rel/ao/qfix/data/'
    phase = np.zeros(349)

    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print('File found? =',tmp)

    if tmp == False:
        tmp0 = cdph+filename
        tmp = os.path.isfile(tmp0)
        print('File found in path ' +cdph+'? =',tmp)
        if tmp == False:
            print('File '+filename+' not found, returning')
        else:
            fname = tmp0
            phase = np.loadtxt(fname)
            np.savetxt(fname, phase)
            print('File written in path '+ cdph)

    else:
        fname = tmp0
        phase = np.loadtxt(fname)
        np.savetxt(fname, phase)
        print('File '+ filename +' written')
