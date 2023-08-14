from typing import List

import pytest


class Solution:
    def __init__(self):
        self.counter = {}

    # Find the top most frequent elements
    def find_top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        self.build_counter(nums)
        return self.find_top(k)

    # Build counter
    def build_counter(self, nums: List[int]):
        self.counter = {}

        for num in nums:
            if num in self.counter:
                self.counter[num] += 1

            else:
                self.counter[num] = 1

    # Find the top most frequent elements from an unsorted counter
    def find_top(self, top: int) -> List[int]:
        pairs = sorted(self.counter.items(), key=lambda item: item[1], reverse=True)
        return [elem for elem, count in pairs[:top]]


@pytest.mark.parametrize("expected,k,nums", [
    ([], 1, []),
    ([1], 1, [1]),
    ([2], 1, [1, 2, 2, 3]),
    ([2, 1], 2, [1, 2, 2, 3]),
    ([2, 1, 3], 3, [1, 2, 2, 3]),
])
def test_find_top_k_frequent_elements(expected, k, nums):
    assert set(expected) == set(Solution().find_top_k_frequent_elements(nums, k))
