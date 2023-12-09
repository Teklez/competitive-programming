class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winned = {}
        lost = {}

        for i in range(len(matches)):
            winned[matches[i][0]] = winned.get(matches[i][0], 0) + 1
            lost[matches[i][1]] = lost.get(matches[i][1], 0) + 1
        
        result = [sorted([key for key, value in winned.items() if lost.get(key, 0) == 0]),sorted([key for key, value in lost.items() if value == 1])]
        return result

        