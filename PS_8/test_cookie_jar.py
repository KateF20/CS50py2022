import unittest
from cookie_jar import Jar


class MyTestCase(unittest.TestCase):
    jar = Jar(9)

    def test_init(self):
        self.assertEqual(self.jar.capacity, 9)

    def test_str(self):
        self.jar.deposit(1)
        self.assertEqual(str(self.jar), '🍪')
        self.jar.deposit(11)
        self.assertEqual(str(self.jar), '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪')

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.jar.deposit(13)
            self.jar.deposit(25)
            self.jar.deposit(-1)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.jar.withdraw(13)
            self.jar.withdraw(25)
            self.jar.withdraw(-1)


if __name__ == '__main__':
    unittest.main()
