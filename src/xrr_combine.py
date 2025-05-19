import pandas as pd


def combine_xrr_measurements(datalist: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Combine XRR measurement dataframes by rescaling the intensity values to account for the use of an attenuator.

    The function assumes that the first dataframe in the list is measured with a strong attenuator and subsequent
    dataframes are measured with weaker or no attenuator. The intensity values are rescaled such that the transition
    between dataframes is smooth. The rescaling is done by adjusting the intensity values of each dataframe so that
    the last intensity value of the current dataframe matches the first intensity value of the next dataframe.

    Parameters:
    datalist (list[pd.DataFrame]): List of dataframes containing XRR measurement data. Each dataframe should have
        columns ["x", "y", "error"] where "x" is the angle, "y" is the intensity, and "error" is the measurement error.

    Returns:
    pd.DataFrame: A single dataframe with combined and rescaled XRR measurement data.
    """
    if not datalist:
        return pd.DataFrame()

    # Reverse and copy the order of the dataframes
    datalist = [data.copy() for data in datalist[::-1]]

    head_value = datalist[0].iloc[0, 1]
    new_datalist = [datalist[0]]

    for data in datalist[1:]:
        rescale_factor = head_value / data.iloc[-1, 1]
        data[["y", "error"]] = data[["y", "error"]] * rescale_factor
        data.drop(index=data.index[-1], inplace=True)
        head_value = data.iloc[0, 1]
        new_datalist.append(data)

    new_datalist.reverse()
    return pd.concat(new_datalist, ignore_index=True)


def read_data(filename: str) -> pd.DataFrame:
    """
    Read XRR measurement data from a file.

    Parameters:
    filename (str): The path to the file containing XRR measurement data.

    Returns:
    pd.DataFrame: A dataframe containing the XRR measurement data with columns ["x", "y", "error"].
    """
    return pd.read_csv(filename, sep="\\s+", header=None, names=["x", "y", "error"])


if __name__ == "__main__":
    # Example data
    data1 = pd.DataFrame(
        {
            "x": [0.1, 0.2, 0.3, 0.4],
            "y": [400, 300, 200, 100],
            "error": [40, 30, 20, 10],
        }
    )

    data2 = pd.DataFrame(
        {"x": [0.5, 0.6, 0.7, 0.8], "y": [320, 240, 160, 80], "error": [32, 24, 16, 8]}
    )

    data3 = pd.DataFrame(
        {"x": [0.9, 1.0, 1.1, 1.2], "y": [280, 210, 140, 70], "error": [28, 21, 14, 7]}
    )

    # Combine the dataframes
    combined_df = combine_xrr_measurements([data1, data2, data3])

    # Print the combined dataframe
    print(combined_df)
