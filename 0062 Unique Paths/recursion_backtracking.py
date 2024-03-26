class Solution:
    def __init__(self, m: int, n: int) -> None:
        self.m: int = m
        self.n: int = n

    def count_unique_paths(self) -> int:
        return self.backtrack(1, 1)  # start top left

    def backtrack(self, x: int, y: int) -> int:
        if x == self.m and y == self.n:
            return 1  # base case

        if x > self.m or y > self.n:
            return 0

        return self.backtrack(x + 1, y) + self.backtrack(x, y + 1)  # move down and right


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()