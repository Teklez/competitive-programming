class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            if abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= abs(target[0]) + abs(target[1]):
                return False
        return True