class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

        self.count: int = 0

    def count_unique_paths(self) -> int:
        self.backtrack(1, 1)  # start top left

        return self.count

    def backtrack(self, x: int, y: int) -> None:
        if x == self.m and y == self.n:
            self.count += 1  # base case

            return

        if x < self.m:
            self.backtrack(x + 1, y)  # move right

        if y < self.n:
            self.backtrack(x, y + 1)  # move down

        return


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()
