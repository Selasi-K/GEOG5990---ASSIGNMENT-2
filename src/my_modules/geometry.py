import math
import numpy as np


# # Define factors to multiply by
# geology_weight = 0.5
# population_weight = 0.2
# transport_weight = 0.3



def multiply_nested_lists_by_factors(data, factors):
    """
    Multiplies each nested list in the input data list by the corresponding factor in the factors list.

    Args:
        data (list): A list containing the nested lists to be multiplied.
        factors (list): A list of numbers representing the factors to multiply each nested list with.

    Returns:
        list: A new list containing the multiplied nested lists.
    """
    updated_data = []
    for i in range(len(data)):
        nested_list = data[i]
        factor = factors[i]
        updated_nested_list = []
        for row in nested_list:
            updated_row = [value * factor for value in row]
            updated_nested_list.append(updated_row)
        updated_data.append(updated_nested_list)
    return updated_data

# def multiply_nested_lists_by_factors(data, geology_weight, population_weight, transport_weight):
#     """
#     Multiplies the values in the geology, population, and transport nested lists within the data list by the specified factors,
#     creating a new list to store the modified data.
    
#     Args:
#         data (list): A list containing the nested geology, population, and transport lists.
#         geology_weight (float): The factor to multiply the values in the geology list by.
#         population_weight (float): The factor to multiply the values in the population list by.
#         transport_weight (float): The factor to multiply the values in the transport list by.
    
#     Returns:
#         updated_data (list): A new list containing the updated data with the multiplied values.
#     """
#     # Create a new list to store the modified data
#     updated_data = []
    
#     # Iterate over each nested list in data
#     for nested_list in data:
#         # Create a new list to store the updated nested list
#         updated_nested_list = []
#         # Iterate over each row in nested list
#         for row in nested_list:
#             # Create a new list to store the updated row
#             updated_row = []
#             # Iterate over each value in row
#             for i, value in enumerate(row):
#                 # Check which list the value belongs to and multiply by appropriate factor
#                 if i < len(nested_list[0])/3: # Geology list
#                     updated_row.append(value * geology_weight)
#                 elif i < 2*len(nested_list[0])/3: # Population list
#                     updated_row.append(value * population_weight)
#                 else: # Transport list
#                     updated_row.append(value * transport_weight)
#             # Append the updated row to the updated nested list
#             updated_nested_list.append(updated_row)
#         # Append the updated nested list to the updated data list
#         updated_data.append(updated_nested_list)
    
#     return updated_data

def add_rasters(data):
    """
    Adds the input rasters together.

    Args:
        data (list): A list containing the nested geology, population, and transport lists.

    Returns:
        list: A nested list representing the added rasters.
    """
    # Get the shape of the nested lists
    num_rows, num_cols = len(data[0]), len(data[0][0])
    
    # Create a new nested list to store the added rasters
    added_rasters = []
    
    # Iterate over each row and column
    for row_idx in range(num_rows):
        added_row = []
        for col_idx in range(num_cols):
            # Sum the pixel values across all three nested lists
            pixel_sum = sum(nested_list[row_idx][col_idx] for nested_list in data)
            added_row.append(pixel_sum)
        added_rasters.append(added_row)
    
    return added_rasters


def rescale_raster(raster):
    """
    Rescales the input raster to have values in the range [0, 255].

    Args:
        raster (list): A 2D array representing the raster.

    Returns:
        list: A 2D array representing the rescaled raster.
    """
    flattened_raster = np.array(raster).flatten()
    min_val = np.min(flattened_raster)
    max_val = np.max(flattened_raster)

    rescaled_weighted_sum = ((np.array(raster) - min_val) / (max_val - min_val)) * 255
    return rescaled_weighted_sum.tolist()












