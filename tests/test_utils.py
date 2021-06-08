import unittest
from src import utils


class testUtils(unittest.TestCase):

    def test_get_risk(self):
        self.assertEqual(
            utils.get_risk(10),
            "Malnutrition"
        )
        self.assertEqual(
            utils.get_risk(24.9),
            "Enhanced"
        )
        self.assertNotEqual(
            utils.get_risk(39.9),
            "High"
        )

    def test_get_bmi(self):
        self.assertEqual(
            utils.get_bmi(8, 200),
            2
        )
        self.assertNotEqual(
            utils.get_bmi(8, 300),
            2
        )

if __name__ == '__main__':
    unittest.main()
