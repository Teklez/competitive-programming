# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current =head
        count = 0
        while current != None:
            count +=1
            current = current.next
        prev = head
        current = head
        if count - n == 0:
            head = head.next
        else:
            for i in range(count - n):
                prev = current
                current = current.next
            prev.next = current.next
        return head
        