import unittest

def divisible(n:int) -> str:
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return str(int)


class TestNumberGenerator(unittest.TestCase):
    def test_fizz(self):
        self.assertTrue(
            divisible(3) == "fizz"
        )
    def test_buzz(self):
        self.assertTrue(
            divisible(5) == "buzz"
        )
