# 572. Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree/


# Tests

```
Input: root = [1, 2, 3], subroot = [1, 2]
Output: True

     1        1
    / \      /
   2   3    2
```

```
Input: root = [1, 2, 3, 4, null, null, null], subroot = [1, 2]
Output: False

     1        1
    / \      /
   2   3    2
  /
 4
```


# Solutions

| Solution                         | Time complexity | Space complexity |
|----------------------------------|-----------------|------------------|
| **Recursive Depth-First Search** | `O(n*m)`        | `O(1)`           |

`n` and `m` are the number of nodes of each tree