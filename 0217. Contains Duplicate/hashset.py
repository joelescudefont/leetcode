from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Assert there is any value that appears at least twice.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
