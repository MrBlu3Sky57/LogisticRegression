# Parser

import kagglehub
import numpy as np
import pathlib
import csv

# Process data
def get_csv_files(name) -> list[str]:
    """ Get the csv files in path object returned by the kaggle dataset given by name
    """
    path = kagglehub.dataset_download(name)
    file_path = pathlib.Path(path)
    return [file for file in file_path.glob("*.csv")]

def read_csv_files(files: list[str]) -> list[np.ndarray] | np.ndarray:
    """
    Read a list of csv files into a list of numpy arrays
    """
    out = []
    for file in files:
        file_arr = []
        with open(file, "r", encoding="UTF8") as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                file_arr.append(list(line))
        out.append(np.array(file_arr))
    if len(out) == 1:
        return out[0]
    return out

def get_data(name) -> list[np.ndarray] | np.ndarray:
    """
    Read in a kaggle dataset into numpy arrays
    """
    return read_csv_files(get_csv_files(name))