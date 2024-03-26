from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Get the indices of the two elements that sum together to a given target.
        """
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1 + 1:]):
                if target == num1 + num2:
                    return [idx1, idx2 + idx1 + 1]
        else:
            raise Exception('Indices not found!')
