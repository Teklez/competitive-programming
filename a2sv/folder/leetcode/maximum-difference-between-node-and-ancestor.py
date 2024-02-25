# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMax(root, val):
            stack = [root]
            res = 0
            while stack:
                cur = stack.pop()
                if cur.left:
                    stack.append(cur.left)
                    res = max(res, abs(cur.left.val - val))
                if cur.right:
                    stack.append(cur.right)
                    res = max(res, abs(cur.right.val - val))

            return res

        max_difference = 0
        stack = [root]
        while stack:
            cur = stack.pop()
            max_difference = max(max_difference, findMax(cur, cur.val))
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return max_difference




        
        