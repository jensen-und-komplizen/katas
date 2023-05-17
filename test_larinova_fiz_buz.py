import unittest


def fiz_buz_generator(number):
    if (number % 3 == 0) and (number % 5 == 0): return "fizbuz"
    if number % 3 == 0: return 'fiz'
    if number % 5 == 0: return 'buz'
    
    return str(number)


class TestNumberGenerator(unittest.TestCase):

    def test_dividable_by_three_returns_fiz(self):
        self.assertTrue(fiz_buz_generator(3) == 'fiz')

    def test_is_string(self):
        self.assertTrue(isinstance(fiz_buz_generator(234), str))

    def test_dividable_by_five_returns_buz(self):
        self.assertTrue(fiz_buz_generator(80) == "buz")

    def test_dividable_by_five_and_three_returns_fizbuz(self):
        self.assertTrue(fiz_buz_generator(75) == "fizbuz")
        
    def test_not_dividable_by_five_and_three_or_five_or_three_returns_fizbus(self):
        self.assertTrue(fiz_buz_generator(7) == "7")
