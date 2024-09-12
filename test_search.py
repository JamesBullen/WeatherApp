import unittest
import unittest.mock
import sqlite3
from search import fetchCoords

class TestFetchCoords(unittest.TestCase):
    def testTownName(self):
        function = fetchCoords('attleborough', 10)
        output = ['Attleborough, UK', 'North West', 'North East', 'South West', 'South East']
        self.assertEqual(function[0], output)

    def testTownCoords(self):
        function = fetchCoords('attleborough', 10)
        output = [[52.518064, 52.62040482178106, 52.62040482178106, 52.41572317821895, 52.41572317821895], [1.015527, 0.8469517716254731, 1.184102228374527, 0.8477352790249622, 1.183318720975038]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)

    def testCityName(self):
        function = fetchCoords('london', 30)
        output = ['London, UK', 'North West', 'North East', 'South West', 'South East']
        self.assertEqual(function[0], output)

    def testCityCoords(self):
        function = fetchCoords('london', 30)
        output = [[51.5072178, 51.81424026534317, 51.81424026534317, 51.200195334656826, 51.200195334656826], [-0.1275862, -0.6242150894945779, 0.36904268949457797, -0.6175668889587284, 0.3623944889587283]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)

    def testFullAddressName(self):
        function = fetchCoords('Forbes of Kingennie Dr, Dundee DD5 3RD', 5)
        output = ['Kingennie, Dundee DD5 3RE, UK', 'North West', 'North East', 'South West', 'South East']
        self.assertEqual(function[0], output)

    def testFullAddressCoords(self):
        function = fetchCoords('Forbes of Kingennie Dr, Dundee DD5 3RD', 5)
        output = [[56.5063622, 56.557532610890526, 56.557532610890526, 56.45519178910947, 56.45519178910947], [-2.8439959, -2.9368474132776776, -2.751144386722322, -2.936597118666625, -2.751394681333375]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)

    # def testNoInput(self):
    #     self.assertFalse(fetchCoords())

    def testNoDistance(self):
        function = fetchCoords('london') # Defaults to 10
        output = [[51.5072178, 51.609558621781055, 51.609558621781055, 51.404876978218944, 51.404876978218944], [-0.1275862, -0.29238171619841447, 0.03720931619841447, -0.29164307277562473, 0.036470672775624685]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)
    
    # def testBadInput(self):
    #     self.assertFalse(fetchCoords())

if __name__ == '__main__':
    unittest.main()