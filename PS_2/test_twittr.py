import unittest
from twttr import shorten


class MyTestCase(unittest.TestCase):
    def test_twttr(self):
        assert shorten('love') == 'lv'
        assert shorten('LOVE') == 'LV'
        assert shorten('love, world') == 'lv, wrld'
        assert shorten('1 LOVE') == '1 LV'


if __name__ == '__main__':
    unittest.main()
