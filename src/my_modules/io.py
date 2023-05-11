#Importing packages
import csv #package to help read and write data

# Read input data
def read_data(filepath):
    """
    A function that reads a CSV file and stores its contents in a two-dimensional list. 
    It also checks that each row of data contains the same number of values, and returns the number of rows and columns.

    Parameters:
    filepath (str): path to the CSV file

    Returns:
    tuple: a tuple containing three elements:
        - data (list): a two-dimensional list of the data in the CSV file
        - n_rows (int): the number of rows in the data
        - n_cols (int): the number of columns in the data
    """
    f = open(filepath, newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        data.append(row)
    f.close()
    #print(data)  

#Checking that each row of data contains the same number of values, and returning the num of rows and columns
  #Checking number of rows and columns
    n_rows = len(data)
    n_cols0 = len(data[0])
   #Checking if there equal number of rows and columns and printing the num 
    for row in range(1,n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
        return data, n_rows, n_cols
        f.close()


def write_data(filepath, rescaled_raster):
    """
  A function that writes a two-dimensional list of floats to a CSV file.
  
  Parameters:
   filepath (str): The file path to save the CSV file.
  rescaled_raster (list): a two-dimensional list of floats representing the rescaled weighted raster data (final output).

  Returns:
  None
  """
    # Open a CSV file with the given file path and write the data from the rescaled raster to it
    with open(filepath,'w', newline='') as f:
        writer=csv.writer(f, delimiter=',')
        for row in rescaled_raster:
            writer.writerow(row)
    f.close()
        



