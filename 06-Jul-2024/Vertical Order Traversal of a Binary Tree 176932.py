# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        values = []
        # que = deque([(root,(0,0))])
        # while que:
        #     n = len(que)
        #     for _ in range(n):
        #         cur = que.popleft()
        #         store[cur[1][1]].append(cur[0].val)
        #         if cur[0].left:
        #             cell = (cur[1][0] + 1, cur[1][1] - 1)
        #             que.append((cur[0].left, cell))
        #         if cur[0].right:
        #             cell = (cur[1][0] + 1, cur[1][1] + 1)
        #             que.append((cur[0].right, cell))
        # for k in store:
        #     store[k] = sorted(store[k])
        
        # vertical = sorted(store.keys())
        # return [store[i] for i in vertical]
        def dfs(root, row, col):
            if not root:return
            values.append(((row, col), root.val))
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
        dfs(root, 0, 0)
        values.sort(key = lambda x: x[1])
        values.sort(key = lambda x: x[0][0])
        for pairs in values:
            store[pairs[0][1]].append(pairs[1])
        vertical = sorted(store.keys())
        return [store[i] for i in vertical]

                



        

