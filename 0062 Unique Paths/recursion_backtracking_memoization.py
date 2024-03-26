from typing import Dict, Tuple


class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

        self.memo: Dict[Tuple[int, int]: int] = {(m, n): 1}

    def count_unique_paths(self) -> int:
        return self.backtrack(1, 1)  # start top left

    def backtrack(self, x: int, y: int) -> int:
        if (x, y) in self.memo:
            return self.memo[(x, y)]  # memoized tile

        if x > self.m or y > self.n:
            return 0

        self.memo[(x, y)] = self.backtrack(x + 1, y) + self.backtrack(x, y + 1)  # move down and right

        return self.memo[(x, y)]


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()
