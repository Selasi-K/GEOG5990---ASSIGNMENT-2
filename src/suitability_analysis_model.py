#Importing packages
import my_modules.io as io
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
from matplotlib import pyplot as plt
import my_modules.geometry as geometry
import imageio
import os
import matplotlib.animation as anim
import tkinter as tk

#Extracting and displaying geology raster
geology= io.data[0]
plt.imshow(geology)
plt.show()

#Extracting and displaying population raster
population= io.data[1]
plt.imshow(population)
plt.show()

#Extracting and displaying transport raster
transport= io.data[2]
plt.imshow(transport)
plt.show()

#Calling weighted function 
factors = [0.6,0.1, 0.3]
weighted_rasters = geometry.multiply_nested_lists_by_factors(io.data,factors )
#print(weighted_rasters)

#Adding weighted rasters
weighted_sum = geometry.add_rasters(weighted_rasters)
#print(weighted_sum)
  
#Calling rescaled weighted sum
rescaled_weighted_sum = geometry.rescale_raster(weighted_sum)
#print(rescaled_raster)

#Alternated rescaled weighted sum function
# weighted_rasters = geometry.get_weighted_rasters(geology, population, transport, geology_weight=0.3, population_weight=0.5, transport_weight=0.2)



# Create directory to write images to.
try:
    os.makedirs('../data/output/images/')
except FileExistsError:
    print("path exists")

# For storing images
global ite
ite = 1
images = []
#Calling write_data function
n_cols = io.write_data(rescaled_weighted_sum)

plt.imshow(rescaled_weighted_sum, cmap ='Greens')
filename = '../data/output/images/final raster' + str(ite) + '.png'
plt.savefig(filename)
plt.show()
plt.close()
images.append(imageio.imread(filename))

# Print the weighted sum
#print("Weighted sum:", weighted_rasters)











