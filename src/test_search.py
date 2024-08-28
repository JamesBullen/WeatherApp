import unittest
import unittest.mock
from search import fetchCoords

# Assuming empty database
class TestFetchCoords(unittest.TestCase):
    def testTownName(self):
        function = fetchCoords('dundee', 10)
        output = ['Dundee, UK', 'North West', 'North East', 'South West', 'South East']
        self.assertEqual(function[0], output)

    def testTownCoords(self):
        function = fetchCoords('dundee', 10)
        output = [[56.462018, 56.564358821781056, 56.564358821781056, 56.359677178218945, 56.359677178218945], [-2.970721, -3.1564575336280933, -2.784984466371907, -3.155459196861468, -2.7859828031385323]]
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
        function = fetchCoords('261 Prestwick RD, Watford, WD19 6XU', 15)
        output = ['261 Prestwick Rd, Watford WD19 6XU, UK', 'North West', 'North East', 'South West', 'South East']
        self.assertEqual(function[0], output)

    def testFullAddressCoords(self):
        function = fetchCoords('261 Prestwick RD, Watford, WD19 6XU', 15)
        output = [[51.6184119, 51.77192313267159, 51.77192313267159, 51.46490066732841, 51.46490066732841], [-0.389738, -0.6378195540800995, -0.14165644591990045, -0.6361468679748173, -0.14332913202518258]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)

    # def testNoInput(self):
    #     self.assertFalse(fetchCoords())

    def testNoDistance(self):
        function = fetchCoords('london')
        output = [[51.5072178, 51.609558621781055, 51.609558621781055, 51.404876978218944, 51.404876978218944], [-0.1275862, -0.29238171619841447, 0.03720931619841447, -0.29164307277562473, 0.036470672775624685]]
        for i in range(len(output)):
            self.assertAlmostEqual(function[1][i], output[i], delta=1)
    
    # def testBadInput(self):
    #     self.assertFalse(fetchCoords())

if __name__ == '__main__':
    unittest.main()