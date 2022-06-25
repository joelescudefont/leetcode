from typing import List


class Solution:
    def counting_bits(self, n: int) -> List[int]:
        """
        Count the number of ones in the binary representation for each index.
        """
        res = []
        for idx in range(n + 1):
            res.append(self.hamming_weight(idx))
        return res

    def hamming_weight(self, n: int) -> int:
        """
        Count the number of 1 bits.
        """
        count = 0
        while n:
            count += n % 2
            n = int(n / 2)
        return count
