import unittest
import unittest.mock
from search import fetchCoords, fetchCoordsLoop

class TestFetchCoords(unittest.TestCase):
    def testTownName(self):
        # watford
        with unittest.mock.patch('builtins.input', return_value='watford'):
            self.assertAlmostEqual(fetchCoords()[0][0], 51.66090404041253, delta=1)
            self.assertAlmostEqual(fetchCoords()[0][1], -0.3958991253953702, delta=1)

    def testCityName(self):
        # london
        with unittest.mock.patch('builtins.input', return_value='london'):
            self.assertAlmostEqual(fetchCoords()[0][0], 51.50502529339357, delta=1)
            self.assertAlmostEqual(fetchCoords()[0][1], -0.1311339760081772, delta=1)

    def testFullAddress(self):
        with unittest.mock.patch('builtins.input', return_value='261 Prestwick RD, Watford, WD19 6XU'):
            self.assertAlmostEqual(fetchCoords()[0][0], 51.618485148176, delta=1)
            self.assertAlmostEqual(fetchCoords()[0][1], -0.3897272736689019, delta=1)

    def testNoInput(self):
        with unittest.mock.patch('builtins.input', return_value=None):
            self.assertFalse(fetchCoords())
    
    def testBadInput(self):
        with unittest.mock.patch('builtins.input', return_value='adsjlkfsawqbjkwqejbk'):
            #self.assertRaises(Exception, fetchCoords())
            self.assertFalse(fetchCoords())

class TestFetchCoordsLoop(unittest.TestCase):
    def testTownName(self):
        with unittest.mock.patch('builtins.input', return_value='watford'):
            self.assertAlmostEqual(fetchCoordsLoop()[0][0], 51.66090404041253, delta=1)
            self.assertAlmostEqual(fetchCoordsLoop()[0][1], -0.3958991253953702, delta=1)
    
    #def testNoInput(self):
    #    with unittest.mock.patch('builtins.input', return_value=None):
    #        self.assertFalse(fetchCoordsLoop())

if __name__ == '__main__':
    unittest.main()