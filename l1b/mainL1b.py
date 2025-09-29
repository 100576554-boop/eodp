
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\EODP_code\\eodp\\auxiliary'
indir = r"C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\EODP-TS-L1B\\input"
outdir = r"C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\MyOutputFALSE_EODP"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
