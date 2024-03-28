from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

        self.grid: List[int] = [1 for _ in range(n)]  # 1D array

    def count_unique_paths(self):
        self.dp()  # dynamic programming

        return self.grid[self.n - 1]  # bottom right

    def dp(self) -> None:
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.grid[j] = self.grid[j] + self.grid[j - 1]  # update inner cells

        return


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()
