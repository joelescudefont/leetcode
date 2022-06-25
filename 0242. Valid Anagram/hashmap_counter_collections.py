from collections import Counter


class Solution:
    def is_anagram(self, str1: str, str2: str) -> bool:
        """
        Assert if two strings are anagrams.
        """
        if len(str1) != len(str2):
            return False
        return Counter(str1) == Counter(str2)
