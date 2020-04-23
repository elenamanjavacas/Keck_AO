# Function to read the interaction matrix
# Rewritten for the NGWFC
# Marcos van Dam, April 2006

def readimx(filename):
    H = np.zeros((349,608))
    path2imx='/kroot/rel/ao/qfix/data/ControlParms/SystemMatrix/'

    tmp0 = filename
    tmp = os.path.isfile(tmp0)
    print('File found? =',tmp)

    if tmp == False:
        tmp0 = path2imx+filename
        tmp = os.path.isfile(tmp0)
        print('File found? =',tmp)
        if tmp == False:
            print('File '+filename+' not found, returning')

    else:
        fname = tmp0
        H = np.loadtxt(fname)
        np.savetxt(fname, H)
        print('File '+ filename +' written')
