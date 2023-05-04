import math
import my_modules.io as io
import numpy as np

# Define factors to multiply by
geology_weight = 0.3
population_weight = 0.3
transport_weight = 0.4


def weighting_rasters(n_rows, n_cols, geology, population, transport):
    weighted_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            final_weight = geology[i][j] * geology_weight + population[i][j] * population_weight + transport[i][j] * transport_weight
            row.append(final_weight)
        weighted_output.append(row)
    return weighted_output

def rescale(weighted_output,n_rows,n_cols):
    max_value = 0
    min_value = math.inf
    for i in range(n_rows):
        for j in range(n_cols):
            max_value = max(max_value, weighted_output[i][j])
            min_value = min(min_value, weighted_output[i][j])
            
    # Rescale the values into the range 0-255
    rescaled_raster = []
    for row in weighted_output:
        rescaled_row = []
        for value in row:
            rescaled_value = ((value - min_value) / (max_value - min_value)) * 255
            rescaled_row.append(rescaled_value)
        rescaled_raster.append(rescaled_row)
        #print(min_value)
        #print(max_value)
    return rescaled_raster















