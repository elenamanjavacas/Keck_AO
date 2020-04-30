# function to read the zipped and unzipped reconstructor files
#
# Marcos van Dam
# Modified DLM: 31 January 2005, removed hard links to ulua
# Modified MvD: 08 February 2005, now reads .gz files even if extension is not explicit in the filename
# Modified MvD: for use with the NGWFC
# Modified Elena Manjavacas, April 2020
#
# Usage hinv=readmr('31Aug_B145.mr',actsubs=actsubs)
# reads 31Aug_B145.mr or 31Aug_B145.mr.gz

import numpy as np
import os.path
import gzip

def readmr(filename):
    actsubs = bytearray(304)
    Hinv = np.zeros((608,352))

    path2mr='/kroot/rel/ao/qfix/data/ControlParms/Recon/'

    tmp0 = filename
    print(tmp0)
    tmp = os.path.isfile(tmp0)
    print(tmp)

    if tmp == False:
        tmp0 = path2mr+filename
        tmp = os.path.isfile(tmp0)
        print('File found in path '+path2mr+'? =' ,tmp)

        if tmp == False:
            tmp0 = path2mr+filename+'.gz'
            tmp = os.path.isfile(tmp0)

            if tmp == False:
                print('File '+filename+' not found, returning')

            else:
                fname = tmp0
                with gzip.open(fname, 'rt') as f:
                    Hinv = np.array(f.read())
                    np.savetxt(fname, Hinv)
                    print(Hinv)
                    print('File '+ filename +' written in path: '+path2mr)

    else:
        fname = tmp0

        if fname.endswith('.gz') == True:
            with gzip.open(fname, 'rt') as f:
                Hinv = np.array(f.read())
                print(Hinv)
                #np.savetxt(fname, Hinv)
                #print('File '+ filename +' written')
        else:

            fname = tmp0
            Hinv = np.loadtxt(fname)
            np.savetxt(fname, Hinv)
            print(Hinv)
            print('File '+ filename +' written')
