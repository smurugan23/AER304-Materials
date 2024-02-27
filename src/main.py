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

# for reading to pd df
test_num = 1
file_path = "data\Group8\B" + str(test_num) + ".txt"
skip_rows = 22

print("Loading Data for Sample #" + str(test_num) + "...")
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




print("Analysis Complete...")
print("=========================================")


# PROCESSING DATA
########################

sensor = ['MTS']
StrainGraph(raw_data, test_num, sensor)

# print("Saving Data CSVs...")
# Saving data raw data to CSV