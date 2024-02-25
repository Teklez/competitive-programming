# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        zigzag_order = []
        que = deque([root])
        level = 0
        while que:
            breadth = []
            for _ in range(len(que)):
                cur = que.popleft()
                breadth.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            breadth = breadth[::-1] if level % 2 == 1 else breadth
            zigzag_order.append(breadth)
            level += 1
        return zigzag_order



                                                                                                                 


        