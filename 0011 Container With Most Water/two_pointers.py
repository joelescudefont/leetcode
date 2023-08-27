"""

11 Container With Most Water


1, 8, 6, 2, 5, 4, 8, 3, 7 	=> Max area = 49



SOLUTION: Brute Force

TC: O(n^2)
SC: O(1)




SOLUTION: Two pointers

TC: O(n)
SC: O(1)


4  4  4  4
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
---------- x

4, 4, 4, 4 	=> Max area: 12 = (4-1)*min(4,4)



4  1  1  4
|        |
|        |
|        |
|  |  |  |
---------- x

4, 1, 1, 4 	=> Max area: 12 = (4-1)*min(4,4)



1  2  3  4
         |
      |  |
   |  |  |
|  |  |  |
---------- x

1, 2, 3, 4 	=> Max area: 8 = (4-2)*min(2, 4)



1  5  5  1  1
   |  |
   |  |
   |  |
   |  |
|  |  |  |  |
------------- x

1, 5, 5, 1, 1

=> Prev area: 4 = (4-0)*min(1,1)
=> Max area: 5 = (3-2)*min(5,5)

CONDITION: More height = more potential.

l=0,r=4: Both pointers have the same potential. Move left +1.
l=1,r=4: Keeping the left pointer has more potential. Move right -1.
l=1,r=3: Keeping the left pointer more potential. Move right -1.
l=1,r=2: Max area.


MAX AREA: (x1 - x0) * min(height0, height1)

=> MAX AREA: ( x1 * min height ) - ( x0 * min height )

"""

from typing import List

import pytest


class Solution:
    @staticmethod
    def find_max_area(heights: List[int]) -> int:
        largest = 0

        l = 0
        r = len(heights) - 1

        while r - l > 0:
            area = (r - l) * min(heights[l], heights[r])

            if area > largest:
                largest = area

            if heights[l] > heights[r]:
                r -= 1

            else:
                l += 1

        return largest


@pytest.mark.parametrize("expected,nums", [
    (12, [4, 4, 4, 4]),
    (12, [4, 1, 1, 4]),
    (4, [1, 2, 3, 4]),
    (5, [1, 5, 5, 1, 1]),
])
def test_find_max_area(expected, nums):
    assert expected == Solution().find_max_area(nums)
