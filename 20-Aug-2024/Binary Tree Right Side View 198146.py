# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def solve(root, lvl):
        	if root:
        		if len(res)==lvl:
        			res.append(root.val)
        		solve(root.right, lvl + 1)
        		solve(root.left, lvl + 1)
        	return 

        res = []
        solve(root,0)
        return res