# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def postorderTraversalHelper(root,temp=[]):
            if root:
                postorderTraversalHelper(root.left, temp)
                postorderTraversalHelper(root.right, temp)
                temp.append(root.val)
            
            return temp
        return postorderTraversalHelper(root, [])
        