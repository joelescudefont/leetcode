from typing import Optional

from utils import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Assert if a linked list has a cycle.
        """
        while True:
            if not head:
                return False
            if isinstance(head.val, int):
                head.val = []
                head = head.next
                continue
            return True
