# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(low,high):
            mid = (high + low)//2
            if low > high:
                return None
            node = TreeNode(nums[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid+1,high)
            return node
        return build(0, len(nums) - 1)

        