# function to read cog files
# Marcos van Dam
# Modified March 2005 to use lun, rather than a fixed value
# Modified Sept 2006 for the NGWFC
# To python 3.0 Elena Manjavacas April 2020

import numpy as np
import os.path
import matplotlib.pyplot as plt

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
            offsets = np.fromfile(fname, dtype='f', offset=1)
            np.savetxt('new_'+fname, offsets)
            print('File written in path '+ cdcog)
            return offsets
    else: 
        fname = tmp0
        offsets = np.fromfile(fname, dtype='f', offset=1)
        plt.plot(offsets)
        np.savetxt('new_'+fname, offsets)
        print('File '+ filename +' written')
        return offsets
