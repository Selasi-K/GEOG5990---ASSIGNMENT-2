#Importing packages
import csv #package to help read and write data
import glob

def read_files_in_directory(file_paths):
    """
    Reads in data from all files in the specified directory.

    Args:
        file_paths (str): The directory path where the files are stored.

    Returns:
        data (list): A list containing the data from all files in the directory. Each file's data is a nested list of rows, where each row is a list of numeric values.
    """
    # Initialize list to hold data from all files
    data = []
    
    # Get list of file paths for all files in directory
    file_paths = glob.glob('../data/input/*.txt')
    
    # Loop over each file path and read data into list
    for file_path in file_paths:
        with open(file_path, newline='') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            file_data = []
            for row in reader:
                file_data.append(row)
            data.append(file_data)
            
    return data


#Initializing variables outside the function
file_paths = glob.glob('../data/input/*.txt')
data = read_files_in_directory(file_paths)


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
        



