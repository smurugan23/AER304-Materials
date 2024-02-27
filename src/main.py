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

# DEFINITIONS
########################

skip_rows = 22


for test_num in range(1,6):

    # for reading to pd df
    file_path = "Data\Labview Data\B" + str(test_num) + ".txt"

    print("=========================================")
    print("Loading Data for Sample #" + str(test_num) + "...")
    print("=========================================")

    # LOADING TEST DATA
    ##############################
    raw_data = pd.read_csv(file_path, skiprows=skip_rows, sep = '\t')

    # Rename columns
    raw_data = raw_data.rename(columns={'X_Value': 't', 'Untitled': 'MTS_F', 'Untitled 1': 'MTS', 'Untitled 2': 'Laser', 'Untitled 3': 'Strain Guage 1', 'Untitled 4': 'Strain Guage 2'})

    # PROCESSING DATA
    ########################
    # print("=========================================")
    # print("Beginning Analysis...")
    # print("=========================================")




    # print("Analysis Complete...")
    # print("=========================================")


    # PROCESSING DATA
    ########################

    sensor = ['MTS', 'Laser', 'Strain Guage 1', 'Strain Guage 2']
    save = False
    StrainGraph(raw_data, test_num, sensor, save)

    # print("Saving Data CSVs...")
    # Saving data raw data to CSV