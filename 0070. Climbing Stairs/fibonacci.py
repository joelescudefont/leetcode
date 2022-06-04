class Solution:
    def climbing_stairs(self, n: int) -> int:
        """
        Find how many distinct ways you can climb to the top of the stair.
        """
        prev = 1
        res = 2
        if n == prev:
            return n
        if n == res:
            return n
        for _ in range(n - 2):
            tmp = res
            res += prev
            prev = tmp
        return res
