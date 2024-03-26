# 21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/


# Tests

```
Input: head1 = [0, 2], head2 = [1]
Output: [0, 1, 2]

Head1: 0 -> 2
Head2: 1
Output: 0 -> 1 -> 2
```

```
Input: head1 = [0, 2], head2 = [1, 3]
Output: [0, 1, 2, 3]

Head1: 0 -> 2
Head2: 1 -> 3
Output: 0 -> 1 -> 2 -> 3
```

```
Input: head1 = [], head2 = []
Output: []

Head1: null
Head2: null
Output: null
```


# Solutions

| Solution        | Time complexity | Space complexity |
|-----------------|-----------------|------------------|
| **Outplace**    | `O(n+m)`        | `O(1)`           |

`n` and `m` are the lengths of the linked lists.

[//]: # "Hint: Use a dummy head."
