import unittest
from vanity_plates import is_valid


class MyTestCase(unittest.TestCase):
    def test_plates_two_letters(self):
        assert is_valid("AB1234") is True
        assert is_valid("ABC123") is True
        assert is_valid("A123BC") is False
        assert is_valid("123ABC") is False

    def test_plates_len(self):
        assert is_valid("CS5005") is True
        assert is_valid("CS500") is True
        assert is_valid("CS50") is True
        assert is_valid("CS50501") is False

    def test_plates_numbers(self):
        assert is_valid("HEY101") is True
        assert is_valid("OH6666") is True
        assert is_valid("OH111S") is False
        assert is_valid("ABCDE6") is False

    def test_plates_punctuation(self):
        assert is_valid("VAL404") is True
        assert is_valid("VAL403") is True
        assert is_valid("CS50!!") is False
        assert is_valid("HEY,66") is False

    def test_plates_zero(self):
        assert is_valid("BCA210") is True
        assert is_valid("CAD409") is True
        assert is_valid("ABC011") is False
        assert is_valid("AB0123") is False


if __name__ == '__main__':
    unittest.main()
