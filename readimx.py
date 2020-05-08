# Function to read the interaction matrix
# Rewritten for the NGWFC
# Marcos van Dam, April 2006
# Elena Manjavacas April 2020

import numpy as np
import os.path
import matplotlib.pyplot as plt

def readimx(filename):
    path2imx='/kroot/rel/ao/qfix/data/ControlParms/SystemMatrix/'
    
    Hinv = np.zeros((349,608))
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
            H =  np.fromfile(fname, dtype='f', offset=1)
            H = np.insert(H,0,0)
            H = H.reshape((349,608))
            return H
            print(H,np.shape(H))
            np.savetxt(fname, H)
            print('File '+ 'new_'+fname +' written in path '+path2imx)
    else: 
        fname = tmp0
        H = np.fromfile(fname, dtype='f', offset=1)
        H = np.insert(H,0,0)
        H = H.reshape((349,608))
        return H
        plt.plot(H)
        np.savetxt('new_'+fname, H)
        print('File '+ 'new_'+fname +' written')
