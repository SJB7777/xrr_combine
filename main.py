from pathlib import Path

from src.xrr_combine import combine_xrr_measurements, read_data
from src.plot import plot_xrr_data


def main() -> None:
    root: Path = Path("./data")
    save_dir: Path = Path("./results")
    save_dir.mkdir(exist_ok=True, parents=True)

    with open("scan_nums.txt", "r", encoding="utf-8") as f:
        scan_nums = list(map(int, filter(str.strip, f)))
    file_names = [root / f"{num}.dat" for num in scan_nums]
    datalist = [read_data(filename) for filename in file_names]

    result_df = combine_xrr_measurements(datalist)
    new_data_name = f"comb_{'_'.join(map(str, scan_nums))}.csv"
    result_df.to_csv(save_dir / new_data_name, sep=",", header=False, index=False)

    plot_xrr_data(result_df)


if __name__ == "__main__":
    main()
