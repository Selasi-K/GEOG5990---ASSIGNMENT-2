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
import tkinter as tk
import tkinter.ttk as ttk
import math


# Define the weight of each factor and initialise them
gw = 0 #geology weight
pw = 0 #population weight
tw = 0 #transport weight

def plot(gw,pw,tw):
    """
   Plots and redraws the canvas the final MCE map based on the given weights 
   for the geology, population, and transport rasters.
   After weighting it finds the maximum and minimum values of the rasters
   and rescales the values to fall within 0 -255.
    
   Args:
       gw (float): Weight for the geology raster.
       pw (float): Weight for the population raster.
       tw (float): Weight for the transport raster.

   Returns:
       Matplotlib figure object representing the final MCE map.
 
     """
    figure.clear()
    
    weighted_output = geometry.weighting_rasters(gw,pw,tw,n_rows,n_cols, geology,population,transport)
    
    # Find the maximum and minimum values in combined weighted_output = geometry.weighting_rasters(gw,pw,tw,n_rows,n_cols, geology,population,transport)
    max_value = 0
    min_value = math.inf
    for i in range(n_rows):
        for j in range(n_cols):
            max_value = max(max_value, weighted_output[i][j])
            min_value = min(min_value, weighted_output[i][j])
    #These print statements were used for preliminary checks       
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

    # Add the figure plot to the figure object    
    ax = figure.add_subplot(111)
    #Plot it as choropleth map
    im=ax.imshow(rescaled_raster,cmap='Greens')
    #Adds a label to the plot
    ax.set_title('Final MCE MAP') 
    # Add a color bar to the plot
    cbar = figure.colorbar(im)
    #updates the canvas with the created plot
    canvas.draw()
    
    #Saving the final output as a text file
    text_save(rescaled_raster)
    
    return figure

def update(x):
    """
    Updates the plot with new values for geological, population, and transportation weights based on the 
   changes in scales using the sliders.

    Parameters
    ----------
    x : str.
        Number
        The changed values

    Returns
    -------
    None.

    """
    # Extracts the current weights from the sliders
    gw = scale_geology.get()
    scale_geology_label.config(text='geology=' + str(round(gw,1)))
    
    pw = scale_population.get()
    scale_population_label.config(text='population=' + str(round(pw,1)))
    
    tw = scale_transport.get()
    scale_transport_label.config(text='transport=' + str(round(tw,1)))
    
    ## Call the plot function with the current weights and generates a new plot
    plot(gw, pw, tw)
    
  
def text_save(output):
    """
  Saves the final MCE output to a text file in the '../data/output' directory.

  Args:
      output: A string containing the raster txt. data to be saved.

  Returns:
      None.

  """
     #Calling the write data function from io
    io.write_data('../data/output/final_mce.txt', output)
    
def image_save():
    """
   Creates a new file directory if it does not exit and saves the 
   final MCE plot as an image in the directory.
   
    Parameters:
    None
    
    Returns:
    None
    """

    # Create directory to write images to if none exists.
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

    # Reading in geology data and checking number of rows and columns.
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
    #These commented out codes where used for preliminary checks
    #print('Geology', geology)
    #print('n_rows of geology', n_rows )
    #print('n_cols of geology', n_cols)
  
    # Reading in population data and  checking number of rows and columns.
    population, n_rows, n_cols = io.read_data('../data/input/population.txt')
    
    # Reading in transport data and  checking number of rows and columns.
    transport, n_rows, n_cols = io.read_data('../data/input/transport.txt')
    
        
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
    
    #Frame for displaying population raster
    frame2 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame2.place(relx=0.05 + frame_width + frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    #Frame for displaying transport raster
    frame3 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame3.place(relx=0.05 + 2 * frame_width + 2 * frame_padx, rely=0.1, relwidth=frame_width, relheight=frame_height)
    
    
    # Create the second row of frames
    #Frame for displaying scale bar sliders
    frame4 = tk.Frame(root, bg='whitesmoke', bd=border_width, relief='groove')
    frame4.place(relx=0.05, rely=0.55, relwidth=frame_width, relheight=frame_height)
    
    #Frame for displaying final MCE output
    frame5 = tk.Frame(root, bg='white', bd=border_width, relief='groove')
    frame5.place(relx=0.05 + frame_width + frame_padx, rely=0.55, relwidth=frame_width, relheight=frame_height)
    
    #Frame for key and save buttons
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
    # Create a canvas to display the figure in frame 5
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
    
    #Label for scalebar adjustment instruction
    scale_inst_label = tk.Label(frame4, text='Move Sliders to adjust weights',font=('Times', 14))
    scale_inst_label.pack(side= 'bottom',padx=20, pady=5)
    
    #Label for saving outputs
    output_label = tk.Label(frame6, text='Save your final MCE Map',font=('Times', 15))
    output_label.pack(side= 'bottom',padx=20, pady=5)
    
    #Label for fame 6
    key_label = tk.Label(frame6, text='KEY',font=('Times', 15))
    key_label.pack(side= 'top',padx=20, pady=5)
    
    #darker shades key label
    d_label = tk.Label(frame6, text='Areas with darkest shade of green are most suitable',font=('Times', 11))
    d_label.pack(side= 'top',padx=20, pady=5)
    
    #lighter shades key label
    l_label = tk.Label(frame6, text='Areas with lightest shade of green are least suitable',font=('Times', 11))
    l_label.pack(side= 'top',padx=20, pady=5)
    
    
    # Sliders
    #Sliders for adjusting geology weight
    scale_geology = ttk.Scale(frame4, from_=0, to=1,command=update)
    scale_geology.pack(padx=20, pady=10)
    # Create a Label widget to display geology scale value
    scale_geology_label = ttk.Label(frame4, text='Set Geology Scale')
    scale_geology_label.pack(padx=20, pady=5)
    
    #Slider for adjusting population weight
    scale_population = ttk.Scale(frame4, from_=0, to=1, command=update)
    scale_population.pack(padx=20, pady=5)
    # Create a Label widget to display population scale value
    scale_population_label = ttk.Label(frame4, text='Set Population Scale')
    scale_population_label.pack(padx=20, pady=5)
    
    #Slider for adjusting transport weight
    scale_transport = ttk.Scale(frame4, from_=0, to=1,command=update)
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



  
    
    


   

   


  
    
    

