import unittest


def divisible(n:int) -> str:
    if n % 3 == 0:
        return "fizz"
    else:
        return str(int)


class TestNumberGenerator(unittest.TestCase):

    def test_buzz(self):
        self.assertTrue(
            divisible(3) == "fizz"
        )
