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
import math


# Define the weight of each factor and initialise them
gw = 0
pw =0
tw = 0

def plot(gw,pw,tw):
    """
    Redraws the canvas

    """
    figure.clear()
    
    weighted_output = geometry.weighting_rasters(gw,pw,tw,n_rows,n_cols, geology,population,transport)
    
    # Find the maximum and minimum values in combinedweighted_output = geometry.weighting_rasters(gw,pw,tw,n_rows,n_cols, geology,population,transport)
    max_value = 0
    min_value = math.inf
    for i in range(n_rows):
        for j in range(n_cols):
            max_value = max(max_value, weighted_output[i][j])
            min_value = min(min_value, weighted_output[i][j])
            
    #print(min_value)
    #print(max_value)
    #print(weighted_sum)
    
    # Calculate rescaled output
    rescaled_raster = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            rescaled_value = int((weighted_output[i][j] - min_value) / (max_value - min_value) * 255)
            # Add the rescaled value to the current row
            row.append(rescaled_value)
        # Add the current row to the output list
        rescaled_raster.append(row)
        #print(rescaled_output)
        
        
        
    ax = figure.add_subplot(111)
    im=ax.imshow(rescaled_raster,cmap='Greens')
    #Adds a label to the plot
    ax.set_title('Final MCE MAP') 
    # Add a color bar to the plot
    cbar = figure.colorbar(im)
    
    canvas.draw()
    
    text_save(rescaled_raster)
    
    return figure

def update(x):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
    
    gw = int(float(scale_geology.get()))
    scale_geology_label.config(text='g=' + str(gw))
    pw = int(float(scale_population.get()))
    scale_population_label.config(text='p=' + str(pw))
    tw = int(float(scale_transport.get()))
    scale_transport_label.config(text='t=' + str(tw))
    
    # Call the plot function and get the Figure object
    plot(gw, pw, tw)
    
  
def text_save(output):
    io.write_data('../data/output/final_mce.txt', output)
    
def image_save():
    # Create directory to write images to.
    try:
        os.makedirs('../data/output/images/')
    except FileExistsError:
        print("path exists")
    # For storing images
    global ite
    ite = 1
    images = []
    filename = '../data/output/images/final raster' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
     
def exiting():
    """
   Exits the program 

   Parameters:
   None

   Returns:
   None
   """
    root.quit()
    root.destroy()
    #sys.exit(0)

    
     

# Introduce if clause  to keep codes that are not functions. Ensures it is run when the main program runs.
if __name__ == '__main__':  

    # Reading in geology data, checking number of rows and columns, and displaying the raster
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
    #print('Geology', geology)
    #print('n_rows of geology', n_rows )
    #print('n_cols of geology', n_cols)
    # plt.imshow(geology)
    # plt.show()
    
    # Reading in population data,  checking number of rows and columns, and displaying the raster
    population, n_rows, n_cols = io.read_data('../data/input/population.txt')
    # print('Population', population)
    # print('n_rows of population', n_rows )
    # print('n_cols of population', n_cols)
    # plt.imshow(population)
    # plt.show()
    
    # Reading in transport data,  checking number of rows and columns, and displaying the raster
    transport, n_rows, n_cols = io.read_data('../data/input/transport.txt')
    # print('Transport', transport)
    # print('n_rows of transport', n_rows )
    # print('n_cols of transport', n_cols)
    # plt.imshow(transport)
    # plt.show()
       
   
    
   #GUI WINDOW
    root = tk.Tk()
    root.title('Site Suitability Analysis') # Title for GUI Window
    #Title of Program
    program_title = tk.Label(root, text="MCE Site Suitability Analysis for Rock Aggregate Production in the UK", font=('Times', 24))
    program_title.pack(side='top')
    root.iconbitmap('icon.ico') # Creates an icon for the GUI window
    root.geometry("1000x800") # Size of initial window
    
    
    # Define constants for frame properties
    frame_width = 0.3
    frame_height = 0.4
    frame_padx = 0.01
    frame_pady = 0.05
    border_width = 2
    
    
    # Create the first row of frames
    #Frame for displaying geology raster
    frame1 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame1.place(relx=0.05, rely=0.1, relwidth=frame_width, relheight=frame_height)
    #Frame for population population raster
    frame2 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame2.place(relx=0.05 + frame_width + frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    #Frame for displaying transport raster
    frame3 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame3.place(relx=0.05 + 2 * frame_width + 2 * frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    # Create the second row of frames
    #Frame for displaying scale bar controls
    frame4 = tk.Frame(root, bg='whitesmoke', bd=border_width, relief='groove')
    frame4.place(relx=0.05, rely=0.55, relwidth=frame_width, relheight=frame_height)
    #Frame for displaying final MCE output
    frame5 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame5.place(relx=0.05 + frame_width + frame_padx, rely=0.55, relwidth=frame_width, relheight=frame_height)
    #Frame for save and other function buttons
    frame6 = tk.Frame(root, bg='whitesmoke', bd=border_width, relief='groove')
    frame6.place(relx=0.05 + 2 * frame_width + 2 * frame_padx, rely=0.55, relwidth=frame_width, relheight=frame_height)

    #Displaying Geology map in GUI
    # Create a figure object
    fig1 = plt.Figure(figsize=(4, 4), dpi=100)
    # Add the geology plot to the figure object
    ax1 = fig1.add_subplot(111)
    im=ax1.imshow(geology)
    #Adds a label to the plot
    ax1.set_title('Geology') 
    # Add a color bar to the plot
    cbar = fig1.colorbar(im)
    # Create a canvas object
    canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
    canvas1.draw()
    # Embed the canvas within frame1
    canvas1.get_tk_widget().pack()
    
    #Displaying Population map in GUI
    # Create a figure object
    fig2 = plt.Figure(figsize=(4, 4), dpi=100)
    # Add the population plot to the figure object
    ax2 = fig2.add_subplot(111)
    im=ax2.imshow(population)
    #Adds a label to the plot
    ax2.set_title('Population') 
    # Add a color bar to the plot
    cbar = fig2.colorbar(im)
    # Create a canvas object
    canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
    canvas2.draw()
    # Embed the canvas within frame2
    canvas2.get_tk_widget().pack()
    
    #Displaying Transport map in GUI
    # Create a figure object
    fig3 = plt.Figure(figsize=(4, 4), dpi=100)
    # Add the transport plot to the figure object
    ax3 = fig3.add_subplot(111)
    im=ax3.imshow(transport)
    #Adds a label to the plot
    ax3.set_title('Transport') 
    # Add a color bar to the plot
    cbar = fig3.colorbar(im)
    # Create a canvas object
    canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
    canvas3.draw()
    # Embed the canvas within frame3
    canvas3.get_tk_widget().pack()
    
    #Displaying final MCE Map
    # Initialise figure
    figure = matplotlib.pyplot.figure(figsize=(6, 6))
    # Create a canvas to display the figure
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=frame5)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    # Create buttons
    #button to save final image file
    button_image = ttk.Button(frame6, text="Save as Image", command=image_save)
    button_image.pack(side='bottom',padx=5, pady=5)
    #button to save final text file
    button_text = ttk.Button(frame6, text="Save as Text file", command=text_save)
    button_text.pack(side='bottom',padx=20, pady=5)

    
    #Scalebar labels
    #Label for scalebar section heading
    scale_header_label = tk.Label(frame4, text='SET SCALE FOR RASTERS',font=('Times', 16))
    scale_header_label.pack(side= 'top',padx=20, pady=5)
    #Label for scalebar adjustment info
    scale_inst_label = tk.Label(frame4, text='Move Sliders to adjust weights',font=('Times', 14))
    scale_inst_label.pack(side= 'bottom',padx=20, pady=5)
    #Label for saving outputs
    output_label = tk.Label(frame6, text='Save your final MCE Map',font=('Times', 15))
    output_label.pack(side= 'bottom',padx=20, pady=5)
    #Label for fame 6
    key_label = tk.Label(frame6, text='KEY',font=('Times', 15))
    key_label.pack(side= 'top',padx=20, pady=5)
    #darker shades
    d_label = tk.Label(frame6, text='Areas with darkest shade of green are most suitable',font=('Times', 11))
    d_label.pack(side= 'top',padx=20, pady=5)
    #lighter shades
    l_label = tk.Label(frame6, text='Areas with lightest shade of green are least suitable',font=('Times', 11))
    l_label.pack(side= 'top',padx=20, pady=5)
    
    
    # Scales
    #Scale bar for adjusting geology weight
    scale_geology = ttk.Scale(frame4, from_=1, to=10,command=update)
    scale_geology.pack(padx=20, pady=10)
    # Create a Label widget to display geology scale value
    scale_geology_label = ttk.Label(frame4, text='Set Geology Scale')
    scale_geology_label.pack(padx=20, pady=5)
    
    #Scale bar for adjusting population weight
    scale_population = ttk.Scale(frame4, from_=1, to=10, command=update)
    scale_population.pack(padx=20, pady=5)
    # Create a Label widget to display population scale value
    scale_population_label = ttk.Label(frame4, text='Set Population Scale')
    scale_population_label.pack(padx=20, pady=5)
    #Scale bar for adjusting transport weight
    scale_transport = ttk.Scale(frame4, from_=1, to=10,command=update)
    scale_transport.pack(padx=20, pady=5)
    # Create a Label widget to display transport scale value
    scale_transport_label = ttk.Label(frame4, text='Set Transport Scale.')
    scale_transport_label.pack(padx=20, pady=5)
    
    # Create a Button widget and link this with the exiting function
    exit_button = ttk.Button(root, text="Exit", command=exiting)
    exit_button.pack(side = 'bottom', padx=5, pady=5)
    
    # Configure the grid columns to have equal weight
    root.grid
    
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    
    # Start the main event loop of the GUI 
    root.mainloop()



  
    
    


   

   


  
    
    

