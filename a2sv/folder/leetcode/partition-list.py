# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left = dummy
        current = head
        prev = dummy
        while current:
            nxt = current.next
            if current.val < x:
                if left != prev:
                    prev.next = nxt
                    current.next = left.next
                    left.next = current
                else:
                    prev = current
                left = current
            else:
                prev = current
            current = nxt
        
        return dummy.next
        