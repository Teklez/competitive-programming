# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}
        # def dp(i, amount):
        #     if amount == 0:
        #         return 1
        #     if amount < 0 or i >= len(coins):
        #         return 0
        #     if (i, amount) not in memo:
        #         memo[(i, amount)] = dp(i, amount - coins[i]) + dp(i + 1, amount)
        #     return memo[(i, amount)]
            
        # return dp(0, amount)


        # dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # dp[0][0] = 1
        
        # for i in range(amount + 1):
        #     for j in range(1, len(coins) + 1):
        #         pick = i - coins[j - 1]
        #         dp[j][i] = (dp[j][pick] if pick >= 0 else 0) + dp[j - 1][i]

        # return dp[-1][-1]

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for j in range(1, len(coins) + 1):
            for i in range(amount + 1):
                pick = i - coins[j - 1]
                dp[i] = (dp[pick] if pick >= 0 else 0) + dp[i]

        return dp[-1]

    

