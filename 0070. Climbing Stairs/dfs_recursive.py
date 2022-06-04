class Solution:
    def climbing_stairs(self, n: int) -> int:
        """
        Find how many distinct ways you can climb to the top of the stair.
        """
        if n == 0:
            return 1
        if n == -1:
            return 0
        return self.climbing_stairs(n - 1) + self.climbing_stairs(n - 2)
