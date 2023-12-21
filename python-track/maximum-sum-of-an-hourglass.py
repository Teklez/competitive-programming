class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxm = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                tSum = sum(grid[i][j: j + 3]) + sum(grid[i + 2][j: j + 3])
                tSum += grid[i + 1][j + 1]
                maxm = max(maxm, tSum)

        return maxm


        