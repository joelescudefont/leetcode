from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        """
        Count the number of bits one.
        """
        res = [0]
        if n == 0:
            return res
        block = 1
        for idx in range(1, n + 1):
            if idx % (2 * block) == 0:
                block *= 2
            res.append(1 + res[idx - block])
        return res
