# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_list = []
        def inorder(root):
            if not root:return None
            inorder(root.left)
            sorted_list.append(root.val)
            inorder(root.right)

        def buildTree(left,right):
            if left > right:
                return None
            mid = (left + right)//2
            node = TreeNode(sorted_list[mid])
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid+1, right)
            return node
            
        inorder(root)
        return buildTree(0, len(sorted_list) - 1)


        