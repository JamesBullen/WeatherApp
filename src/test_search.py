import unittest
from search import fetchCoords

class TestFetchMethod(unittest.TestCase):
    def test_town_name(self):
        self.assertAlmostEqual(fetchCoords('watford')[0], 51.66090404041253, delta=1)
        self.assertAlmostEqual(fetchCoords('watford')[1], -0.3958991253953702, delta=1)

    def test_city_name(self):
        self.assertAlmostEqual(fetchCoords('london')[0], 51.50502529339357, delta=1)
        self.assertAlmostEqual(fetchCoords('london')[1], -0.1311339760081772, delta=1)

    def test_full_address(self):
        self.assertAlmostEqual(fetchCoords('261 Prestwick RD, Watford, WD19 6XU')[0], 51.618485148176, delta=1)
        self.assertAlmostEqual(fetchCoords('261 Prestwick RD, Watford, WD19 6XU')[1], -0.3897272736689019, delta=1)

if __name__ == '__main__':
    unittest.main()