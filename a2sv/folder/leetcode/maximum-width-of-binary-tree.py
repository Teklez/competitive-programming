# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([(root,1)])
        max_distance = 0
        while que:
            n = len(que)
            for i in range(n):
                cur = que.popleft()
                if i == 0:
                    left = cur[1]
                if i ==  n - 1:
                    right = cur[1]

                if cur[0].left:
                    tup = (cur[0].left, 2*cur[1])
                    que.append(tup)
                if cur[0].right:
                    tup = (cur[0].right, 2*cur[1] + 1)
                    que.append(tup)
            max_distance = max(max_distance, right-left + 1) 
        return max_distance
                
                





        
        