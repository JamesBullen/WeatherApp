import unittest
import unittest.mock
from report import printReport, getForecast

class TestPrintReport(unittest.TestCase):
    def test(self):
        input = 0
        function = getForecast(input)
        output = 'Clear Skies'
        self.assertEqual(function, output)

class TestGetForecast(unittest.TestCase):
    def testNormal(self):
        input = 0
        function = getForecast(input)
        output = 'Clear Skies'
        self.assertEqual(function, output)

    def testWrongNumber(self):
        input = '100'
        function = getForecast(input)
        output = 'Unknown'
        self.assertEqual(function, output)

    def testNonNumber(self):
        input = 'string'
        function = getForecast(input)
        output = 'Unknown'
        self.assertEqual(function, output)

    def testEmpty(self):
        input = None
        function = getForecast(input)
        output = 'Unknown'
        self.assertEqual(function, output)

if __name__ == '__main__':
    unittest.main()