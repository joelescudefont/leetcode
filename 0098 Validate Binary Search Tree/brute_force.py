"""
0098 Validate Binary Search Tree

GIVEN: the root of a binary search tree

RETURN: true if it is a valid binary search tree (BST)

A valid binary search tree
- the left subtree of a node contains only nodes with keys less than the node's key.
- the right subtree of a node contains only nodes with key greater than the node's key.
- both the left and the right subtrees must also be binary search trees.

CONDITIONS
- at least one node.


Tree
      5
  3        9
2  4     7   10
        6 8

Validation: True



SOLUTION: Brute Force

TC: O(n^2)
SC: O(1)

- traverse recursive depth-first search
- traverse the left subtree checking that all values are less than the root value.
- traverse the right subtree checking that all values are more than the root value.

IMPLEMENTATION DETAILS

Return
assert(root.left, root.val) AND assert(root.right, root.val)
AND recurse(root.left) AND recurse(root.right)

       5
   3         9
 1   4     7   10
0 2       6 8


"""

from typing import Optional

from utils import TreeNode as Node


class Solution:
    def validate(self, root: Optional[Node]) -> bool:
        if not root:
            return True

        return self.assert_left(root.left, root.val) and self.assert_right(root.right, root.val) \
            and self.validate(root.left) and self.validate(root.right)

    def assert_left(self, root: Optional[Node], boundary: int) -> bool:
        if not root:
            return True

        return (root.val < boundary) and self.assert_left(root.left, boundary) and self.assert_left(root.right, boundary)

    def assert_right(self, root: Optional[Node], boundary: int) -> bool:
        if not root:
            return True

        return (root.val > boundary) and self.assert_right(root.left, boundary) and self.assert_right(root.right, boundary)
