# XRR Data Combination and Plotting

This project combines XRR measurement data from multiple files, rescales the intensity values to account for the use of an attenuator, and plots the combined data.

## Requirements

- `pandas`
- `matplotlib`

## Installation

### Using `venv`

1. Create a virtual environment:
    ```sh
    python -m venv env
    ```

2. Activate the virtual environment:

    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Using `conda`

1. Create a conda environment:
    ```sh
    conda create --name xrr_env
    ```

2. Activate the conda environment:
    ```sh
    conda activate xrr_env
    ```

3. Install the required packages:
    ```sh
    conda install pandas matplotlib
    ```

## Usage

1. Place your XRR measurement data files in the data directory.
2. Create a scan_nums.txt file in the root directory, listing the scan numbers of the data files to be combined, one per line.
3. Run the main.py script:
    ```sh
    python main.py
    ```

The combined data will be saved as a CSV file, and the combined XRR measurement data will be plotted.

## License

This project is licensed under the MIT License.