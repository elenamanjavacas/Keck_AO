# Function to read the interaction matrix
# Rewritten for the NGWFC
# Marcos van Dam, April 2006
# Elena Manjavacas April 2020

import numpy as np
import os.path

def readimx(filename):
    H = np.zeros((349,608))
    path2imx='/kroot/rel/ao/qfix/data/ControlParms/SystemMatrix/'
    
    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print('File found? =',tmp)
    
    if tmp == False:
        tmp0 = path2imx+filename
        tmp = os.path.isfile(tmp0)
        print('File found in path '+path2imx+'? = ',tmp)
        if tmp == False:
            print('File '+filename+' not found, returning')
        else:
            fname = tmp0
            H = np.loadtxt(fname)
            np.savetxt(fname, H)
            print('File written in path '+ path2imx)
    else: 
        fname = tmp0
        H = np.loadtxt(fname)
        np.savetxt(fname, H)
        print('File '+ filename +' written')
