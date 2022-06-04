from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Assert there is any value that appears at least twice.
        """
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if num1 == num2 and idx1 != idx2:
                    return True
        return False
