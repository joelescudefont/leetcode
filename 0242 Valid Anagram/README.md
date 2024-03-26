# 242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

# Tests

```
Input: str1 = "abc", str2 = "cab"
Output: True
```

```
Input: str1 = "abc", str2 = "xyz"
Output: False
```

```
Input: str1 = "abc", str2 = "f"
Output: False
```


# Solutions

| Solution        | Time complexity        | Space complexity              |
|-----------------|------------------------|-------------------------------|
| **Brute Force** | `O(n^2)`               | `O(n)`                        |
| **Sort**        | `O(n^2)` or `O(nlogn)` | `O(n)` or `O(1)` if optimized |
| **Replace**     | `O(n*m)`               | `O(1)`                        |
| **Counter**     | `O(n + m)`             | `O(n + m)`                    |

`n` and `m` are the lengths of the strings.
