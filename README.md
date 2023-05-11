# GEOG5990---ASSIGNMENT-2

#PROJECT TITLE
MULTICRITERIA EVALUATION (MCE) SUITABILITY ANALYSIS SOFTWARE FOR ROCK AGGREGATE PRODUCTION IN THE UNITED KINGDOM

#DESCRIPTION 
The MCE Software is an interactive software, built using python, targeted at aiding analysis for suitability of land for rock aggregate production in 
the United Kingdom. The software is an essential efficient tool which helps in identifying suitable sites and in the long run ensures
effective allocation and use of resources. 

Three important factors for rock aggregate production are used in developing the MCE. These are Geology, Population and Transport. 
A combination of these factors are paramount in finding areas of highest suitability for rock aggregate production. This is what the software seeks to achieve.
The parameter for most suitable sites is areas with the highest values of the factors. 

A Graphical User Interface (GUI) was built to give a user-friendly experience in using the software. The GUI displays a platform with some buttons and frames which aid in using the software (See word document for pictures). Users are allowed set preferred weights for each of the factors simultaneously see the resulting image.

Spyder v3.9 was used in building the software.


#GETTING STARTED
License - Apache 2.0. Attached is a licence file with more information. Alternatively, visit this link for details: https://www.apache.org/licenses/LICENSE-2.0

##CONTENT FILES (File Directory)
data/input  - contains geology.txt, population.txt and transport.txt files which are the 3 raster data read by the program.
    /output - contains all output files from the program. This includes both text and image files.

src/my_modules/io.py (script for reading and writing data functions)
			  /geometry.py (Script with function for weighting rasters)

     /icon.ico (GUI window icon)
     / suitability_analysis_model (Main script with  functions and other source codes for running the software).
     / test.py (unit test script)
   
LICENCE (License information)

README.md (Readme file which contains essential information about the software).

User Manual (word document with useful tips and screenshots of using the software)

.gitignore
	 
	 		  
#PREREQUISITES
The program runs on all python script compatible software. However, for optimum usability and performance, it is recommended that it is
run on Scientific Python Development Environment (Spyder),a constituent software of the Anaconda package on a computer.
Spyder is a free open source python software with easy to use interface which allows visualising the rasters, interactivity and debugging errors easily.
To download Spyder follow the instructions in this link:
https://www.spyder-ide.org/
Additionally, the website offers basic training on getting started with the program. Consider using this resource to familiarize yourself with the program.


#USAGE 
After successfully installing Spyder, launch it. (For help with lauching the program, see the word document).
The Spyder interface has three windows(Editor,Help viewer and ipython console). The Editor window (left side) displays scripts opened and codes.
It is where most of the code for the MCE software was written. Help viewer section(top-right) has useful tools including variable explorer, plots and a Help section.
Lastly, the ipython console displayed print outputs and errors. It also allows some coding. (see https://www.spyder-ide.org/ for more details on the interface).
Additionally, there are some useful resources in the word document.

#DEVELOPMENT PROCESS
1. Text files of the input rasters (geology.txt, population.txt and transport.txt) were read as list of lists using a generic read data function which reads the files
using csv.reader and checks the number of rows and coloums of each of them when called and fed with a filepath(read_data function).
2.The three rasters were multiplied by different weights and summed up to produce a weighted sum list  using weighting_rasters_function.
3.The weighted sum values were further rescaled to fall within 0 - 255 after deriving the minimum and maximum values.
4. A GUI was created to display the results, to allow users to change the weights and save outputs using tkinter, plot and update functions.
5. The program was run a series of time to test it's functionality and fix errors. This is evidenced by sample results found in the output folder. Unit testing was also done.

#RUNNING THE PROGRAM
NB: Before running the program it is imperactive to change the Graphics Backend option to Tkinter. This ensures the GUI codes work well. See word document on steps to do this.

At the top area of the program is a tool bar with useful buttons for using the program (See the word document for screenshots). From the tool bar, click open file or Ctrl + O on your keyboard to open the files.
From the pop-up dialogue box, navigate to the file location and select the files. Note: Select all python files to ensure program runs optimally. 
The needed files are suitability_analysis_model.py, io.py, geometry.py and test.py (Refer to contents section for specific locations of the files). 
After all the files have been selected and opened, ensure 'suitability_analysis_model.py' tab is active. Find the 'run file' button from the tool bar by hovering over the different commands(See screenshots in the word document for help).

Click the run button to run the program.

When the the script is run the GUI window opens displaying the three rasters, sliders and buttons to save final output (See screenshots in the word document). From the GUI window,follow these steps to conduct MCE analysis:

1.In the left bottom area of the GUI window (frame 4), there are adjustable sliders which control the weights used in weighting the input rasters. Adjust the weights according to your preference. Doing this automatically updates the weights applied to the rasters through the Update_function.
2.Results will be simultaneously calculated, redrawn and plotted through the plot_function into the final map frame (frame 5). This map depicts the different suitability levels of areas across the country.Darker shades of green translates as increasing suitability, while lighter shades show decreasing suitability.
3. After producing your desired map. Click the 'Save as text file' button on the bottom right to save the final output text file. Alternatively, you can click the 'Save as Image' button to save the final output map. These files would be found in 'output' folder within the 'data' folder. 
NB: To have larger size of the picture, please resize the pop-up picture window as required before saving the image.
4.To end the program, either click the 'Exit' button or just click the 'close window' button at the top right corner of the window (See screenshots in Word document for help)

#TESTING
Some testing was done for the program. A unit test was done for the weighting_rasters function to check its accuracy. This code can be seen in the test.py file.

Note: In case of any errors, use the debugging tool to detect the problem. ipython console is also 
particularly helpful in doing this.

#FURTHER IMPROVEMENT
One improvement that can be made to the program is to modify the update function to automatically adjust weights to cummulatively add up to 1. This is because many of MCE studies ensure weights add up to 1.

Another improvement to the program can be to make it possible for users to select where to save outputs rather than the pre-defined directory within the GUI interface. 

#CREDITS
ANDY TURNER - Useful tutorials : https://agdturner.github.io/GEOG5990/home/index.html


