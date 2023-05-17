import unittest


def generate_number():
    return 0


class TestNumberGenerator(unittest.TestCase):

    def test_generates_integers(self):
        self.assertTrue(type(generate_number()) == int)

    def test_at_least_two_digits(self):
        self.assertTrue(generate_number() > 9)
