from typing import Optional

from utils import TreeNode


class Solution:
    def maximum_depth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of a binary tree.
        """
        if not root:
            return 0
        return 1 + max(self.maximum_depth(root.left), self.maximum_depth(root.right))
