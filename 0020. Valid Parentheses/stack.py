class Solution:
    def is_valid(self, s: str) -> bool:
        """
        Assert that the parentheses open and close in the correct order by the same type of bracket.
        """
        pairs = {"(": ")", "[": "]", "{": "}"}
        openers = []
        for par in s:
            if par in pairs:
                openers.append(par)
                continue
            if openers and par == pairs[openers[-1]]:
                _ = openers.pop()
            else:
                return False
        return not openers

    

