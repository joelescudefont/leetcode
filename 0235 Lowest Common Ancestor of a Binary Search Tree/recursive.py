from typing import Optional

from utils import TreeNode


class Solution:
    def lowest_common_ancestor(
            self, root: Optional[TreeNode], node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Find the lowest common ancestor.
        """
        if root.val == node1.val or root.val == node2.val:
            return root
        if root.val > node1.val and root.val > node2.val:
            return self.lowest_common_ancestor(root.left, node1, node2)
        if root.val < node1.val and root.val < node2.val:
            return self.lowest_common_ancestor(root.right, node1, node2)
        return root
