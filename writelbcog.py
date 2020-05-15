import numpy as np
import os.path
import matplotlib.pyplot as plt

def writelbcog(filename):
    path2lbcog='/local/kroot/rel/ao/qfix/data/Lbwfs/CentOrigins/'
    file = np.fromfile(path2lbcog+filename, dtype='f', offset=1)
    plt.plot(file)
    print(len(file))
    np.savetxt('new_'+filename, file)
    print('File '+ 'new_'+filename +' written')
