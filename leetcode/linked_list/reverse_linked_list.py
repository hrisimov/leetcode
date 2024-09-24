from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
#
#         def reverse(head):
#             if not head.next:
#                 return head
#
#             new_head = reverse(head.next)
#             head.next.next = head
#             head.next = None
#             return new_head
#
#         return reverse(head)
