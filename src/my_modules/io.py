#Importing packages
import csv #package to help read and write data
import glob

# def read_data(file_paths):
#     """
#     Reads in data from all files in the specified directory.

#     Args:
#         file_paths (str): The directory path where the files are stored.

#     Returns:
#         data (list): A list containing the data from all files in the directory. Each file's data is a nested list of rows, where each row is a list of numeric values.
#     """
#     # Initialize list to hold data from all files
#     data = []
    
#     # Get list of file paths for all files in directory
#     file_paths = glob.glob('../data/input/*.txt')
    
#     # Loop over each file path and read data into list
#     for file_path in file_paths:
#         with open(file_path, newline='') as f:
#             reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#             file_data = []
#             for row in reader:
#                 file_data.append(row)
#             data.append(file_data)
            
#     return data


# #Initializing variables outside the function
# file_paths = glob.glob('../data/input/*.txt')
# data = read_data(file_paths)


# Read input data
def read_data(filepath):
    """
    Read a CSV file  and presents it as a list of list
    
    The fumction opens the text file from '../../data/input/in.txt' directory
    and reads it in using the csv module. Each row is collected as list of lists

   Returns:
       List: A list of lists with data read from the input file.
   """
    f = open(filepath, newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    f.close()
    #print(data)
    
  

#Checking that each row of data contains the same number of values, and returning the num of rows and columns
  #Checking number of rows and columns
    n_rows = len(data)
    #print('n_rows',n_rows)
    n_cols0 = len(data[0])
   # print('n_cols',n_cols0)
   #Checking if there equal number of rows and columns and printing the num 
    for row in range(1,n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
        #print data
        return data, n_rows, n_cols
        f.close()
        #print(data)

def write_data(rescaled_weighted_sum):
    """
    Write a list with final rescaled  data produced to a CSV file.

    This function takes the list of lists produced, opens 
    '../../data/output/out.txt' directory and writes the environment contents
    to it using the csv module. Lists within
    lists are treated as rows written as comma-separated values.
    
    Args:
        environment: A list of lists containing numeric 
        data to be written to the output file.

    Returns:
        None
    """
    
    with open('../data/output/weighted_rasters.txt','w', newline='') as f:
        writer=csv.writer(f, delimiter=',')
        for row in rescaled_weighted_sum:
            writer.writerow(row)
    f.close()
        



