import unittest


def do_something():
    pass

def ttt():
    pass

class TestNumberGenerator(unittest.TestCase):

    def test_something_that_can_be_done(self):
        return True

    def test_fizz(self):
        self.assertTrue(type(ttt()) == str)
