import numpy as np
import os.path
import matplotlib.pyplot as plt

# To run writedm include the file name as first input, and the path to the dm file as second input. 
# If the dm file is in the current directory, then include write ''.

def writedm(filename, path2dm):
    if path2dm == 'path':
        cddm='/kroot/rel/ao/qfix/data/ControlParms/MirrorOrigin/'
        file = np.fromfile(cddm+filename, dtype='f', offset=1)
        plt.plot(file)
        np.savetxt('new_'+filename, file)
        print('File '+ 'new_'+filename +' written')
    else:
        file = np.fromfile(filename, dtype='f', offset=1)
        plt.plot(file)
        np.savetxt('new_'+filename, file)
        print('File '+ 'new_'+filename +' written')
