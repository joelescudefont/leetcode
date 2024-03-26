from typing import Optional

from utils import ListNode


class Solution:
    def __init__(self):
        self.prev = None

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly-linked list.
        """
        if not head:
            return self.prev
        tmp = head.next
        head.next = self.prev
        self.prev = head
        return self.reverse_linked_list(tmp)
