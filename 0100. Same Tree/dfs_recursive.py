from typing import Optional

from utils import TreeNode


class Solution:
    def is_same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Assert if two trees are same.
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)
