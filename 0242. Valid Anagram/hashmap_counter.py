from typing import Dict


class Solution:
    def is_anagram(self, str1: str, str2: str) -> bool:
        """
        Assert if two strings are anagrams.
        """
        if len(str1) != len(str2):
            return False
        counter1 = self.count_characters(str1)
        counter2 = self.count_characters(str2)
        for char in counter1:
            if counter1[char] != counter2.get(char, 0):
                return False
        return True

    def count_characters(self, s: str) -> Dict[str, int]:
        """
        Build a counter of characters.
        """
        counter = {}
        for idx in range(len(s)):
            counter[s[idx]] = counter.get(s[idx], 0) + 1
        return counter
