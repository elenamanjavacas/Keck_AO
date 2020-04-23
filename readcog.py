# function to read cog files
# Marcos van Dam
# Modified March 2005 to use lun, rather than a fixed value
# Modified Sept 2006 for the NGWFC
# To python 3.0 Elena Manjavacas April 2020

import numpy as np
import os.path

def readcog(filename):
    offsets = np.zeros(608)
    cdcog='/local/kroot/rel/ao/qfix/data/ControlParms/CentOrigin/'

    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print('File found? =',tmp)

    if tmp == False:
        tmp0 = cdcog+filename
        tmp = os.path.isfile(tmp0)
        print('File found in path '+cdcog+'? = ' ,tmp)

        if tmp == False:
            print('File '+filename+' not found, returning')

        else:
            fname = tmp0
            offsets = np.loadtxt(fname)
            np.savetxt(fname, offsets)
            print('File written in path '+ cdcog)

    else:
        fname = tmp0
        offsets = np.loadtxt(fname)
        np.savetxt(fname, offsets)
        print('File '+ filename +' written')
