class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Assert if a string is a palindrome.
        """
        s = ''.join([char for char in s.lower() if char.isalnum()])
        return s == s[::-1]
