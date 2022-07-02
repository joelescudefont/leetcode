# 141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/


# Tests

```
Input: head = [1, 2, 3, 2]
Output: True
Explanation: The node with value 3 at position 2 points back to the node with value 2 at position 1.

1 -> 2 -> 3 -> 2 (at position 1) 
```

```
Input: head = [1, 2]
Output: False

1 -> 2
```


# Solutions

| Solution    | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| **Hashset** | `O(n)`          | `O(n)`           |
| **Type**    | `O(n)`          | `O(1)`           |
