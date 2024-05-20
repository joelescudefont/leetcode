from math import factorial


class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

    def unique_paths(self) -> int:
        numerator = factorial(self.m + self.n - 2)
        denominator = factorial(self.m - 1) * factorial(self.n - 1)
        return numerator // denominator


# Test cases
assert 2 == Solution(2, 2).unique_paths()
assert 3 == Solution(2, 3).unique_paths()
assert 6 == Solution(3, 3).unique_paths()
assert 28 == Solution(3, 7).unique_paths()
