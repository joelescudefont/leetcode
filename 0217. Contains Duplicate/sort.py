from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Assert there is any value that appears at least twice.
        """
        nums.sort()
        for idx in range(len(nums)):
            if idx == 0:
                continue
            if nums[idx] == nums[idx - 1]:
                return True
        return False
