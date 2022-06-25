# 338. Counting Bits

https://leetcode.com/problems/counting-bits/

# Tests

```
Input: n = 4
Output: 1
```

```
Input: n = 0
Output: 0
```


# Solutions

| Solution        | Time complexity | Space complexity |
|-----------------|-----------------|------------------|
| **Brute Force** | `O(nlogn)`      | `O(n)`           |
| **Dynamic**     | `O(n)`          | `O(n)`           |

`n` is the length of the output array.

<br>

```
Hint: Use the previous block.

n   bits   count
0   0000   0
1   0001   1 => 1 + dp[idx - 1]
2   0010   1 => 1 + dp[idx - 2]
3   0011   2
4   0100   1 => 1 + dp[idx - 4]
5   0101   2
6   0110   2
7   0111   3
8   1000   1 => 1 + dp[idx - 8]
9   ...
```
