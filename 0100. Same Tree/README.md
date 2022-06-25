# 100. Same Tree

https://leetcode.com/problems/same-tree/


# Tests

```
Input: root1 = [1, 2, 3], root2 = [1, 2, 3]
Output: True

   1       1
  / \     / \
 2   3   2   3
```

```
Input: root1 = [1, 2], root2 = [1, null, 2]
Output: False

   1       1
  /         \
 2           2
```


# Solutions

| Solution                         | Time complexity | Space complexity |
|----------------------------------|-----------------|------------------|
| **Recursive Depth-First Search** | `O(n)`          | `O(1)`           |

