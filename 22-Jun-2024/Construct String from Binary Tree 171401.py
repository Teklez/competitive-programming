# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not (root.right or root.left):
            return str(root.val)
        if (not root.left) and root.right:
            return str(root.val) + "()" + "(" + self.tree2str(root.right) + ")"
        if( not root.right ) and root.left:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"

        return str(root.val) + "(" + self.tree2str(root.left) + ')' \
        +  "(" + self.tree2str(root.right) + ")"
    
        