# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = {}
        while current:
            count[current.val] = 1 + count.get(current.val,0)
            current = current.next
        print(count)
        
        dummy = ListNode()
        pointer = dummy
        current = head
        while current:
            if count[current.val] == 1:
                pointer.next = current
                pointer = current
            current = current.next
            pointer.next = None
        return dummy.next
        