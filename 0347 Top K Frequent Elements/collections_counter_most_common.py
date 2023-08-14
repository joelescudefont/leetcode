from collections import Counter
from typing import List

import pytest


class Solution:
    # Find the top most frequent elements
    @staticmethod
    def find_top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
        return [elem for elem, _ in Counter(nums).most_common(k)]


@pytest.mark.parametrize("expected,k,nums", [
    ([], 1, []),
    ([1], 1, [1]),
    ([2], 1, [1, 2, 2, 3]),
    ([2, 1], 2, [1, 2, 2, 3]),
    ([2, 1, 3], 3, [1, 2, 2, 3]),
])
def test_find_top_k_frequent_elements(expected, k, nums):
    assert set(expected) == set(Solution().find_top_k_frequent_elements(nums, k))
