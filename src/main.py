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
    print("=========================================")

    # LOADING TEST DATA
    ##############################
    raw_data = pd.read_csv(file_path, skiprows=skip_rows, sep = '\t')


    # Rename columns
    raw_data = raw_data.rename(columns={'X_Value': 't', 'Untitled': 'MTS_F', 'Untitled 1': 'MTS', 'Untitled 2': 'Laser', 'Untitled 3': 'Strain Guage 1', 'Untitled 4': 'Strain Guage 2'})
    
  
    # PROCESSING DATA
    ########################
    print("=========================================")
    print("Beginning Analysis...")
    print("=========================================")

    stress = raw_data['MTS_F'] / (sample_dimensions['B' + str(test_num)]['width'] * sample_dimensions['B' + str(test_num)]['thickness'])


    print("Analysis Complete...")
    print("=========================================")


    # PROCESSING DATA
    ########################

    sensor = ['MTS', 'Laser', 'Strain Guage 1', 'Strain Guage 2']
    save = False
    StrainGraph(raw_data, test_num, sensor, save)

    # print("Saving Data CSVs...")
    # Saving data raw data to CSV