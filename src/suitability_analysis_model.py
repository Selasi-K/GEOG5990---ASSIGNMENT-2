#Importing packages
import my_modules.io as io
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import my_modules.geometry as geometry
import imageio
import os
import csv
import tkinter as tk
import tkinter.ttk as ttk



  
def plot_geology():
   # Create a figure object
   fig1 = plt.Figure(figsize=(4, 4), dpi=100)

   # Add the geology plot to the figure object
   ax1 = fig1.add_subplot(111)
   im=ax1.imshow(geology)
   ax1.set_title('Geology') 
   # Add a color bar to the plot
   cbar = fig1.colorbar(im)
   # Create a canvas object
   canvas = FigureCanvasTkAgg(fig1, master=frame1)
   canvas.draw()
   # Embed the canvas within frame1
   canvas.get_tk_widget().pack()
   
def plot_population():
   # Create a figure object
   fig2 = plt.Figure(figsize=(4, 4), dpi=100)

   # Add the geology plot to the figure object
   ax2 = fig2.add_subplot(111)
   im=ax2.imshow(population)
   ax2.set_title('Population') 
   # Add a color bar to the plot
   cbar = fig2.colorbar(im)
   # Create a canvas object
   canvas = FigureCanvasTkAgg(fig2, master=frame2)
   canvas.draw()
   # Embed the canvas within frame2
   canvas.get_tk_widget().pack()
      
def plot_transport():
   # Create a figure object
   fig = plt.Figure(figsize=(4, 4), dpi=100)

   # Add the geology plot to the figure object
   ax3 = fig.add_subplot(111)
   im=ax3.imshow(transport)
   ax3.set_title('Transport') 
   # Add a color bar to the plot
   cbar = fig.colorbar(im)
   # Create a canvas object
   canvas = FigureCanvasTkAgg(fig, master=frame3)
   canvas.draw()
   # Embed the canvas within frame3
   canvas.get_tk_widget().pack()
   
def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)

    
     

# Introduce if clause  to keep codes that are not functions. Ensures it is run when the main program runs.
if __name__ == '__main__':  

    # Reading geology data
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
    #print('Geology', geology)
    #print('n_rows of geology', n_rows )
    #print('n_cols of geology', n_cols)
    plt.imshow(geology)
    plt.show()
    
    # Reading population data
    population, n_rows, n_cols = io.read_data('../data/input/population.txt')
    # print('Population', population)
    # print('n_rows of population', n_rows )
    # print('n_cols of population', n_cols)
    plt.imshow(population)
    plt.show()
    
    # Reading transport data
    transport, n_rows, n_cols = io.read_data('../data/input/transport.txt')
    # print('Transport', transport)
    # print('n_rows of transport', n_rows )
    # print('n_cols of transport', n_cols)
    plt.imshow(transport)
    plt.show()
    
    #Calling the weighted_rasters
    weighted_output = geometry.weighting_rasters(n_rows,n_cols, geology,population,transport)
    #print(weighted_output)
    # plt.imshow(weighted_output, cmap='Blues')
    # plt.show()
   
    
    #Calling the rescale function
    rescaled_data = geometry.rescale(weighted_output,n_rows,n_cols)
    #print(rescaled_data)
    plt.imshow(rescaled_data,cmap='Greens')
    plt.colorbar()  # Add colorbar
    plt.show()
   
  
       
       
  
       
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
    n_cols = io.write_data(rescaled_data)
    
    plt.imshow(rescaled_data, cmap ='Greens')
    plt.colorbar()  # Add colorbar
    filename = '../data/output/images/final raster' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
    
   #GUI WINDOW
    root = tk.Tk()
    root.title('Site Suitability Analysis') # Title for GUI Window
    program_title = tk.Label(root, text="Site Suitability for Rock Aggregate Production", font=('Times', 24))
    program_title.pack(side='top')
    root.iconbitmap('icon.ico') # Creates an icon for the GUI window
    root.geometry("1000x800")
    
    # Define constants for frame properties
    frame_width = 0.3
    frame_height = 0.4
    frame_padx = 0.01
    frame_pady = 0.05
    border_width = 2
    
    # Create the first row of frames
    frame1 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame1.place(relx=0.05, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    frame2 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame2.place(relx=0.05 + frame_width + frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    frame3 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame3.place(relx=0.05 + 2 * frame_width + 2 * frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    # Create the second row of frames
    frame4 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame4.place(relx=0.05, rely=0.55, relwidth=frame_width, relheight=frame_height)
    
    frame5 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame5.place(relx=0.05 + frame_width + frame_padx, rely=0.55, relwidth=frame_width, relheight=frame_height)
    
    frame6 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame6.place(relx=0.05 + 2 * frame_width + 2 * frame_padx, rely=0.55, relwidth=frame_width, relheight=frame_height)
    
    # Create buttons for each frame
    button_geology = tk.Button(frame1, text="Click to see Geology raster", command=plot_geology, fg='red')
    button_geology.pack(side='bottom')
    
    button_population = tk.Button(frame2, text="Click to see Population raster", command=plot_population, fg='red')
    button_population.pack(side='bottom')
    
    button_transport = tk.Button(frame3, text="Click to see Transport data", command=plot_transport, fg='red')
    button_transport.pack(side='bottom')
    
    # button_weather = tk.Button(frame4, text="Weather data", command=plot_weather, fg='red')
    # button_weather.pack(side='bottom')
    
    # button_infrastructure = tk.Button(frame5, text="Infrastructure data", command=plot_infrastructure, fg='red')
    # button_infrastructure.pack(side='bottom')
    
    # button_soil = tk.Button(frame6, text="Soil data", command=plot_soil, fg='red')
    # button_soil.pack(side='bottom')
    
    # Create a button to exit the program
    button_quit = tk.Button(root, text="Exit Program", command=exiting, fg='red')
    button_quit.pack(side="bottom", padx=5, pady=5)
    
    # Configure the grid columns to have equal weight
    root.grid



  
    
    


   

   


  
    
    

