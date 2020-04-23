import os.path
import numpy as np

# function to read dm origin files
# Marcos van Dam

def readdm(filename):
    dmorigin = np.zeros(349)
    cddm = '/kroot/rel/ao/qfix/data/ControlParms/MirrorOrigin/'
    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print(tmp)
    if tmp == False:
        tmp0 = cddm+filename
        tmp = os.path.isfile(tmp0)
        print('File found? = ',tmp)
        if tmp == False:
            print('File '+filename+' not found, returning')

    else:
        fname = tmp0
        dmorigin = np.loadtxt(fname)
        np.savetxt(fname, dmorigin)
        print(dmorigin)
        print('File written')
