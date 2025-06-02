"""
Some Helpers for data parsing
"""

import kagglehub
import pathlib
import numpy as np
import csv

def get_csv_files(name: str="uciml/pima-indians-diabetes-database") -> list[str]:
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
        with open(file, "r") as f:
            csvFile = csv.reader(f)
            for line in csvFile:
                file_arr.append(list(line))
        out.append(np.array(file_arr))
    if len(out) == 1:
        return out[0]
    else:
        return out

def get_data(name: str="uciml/pima-indians-diabetes-database") -> list[np.ndarray] | np.ndarray:
    """
    Read in a kaggle dataset into numpy arrays
    """
    return read_csv_files(get_csv_files(name))

