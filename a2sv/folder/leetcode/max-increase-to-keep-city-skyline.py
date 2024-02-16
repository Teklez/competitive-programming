class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        column = [[0 for i in range(len(grid))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                column[i][j] = grid[j][i]
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                max1 = max(grid[i])
                max2 = max(column[j])
                maxm = min(max2, max1)
                if grid[i][j] < maxm:
                    res += maxm - grid[i][j]
        return res