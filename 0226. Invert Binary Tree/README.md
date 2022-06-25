# 226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/


# Tests

```
Input: root = [1, 2, 3, 4, null, null, null]
Output: [1, 3, 2, null, null, null, 4]

    1    ->    1
   / \        / \
  2   3      3   2
 /                \
4                  4
```

```
Input: root = []
Output: []
```


# Solutions

| Solution                           | Time complexity | Space complexity |
|------------------------------------|-----------------|------------------|
| **Recursive Depth-First Search**   | `O(n)`          | `O(1)`           |

