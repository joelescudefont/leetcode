from typing import List


class Solution:
    def __init__(self, text1: str, text2: str):
        self.text1: str = text1
        self.text2: str = text2

        self.n: int = len(text1)
        self.m: int = len(text2)

        # initiate a 2D table, for each length plus an empty string
        self._table: List[List[int]] = [[0] * (self.m + 1) for _ in range(self.n + 1)]

    def longest_common_subsequence(self) -> int:
        self._dp()

        return self._table[self.n][self.m]

    def _dp(self) -> None:
        # fill the 2D table
        for idx1, char1 in enumerate(self.text1, start=1):
            for idx2, char2 in enumerate(self.text2, start=1):
                # if the character of both strings match
                if char1 == char2:
                    self._table[idx1][idx2] = 1 + self._table[idx1 - 1][idx2 - 1]

                # if the character does not match
                else:
                    self._table[idx1][idx2] = max(self._table[idx1 - 1][idx2], self._table[idx1][idx2 - 1])

        return


# Test cases
assert 0 == Solution("", "").longest_common_subsequence()
assert 0 == Solution("abc", "de").longest_common_subsequence()
assert 1 == Solution("abc", "bd").longest_common_subsequence()
assert 2 == Solution("abcd", "bd").longest_common_subsequence()
assert 5 == Solution("abcba", "abcbcba").longest_common_subsequence()
