# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # prev = node
        current = node
        nxt = node.next
        
        # while current.next:
        #     nxt = current.next
        #     current.val = nxt.val
        #     prev = current
        #     current = nxt
        
        # prev.next = None
        current.val = nxt.val
        current.next = nxt.next


        