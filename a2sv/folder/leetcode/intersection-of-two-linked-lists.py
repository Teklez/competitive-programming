# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # dic = {}
        # curr = headA
        # while curr:
        #     dic[curr] = 1
        #     curr = curr.next
            
        # curr = headB
        # while curr:
        #     if curr in dic:
        #         return curr
        #     curr = curr.next
        # return None

        def countNodes(head):
            current, count = head, 0
            while current:
                count += 1
                current = current.next
            return count

        countA = countNodes(headA)
        countB = countNodes(headB)
        start = headB if countA < countB else headA
        current = headA if countA < countB else headB

        while start:
            for _ in range(abs(countA - countB)):
                start = start.next
            while start and current:
                if start == current:
                    return current
                start = start.next
                current = current.next
        return None
            
            

            
        


        