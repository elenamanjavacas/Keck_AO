import numpy as np
import os.path
import matplotlib.pyplot as plt

# function to write cog files

def writecog(filename):
    path='/kroot/rel/ao/qfix/data/ControlParms/CentOrigin/'
    file = np.fromfile(filename, dtype='f', offset=1)
    plt.plot(file)
    np.savetxt('new_'+filename, file)
    print('File '+ 'new_'+filename +' written')
    
