import numpy as np
import os.path
import matplotlib.pyplot as plt

def writemr(filename):
    path2mrfn='/kroot/rel/ao/qfix/data/ControlParms/Recon/'
    file = np.fromfile(path2mrfn+filename, dtype='f', offset=1)
    plt.plot(file)
    np.savetxt('new_'+filename, file)
    print('File '+ 'new_'+filename +' written')
