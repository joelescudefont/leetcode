# 191. Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/


# Tests

```
Input: n = 6
Output: 2
Explanation: 6 has 110 bytes with two ones.
```

```
Input: n = 4
Output: 1
```


# Solutions

| Solution     | Time complexity | Space complexity |
|--------------|-----------------|------------------|
| **Mod**      | `O(1)`          | `O(1)`           |
| **Subtract** | `O(1)`          | `O(1)`           |

As for a binary string of length `32`.

<br>

Hints: 
Detect first bit as `0` or `1`. 
Move to the next bit.
Count the ones.

Hint: 
Update the binary string with its current value minus one bit.