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

    diff_rel = np.abs((toa - toa_out) / toa_out) * 100  # % difference

    # check values under threshold
    verify = diff_rel < threshold_percent
    percent_check = np.sum(verify) / verify.size * 100 #it could be used also a mean value of the difference and considering
    # the std deviation, evaluating the 3sigma of the values, but to be more precise I choose to check each value (not good for big matrix)

    print(f"{filename}: {percent_check:.2f}% of values has difference < {threshold_percent}%")

    if percent_check >= 99.7:
        print("✅ PASS: at least 3_sigma of values have differences under threshold\n")
    else:
        print("❌ FAIL\n")


def plot_comparison(dir1, dir2, file1, file2,label1="File1", label2="File2", title=None):

    """
    Compare two TOA files along the central ALT line.
    """
    # Reading
    toa1 = readToa(dir1, file1)
    toa2 = readToa(dir2, file2)

    print(f"{file1} shape: {toa1.shape}")
    print(f"{file2} shape: {toa2.shape}")

    # Central ALT line
    center_row1 = toa1.shape[0] // 2
    center_row2 = toa2.shape[0] // 2

    line1 = toa1[center_row1, :]
    line2 = toa2[center_row2, :]

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(line1, label=label1, color='k', linewidth=1)
    plt.plot(line2, label=label2, color='red', linewidth=1)
    plt.xlabel("ACT_columns")
    plt.ylabel("TOA")
    plt.grid(True)
    plt.legend()
    plt.title(title if title else f"Compare TOA: {file2}")
    plt.show()

# --- Folders ---
isrf_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\EODP-TS-ISM\output"
myout_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputs_EODP"
out_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\EODP-TS-L1B\output"
noeq_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputFALSE_EODP"

# --- Loop comparing values ---
for i in range(4):
    filename = f"l1b_toa_VNIR-{i}.nc"
    check_toa_difference(myout_dir, out_dir, filename)

# Loop 1: ISRF vs MyOutputs
for i in range(4):
    file_isrf = f"ism_toa_isrf_VNIR-{i}.nc"
    file_mine = f"l1b_toa_VNIR-{i}.nc"
    plot_comparison(isrf_dir, myout_dir, file_isrf, file_mine,label1="ism_toa_isrf", label2="l1b_toa",title=f"Compare TOA (central ALT) VNIR-{i}")

# Loop 2: NoEq vs MyOutputs
for i in range(4):
    file_noeq = f"l1b_toa_VNIR-{i}.nc"
    file_mine = f"l1b_toa_VNIR-{i}.nc"
    plot_comparison(noeq_dir, myout_dir, file_noeq, file_mine,label1="no_eq", label2="eq",title=f"(EQ=FALSE) Compare TOA VNIR-{i}")



