"""
417



1 1 1
1 1 1
1 1 1
all positions

1 1 1
1 2 1
1 1 1
all positions

1 1 2
1 2 1
2 1 1
the diagonal of 2s

1 2 2
2 2 2
2 2 1
all 2s

2 3 4
3 1 3
4 3 2
the two 4 extremes only



BRUTE FORCE O( (N*M)^2 )
- traverse the grid
- graph traversal: at each cell, check if there's a path to both oceans: explore top, right, bottom, left cells until both ocean edges are checked
-- Pacific sea: top or left border
-- Atlantic ocean: right or bottom border
- return the list of positions that have a path to both oceans



"""

from typing import List

import pytest


class Solution:
    def __init__(self):
        self.heights: List[List[int]] = []

        self.nrows: int = 0
        self.ncols: int = 0

        self.coordinates: List[List[int]] = []

    def find_flows(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights

        self.traverse_grid()

        return self.coordinates

    def traverse_grid(self) -> None:
        """
        Traverse the island.
        """
        self.nrows = len(self.heights)
        self.ncols = len(self.heights[0])

        for irow in range(self.nrows):
            for icol in range(self.ncols):
                if self.check_pacific(irow, icol) and self.check_atlantic(irow, icol):
                    self.coordinates.append([irow, icol])

    def check_pacific(self, irow: int, icol: int) -> bool:
        """
        Check the flow to the Pacific ocean.
        """
        if irow - 1 == -1 or icol - 1 == -1:
            return True

        height = self.heights[irow][icol]

        top, left, bottom, right = False, False, False, False

        if self.heights[irow - 1][icol] <= height:
            top = self.check_pacific(irow - 1, icol)

        if self.heights[irow][icol - 1] <= height:
            left = self.check_pacific(irow, icol - 1)

        if irow + 1 <= self.nrows - 1 and self.heights[irow + 1][icol] <= height:
            bottom = self.check_pacific(irow + 1, icol)

        if icol + 1 <= self.ncols - 1 and self.heights[irow][icol + 1] <= height:
            right = self.check_pacific(irow, icol + 1)

        return top or left or bottom or right

    def check_atlantic(self, irow: int, icol: int) -> bool:
        """
        Check the flow to the Atlantic ocean.
        """
        if irow + 1 == self.nrows or icol + 1 == self.ncols:
            return True

        height = self.heights[irow][icol]

        top, left, bottom, right = False, False, False, False

        if self.heights[irow + 1][icol] <= height:
            bottom = self.check_atlantic(irow + 1, icol)

        if self.heights[irow][icol + 1] <= height:
            right = self.check_atlantic(irow, icol + 1)

        if irow - 1 >= 0 and self.heights[irow - 1][icol] <= height:
            top = self.check_atlantic(irow - 1, icol)

        if icol - 1 >= 0 and self.heights[irow][icol - 1] <= height:
            left = self.check_atlantic(irow, icol - 1)

        return top or left or bottom or right


@pytest.mark.parametrize("expected,grid", [
    (
            [[0, 0]],
            [[1]]
    ),
    (
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            [[1, 1],
             [1, 1]]
    ),
    (
            [[0, 1], [1, 0]],
            [[1, 2],
             [2, 1]]
    ),
    (
            [[0, 2], [1, 1], [2, 0]],
            [[1, 2, 3],
             [2, 3, 2],
             [3, 2, 1]]
    ),
    # (
    #         [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    #         [[1, 2, 2, 3, 5],
    #          [3, 2, 3, 4, 4],
    #          [2, 4, 5, 3, 1],
    #          [6, 7, 1, 4, 5],
    #          [5, 1, 1, 2, 4]]
    # ),
])
def test_find_flows(expected, grid):
    assert expected == Solution().find_flows(grid)
