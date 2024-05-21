# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # memo = {}
        # n = len(arr)

        # def dp(i,last):
        #     if i >= len(arr):
        #         return 0
        #     include = 0
        #     if (i, last) not in memo:
        #         if last == -1 or arr[i] - arr[last] == difference:
        #             include = 1 + dp(i + 1, i)
        #         exclude = dp(i + 1 , last)
        #         memo[(i, last)] = max(include, exclude)
        #     return memo[(i, last)]

        # return dp(0, -1)
        n = len(arr)
        dp = defaultdict(int)
        dp[arr[0]] = 1

        for i in range(1,n):
            dp[arr[i]] = 1 + dp[arr[i] - difference]
            
        return max(dp.values())

        


