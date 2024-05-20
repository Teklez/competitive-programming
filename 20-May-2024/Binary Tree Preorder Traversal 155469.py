# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorderTraversalHelper(root,temp):
            if root:
                temp.append(root.val)
                preorderTraversalHelper(root.left,temp)
                preorderTraversalHelper(root.right,temp)
            return temp
        return preorderTraversalHelper(root,[])
        
        