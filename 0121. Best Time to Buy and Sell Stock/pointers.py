from typing import List


class Solution:
    def maximum_profit(self, prices: List[int]) -> int:
        """
        Find the maximum profit.
        """
        res = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            if prices[right] - prices[left] > res:
                res = prices[right] - prices[left]
            right += 1
        return res
