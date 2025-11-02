from common.io.writeToa import writeToa, readToa
import numpy as np
import os
import matplotlib.pyplot as plt


def check_toa_difference(myout_dir, out_dir, filename, threshold_percent=0.01):
    """
    Compare TOA_MyOutputs with TOA_output and looks if the difference < 0.01% for at least 3sigma (99.7%) of values.
    """
    toa = readToa(myout_dir, os.path.join(myout_dir, filename))
    toa_out = readToa(out_dir, os.path.join(out_dir, filename))

    # Compute relative difference (avoid division by zero)
    diff_rel = np.zeros_like(toa_out)
    #diff_rel = np.abs((toa - toa_out) / np.maximum(np.abs(toa_out), 1e-12))
    #diff_rel = np.abs((toa - toa_out) / toa_out) * 100  # % difference
    mask = toa_out != 0
    diff_rel[mask] = np.abs((toa[mask] - toa_out[mask]) / toa_out[mask]) * 100

    # check values under threshold
    verify = diff_rel < threshold_percent
    percent_check = np.sum(verify) / verify.size * 100 #it could be used also a mean value of the difference and considering
    # the std deviation, evaluating the 3sigma of the values, but to be more precise I choose to check each value (not good for big matrix)

    print(f"{filename}: {percent_check:.2f}% of values has difference < {threshold_percent}%")

    if percent_check >= 99.7:
        print("✅ PASS: at least 3_sigma of values have differences under threshold\n")
    else:
        print("❌ FAIL\n")


# --- Folders ---
myout_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputs_ISM_EODP"
out_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\EODP-TS-ISM\output"

# --- Loop comparing values ---
for i in range(4):
    filename = f"ism_toa_isrf_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_optical_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_detection_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_prnu_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_e_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_ds_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

for i in range(4):
    filename = f"ism_toa_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

