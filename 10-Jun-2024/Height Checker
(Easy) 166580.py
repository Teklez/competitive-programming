# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeight = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sortedHeight[i] != heights[i]:
                count += 1
        return count

        