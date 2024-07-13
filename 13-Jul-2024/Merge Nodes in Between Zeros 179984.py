# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        head = head.next
        currSum = 0
        while head:
            if head.val == 0:
                head.val = currSum
                curr.next = head
                curr = curr.next
                currSum = 0
            else:
                currSum += head.val
            head = head.next
        return dummy.next

            
        