# 235. Lowest Common Ancestor of a Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Tests

```
Input: 2, 6
Output: 4

         4
      /     \
     2       6
    / \     / \
   1   3   5   7
```


```
Input: 2, 3
Output: 2

         4
      /     \
     2       6
    / \     / \
   1   3   5   7
```


# Solutions

| Solution                         | Time complexity | Space complexity |
|----------------------------------|-----------------|------------------|
| **Recursive Depth-First Search** | `O(logn)`       | `O(1)`           |

`logn` is the height of the tree approx

[//]: # "Hint: Find the split."
