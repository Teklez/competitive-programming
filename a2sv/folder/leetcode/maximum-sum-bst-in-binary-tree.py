# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        sums = [0]
        def isBST(node):
            if not node: return 0, True, -inf, inf
            
            s1, isBST1, max1, min1 = isBST(node.left)
            s2, isBST2, max2, min2 = isBST(node.right)
            if isBST1 and isBST2 and max1 < node.val < min2:
                val = node.val + s1 + s2
                sums[0] = max(sums[0], val)
                return val, True, max(max2, node.val), min(node.val, min1)
            
            return 0, False, -inf, inf
        
        isBST(root)
        return sums[0]