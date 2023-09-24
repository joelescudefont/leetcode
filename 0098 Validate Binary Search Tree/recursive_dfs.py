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
       6
   3       8
 2   5    7 9
    4

Validation: true


SOLUTION: Recursive depth-first search, asserting boundaries.

TC: O(n)
SC: O(1)

1- traverse the tree with recursive depth-first search
2- validate each node boundaries
-- previus left value < left value < node value
-- node value < right value < previous right value

Boundaries validations: left and right
- there's always one boundary witch is the parent node value.

left 	-inf < 3 < 5	<- -inf prev left val <--> prev right val
left 	-inf < 2 < 3	<- ...
right	3 < 4 < 5	<- ...

right 	5 < 9 < +inf	<- prev left val <--> prev right val +inf
left	5 < 7 < 9	<- prev left val <--> prev right val
left	5 < 6 < 7	<- ...
right 	7 < 8 < 9	<- ...
right 	9 < 10 < +inf 	<- prev left val <--> prev right val +inf



IMPLEMENTATION DETAILS


Func: validate_tree

Return
validate_node(-inf, root.left, root.val)
validate_node(root.val, root.right, +inf)


Func: validate_node

If root is null, return True.

Return
(left_boundary < root.val < right_boundary)
validate_node(left_boundary, root.left, root.val)
validate_node(root.val, root.right, right_boundary)

       6
   3       8
 2   5    7 9
    4

"""

from typing import Optional

from utils import TreeNode as Node


class Solution:
    def validate_tree(self, root: Optional[Node]) -> bool:
        return self.validate_node(float("-inf"), root.left, root.val) \
            and self.validate_node(root.val, root.right, float("inf"))

    def validate_node(self, left_boundary: float, root: Optional[Node], right_boundary: float) -> bool:
        if not root:
            return True

        return left_boundary < root.val < right_boundary \
            and self.validate_node(left_boundary, root.left, root.val) \
            and self.validate_node(root.val, root.right, right_boundary)
