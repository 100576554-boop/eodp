from l1b.src.initL1b import initL1b
from common.io.writeToa import writeToa, readToa
from common.src.auxFunc import getIndexBand
from common.io.readFactor import readFactor, EQ_MULT, EQ_ADD, NC_EXT
import numpy as np
import os
import matplotlib.pyplot as plt


def check_toa_difference(ref_dir, out_dir, filename, threshold_percent=0.01):
    """
    Confronta un file TOA di riferimento con un file di output.
    """
    toa = readToa(r"C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\MyOutputs_EODP", os.path.join(ref_dir, filename))
    toa_out = readToa(r"C:\\Users\\ciroa\\Desktop\\UNI\\Erasmus\\EODP\\EODP-TS-L1B\\output", os.path.join(out_dir, filename))


    diff_rel = np.abs((toa - toa_out) / (toa_out + 1e-12)) * 100

    mean_diff = np.mean(diff_rel)
    std_diff = np.std(diff_rel)
    threshold_3sigma = mean_diff + 3 * std_diff

    print(f"{filename}: Media={mean_diff:.6f}%, Std={std_diff:.6f}%, 3σ={threshold_3sigma:.6f}%")

    if threshold_3sigma < threshold_percent:
        print(f"✅ Pass: difference < {threshold_percent}% entro 3σ\n")
    else:
        print(f"❌ Fail: too high difference\n")


# --- Folders ---
ref_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputs_EODP"
out_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\EODP-TS-L1B\output"

# --- Cicle on the file ---
for i in range(4):
    filename = f"l1b_toa_VNIR-{i}.nc"
    check_toa_difference(ref_dir, out_dir, filename)
