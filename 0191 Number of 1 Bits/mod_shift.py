class Solution:
    def hamming_weight(self, n: int) -> int:
        """
        Count the number of bits one.
        """
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res
