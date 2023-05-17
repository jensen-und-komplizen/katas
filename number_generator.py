import unittest


def generate_number():
    return 10


class TestNumberGenerator(unittest.TestCase):

    def test_generates_integers(self):
        self.assertTrue(type(generate_number()) == int)

    def test_at_least_two_digits(self):
        self.assertTrue(generate_number() > 9)

    def test_generate_odd_numbers(self):
        self.assertTrue(generate_number() % 2 is not 0)
