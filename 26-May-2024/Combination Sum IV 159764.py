# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        
        for t in range(1, target + 1):
            dp[t] = 0
            for n in nums:
                dp[t] += dp[t - n]
                
        return dp[target]