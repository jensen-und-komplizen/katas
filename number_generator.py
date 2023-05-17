import unittest

class TestNumberGenerator(unittest.TestCase):

    def test_generates_integers(self):
        self.assertTrue(generate_number() == type(int))
