"""
Main script for running all data processing and plotting.
    {Depenancies}: scipy, matplotlib, numpy, pandas
"""
# IMPORTS
#####################
# Dependancies
from scipy import io
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

# Custom Functions/libraies
from graphing import *
from analysis import *

# DEFINITIONS
########################

skip_rows = 22

sample_dimensions = { 'B1': {'width': 14.887, 'thickness': 3.203},
                      'B2': {'width': 14.893, 'thickness': 3.177},
                      'B3': {'width': 15.023, 'thickness': 3.143},
                      'B4': {'width': 15.070, 'thickness': 3.373},
                      'B5': {'width': 14.997, 'thickness': 3.300}}




for test_num in range(1,6):

    # for reading to pd df
    file_path = "Data\Labview Data\B" + str(test_num) + ".txt"

    print("=========================================")
    print("Loading Data for Sample #" + str(test_num) + "...")
    # print("=========================================")

    # LOADING TEST DATA
    ##############################
    raw_data = pd.read_csv(file_path, skiprows=skip_rows, sep = '\t')

  
    # PROCESSING DATA
    ########################
    print("=========================================")
    print("Beginning Analysis...")
    print("=========================================")

    parsed_data = StrainProcess(raw_data, test_num, sample_dimensions)

    modulus = ModulusProcess(parsed_data, test_num)

    print(modulus)

    # print(parsed_data)
    print("Analysis Complete...")
    print("=========================================")

    # GRAPHING DATA
    ########################

    sensor = ['MTS', 'Laser', 'Strain Guage 1', 'Strain Guage 2']
    save = True
    StrainGraph(parsed_data, test_num, sensor, modulus, save)
    print("=========================================")

    # print("Saving Data CSVs...")
    # Saving data raw data to CSV