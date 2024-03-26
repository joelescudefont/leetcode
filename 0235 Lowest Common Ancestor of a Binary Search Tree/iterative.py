from typing import Optional

from utils import TreeNode


class Solution:
    def lowest_common_ancestor(
            self, root: Optional[TreeNode], node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Find the lowest common ancestor.
        """
        while root:
            if root.val > node1.val and root.val > node2.val:
                root = root.left
            elif root.val < node1.val and root.val < node2.val:
                root = root.right
            else:
                return root
        return
