from typing import List

import pytest


class Solution:
    @staticmethod
    def group_anagrams(strings: List[str]) -> List[List[str]]:
        groups = {}

        for s in strings:
            for key in groups:
                if set(s) == set(key):
                    groups[key].append(s)
                    break

            else:
                groups[s] = [s]

        return list(groups.values())


@pytest.mark.parametrize("expected,strings", [
    ([[""]], [""]),
    ([["aa"]], ["aa"]),
    ([["abc", "bca"], ["eeff"]], ["abc", "bca", "eeff"]),
])
def test_group_anagrams(expected, strings):
    assert expected == Solution.group_anagrams(strings)
