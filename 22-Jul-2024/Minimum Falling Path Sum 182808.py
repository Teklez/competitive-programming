# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf for _ in range(n)] for _ in range(n)]
        dp[-1] = matrix[-1]

        def minFall(r, c):
            if not( 0 <= r < n) or not(0 <= c < n):
                return float(inf)
            return dp[r][c]


        for row in range(n - 2, -1, -1):
            for col in range(n - 1, -1, -1):
                dp[row][col] = matrix[row][col] + min(minFall(row + 1, col), \
                minFall(row + 1, col - 1), \
                minFall(row + 1, col + 1))

        return min(dp[0])

