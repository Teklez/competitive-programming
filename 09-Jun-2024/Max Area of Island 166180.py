# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def inBound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(row, col):
            nonlocal area
            if not grid[row][col]:
                return 

            area += 1
            grid[row][col] = 0
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inBound(new_row, new_col) and grid[new_row][new_col]:
                    dfs(new_row, new_col)

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(area, max_area)

        return max_area
                    
                

    

       







