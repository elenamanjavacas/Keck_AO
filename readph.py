# function to read the WYKO interferometer
# Marcos van Dam
# November 2005
# Elena Manjavacas, April 2020

import numpy as np
import os.path
import matplotlib.pyplot as plt

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
            phase = open(fname,'r').read()
            phase = np.array(phase.replace("\n", "").split()).astype(float)
            plt.plot(phase)
            print('File written in path '+ cdph)
            return phase
    else: 
        fname = tmp0
        phase = open(fname,'r').read()
        phase = np.array(phase.replace("\n", "").split()).astype(float)
        
        #print(phase)
        plt.plot(phase)
        #np.savetxt('new'+fname, phase)
        print('File '+ filename +' written')
        return phase
