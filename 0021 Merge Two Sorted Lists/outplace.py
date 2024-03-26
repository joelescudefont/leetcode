from typing import Optional

from utils import ListNode


class Solution:
    def merge_sorted_linked_lists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.
        """
        if not head1 and not head2:
            return None
        res = ListNode()
        head3 = res
        while head1 or head2:
            if not head1 and head2:
                head3.next = head2
                return res.next
            if head1 and not head2:
                head3.next = head1
                return res.next
            if head1.val <= head2.val:
                head3.next = head1
                head1 = head1.next
            else:
                head3.next = head2
                head2 = head2.next
            head3 = head3.next
