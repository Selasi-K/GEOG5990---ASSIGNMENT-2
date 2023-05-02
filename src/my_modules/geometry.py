import math
import my_modules.io as io
import suitability_analysis_model as model
import numpy as np

# Define factors to multiply by
geology_weight = 0.5
population_weight = 0.2
transport_weight = 0.3



# def weighting_rasters(n_rows,n_cols, geology,population,transport):
#     weighted_output = []
#     for i in range(n_rows):
#         for j in range(n_cols):
#             final_weight = geology[i][j]*geology_weight + population[i][j]*population_weight + transport[i][j]*transport_weight 
#             weighted_output.append(final_weight)
#     return weighted_output
#     print('final',weighted_output)
    
def weighting_rasters(n_rows, n_cols, geology, population, transport):
    weighted_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            final_weight = geology[i][j] * geology_weight + population[i][j] * population_weight + transport[i][j] * transport_weight
            row.append(final_weight)
        weighted_output.append(row)
    return weighted_output



# def rescale_raster(raster):
#     """
#     Rescales the input raster to have values in the range [0, 255].

#     Args:
#         raster (list): A 2D array representing the raster.

#     Returns:
#         list: A 2D array representing the rescaled raster.
#     """
#     flattened_raster = np.array(raster).flatten()
    # min_val = 0
    # max_val = 255
    
#     for n_rows in weight:
#         rescaled_data = []

#     rescaled_weighted_sum = ((val - min_val) / (max_val - min_val)) * 255
#     return rescaled_weighted_sum.tolist()



def rescale(n_rows,n_cols,weighted_output):
    min_val = min(weighted_output)
    max_val = max(weighted_output)
    rescaled_raster = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            rescaled_val = ((weighted_output[i][j]) - min_val) / (max_val - min_val) * 255
            row.append(rescaled_val)
            rescaled_raster.append(rescaled_val)
        
    return rescaled_raster












