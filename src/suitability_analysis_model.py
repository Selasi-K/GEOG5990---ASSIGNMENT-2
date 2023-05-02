#Importing packages
import my_modules.io as io
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib
from matplotlib import pyplot as plt
import my_modules.geometry as geometry
import imageio
import os
import csv
# import tkinter as tk
# import tkinter.ttk as ttk

# Introduce if clause  to keep codes that are not functions. Ensures it is run when the main program runs.
if __name__ == '__main__':  

    # Reading geology data
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
   # print('Geology', geology)
    print('n_rows of geology', n_rows )
    print('n_cols of geology', n_cols)
    plt.imshow(geology)
    plt.show()
    
    # Reading population data
    population, n_rows, n_cols = io.read_data('../data/input/population.txt')
   # print('Population', population)
    plt.imshow(population)
    plt.show()
    
    # Reading transport data
    transport, n_rows, n_cols = io.read_data('../data/input/transport.txt')
   # print('Transport', transport)
    plt.imshow(transport)
    plt.show()
    
    #Calling the weighted_rasters
    weighted_output = geometry.weighting_rasters(n_rows,n_cols, geology,population,transport)
   # print(weighted_output)
    
    
    rescaled_data = geometry.rescale(n_cols,n_rows,weighted_output)
    print(rescaled_data)
    plt.imshow(rescaled_data)
    plt.show()
   
    
  
       
    # # Create directory to write images to.
    # try:
    #     os.makedirs('../data/output/images/')
    # except FileExistsError:
    #     print("path exists")
    
    # # For storing images
    # global ite
    # ite = 1
    # images = []
    # #Calling write_data function
    # n_cols = io.write_data(rescaled_weighted_sum)
    
    # plt.imshow(rescaled_weighted_sum, cmap ='Greens')
    # filename = '../data/output/images/final raster' + str(ite) + '.png'
    # plt.savefig(filename)
    # plt.show()
    # plt.close()
    # images.append(imageio.imread(filename))
    
    # # Print the weighted sum
    # #print("Weighted sum:", weighted_rasters)
    
    
    

