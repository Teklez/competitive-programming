# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraversalHelper(root,store):
            if root:
                store[root.val] += 1
                postorderTraversalHelper(root.left, store)
                postorderTraversalHelper(root.right, store)
            return store
        store  = postorderTraversalHelper(root,defaultdict(int))
        maxm = 0
        for key, value in store.items():
            maxm = max(maxm, value)
        return  [key for key,value in store.items() if value == maxm]
        
        

        