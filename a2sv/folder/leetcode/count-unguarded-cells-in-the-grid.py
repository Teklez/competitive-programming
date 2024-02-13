class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for i in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 1

        print(grid)
        for r, c in guards:
            row, col = r, c
            if row + 1 < m:
                row += 1
            while row < m and (grid[row][col] == 0 or grid[row][col] == 2) :
                grid[row][col] = 2
                row += 1

            row, col = r, c
            if row - 1 >= 0:
                row -= 1
            while row >= 0 and (grid[row][col] == 0 or grid[row][col] == 2):
                # print(row, col)
                grid[row][col] = 2
                row -= 1

            row, col = r, c
            if col + 1 < n:
                col += 1
            while col < n and (grid[row][col] == 0 or grid[row][col] == 2):
                grid[row][col] = 2
                col += 1

            row, col = r, c
            if col - 1 >= 0:
                col -= 1
            while col >= 0 and (grid[row][col] == 0 or grid[row][col] == 2):
                print(row, col)
                grid[row][col] = 2
                col -= 1

        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1
        print(grid)

        return unguarded




            

        
        