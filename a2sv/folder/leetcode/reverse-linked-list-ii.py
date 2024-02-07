# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        lefty = head
        
        for i in range(left - 1):
            prev = lefty
            lefty = lefty.next
            
        prvs = None
        righty = lefty
        for i in range(right - left + 1):
            nxt = righty.next
            righty.next = prvs
            prvs = righty
            righty = nxt
            
        lefty.next = nxt
        prev.next = prvs
        
        return dummy.next
        