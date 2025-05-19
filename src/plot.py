import pandas as pd
import matplotlib.pyplot as plt


def plot_xrr_data(df: pd.DataFrame) -> None:
    """
    Plot the combined XRR measurement data.

    Parameters:
    df (pd.DataFrame): The combined XRR measurement data.
    """
    _, ax = plt.subplots(1, 2, figsize=(12, 5))
    # Linear scale
    ax[0].set_title("Combined XRR Measurement Data")
    ax[0].set_xlabel("2θ [°]")
    ax[0].set_ylabel("Intensity [a.u.]")
    ax[0].plot(df["x"], df["y"], "-", markersize=3)
    ax[0].errorbar(
        df["x"], df["y"], yerr=df["error"], fmt=".", capsize=5, ecolor="black"
    )
    ax[0].set_yscale("linear")
    # log scale
    ax[1].set_title("Combined XRR Measurement Data (log scale)")
    ax[1].set_xlabel("2θ [°]")
    ax[1].set_ylabel("Intensity [a.u.]")
    ax[1].plot(df["x"], df["y"], "-", markersize=3)
    ax[1].errorbar(
        df["x"], df["y"], yerr=df["error"], fmt=".", capsize=5, ecolor="black"
    )
    ax[1].set_yscale("log")

    plt.show()
