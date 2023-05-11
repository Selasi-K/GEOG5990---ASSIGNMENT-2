import unittest
import my_modules.geometry as gm


class test_program(unittest.TestCase):
    def test_weighting_rasters(self):
    # Set constants for the parameters of the weighting_rasters function test
        gw = 0.5
        pw = 0.2
        tw = 0.3
        n_rows = 2
        n_cols = 1
        geology = [[1], [2]]
        population = [[3], [4]]
        transport = [[5], [6]]
        # Call the weighting_rasters function with the defined parameters
        result = gm.weighting_rasters(gw, pw, tw, n_rows, n_cols, geology, population, transport)
        # Set the expected result
        expected = [[2.6], [3.5999999999999996]]
        # Check if the actual result is equal to the expected result
        self.assertEqual(result, expected)
        
    
    
    
# Introduce if clause  to keep codes that are not functions. Ensures it is run when the main program runs.
if __name__ == '__main__':
    unittest.main()