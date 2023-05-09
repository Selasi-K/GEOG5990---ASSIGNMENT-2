#Importing packages
import math

def weighting_rasters(gw,pw,tw,n_rows, n_cols, geology, population, transport):
    """
    The function calcualates weighted avarge of the three rasters using defined weights,
    for each raster. The results are stored as a list.

   Parameters:
   n_rows (int): The number of rows in the rasters.
   n_cols (int): The number of columns in the rasters.
   geology (list): A two-dimensional list of geology raster values.
   population (list): A two-dimensional list of population values.
   transport (list): A two-dimensional list of transport values.

   Returns:
   weighted_output (list): A two-dimensional list of weighted values, where each value represents the weighted average 
   of geology, population, and transport values.
   """
    weighted_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            final_weight = geology[i][j] * gw + population[i][j] * pw + transport[i][j] * tw
            row.append(final_weight)
        weighted_output.append(row)
    return weighted_output

















