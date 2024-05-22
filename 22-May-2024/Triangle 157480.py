# Problem: Triangle - https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*i for i in range(1, n + 1)]
        dp[0][0] = triangle[0][0]
        print(dp)
        for r in range(1, n):
            for c in range(r + 1):
                if c == 0:
                    dp[r][c] = triangle[r][c] + dp[r - 1][c]
                elif c == r:
                    dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]
                else:
                    dp[r][c] = triangle[r][c] + min(dp[r - 1][c], dp[r - 1][c - 1])
        return min(dp[-1])
