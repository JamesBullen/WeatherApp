import unittest
import unittest.mock
from search import fetchCoords

class TestFetchMethod(unittest.TestCase):
    def test_town_name(self):
        # watford
        self.assertAlmostEqual(fetchCoords('watford')[0][0], 51.66090404041253, delta=1)
        self.assertAlmostEqual(fetchCoords('watford')[0][1], -0.3958991253953702, delta=1)

    def test_city_name(self):
        # london
        self.assertAlmostEqual(fetchCoords('london')[0][0], 51.50502529339357, delta=1)
        self.assertAlmostEqual(fetchCoords('london')[0][1], -0.1311339760081772, delta=1)

    def test_full_address(self):
        # 261 Prestwick RD, Watford, WD19 6XU
        self.assertAlmostEqual(fetchCoords('261 Prestwick RD, Watford, WD19 6XU')[0][0], 51.618485148176, delta=1)
        self.assertAlmostEqual(fetchCoords('261 Prestwick RD, Watford, WD19 6XU')[0][1], -0.3897272736689019, delta=1)

    def test_no_input(self):
        with unittest.mock.patch('builtins.input', return_value='261 Prestwick RD, Watford, WD19 6XU'):
            self.assertAlmostEqual(fetchCoords()[0][0], 51.618485148176, delta=1)

if __name__ == '__main__':
    unittest.main()