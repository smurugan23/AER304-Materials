"""
Functions related to plotting results
"""
# IMPORTS
#####################
# Dependancies
from scipy import io
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import os


def StrainGraph(data: pd.DataFrame, test_num: np.int8, sensor: np.array, save: bool):
    '''
    PLots the strain graphs.

    Parameters:
    -----------   
    data : pd.DataFrame
        data from sensors
    test_num : np.int
        sample number
    sensor : np.array
        which sensors a plot must be made for
    save : bool
        save graphs or not
    '''

    for s in sensor:
        print(" Generating " + str(s) + " strain plot..")
        plt.plot(data.t, data[s], color = 'r')
        params = {'mathtext.default': 'regular' }          
        plt.rcParams.update(params)
        plt.rcParams.update({'font.size': 12})
        plt.title(str(s) + ' Strain vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel(str(s) + ' Strain (mm)')
        plt.legend([str(s) + ' Strain data'])
        plt.grid()
        if save:
            os.makedirs(f'results/Test_{test_num}-graphs/', exist_ok=True)
            plt.savefig(f'results/Test_{test_num}-graphs/{s}_strain.png')
        # plt.show()
        plt.clf()