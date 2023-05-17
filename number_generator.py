import unittest


def generate_number():
    return 11


class TestNumberGenerator(unittest.TestCase):

    def test_is_integer(self):
        self.assertTrue(type(generate_number()) == int)

    def test_has_at_least_two_digits(self):
        self.assertTrue(generate_number() > 9)

    def test_is_odd_number(self):
        self.assertTrue(generate_number() % 2 != 0)

