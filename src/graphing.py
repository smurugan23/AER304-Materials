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
    # finding plot limits:
    max_strain = max(data[['MTS', 'Laser', 'Strain Guage 1', 'Strain Guage 2']].max(axis=1))
    max_stress = max(data['MTS_stress'])

    for s in sensor:
        print(" Generating " + str(s) + " strain plot..")
        plt.plot(data[s], data.MTS_stress, color = 'r')
        params = {'mathtext.default': 'regular' }          
        plt.rcParams.update(params)
        plt.rcParams.update({'font.size': 12})
        plt.title(f'Material #{test_num}: {str(s)}, Stress vs Strain')
        plt.xlabel(str(s) + ' Strain (mm)')
        plt.ylabel('Stress (MPa)')
        # plt.legend([str(s) + ' Data - Material #' + str(test_num)])
        plt.grid()
        if s not in ['Strain Guage 1', 'Strain Guage 2']:
            plt.xlim((max_strain*-0.1,max_strain*1.1))
            plt.ylim((max_stress*-0.1,max_stress*1.1))
        if save:
            os.makedirs(f'results/Test_{test_num}-graphs/', exist_ok=True)
            plt.savefig(f'results/Test_{test_num}-graphs/{s}_strain.png')
        # plt.show()
        plt.clf()