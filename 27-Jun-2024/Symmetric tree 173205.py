# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # right = [root.right] if root.right else None
        # left = [root.left] if root.left else None
        # while right and left:
        #     cur1 = right.pop()
        #     cur2 = left.pop()
        #     if cur1.val != cur2.val:
        #         return False
        #     if cur1.right and cur2.left:
        #         right.append(cur1.right)
        #         left.append(cur2.left)
        #         print(cur1.right.val, cur2.left.val)
        #     elif cur1.right or cur2.left:
        #         return False
        #     if cur1.left and cur2.right:
        #         right.append(cur1.left)
        #         left.append(cur2.right)
        #         print(cur1.left.val, cur2.right.val)
        #     elif cur1.left or cur2.right:
        #         return False
        # return True if not(left or right) else False
        left = root.left
        right = root.right
        def helper(left, right):
            if not(left or right):return True
            if not(left and right):return False
            print(left.val, right.val)
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        return helper(left,right)








            
        














