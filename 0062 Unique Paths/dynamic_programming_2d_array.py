from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

        self.grid: List[List[int]] = [[0] * n for _ in range(m)]  # 2D array

    def count_unique_paths(self):
        self.dp()  # top-down dynamic programming

        return self.grid[self.m - 1][self.n - 1]  # bottom right

    def dp(self) -> None:
        for i in range(self.m):
            for j in range(self.n):
                if i == 0:
                    self.grid[0][j] = 1  # top row

                elif j == 0:
                    self.grid[i][0] = 1  # left column

                else:
                    self.grid[i][j] = self.grid[i - 1][j] + self.grid[i][j - 1]  # update inner cells

        return


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()
