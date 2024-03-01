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


def StrainGraph(data: pd.DataFrame, test_num: np.int8, sensor: np.array, modulus : np.array, yield_strength : np.array, ultimate_strength : np.array, save: bool):
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
    modulus : np.float64
        elastic modulus of that material
    yield_strength : np.array
        yield strenngth location and value for that sample
    ultimate_strength : np.array
        ultimate strenngth location value for that sample
    save : bool
        save graphs or not
    '''

    end_indices = [600, 70, 500, 550, 500]
    
    end_ind = end_indices[test_num-1]
    
    end_ind = -1

    # finding plot limits:
    max_strain = max(data[[ 'Laser', 'Strain Guage 1', 'Strain Guage 2']][0:end_ind].max(axis=1))
    max_stress = max(data['MTS_stress'])

    for s in sensor:
        print(" Generating " + str(s) + " strain plot..")

        if s in ['Strain Guage 1', 'Strain Guage 2'] and test_num == 2:
            end_ind = 500

        plt.plot(data[s][0:end_ind], data.MTS_stress[0:end_ind], color = 'r')

        mod = 0
        
        if s in ['Laser', 'Strain Guage 2', 'Strain Guage 1']:
            
            if s == 'Laser':
                mod = modulus[0]
                plt.scatter(yield_strength[0], yield_strength[1], s=50)
                plt.scatter(ultimate_strength[0], ultimate_strength[1], s=50)
            elif s == 'Strain Guage 2':
                mod = modulus[1]
                plt.scatter(yield_strength[0], yield_strength[1], s=50)
            else:
                mod = modulus[2]
            
            plt.legend([f'Young\'s Modulus = {round(mod, 2)} MPa', f'Yield Stength = {round(yield_strength[1], 2)} MPa', f'Ultimate Stength = {round(ultimate_strength[1], 2)} MPa'])


        params = {'mathtext.default': 'regular' }          
        plt.rcParams.update(params)
        plt.rcParams.update({'font.size': 12})
        plt.title(f'Material #{test_num}: {str(s)}, Stress vs Strain')
        plt.xlabel(str(s) + ' Strain (mm/mm)')
        plt.ylabel('Stress (MPa)')

        # x = np.linspace(0, 1, 100)
        # y = x*mod - mod*0.002
        # plt.plot(x, y)

        plt.grid()
        # if s not in ['Strain Guage 1', 'Strain Guage 2']:
        plt.xlim((max_strain*-0.1,max_strain*1.1))
        plt.ylim((max_stress*-0.1,max_stress*1.1))
        if save:
            os.makedirs(f'results/Test_{test_num}-graphs/', exist_ok=True)
            plt.savefig(f'results/Test_{test_num}-graphs/{s}_strain.png')
        # plt.show()
        plt.clf()