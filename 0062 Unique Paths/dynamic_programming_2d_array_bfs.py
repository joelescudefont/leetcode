from collections import deque
from typing import List, Set


class Solution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

        self.grid: List[List[int]] = [[0 for _ in range(n)] for _ in range(m)]

        self.queue: deque = deque([(0, 0)])
        self.seen: Set = set()

    def count_unique_paths(self) -> int:
        self.grid[0][0] = 1  # top left

        self.bfs()  # traverse with breath-first search

        return self.grid[self.m - 1][self.n - 1]

    def bfs(self) -> None:
        while self.queue:
            cell = self.queue.popleft()

            if cell not in self.seen:
                self.seen.add(cell)  # save visited tile

                i, j = cell

                if i + 1 < self.m:
                    self.grid[i + 1][j] += self.grid[i][j]  # update down
                    self.queue.append((i + 1, j))

                if j + 1 < self.n:
                    self.grid[i][j + 1] += self.grid[i][j]  # update right
                    self.queue.append((i, j + 1))

        return


# Test cases
assert 2 == Solution(2, 2).count_unique_paths()
assert 3 == Solution(2, 3).count_unique_paths()
assert 6 == Solution(3, 3).count_unique_paths()
assert 28 == Solution(3, 7).count_unique_paths()
