class Solution:
    def __init__(self):
        self.seen = {0: 1, -1: 0}

    def climbing_stairs(self, n: int) -> int:
        """
        Find how many distinct ways you can climb to the top of the stair.
        """
        if n in self.seen:
            return self.seen[n]
        self.seen[n] = self.climbing_stairs(n - 2) + self.climbing_stairs(n - 1)
        return self.seen[n]
