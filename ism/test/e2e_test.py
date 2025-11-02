from common.io.writeToa import writeToa, readToa
import numpy as np
import os
import matplotlib.pyplot as plt


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
myout_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputs_ISM1_EODP"
l1b_dir = r"C:\Users\ciroa\Desktop\UNI\Erasmus\EODP\MyOutputL1B_16_10_EODP"

# --- Loop comparing values ---
for i in range(4):
    file_isrf = f"ism_toa_isrf_VNIR-{i}.nc"
    file_l1b = f"l1b_toa_VNIR-{i}.nc"
    plot_comparison(l1b_dir, myout_dir, file_l1b, file_isrf, label2="ism_toa_isrf", label1="l1b_toa",
                title=f"Compare TOA VNIR-{i}")


