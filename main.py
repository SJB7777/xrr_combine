import os

import matplotlib.pyplot as plt
import pandas as pd

from src.xrr_combine import combine_xrr_measurements, read_data


def plot_xrr_data(df: pd.DataFrame) -> None:
    """
    Plot the combined XRR measurement data.

    Parameters:
    df (pd.DataFrame): The combined XRR measurement data.
    """
    _, ax = plt.subplots(1, 2, figsize=(12, 5))
    # Linear scale
    ax[0].set_title('Combined XRR Measurement Data')
    ax[0].set_xlabel('2θ [°]')
    ax[0].set_ylabel('Intensity [a.u.]')
    ax[0].plot(df['x'], df['y'], '-', markersize=3)
    ax[0].errorbar(df['x'], df['y'], yerr=df['error'], fmt='.', capsize=5, ecolor='black')
    ax[0].set_yscale('linear')
    # log scale
    ax[1].set_title('Combined XRR Measurement Data (log scale)')
    ax[1].set_xlabel('2θ [°]')
    ax[1].set_ylabel('Intensity [a.u.]')
    ax[1].plot(df['x'], df['y'], '-', markersize=3)
    ax[1].errorbar(df['x'], df['y'], yerr=df['error'], fmt='.', capsize=5, ecolor='black')
    ax[1].set_yscale('log')

    plt.show()


def main() -> None:
    root: str = '.\\data'
    with open('scan_nums.txt', 'r', encoding='utf-8') as f:
        scan_nums = list(map(int, filter(str.strip, f)))
    file_names = [os.path.join(root, f'{num}.dat') for num in scan_nums]
    datalist = [read_data(filename) for filename in file_names]

    result_df = combine_xrr_measurements(datalist)
    new_data_name = f"combined_data_{'_'.join(map(str, scan_nums))}.csv"
    result_df.to_csv(new_data_name, sep=',', header=False, index=False)

    plot_xrr_data(result_df)



if __name__ == '__main__':
    main()
