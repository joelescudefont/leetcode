class Solution:
    def is_anagram(self, str1: str, str2: str) -> bool:
        """
        Assert if two strings are anagrams.
        """
        if len(str1) != len(str2):
            return False
        for char in str1:
            str2 = str2.replace(char, '', 1)
        return not str2
