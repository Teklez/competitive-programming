class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        preSum = [0]*len(nums)
        tot = 0
        for i, j in requests:
            preSum[i] += 1
            if j + 1 < len(nums):
                preSum[j + 1] -= 1
        
        summ = 0
        for i in range(len(nums)):
            summ += preSum[i]
            preSum[i] = summ
        
        maxSum = 0
        nums.sort()
        preSum.sort()
        for i in range(len(nums)):
            maxSum += preSum[i]*nums[i]
        return maxSum%(10**9 + 7)
        
        