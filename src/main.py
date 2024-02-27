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
    # print("=========================================")

    # LOADING TEST DATA
    ##############################
    raw_data = pd.read_csv(file_path, skiprows=skip_rows, sep = '\t')


    # Rename columns
    parsed_data = raw_data.rename(columns={'X_Value': 't', 'Untitled': 'MTS_F', 'Untitled 1': 'MTS', 'Untitled 2': 'Laser', 'Untitled 3': 'Strain Guage 1', 'Untitled 4': 'Strain Guage 2', 'Untitled 5': 'MTS_stress'})
    
  
    # PROCESSING DATA
    ########################
    print("=========================================")
    print("Beginning Analysis...")
    print("=========================================")

    parsed_data.MTS_stress = parsed_data['MTS_F'] / (sample_dimensions['B' + str(test_num)]['width'] * sample_dimensions['B' + str(test_num)]['thickness'])
    parsed_data.Laser = ((parsed_data['Laser']-parsed_data['Laser'][0])/parsed_data['Laser'][0])
    parsed_data.MTS = -((parsed_data['MTS']-parsed_data['MTS'][0])/parsed_data['MTS'][0])
    parsed_data['Strain Guage 1'] = -1 * parsed_data['Strain Guage 1'][0:800] # filtering out some 'post guage break' 
    parsed_data['Strain Guage 2'] =      parsed_data['Strain Guage 2'][0:800]

    print(parsed_data[0:500])
    if test_num == 1:
        parsed_data.Laser = parsed_data.Laser[0:985] # Filtering out noise

    # print(parsed_data)
    print("Analysis Complete...")
    print("=========================================")

    # PROCESSING DATA
    ########################

    sensor = ['MTS', 'Laser', 'Strain Guage 1', 'Strain Guage 2']
    save = True
    StrainGraph(parsed_data, test_num, sensor, save)
    print("=========================================")

    # print("Saving Data CSVs...")
    # Saving data raw data to CSV