"""
Functions related to analysing results
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


def StrainProcess(data: pd.DataFrame, test_num: np.int8, sample_dimensions: np.array):
    '''
    Process the strain values.

    Parameters:
    -----------   
    data : pd.DataFrame
        data from sensors
    test_num : np.int
        sample number
    sample_dimensions : np.array
        averaged cross-sectional area of the samples

    Returns:
    -----------   
    parsed_data : pd.DataFrame
        dataframe after processing for strain values
    '''

    # Rename columns
    parsed_data = data.rename(columns={'X_Value': 't', 'Untitled': 'MTS_F', 'Untitled 1': 'MTS', 'Untitled 2': 'Laser', 'Untitled 3': 'Strain Guage 1', 'Untitled 4': 'Strain Guage 2', 'Untitled 5': 'MTS_stress'})
    
    parsed_data.MTS_stress = parsed_data['MTS_F'] / (sample_dimensions['B' + str(test_num)]['width'] * sample_dimensions['B' + str(test_num)]['thickness'])
    parsed_data.Laser = ((parsed_data['Laser']-parsed_data['Laser'][0])/parsed_data['Laser'][0])
    parsed_data.MTS = -((parsed_data['MTS']-parsed_data['MTS'][0])/parsed_data['MTS'][0])
    parsed_data['Strain Guage 1'] = -1 * parsed_data['Strain Guage 1'][0:730] # filtering out some 'post guage break' 
    parsed_data['Strain Guage 2'] =      parsed_data['Strain Guage 2'][0:730]

    # print(parsed_data[0:500])
    if test_num == 1:
        parsed_data.Laser = parsed_data.Laser[0:985] # Filtering out noise
    
    return(parsed_data)

def ModulusProcess(data: pd.DataFrame, test_num: np.int8):
    '''
    Calculate the young's modulus of the sample.

    Parameters:
    -----------   
    data : pd.DataFrame
        data from sensors
    test_num : np.int
        sample number

    Returns:
    -----------   
    modulus : np.int
        elastic modulus for that sample
    '''
    end_indices = [600, 74, 300, 550, 500] # region within which each graph is linear, determined observationally
    
    end_ind = end_indices[test_num-1]

    # print(data[['MTS_stress', 'Laser']][0:end_ind])

    modulus = [0, 0, 0]

    modulus[0], intercept = np.polyfit(data['Laser'][30:end_ind], data.MTS_stress[30:end_ind], deg=1)
    modulus[1], intercept = np.polyfit(data['Strain Guage 2'][0:end_ind], data.MTS_stress[0:end_ind], deg=1)
    modulus[2], intercept = np.polyfit(data['Strain Guage 1'][0:end_ind], data.MTS_stress[0:end_ind], deg=1) # transverse

    if test_num == 3:
        modulus[0], intercept = np.polyfit(data['Laser'][0:end_ind], data.MTS_stress[0:end_ind], deg=1)    
        modulus[2], intercept = np.polyfit(data['Strain Guage 1'][0:end_ind], data.MTS_stress[0:end_ind], deg=1) # transverse

    
    return modulus

def YieldProcess(data: pd.DataFrame, test_num: np.int8, modulus: np.array):
    '''
    Calculate the young's modulus of the sample.

    Parameters:
    -----------   
    data : pd.DataFrame
        data from sensors
    test_num : np.int
        sample number
    modulus : np.array
        elastic modulus of the sample

    Returns:
    -----------   
    yield_strength : np.array
        yield strenngth location and value for that sample
    '''
    end_indices = [675, 200, 500, 625, 600] # region within which each graph is linear, determined observationally
    
    end_ind = end_indices[test_num-1]

    mod = modulus[0 if (test_num == 3) else 1]
    strain_guage = data['Strain Guage 2'][0:end_ind]
    strain_laser = data['Laser'][0:end_ind]
    stress_measured = data['MTS_stress'][0:end_ind]
    stress_offset_guage = [x*mod - mod*0.002 for x in strain_guage]
    stress_offset_laser = [x*mod - mod*0.002 for x in strain_laser]

    if test_num == 3:
        plt.plot(strain_laser, stress_measured)
        plt.plot(strain_laser, stress_offset_laser)

        diff = abs(stress_measured - stress_offset_laser)
        intersect_ind = list(diff).index(min(diff))
        yield_strength = [strain_laser[intersect_ind], stress_measured[intersect_ind]]
    else:
        plt.plot(strain_guage, stress_measured)
        plt.plot(strain_guage, stress_offset_guage)

        diff = abs(stress_measured - stress_offset_guage)
        intersect_ind = list(diff).index(min(diff))
        yield_strength = [strain_guage[intersect_ind], stress_measured[intersect_ind]]
    
    return yield_strength


def UltimateProcess(data: pd.DataFrame, test_num: np.int8):
    '''
    Calculate the young's modulus of the sample.

    Parameters:
    -----------   
    data : pd.DataFrame
        data from sensors
    test_num : np.int
        sample number

    Returns:
    -----------   
    ultimate_strength : np.array
        ultimate strenngth location value for that sample
    '''

    end_indices = [700, 700, 700, 700, 700] # region within which each graph is linear, determined observationally
    
    end_ind = end_indices[test_num-1]

    end_ind = -1; 

    sensor = ['Laser', 'Strain Guage 2']

    stress_measured = data['MTS_stress'][0:end_ind]
    ultimate_strength = [data.Laser[list(stress_measured).index(max(stress_measured))] , max(stress_measured)]
    
    
    return ultimate_strength

    