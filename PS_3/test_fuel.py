import unittest
from fuel_gauge import get_fuel, get_gauge
import unittest.mock


class MyTestCase(unittest.TestCase):
    def test_get_fuel(self):
        with unittest.mock.patch('builtins.input', return_value = '1/2'):
            self.assertEqual(get_fuel(), 50)

        with unittest.mock.patch('builtins.input', return_value='1/3'):
            self.assertEqual(get_fuel(), 33)

        with unittest.mock.patch('builtins.input', return_value='3/4'):
            self.assertEqual(get_fuel(), 75)

        # with unittest.mock.patch('builtins.input', return_value='3/0'):
        #     self.assertRaises(ZeroDivisionError, get_fuel)

        # with unittest.mock.patch('builtins.input', return_value='abc'):
        #     self.assertRaises(ValueError, get_fuel)

    def test_get_gauge(self):
        assert get_gauge(33) == '33%'
        assert get_gauge(55) == '55%'
        assert get_gauge(1) == 'E'
        assert get_gauge(100) == 'F'

if __name__ == '__main__':
    unittest.main()
