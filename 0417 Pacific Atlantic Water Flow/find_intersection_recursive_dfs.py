"""
0417 Pacific Atlantic Water Flow

SOLUTION: Optimized, find the shared highest points comparing the traversing from each ocean sides.

Find the positions with the highest point (increasing or equal value) from
- the Pacific ocean North and West borders
- the Atlantic ocean South and East borders

Find the intersection between both sides.


Example:

1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4

From the Pacific sides:
1 2 2 3 5
3 2 3 4 4
2 4 5 - -
6 7 - - -
5 - - - -

From the Atlantic sides:
- - - - 5
- - - 4 4
- - 5 3 1
6 7 1 4 5
5 1 1 2 4

The intersection between both ocean sides:
- - - - 5
- - - 4 4
- - 5 - -
6 7 - - -
5 - - - -


Position (0, 4) with value 5 appears both in
- Pacitic left to right: 1 < 2 <= 2 < 3 < 5 (highest)
- Atlantic right to left: 5 (highest)
- Pacific top to bottom (repeated)

Position (3, 4) with value 5 only appears in
- Atlantic right to left
- Atlantic bottom to top
- but not from the Pacific sides


TC: O( NM )
SC: O( NM )

"""


from typing import List, Set, Tuple

import pytest


class Solution:
    def __init__(self, heights: List[List[int]]):
        self.grid: List[List[int]] = heights

        self.nrows: int = len(heights)
        self.ncols: int = len(heights[0])

        self.seen: Set[Tuple[int, int]] = set()

        self.coordinates: List[List[int]] = []

    def find_flows(self) -> List[List[int]]:
        """
        Find flows from each ocean border.
        """
        # From the Pacific ocean
        self.seen = set()

        self.from_west()
        self.from_north()

        pacific = self.seen

        # From the Atlantic ocean
        self.seen = set()

        self.from_east()
        self.from_south()

        atlantic = self.seen

        # Get the intersection
        self.get_intersection(pacific, atlantic)

        return self.coordinates

    def from_west(self) -> None:
        """
        Traverse from the West side of the Pacific ocean.
        """
        for irow in range(self.nrows):
            self.traverse(irow, 0)

        return

    def from_north(self):
        """
        Traverse from the North side of the Pacific ocean.
        """
        for icol in range(self.ncols):
            self.traverse(0, icol)

        return

    def from_east(self):
        """
        Traverse from the East side of the Atlantic ocean.
        """
        for irow in range(self.nrows):
            self.traverse(irow, self.ncols - 1)

        return

    def from_south(self):
        """
        Traverse from the South side of the Atlantic ocean.
        """
        for icol in range(self.ncols):
            self.traverse(self.nrows - 1, icol)

        return

    def traverse(self, irow: int, icol: int) -> None:
        """
        Traverse a flow uphill.
        """
        if (irow, icol) in self.seen:
            return

        self.seen.add((irow, icol))

        # top
        if irow - 1 >= 0 and self.grid[irow - 1][icol] >= self.grid[irow][icol]:
            self.traverse(irow - 1, icol)

        # right
        if icol + 1 < self.ncols and self.grid[irow][icol + 1] >= self.grid[irow][icol]:
            self.traverse(irow, icol + 1)

        # bottom
        if irow + 1 < self.nrows and self.grid[irow + 1][icol] >= self.grid[irow][icol]:
            self.traverse(irow + 1, icol)

        # left
        if icol - 1 >= 0 and self.grid[irow][icol - 1] >= self.grid[irow][icol]:
            self.traverse(irow, icol - 1)

        return

    def get_intersection(self, pacific: Set[Tuple[int, int]], atlantic: Set[Tuple[int, int]]) -> None:
        """
        Get the highest intersection points from both oceans.
        """
        intersection = pacific & atlantic

        self.coordinates = [list(item) for item in intersection]


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
    (
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            [[1, 2, 2, 3, 5],
             [3, 2, 3, 4, 4],
             [2, 4, 5, 3, 1],
             [6, 7, 1, 4, 5],
             [5, 1, 1, 2, 4]]
    ),
])
def test_find_flows(expected, grid):
    actual = Solution(grid).find_flows()

    assert set([tuple(e) for e in expected]) == set([tuple(a) for a in actual])
