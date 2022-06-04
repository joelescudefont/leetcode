from typing import List


class Solution:
    def maximum_profit(self, prices: List[int]) -> int:
        """
        Find the maximum profit.
        """
        res = 0
        for idx1, price1 in enumerate(prices):
            for price2 in prices[idx1 + 1:]:
                res = max(res, price2 - price1)
        return res
