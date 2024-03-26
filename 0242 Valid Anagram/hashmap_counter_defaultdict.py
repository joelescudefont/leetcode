from collections import defaultdict
from typing import Dict


class Solution:
    def valid_anagram(self, str1: str, str2: str) -> bool:
        """
        Assert if two strings are anagrams.
        """
        if len(str1) != len(str2):
            return False
        return self.count_characters(str1) == self.count_characters(str2)
  
    def count_characters(self, token: str) -> Dict[str, int]:
        """
        Build a counter of characters.
        """
        counter = defaultdict(int)
        for char in token:
            counter[char] += 1
        return counter
