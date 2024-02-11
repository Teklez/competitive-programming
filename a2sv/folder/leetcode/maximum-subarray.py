class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = float(-inf)
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            maxm = max(runSum, maxm)
            if runSum < 0:
                runSum = 0
        return maxm

