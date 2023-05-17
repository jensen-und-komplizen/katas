import unittest


def do_fizz_buzz(number_input: int):
    return "fizz"



class TestNumberGenerator(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(do_fizz_buzz(3), "fizz")

    def test_buzz(self):
        self.assertEqual(do_fizz_buzz(5), "buzz")
