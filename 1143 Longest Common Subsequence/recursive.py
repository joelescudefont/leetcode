class Solution:
    def __init__(self, text1: str, text2: str):
        self.text1: str = text1
        self.text2: str = text2

    def longest_common_subsequence(self):
        return self._recursion(len(self.text1), len(self.text2))

    def _recursion(self, n1: int, n2: int):
        # base case: if either string is empty
        if n1 == 0 or n2 == 0:
            return 0

        # if the last character of both strings match
        elif self.text1[n1 - 1] == self.text2[n2 - 1]:
            return 1 + self._recursion(n1 - 1, n2 - 1)

        # if the last character does not match
        else:
            return max(self._recursion(n1 - 1, n2), self._recursion(n1, n2 - 1))


# Test cases
assert 0 == Solution("", "").longest_common_subsequence()
assert 0 == Solution("abc", "de").longest_common_subsequence()
assert 1 == Solution("abc", "bd").longest_common_subsequence()
assert 2 == Solution("abcd", "bd").longest_common_subsequence()
