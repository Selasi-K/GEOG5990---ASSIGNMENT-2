import unittest
import suitability_analysis_model as sm
import my_modules.geometry as gm


class test_program(unittest.TestCase):
    def test_weighting_rasters(self):
        gw = 0.5
        pw = 0.2
        tw = 0.3
        n_rows = 2
        n_cols = 1
        geology = [[1], [2]]
        population = [[3], [4]]
        transport = [[5], [6]]
        result = gm.weighting_rasters(gw, pw, tw, n_rows, n_cols, geology, population, transport)
        expected = [[2.6], [3.5999999999999996]]
        self.assertEqual(result, expected)
    
    

if __name__ == '__main__':
    unittest.main()