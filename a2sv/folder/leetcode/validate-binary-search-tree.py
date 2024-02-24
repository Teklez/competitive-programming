# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_valid = True
        my_order = by(root,temp=[])
        for i in range(len(my_order) - 1):
            if my_order[i] >= my_order[i + 1]:
                is_valid = False
                break
        return is_valid


def by(root,temp = []):
    if root:
        by(root.left,temp)
        temp.append(root.val)
        by(root.right,temp)
    return temp
        