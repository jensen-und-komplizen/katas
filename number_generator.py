import unittest


def do_fizz_buzz():
    pass


class TestNumberGenerator(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(do_fizz_buzz(3), "fizz")
