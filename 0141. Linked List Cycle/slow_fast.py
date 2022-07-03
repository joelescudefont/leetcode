from typing import Optional

from utils import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Assert if a linked list has a cycle.
        """
        if not head or not head.next or not head.next.next:
            return False
        slow = head.next
        fast = head.next.next
        while fast != slow:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
