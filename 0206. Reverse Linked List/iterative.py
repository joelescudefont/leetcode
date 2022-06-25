from typing import Optional

from utils import ListNode


class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly-linked list.
        """
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
