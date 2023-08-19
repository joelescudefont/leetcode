from typing import List

import pytest


class Solution:
    def __init__(self):
        self.stop_token: str = "#"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + self.stop_token + s

        return encoded

    def decode(self, encoded: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(encoded):
            j = i
            length = ""
            while encoded[j] != self.stop_token:
                length += encoded[j]
                j += 1

            length = int(encoded[i: j])
            decoded.append(encoded[j + 1: j + 1 + length])

            i = j + 1 + length

        return decoded


@pytest.mark.parametrize("encoded,decoded", [
    ("4#this4#that", ["this", "that"]),
])
def test_find_top_k_frequent_elements(encoded, decoded):
    assert encoded == Solution().encode(decoded)
    assert decoded == Solution().decode(encoded)
