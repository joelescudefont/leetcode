from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Assert there is any value that appears at least twice.
        """
        return len(nums) > len(set(nums))
