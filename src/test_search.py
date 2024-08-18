import unittest
import unittest.mock
from search import fetchCoords, fetchCoordsLoop

class TestFetchCoords(unittest.TestCase):
    def testTownName(self):
        with unittest.mock.patch('builtins.input', return_value='watford'):
            function = fetchCoords()[0]
            output = [51.66090404041253, -0.3958991253953702]
            self.assertAlmostEqual(function[0], output[0], delta=1)
            self.assertAlmostEqual(function[1], output[1], delta=1)

    def testCityName(self):
        with unittest.mock.patch('builtins.input', return_value='london'):
            function = fetchCoords()[0]
            output = [51.50502529339357, -0.1311339760081772]
            self.assertAlmostEqual(function[0], output[0], delta=1)
            self.assertAlmostEqual(function[1], output[1], delta=1)

    def testFullAddress(self):
        with unittest.mock.patch('builtins.input', return_value='261 Prestwick RD, Watford, WD19 6XU'):
            function = fetchCoords()[0]
            output = [51.618485148176, -0.3897272736689019]
            self.assertAlmostEqual(function[0], output[0], delta=1)
            self.assertAlmostEqual(function[1], output[1], delta=1)

    def testNoInput(self):
        with unittest.mock.patch('builtins.input', return_value=None):
            self.assertFalse(fetchCoords())
    
    def testBadInput(self):
        with unittest.mock.patch('builtins.input', return_value='adsjlkfsawqbjkwqejbk'):
            self.assertFalse(fetchCoords())

class TestFetchCoordsLoop(unittest.TestCase):
    def testTownName(self):
        with unittest.mock.patch('builtins.input', return_value='watford'):
            function = fetchCoordsLoop()[0]
            output = [51.66090404041253, -0.3958991253953702]
            self.assertAlmostEqual(function[0], output[0], delta=1)
            self.assertAlmostEqual(function[1], output[1], delta=1)
    
    #def testNoInput(self):
    #    with unittest.mock.patch('builtins.input', return_value=None):
    #        self.assertFalse(fetchCoordsLoop())

if __name__ == '__main__':
    unittest.main()