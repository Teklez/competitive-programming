# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)

        def build(nums):
            nonlocal left, right
            if  not nums:
                return None
            idx = 0
            maxm = nums[0]
            for i in range(len(nums)):
                if nums[i] > maxm:
                    idx = i
                    maxm = nums[i]
            
            node = TreeNode(nums[idx])
            node.left = build(nums[left:idx])
            node.right = build(nums[idx + 1:right])
            return node
        return build(nums)

            

        

        