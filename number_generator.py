import unittest


def do_fizz_buzz(number_input: int):
    if number_input % 3 == 0:
        return "fizz"
    if number_input % 5 == 0:
        return "buzz"


class TestNumberGenerator(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(do_fizz_buzz(3), "fizz")

    def test_buzz(self):
        self.assertEqual(do_fizz_buzz(5), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(do_fizz_buzz(15), "fizzbuzz")
