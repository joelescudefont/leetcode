class Solution:
    def is_anagram(self, str1: str, str2: str) -> bool:
        """
        Assert if two strings are anagrams.
        """
        if len(str1) != len(str2):
            return False
        seen = []
        for char1 in list(str1):
            for idx2, char2 in enumerate(list(str2)):
                if char1 == char2 and idx2 not in seen:
                    seen.append(idx2)
                    break
            else:
                return False
        return True
