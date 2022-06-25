from typing import Optional

from utils import TreeNode


class Solution:
    def invert_binary_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree.
        """
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
        return root
