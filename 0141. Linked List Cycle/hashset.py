from typing import Optional

from utils import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Assert if a linked list has a cycle.
        """
        seen = []
        while True:
            if not head:
                return False
            if head not in seen:
                seen.append(head)
                head = head.next
                continue
            return True
