import unittest


def do_something():
    pass


class TestNumberGenerator(unittest.TestCase):

    def test_something_that_can_be_done(self):
        return True

    def test_is_fizz(self):
        self.assertTrue(type(make_fizz()) == str)
