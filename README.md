# XRR Data Combination and Plotting

This project combines XRR measurement data from multiple files, rescales the intensity values to account for the use of an attenuator, and plots the combined data.

## Requirements

- `requirements.txt` file for `venv` setup

## Installation

### Using `venv`

1. Create a virtual environment:
    ```
    python -m venv .venv
    ```

2. Activate the virtual environment:

    - On Windows:
        ```
        .\.venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source .venv/bin/activate
        ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

### Using `conda`

1. Create a conda environment:
    ```
    conda create --name xrr_env
    ```

2. Activate the conda environment:
    ```
    conda activate xrr_env
    ```

3. Install the required packages:
    ```
    conda install pandas matplotlib
    ```

## Usage

1. Place your XRR measurement data files in the data directory.
2. Create a scan_nums.txt file in the root directory, listing the scan numbers of the data files to be combined, one per line.
3. Run the main.py script:

   - **Using Command Line (Recommended for all OS):**
     Make sure your virtual environment (venv or conda) is activated, then run:
     ```
     python main.py
     ```

   - **Using Batch Script (For Windows Users):**
     A batch script (`run_script.bat`) is provided for convenience. This script automatically handles virtual environment creation (if needed), dependency installation from `requirements.txt`, activation, and running the main script.
     Simply double-click the `run_script.bat` file located in the project root directory. Ensure `requirements.txt` exists if you rely on the automatic setup.

The combined data will be saved as a CSV file, and the combined XRR measurement data will be plotted.

## License

This project is licensed under the MIT License.