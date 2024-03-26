from typing import List


class Solution:
    def maximum_profit(self, prices: List[int]) -> int:
        """
        Find the maximum profit.
        """
        res = 0
        buy = prices[0]
        for price in prices[1:]:
            buy = min(buy, price)
            res = max(res, price - buy)
        return res
