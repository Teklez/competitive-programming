# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        left = head
        prev = head
        current = head
        
        while current:
            nxt = current.next
            if count % 2 == 1 and count != 1:
                current.next = left.next
                left.next = current
                prev.next = nxt
                left = current
            else:
                prev = current
            current = nxt
            count += 1
        return head
        