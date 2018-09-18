import unittest
from TimeString import TimeString
class TestTimeString(unittest.TestCase):

    def test_str_to_hours(self):
        data = {'1h': 1, '1d': 24, '1d4h': 28, '2w3d': 408}
        for value, exp in data.items():
            self.assertEqual(exp, TimeString.to_hours(value))

    def test_hours_to_str(self):
        data = {'1h': 1, '1d': 24, '1d4h': 28, '2w3d': 408, '5y34w':49512}
        for exp, value in data.items():
            self.assertEqual(exp, TimeString.convert(value))


if __name__ == '__main__':
    unittest.main()
