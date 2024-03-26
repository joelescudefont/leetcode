class Solution:
    def hamming_weight(self, n: int) -> int:
        """
        Count the number of bits one.
        """
        res = 0
        while n:
            res += 1
            n &= (n - 1)
        return res
