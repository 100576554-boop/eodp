
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\EODP_code\\eodp\\auxiliary'
indir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\EODP-TS-ISM\input\gradient_alt100_act150" #small scene
outdir = r"C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\MyOutputs_ISM_EODP"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
