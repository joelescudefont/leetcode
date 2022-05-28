from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Get the indices of the two elements that sum together to a given target.
        """
        seen = {}
        for idx, num in enumerate(nums):
            if num in seen:
                return [seen[num], idx]
            seen[target - num] = idx
        return []
