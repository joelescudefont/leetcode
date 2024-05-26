from typing import List
from itertools import combinations


class Solution:
    def __init__(self, text_1: str, text_2: str):
        self.text_1: str = text_1
        self.text_2: str = text_2

    def longest_common_subsequence(self):
        subsequences_1 = self._generate_subsequences(self.text_1)
        subsequences_2 = self._generate_subsequences(self.text_2)

        return self._find_longest_subsequence(subsequences_1, subsequences_2)

    @staticmethod
    def _generate_subsequences(text: str) -> List[str]:
        subsequences = []

        for n in range(len(text) + 1):
            for combination in combinations(text, n):
                subsequences.append(''.join(combination))

        return subsequences

    @staticmethod
    def _find_longest_subsequence(subsequences_1: List[str], subsequences_2: List[str]) -> int:
        longest = 0

        for sub_1 in subsequences_1:
            for sub_2 in subsequences_2:
                if sub_1 == sub_2:
                    longest = max(longest, len(sub_1))

        return longest


# Test cases
assert 0 == Solution("", "").longest_common_subsequence()
assert 0 == Solution("abc", "de").longest_common_subsequence()
assert 1 == Solution("abc", "bd").longest_common_subsequence()
assert 2 == Solution("abcd", "bd").longest_common_subsequence()
