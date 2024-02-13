# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        curr = head.next
        p = dummy.next
        while curr:
            prev = dummy
            current = dummy.next
            while current and curr.val > current.val:
                prev = current
                current = current.next
            if curr == current:
                p = curr
                curr = curr.next
                continue
            
            nxt = curr.next
            prev.next = curr
            p.next = nxt
            # p = curr
            curr.next = current
            curr = nxt
        return dummy.next



        